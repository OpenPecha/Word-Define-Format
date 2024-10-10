import csv
import json
import os
from collections import defaultdict

def csv_to_json(csv_file: str, json_file: str):
    """
    Convert CSV data into JSON format by extracting word and definition pairs.
    Handles multiple definitions for the same word by storing them in a list.
    """
    # Create a dictionary to store words and their definitions
    word_dict = defaultdict(list)

    # Read the CSV file
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')  # Assuming '|' is the delimiter in your CSV file

        # Iterate over each row in the CSV
        for row in reader:
            if len(row) != 2:
                continue  # Skip rows that don't have exactly two values
            word, definition = row[0].strip(), row[1].strip()
            word_dict[word].append(definition)

    # Convert dictionary to the required JSON format
    result = []
    for word, definitions in word_dict.items():
        result.append({
            "word": word,
            "definition": definitions  # Store definitions as a list
        })

    # Ensure the directory exists before writing the JSON file
    output_file_path = os.path.dirname(json_file)
    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path)
        print(f"Created directory: {output_file_path}")

    # Write the result to a JSON file with the correct formatting
    with open(json_file, 'w', encoding='utf-8') as json_output:
        json.dump(result, json_output, ensure_ascii=False, indent=4)

    print(f"Data has been written to {json_file}")

# Define the CSV file and output JSON file
csv_file = 'data/input/Common Chinese-Tibetan-English Buddhist Terminology (only Tib-En, Cleaned).csv'  # Replace with the actual path to your CSV file
json_file = 'data/output/Common_Chinese_Tibetan-English/Common_Chinese_Tibetan-English.json'

# Convert CSV to JSON
csv_to_json(csv_file, json_file)
