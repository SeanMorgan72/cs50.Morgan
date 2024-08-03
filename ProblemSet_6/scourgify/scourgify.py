import csv
import sys


def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Read the input CSV file
        with open(input_file, mode='r') as infile:
            reader = csv.DictReader(infile)
            data = []

            for row in reader:
                # Split the name into first and last
                last, first = row['name'].split(", ")
                data.append({"first": first, "last": last, "house": row['house']})

        # Write to the output CSV file
        with open(output_file, mode='w', newline='') as outfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
       sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()