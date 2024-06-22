"""
    Main function to prompt the user to input a fruit name and output the number of calories
    in one portion of that fruit according to the FDA's poster for fruits.
"""

def main():
    # Dictionary with fruit names and their corresponding calories
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Prompt the user to input the name of a fruit
    fruit_input = input("Item: ").strip().lower()

    # Check if the fruit is in the dictionary and output the calories
    if fruit_input in fruit_calories:
        print(f"Calories: {fruit_calories[fruit_input]} ")
    else:
        print(end='') 

if __name__ == "__main__":
    main()
