import pytest
from twttr import shorten

def test_shorten_vowels_only():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_no_vowels():
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_shorten_mixed_characters():
    assert shorten("Hello, World!") == "Hll, Wrld!"

def test_shorten_uppercase_vowels():
    assert shorten("AEIOU") == ""

def test_shorten_lowercase_vowels():
    assert shorten("aeiou") == ""

def test_shorten_mixed_case_vowels():
    assert shorten("AeIoU") == ""

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_numbers_and_punctuation():
    assert shorten("12345!@#$%") == "12345!@#$%"

def test_shorten_sentence():
    assert shorten("This is a test sentence.") == "Ths s  tst sntnc."

if __name__ == "__main__":
    pytest.main()
