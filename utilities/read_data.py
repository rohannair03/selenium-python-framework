# Import CSV
import csv
import os

def getCSVData(filename):
    rows = []
    with open(filename, "r") as dataFile:
        reader = csv.reader(dataFile)
        next(reader)  # Skip headers
        for row in reader:
            rows.append(row)
    return rows

def getCSVDataRelative(relative_path="testdata.csv"):
    """
    Resolves path relative to the project root (two levels up from this file).
    Use this instead of hardcoding absolute paths.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(base_dir, relative_path)
    return getCSVData(filename)