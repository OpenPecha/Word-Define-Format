from WordDefine.utils import create_dir
from WordDefine.word_def_curl import text_to_json_with_first_curly_braces


def test_word_def_curl():
    # Define the file paths
    input_file = "tests/data/input/tibetan_dictionaries/42-བསྡུས་གྲྭའི་མཚན་ཉིད།.txt"  # noqa  # Replace with your actual text file
    output_file = (
        "tests/data/output/42-བསྡུས་གྲྭའི་མཚན་ཉིད།/42-བསྡུས་གྲྭའི་མཚན་ཉིད།.json"
    )
    create_dir(output_file)
    # Convert text to JSON
    text_to_json_with_first_curly_braces(input_file, output_file)


if __name__ == "__main__":
    test_word_def_curl()
