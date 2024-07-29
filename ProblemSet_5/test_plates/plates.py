def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if length is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if it starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters
    if not s.isalnum():
        return False

    # Check numbers position and rules
    if any(char.isdigit() for char in s):
        first_digit_index = next((i for i, char in enumerate(s) if char.isdigit()), None)
        if first_digit_index is not None:
            # Ensure numbers are at the end
            for char in s[first_digit_index:]:
                if not char.isdigit():
                    return False
            # Ensure the first number is not '0'
            if s[first_digit_index] == '0':
                return False

    return True

if __name__ == "__main__":
    main()