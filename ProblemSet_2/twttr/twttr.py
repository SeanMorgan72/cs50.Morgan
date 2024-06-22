"""
    Remove vowels from the input text.
    
    Args:
    text (str): The input string from which vowels will be removed.
    
    Returns:
    str: The string after removing all vowels (A, E, I, O, U) regardless of case.
"""

def remove_vowels(text):
    # Define a string containing all vowels in uppercase and lowercase
    vowels = "AEIOUaeiou"
    # Use a list comprehension to filter out vowels and join the remaining 
    # characters into a new string
    return ''.join([char for char in text if char not in vowels])
"""
    Main function to execute the vowel removal process.
"""
def main():
    #Prompt the user to enter some text
    user_input = input("Enter some text: ")
    # Call the remove_vowels function with the user input and store the result
    result = remove_vowels(user_input)
    # Print the result to the console
    print(result)

if __name__ == "__main__":
    main()
