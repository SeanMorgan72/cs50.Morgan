import pytest
from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("8.8.8.8") == True

def test_invalid_ips():
    assert validate("256.256.256.256") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.-1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("192.168.1") == False
    assert validate("abc.def.ghi.jkl") == False

def test_invalid_formats():
    assert validate("") == False
    assert validate("192.168.1.") == False
    assert validate(".192.168.1.1") == False
    assert validate("192.168..1") == False
    assert validate("192..168.1.1") == False
    assert validate("192.168.1.1.") == False
    assert validate(" 192.168.1.1") == False
    assert validate("192.168.1.1 ") == False
    assert validate("192.168. 1.1") == False

if __name__ == "__main__":
    pytest.main()