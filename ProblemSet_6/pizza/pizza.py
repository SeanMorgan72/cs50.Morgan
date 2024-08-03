import sys
import os
import csv
from tabulate import tabulate

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Get the filename from the command-line argument
    filename = sys.argv[1]

    # Check if the file has a .csv extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit("The file does not exist")

    # Read the CSV file and store the contents
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
    except Exception as e:
        sys.exit(f"Could not read the file. {e}")

    # Use tabulate to format the data as a table
    table = tabulate(data, headers="firstrow", tablefmt="grid")

    # Print the formatted table
    print(table)

if __name__ == "__main__":
    main()