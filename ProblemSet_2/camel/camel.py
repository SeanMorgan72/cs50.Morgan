def camel_to_snake(name):
    """
    Convert a camel case string to snake case.
    
    Parameters:
    name (str): A camel case string.
    
    Returns:
    str: The corresponding snake case string.
    """

    snake_case = ''
    for char in name:
        if char.isupper():
            if snake_case:  # To avoid adding underscore at the start
                snake_case += '_'
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    """
    Main function to prompt user for a camel case variable name
    and output the corresponding snake case variable name.
    """
    # Get user input
    camel_case_name = input("camelCase: ")
    # Convert to snake case
    snake_case_name = camel_to_snake(camel_case_name)
    # Print the result
    print("snake_case:", snake_case_name)

if __name__ == "__main__":
    main()
