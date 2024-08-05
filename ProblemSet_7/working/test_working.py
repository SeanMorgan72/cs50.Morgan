import pytest
from working import convert

def test_valid_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1:30 PM to 2:15 AM") == "13:30 to 02:15"
    assert convert("1 PM to 2:15 AM") == "13:00 to 02:15"
    assert convert("12:01 PM to 12:01 AM") == "12:01 to 00:01"

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("8:00 AM 4:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 AMM")
    with pytest.raises(ValueError):
        convert("9:00 XM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 9 PM PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 9:00 PM PM")

def test_edge_cases():
    assert convert("12:00 AM to 11:59 PM") == "00:00 to 23:59"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("11:59 AM to 12:00 PM") == "11:59 to 12:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"

if __name__ == "__main__":
    pytest.main()
