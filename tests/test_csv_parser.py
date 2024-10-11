import os

from WordDefine.csv_parser import csv_to_json


def test_csv_parser():
    csv_file = "tests/data/input/christiansteinert_tib_dictionaries/Common Chinese-Tibetan-English Buddhist Terminology (only Tib-En, Cleaned).csv"  # noqa
    json_file = "tests/data/output/Common_Chinese_Tibetan-English/Common_Chinese_Tibetan-English.json"
    json_file_dir = os.path.dirname(json_file)
    if not os.path.exists(json_file_dir):
        os.makedirs(json_file_dir)
    csv_to_json(csv_file, json_file)
