import pyewts
from WordDefine.utils import save_json,create_dir

def text_to_word_definition_with_wylie_conversion(text_file: str, output_file: str):
    """
    Convert a text file with Wylie transliterated words and definitions to JSON format.
    Both the word and the definition are converted from Wylie to Unicode Tibetan script.

    Args:
        text_file (str): Path to the input text file containing words and definitions in Wylie format.
        output_file (str): Path where the resulting JSON file will be saved.

    """
    converter = pyewts.pyewts()  # Wylie to Unicode converter
    word_dict = {}

    # Read the input text file line by line
    with open(text_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                word_wylie, definition_wylie = line.split("|", 1)  # Split only at the first occurrence of "|"
                word_wylie = word_wylie.strip()
                definition_wylie = definition_wylie.strip()

                # Convert word and definition from Wylie to Unicode Tibetan script
                word_unicode = converter.toUnicode(word_wylie)
                definition_unicode = converter.toUnicode(definition_wylie)

                # Check if the word already exists in the dictionary
                if word_unicode in word_dict:
                    # Append the definition if it already exists
                    word_dict[word_unicode].append(definition_unicode)
                else:
                    # Create a new entry for the word
                    word_dict[word_unicode] = [definition_unicode]

    # Convert dictionary to the required JSON format
    result = [{"word": word, "definition": definitions} for word, definitions in word_dict.items()]

    save_json(result, filename=output_file) 

    print(f"Data has been written to {output_file}")



# Example usage
text_file = 'data/input/25-tshig-mdzod-chen-mo-Tib.txt'  # Replace with the actual path to your input text file
output_file = 'data/output/25-tshig-mdzod-chen-mo-Tib/25-tshig-mdzod-chen-mo-Tib.json'  # Replace with the desired path for the output JSON file
create_dir(output_file)
# Convert the text file to JSON format
text_to_word_definition_with_wylie_conversion(text_file, output_file)
