import json
import pyewts
import os 
def text_to_word_definition_with_wylie_conversion(text_file: str, output_file: str):
    """
    Convert a text file to JSON format where each word is associated with its definition.
    If a word has multiple definitions, they will be stored in a list.
    Both words and definitions in Wylie transliteration are converted to Unicode Tibetan script using pyewts.
    """
    word_dict = {}
    converter = pyewts.pyewts()  # Create the pyewts converter

    # Read the input text file line by line
    with open(text_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                word, definition = line.split("|", 1)  # Split only at the first occurrence of "|"
                word = word.strip()
                definition = definition.strip()

                # Convert the word and definition from Wylie to Unicode (Tibetan script)
                try:
                    word_unicode = converter.toUnicode(word)
                    definition_unicode = converter.toUnicode(definition)
                except Exception as e:
                    print(f"Failed to convert Wylie for word: {word} or definition: {definition}. Error: {e}")
                    word_unicode = word  # If conversion fails, keep the original Wylie
                    definition_unicode = definition

                # Check if the word already exists in the dictionary
                if word_unicode in word_dict:
                    # Append the definition to the list if multiple definitions exist
                    word_dict[word_unicode].append(definition_unicode)
                else:
                    # Create a new entry for the word with the first definition
                    word_dict[word_unicode] = [definition_unicode]

    # Convert dictionary to the required JSON format
    result = [{"word": word, "definition": definitions} for word, definitions in word_dict.items()]

    # Write the result to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    print(f"Data has been written to {output_file}")



# Example usage
text_file = 'data/input/49-LokeshChandraTib.txt'  # Replace with the actual path to your input text file
output_file = 'data/output/49-LokeshChandraTib/49-LokeshChandraTib.json'  # Replace with the desired path for the output JSON file
output_file_dir = os.path.dirname(output_file)
if not os.path.exists(output_file_dir):
    os.makedirs(output_file_dir)
# Convert the text file to JSON format
text_to_word_definition_with_wylie_conversion(text_file, output_file)
