import sys
import collections

def main():
    # Using collections.Counter to count items
    grocery_list = collections.Counter()

    print("Enter items for your grocery list. Press Ctrl-D (or Ctrl-Z on Windows) to finish.")

    try:
        while True:
            item = input().strip().lower()
            if item:
                grocery_list[item] += 1
    except EOFError:
        pass

    # Sorting items alphabetically and converting to uppercase
    sorted_items = sorted(grocery_list.items())

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

    # Exit with code 0
    sys.exit(0)

main()

