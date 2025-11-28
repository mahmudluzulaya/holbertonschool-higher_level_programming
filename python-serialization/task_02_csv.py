#!/usr/bin/python3
"""Convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into JSON format and writes it to data.json.
    Returns True on success, False on failure.
    """
    try:
        data_list = []

        # Read CSV file
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Write to JSON file
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False
