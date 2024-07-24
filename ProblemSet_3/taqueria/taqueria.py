menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_cost = 0.0
    print("Welcome to Felipe’s Taqueria! Enter your items one at a time. Press Ctrl-D (or Ctrl-Z on Windows) to finish.")

    while True:
        try:
            item = input("Item: ").strip().title()
            if item in menu:
                total_cost += menu[item]
                print(f"Total: ${total_cost:.2f}")
            else:
                print(f"{item} is not on the menu.")
        except EOFError:
            print("\nThank you for your order!")
            break

main()