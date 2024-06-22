def main():
# Define the target amount and accepted denominations
    target_amount = 50
    accepted_coins = [25, 10, 5]
    total_inserted = 0

    # Continue prompting the user until the total inserted amount is at least the target amount
    while total_inserted < target_amount:
        print(f"Amount Due: {target_amount - total_inserted}")
        try:
            coin = int(input("Insert coin: "))
            if coin in accepted_coins:
                total_inserted += coin
            else:
                print(f"Amount Due: {target_amount - total_inserted}")
        except ValueError:
            print("Invalid input. Please insert an integer value.")

    # Calculate and display the change
    change = total_inserted - target_amount
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
