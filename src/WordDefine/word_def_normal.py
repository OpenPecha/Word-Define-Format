import os

from WordDefine.utils import create_dir, save_json


def parse_line(line: str):
    """
    Parse a single line of text to extract the word and its definition.
    The word is before the first occurrence of '༑', and the definition is after it.
    Args:
        line (str): A line of text containing the word and definition.

    Returns:
        dict: A dictionary with 'word' and 'definition' keys if parsing is successful.
              Returns None if the line doesn't contain the expected format.
    """
    if "༑" in line:
        word, definition = line.split("༑", 1)
        return {"word": word.strip(), "definition": definition.strip()}
    return None


def text_to_json(input_file: str, output_file: str):
    """
    Parse the text file where each line contains a word and its definition,
    then convert it into a JSON format.

    Args:
        input_file (str): The path to the input text file.
        output_file (str): The path to the output JSON file.

    """
    result = []

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} was not found.")
        return

    # Read the input text file
    with open(input_file, encoding="utf-8") as file:
        for line in file:
            parsed_line = parse_line(line.strip())
            if parsed_line:
                result.append(parsed_line)

    # Write the parsed result to a JSON file
    save_json(result, output_file)


if __name__ == "__main__":
    # Define the file paths
    input_file = "data/input/tibetan_dictionaries/37-དག་ཡིག་གསར་བསྒྲིགས།.txt"  # Replace with your actual text file
    output_file = "data/output/37-དག་ཡིག་གསར་བསྒྲིགས།/37-དག་ཡིག་གསར་བསྒྲིགས།.json"
    create_dir(output_file)
    # Convert text to JSON
    text_to_json(input_file, output_file)
