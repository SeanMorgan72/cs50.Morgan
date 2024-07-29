def main():
    # Prompt the user for a greeting
    greeting = input("Enter a greeting: ").strip()

    # Calculate the value based on the greeting
    result = value(greeting)

    # Print the result
    print(f"${result}")

def value(greeting):
    # Convert greeting to lowercase for case-insensitive comparison
    greeting = greeting.lower()

    # Determine the value based on the greeting
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()