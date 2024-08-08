import pytest
from datetime import date
from seasons import calculate_age_in_minutes, number_to_words

def test_calculate_age_in_minutes():
    # Test case 1: birth date is today
    assert calculate_age_in_minutes(date(2024, 8, 7), date(2024, 8, 7)) == 0

    # Test case 2: birth date one day ago
    assert calculate_age_in_minutes(date(2024, 8, 6), date(2024, 8, 7)) == 1440

    # Test case 3: birth date one year ago (non-leap year, but spans a leap year)
    assert calculate_age_in_minutes(date(2023, 8, 7), date(2024, 8, 7)) == 366 * 24 * 60

    # Test case 4: birth date one year ago (leap year)
    assert calculate_age_in_minutes(date(2020, 8, 7), date(2021, 8, 7)) == 365 * 24 * 60

def test_number_to_words():
    # Test case 1: converting zero
    assert number_to_words(0) == "Zero"

    # Test case 2: converting single digits
    assert number_to_words(7) == "Seven"

    # Test case 3: converting two digits less than 20
    assert number_to_words(13) == "Thirteen"

    # Test case 4: converting two digits greater than or equal to 20
    assert number_to_words(85) == "Eighty-five"

    # Test case 5: converting three digits
    assert number_to_words(123) == "One hundred twenty-three"

    # Test case 6: converting four digits
    assert number_to_words(2024) == "Two thousand, twenty-four"

    # Test case 7: edge case for round number in thousands
    assert number_to_words(2000) == "Two thousand"

    # Test case 8: large number
    assert number_to_words(123456) == "One hundred twenty-three thousand, four hundred fifty-six"

    # Test case 9: very large number
    assert number_to_words(123456789) == "One hundred twenty-three million, four hundred fifty-six thousand, seven hundred eighty-nine"

if __name__ == "__main__":
    pytest.main()
