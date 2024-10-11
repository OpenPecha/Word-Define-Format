import re
from  WordDefine.utils import save_json,create_dir

def parse_line_with_first_curly_braces(line: str) -> dict:
    """
    Parse a single line of text to extract the word and its definition.
    The word is before '༑', and the definition is the content inside the first curly braces after '༑'.
    Any additional content after the first curly braces will be ignored.
    Args:
        line (str): A single line of text containing a word and its definition.

    Returns:
        dict: A dictionary with 'word' and 'definition' keys if parsing is successful.
              Returns None if the line doesn't match the expected pattern.
    
    """
    word_def_pattern = r'(.+?)༑\{(.+?)\}'
    match = re.search(word_def_pattern, line)
    
    if match:
        word = match.group(1).strip()
        definition = match.group(2).strip()
        return {
            "word": word,
            "definition": definition
        }
    return None

def text_to_json_with_first_curly_braces(input_file: str, output_file: str):
    """
    Parse the text file where each line contains a word and a definition within the first curly braces after '༑',
    then convert it into a JSON format.
      
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output JSON file.

    """
    result = []
    
    # Read the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            parsed_line = parse_line_with_first_curly_braces(line.strip())
            if parsed_line:
                result.append(parsed_line)
    
    # Write the parsed result to a JSON file
    save_json(result, filename=output_file)

# Define the file paths
input_file = 'data/input/tibetan_dictionaries/42-བསྡུས་གྲྭའི་མཚན་ཉིད།.txt'  # Replace with your actual text file
output_file = 'data/output/42-བསྡུས་གྲྭའི་མཚན་ཉིད།/42-བསྡུས་གྲྭའི་མཚན་ཉིད།.json'
create_dir(output_file)
# Convert text to JSON
text_to_json_with_first_curly_braces(input_file, output_file)

output_file
