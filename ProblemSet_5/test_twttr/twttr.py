def main():
    # Prompt the user to enter some text
    user_input = input("Enter some text: ")
    # Call the shorten function with the user input and store the result
    result = shorten(user_input)
    # Print the result to the console
    print(result)

def shorten(word):
    """
    Remove vowels from the input text.

    Args:
    word (str): The input string from which vowels will be removed.

    Returns:
    str: The string after removing all vowels (A, E, I, O, U) regardless of case.
    """
    # Define a string containing all vowels in uppercase and lowercase
    vowels = "AEIOUaeiou"
    # Use a list comprehension to filter out vowels and join the remaining
    # characters into a new string
    return ''.join([char for char in word if char not in vowels])

if __name__ == "__main__":
    main()