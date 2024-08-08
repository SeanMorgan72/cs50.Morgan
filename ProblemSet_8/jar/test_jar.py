import pytest
from jar import Jar

def test_initial_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    assert str(jar) == ""

def test_custom_capacity():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-5)

    with pytest.raises(ValueError):
        Jar("ten")

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    jar.deposit(4)
    assert jar.size == 9
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(2)  # Exceeds capacity

def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4
    assert str(jar) == "🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.withdraw(5)  # Not enough cookies

def test_string_representation():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

if __name__ == "__main__":
    pytest.main()