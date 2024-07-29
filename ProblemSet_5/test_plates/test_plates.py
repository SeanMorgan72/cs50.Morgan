import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("AB123") == True
    assert is_valid("ABC123") == True
    assert is_valid("AB") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("") == False

def test_invalid_start():
    assert is_valid("1ABC") == False
    assert is_valid("A1BC") == False
    assert is_valid("12ABC") == False
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("12AB") == False
    assert is_valid("A1BC") == False

def test_invalid_characters():
    assert is_valid("AB@123") == False
    assert is_valid("ABC 123") == False
    assert is_valid("AB#123") == False

def test_invalid_number_rules():
    assert is_valid("AB0123") == False
    assert is_valid("ABC12A") == False
    assert is_valid("AB12C3") == False

def test_valid_number_positions():
    assert is_valid("AB123") == True
    assert is_valid("AB12") == True
    assert is_valid("AB1") == True

if __name__ == "__main__":
    pytest.main()
