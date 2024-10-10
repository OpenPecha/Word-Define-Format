import sqlite3
import json
from collections import defaultdict
import os

def db_to_json(db_file: str, output_file: str):
    """
    Convert database data into JSON format where:
    - 'word' is a list of values from the SpCn (second column) and TdCn (third column).
    - 'definition' is a list of definitions from SpCnDf (fifth column).
    If multiple definitions exist for the same word, they are aggregated in the 'definition' list.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get the first table name from the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("No tables found in the database.")
        return

    # Use the first table in the list
    table_name = tables[0][0]
    print(f"Using table: {table_name}")

    # Query necessary columns: SpCn (second column), TdCn (third column), and SpCnDf (fifth column)
    query = f"SELECT SpCn, TdCn, SpCnDf FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Create a dictionary to store words and their definitions
    word_dict = defaultdict(list)

    # Iterate over the rows to collect words (SpCn and TdCn) and definition (SpCnDf)
    for row in rows:
        spcn, tdcn, definition = row[0].strip(), row[1].strip(), row[2].strip()

        # Combine SpCn and TdCn into the word field as a tuple (for unique grouping)
        word_tuple = (spcn, tdcn)

        # Check if the definition is not already in the list to avoid duplicates
        if definition not in word_dict[word_tuple]:
            word_dict[word_tuple].append(definition)

    # Convert dictionary to the required JSON format
    result = []
    for word_tuple, definitions in word_dict.items():
        result.append({
            "word": list(word_tuple),  # Convert the tuple to a list
            "definition": definitions  # Keep definitions as a list
        })

    # Write the result to a JSON file with the correct formatting
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    # Close the database connection
    conn.close()



# Define the SQLite DB file and output JSON file
db_file = 'data/input/dictionarys/CnTbDic2022.db'  # Replace with the actual path to your SQLite database
output_file = 'data/output/CnTbDic2022/CnTbDic2022.json'
output_file_path = os.path.dirname(output_file)
if not os.path.exists(output_file_path):
    os.makedirs(output_file_path)

# Convert DB to JSON with multiple definitions handling
db_to_json(db_file, output_file)  # You can change the delimiter if needed

print(f"Data has been written to {output_file}")
