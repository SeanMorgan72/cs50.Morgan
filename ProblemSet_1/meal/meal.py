def main():
    time_input = input("Enter the time in 24-hour format (HH:MM): ")
    
    # Validate the input format
    if not validate_time_format(time_input):
        print("Invalid time format. Please enter in HH:MM format.")
        return
    
    # Convert the time string to hours
    time_in_hours = convert(time_input)
    
    # Determine meal time
    if is_breakfast_time(time_in_hours):
        print("It's breakfast time!")
    elif is_lunch_time(time_in_hours):
        print("It's lunch time!")
    elif is_dinner_time(time_in_hours):
        print("It's dinner time!")

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time.split(":"))
    
    # Calculate the total hours
    total_hours = hours + (minutes / 60)
    
    return total_hours

def validate_time_format(time):
    try:
        hours, minutes = map(int, time.split(":"))
        if not (0 <= hours <= 23):
            return False
        if not (0 <= minutes <= 59):
            return False
        return True
    except ValueError:
        return False

def is_breakfast_time(hours):
    # Breakfast time is from 7:00 to 9:59
    return 7.0 <= hours < 10.0

def is_lunch_time(hours):
    # Lunch time is from 12:00 to 13:59
    return 12.0 <= hours < 14.0

def is_dinner_time(hours):
    # Dinner time is from 18:00 to 20:59
    return 18.0 <= hours < 21.0

if __name__ == "__main__":
    main()
