def convert(text):
    '''
    Converts emoticons in the input text to corresponding emojis.
    
    Args:
    text (str): The input text containing emoticons.
    
    Returns:
    str: The text with emoticons converted to emojis.
    
    '''
    modified_text = text.replace(":)", "🙂")
    modified_text = modified_text.replace(":(", "🙁")
    return modified_text

def main():
    """
    Prompts the user for input, converts any emoticons in the input to emojis,
    and prints the result.
    
    """
    user_input = input("")
    result = convert(user_input)
    print(result)

#Call the main function
if __name__ == "__main__":
    main()