from datetime import date, datetime
import sys

def main():
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    today = date.today()
    age_in_minutes = calculate_age_in_minutes(dob, today)

    age_in_words = number_to_words(age_in_minutes)
    print(f"{age_in_words} minutes")

def calculate_age_in_minutes(birth_date, current_date):
    delta = current_date - birth_date
    return delta.days * 24 * 60

def number_to_words(n):
    def one(num):
        switcher = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
            14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
            18: "eighteen", 19: "nineteen"
        }
        return switcher.get(num)

    def two_less_20(num):
        return one(num)

    def tens(num):
        switcher = {
            2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
            6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
        }
        return switcher.get(num)

    def two(num):
        if not num:
            return ""
        elif num < 20:
            return two_less_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            return f"{tens(tenner)}{'-' + one(rest) if rest else ''}"

    def three(num):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return f"{one(hundred)} hundred {two(rest)}"
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return f"{one(hundred)} hundred"

    def num_to_words(num):
        if num == 0:
            return "zero"
        elif num < 100:
            return two(num)
        elif num < 1000:
            return three(num)
        elif num < 1000000:
            thousand = num // 1000
            rest = num - thousand * 1000
            if thousand and rest:
                return f"{three(thousand)} thousand, {three(rest)}"
            elif not thousand and rest:
                return three(rest)
            elif thousand and not rest:
                return f"{three(thousand)} thousand"
        else:
            million = num // 1000000
            rest = num - million * 1000000
            if million and rest:
                return f"{three(million)} million, {num_to_words(rest)}"
            elif not million and rest:
                return num_to_words(rest)
            elif million and not rest:
                return f"{three(million)} million"

    words = num_to_words(n)
    words = words.capitalize()

    return words

if __name__ == "__main__":
    main()
