import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)  # Exit with status code 1 on error

def convert(s):
    # Define the regular expression for matching the input string
    pattern = r"^(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError

    start_time, _, start_period, end_time, _, end_period = match.groups()

    start_24 = convert_to_24_hour(start_time, start_period)
    end_24 = convert_to_24_hour(end_time, end_period)

    return f"{start_24} to {end_24}"

def convert_to_24_hour(time, period):
    if ":" in time:
        hour, minute = map(int, time.split(":"))
    else:
        hour = int(time)
        minute = 0

    if not (0 <= hour <= 12 and 0 <= minute < 60):
        raise ValueError

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
