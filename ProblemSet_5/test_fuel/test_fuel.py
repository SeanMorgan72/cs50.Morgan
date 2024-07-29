import pytest
from fuel import convert, gauge

def test_convert():
    # Test valid inputs
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("2/3") == 67
    assert convert("99/100") == 99

    # Test rounding
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("1/4") == 25

    # Test invalid inputs
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    # Test boundary conditions
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

    # Test other conditions
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"

if __name__ == "__main__":
    pytest.main()
