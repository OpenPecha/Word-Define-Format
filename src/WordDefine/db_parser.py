import sqlite3
from collections import defaultdict
from WordDefine.utils import save_json,create_dir
def db_to_json(db_file: str, output_file: str):
    """
    Convert a SQLite database table to JSON format by extracting word-definition pairs from the columns 'tb_key' and 'def_dic'.
    Multiple definitions for the same word are stored in a list.

    Args:
        db_file (str): The path to the SQLite database file.
        output_file (str): The path where the resulting JSON file will be saved.
    
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

    save_json(result, filename=output_file)
    # Close the database connection
    conn.close()


# Define the SQLite DB file and output JSON file
db_file = 'data/input/dictionarys/Tb_En_Dic.db'  # Replace with the actual path to your SQLite database
output_file = 'data/output/Tb_En_Dic/Tb_En_Dic.json'
create_dir(output_file)

# Convert DB to JSON
db_to_json(db_file, output_file)

print(f"Data has been written to {output_file}")

