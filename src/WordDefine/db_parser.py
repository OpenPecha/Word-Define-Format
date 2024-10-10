import sqlite3
import json
from collections import defaultdict
import os

def db_to_json(db_file: str, output_file: str):
    """
    Convert database data into JSON format by extracting EnWord (word) and TbDef (definition).
    Handles multiple definitions by storing them in a list.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Use the correct table "EnToTb"
    table_name = "TbToEn"
    print(f"Using table: {table_name}")

    # Query the necessary columns (tb_key and def_dic) from the "EnToTb" table
    query = f"SELECT tb_key, def_dic FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Create a dictionary to store words and their definitions
    word_dict = defaultdict(list)

    # Iterate over the rows to collect word and definition
    for row in rows:
        word, definition = row[0].strip(), row[1].strip()
        word_dict[word].append(definition)

    # Convert dictionary to the required JSON format
    result = []
    for word, definitions in word_dict.items():
        result.append({
            "word": word,
            "definition": definitions  # Keep definitions as a list
        })

    # Write the result to a JSON file with the correct formatting
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    # Close the database connection
    conn.close()


# Define the SQLite DB file and output JSON file
db_file = 'data/input/dictionarys/Tb_En_Dic.db'  # Replace with the actual path to your SQLite database
output_file = 'data/output/Tb_En_Dic/Tb_En_Dic.json'
output_file_path = os.path.dirname(output_file)
if not os.path.exists(output_file_path):
    os.makedirs(output_file_path)

# Convert DB to JSON
db_to_json(db_file, output_file)

print(f"Data has been written to {output_file}")

