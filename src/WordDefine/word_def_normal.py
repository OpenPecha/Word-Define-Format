import json
import os

def parse_line(line: str) -> dict:
    """
    Parse a single line of text to extract the word and its definition.
    The word is before the first occurrence of '༑', and the definition is after it.
    """
    if '༑' in line:
        word, definition = line.split('༑', 1)
        return {
            "word": word.strip(),
            "definition": definition.strip()
        }
    return None

def text_to_json(input_file: str, output_file: str):
    """
    Parse the text file where each line contains a word and its definition,
    then convert it into a JSON format.
    """
    result = []
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} was not found.")
        return

    # Read the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            parsed_line = parse_line(line.strip())
            if parsed_line:
                result.append(parsed_line)
    
    # Write the parsed result to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)
    print(f"Data successfully written to {output_file}")

# Define the file paths
input_file = 'data/input/tibetan_dictionaries/37-དག་ཡིག་གསར་བསྒྲིགས།.txt'  # Replace with your actual text file
output_file = 'data/output/37-དག་ཡིག་གསར་བསྒྲིགས།/37-དག་ཡིག་གསར་བསྒྲིགས།.json'
output_file_dir = os.path.dirname(output_file)
if not os.path.exists(output_file_dir):
    os.makedirs(output_file_dir)

# Convert text to JSON
text_to_json(input_file, output_file)
