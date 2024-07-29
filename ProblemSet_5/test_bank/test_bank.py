import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello world") == 0
    assert value("Hello World") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("howdy") == 20
    assert value("Hi") == 20
    assert value("HEY") == 20

def test_other():
    assert value("goodbye") == 100
    assert value("greetings") == 100
    assert value("what's up") == 100
    assert value("Good Morning") == 100
    assert value("Salutations") == 100

if __name__ == "__main__":
    pytest.main()