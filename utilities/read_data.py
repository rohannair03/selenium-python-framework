# Import CSV
import csv

def getCSVData(filename):
    # Create empty list
    rows = []
    # Open CSV
    dataFile = open(filename, "r")
    # Create a CSV reader from CSV file
    reader = csv.reader(dataFile)
    # Skip the headers
    next(reader)
    # Add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows