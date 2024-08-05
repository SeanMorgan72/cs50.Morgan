import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regex to find "um" as a whole word, case-insensitively
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()