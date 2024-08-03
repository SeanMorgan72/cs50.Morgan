import sys

def main():
    # Check if the command-line has the right number of arguments.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
        
    # Get the filename from the command-line arguments.
    filename = sys.argv[1]
    
    # Check if the argument is a Python file.
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")
        
    # Print the number of lines of code in the file by calling the count_lines function.
    print(count_lines(filename))

def count_lines(filename):
    # Open the file in read mode, then read all the lines from the file.
    # Exit the program with an error message if the file does not exist.
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit(f"File does not exist")

    code_lines = 0
    
    # Iterate over each line in the file, while striping the leading and 
    # trailing whitespaces from the line.
    # Check if the line is not empty and does not start with a comment.
    # Increment the counter for lines of code.
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            code_lines += 1

    # Return the number of lines of code
    return code_lines

if __name__ == "__main__":
    main()