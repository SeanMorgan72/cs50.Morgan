import pytest
from um import count

def test_single_um():
    assert count("um") == 1

def test_um_in_sentence():
    assert count("Hello, um, world") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3

def test_um_at_boundaries():
    assert count("um, um, yummy, um") == 3

def test_um_case_insensitive():
    assert count("Um, UM, uM, um") == 4

def test_um_as_substring():
    assert count("yummy, umbrella, autumn") == 0

if __name__ == "__main__":
    pytest.main()