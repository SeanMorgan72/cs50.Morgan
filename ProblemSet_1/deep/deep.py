def main():
    #Prompt the user for their answer
    answer = input("What is the answer to the Greatest Question of life, "+
                   "the Universe and Everything? ").strip()
    
    #Check if the input matches 42, forty-two, or forty two
    print("Yes") if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two" else print("No")
    
#Call main function
if __name__ == "__main__":
    main()
