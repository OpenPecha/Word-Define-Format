import csv
from collections import defaultdict

from WordDefine.utils import create_dir


def csv_to_json(csv_file: str, json_file: str):
    """
    Convert a CSV file to JSON format, extracting word-definition pairs.
    If a word has multiple definitions, they are stored in a list under the "definition" field.

    Args:
        csv_file (str): The path to the CSV file where each line contains a word and its definition separated by '|'.
        json_file (str): The path where the resulting JSON file will be saved.

    """
    # Create a dictionary to store words and their definitions
    word_dict = defaultdict(list)

    # Read the CSV file
    with open(csv_file, encoding="utf-8") as file:
        reader = csv.reader(
            file, delimiter="|"
        )  # Assuming '|' is the delimiter in your CSV file

        # Iterate over each row in the CSV
        for row in reader:
            if len(row) != 2:
                continue  # Skip rows that don't have exactly two values
            word, definition = row[0].strip(), row[1].strip()
            word_dict[word].append(definition)

    # Convert dictionary to the required JSON format
    result = []
    for word, definitions in word_dict.items():
        result.append(
            {"word": word, "definition": definitions}  # Store definitions as a list
        )

    print(f"Data has been written to {json_file}")


# Define the CSV file and output JSON file
if __name__ == "__main__":
    csv_file = "data/input/Common Chinese-Tibetan-English Buddhist Terminology (only Tib-En, Cleaned).csv"  # noqa # Replace with the actual path to your CSV file
    json_file = (
        "data/output/Common_Chinese_Tibetan-English/Common_Chinese_Tibetan-English.json"
    )
    create_dir(json_file)
    # Convert CSV to JSON
    csv_to_json(csv_file, json_file)
