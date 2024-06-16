def main():
    # Prompt the user for a greeting
    greeting = input("Enter a greeting: ").strip().lower()

    # Use match case for the conditions
    match greeting:
        case g if g.startswith("hello"):
            print("$0")
        case g if g.startswith("h"):
            print("$20")
        case _:
            print("$100")

if __name__ == "__main__":
    main()
