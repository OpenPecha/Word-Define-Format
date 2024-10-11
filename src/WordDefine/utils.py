import json
import os

def save_json(data, file_path):
    """Saves a Python object as a JSON file.

    Args:
        data (object): The Python data (e.g., list or dictionary) to be saved as JSON.
        file_path (str): The path where the JSON file will be saved.

    The function serializes the provided Python object and saves it as a JSON file in the specified location.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def create_dir(output_file):
    """Creates the directory for the output file if it does not already exist.

    Args:
        output_file (str): The path to the file, whose directory will be created if missing.

    The function checks if the directory of the provided file path exists and creates it if not.
    """
    output_file_dir = os.path.dirname(output_file)
    if not os.path.exists(output_file_dir):
        os.makedirs(output_file_dir)
        print(f"Created directory: {output_file_dir}")
