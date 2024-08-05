import validator

def main():
    email = input("Please enter an email address: ")
    if validator.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()