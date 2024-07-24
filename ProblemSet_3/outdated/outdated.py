import re
from datetime import datetime

def main():
    valid_date = get_valid_date()
    
    print(f"Formatted date: {valid_date}")

def get_valid_date():
    months = [
        "January", "February", "March", "April", "May",
        "June", "July", "August", "September", "October",
        "November", "December"
    ]
    
    while True:
        date_input = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ").strip()
        
        # Check for format MM/DD/YYYY
        match_mdY = re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', date_input)
        if match_mdY:
            try:
                date_obj = datetime.strptime(date_input, '%m/%d/%Y')
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                pass  # Invalid date

        # Check for format Month D, YYYY
        match_mdY = re.match(rf'^({"|".join(months)}) \d{{1,2}}, \d{{4}}$', date_input)
        if match_mdY:
            try:
                date_obj = datetime.strptime(date_input, '%B %d, %Y')
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                pass  # Invalid date
        
        print("Invalid date format. Please try again.")

main()