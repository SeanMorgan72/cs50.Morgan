class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._cookies += n

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

def main():
    # Create a jar with a capacity of 12 cookies
    jar = Jar()

    # Display the initial state of the jar
    print(f"Initial jar: {jar}")

    # Deposit 5 cookies
    jar.deposit(5)
    print(f"After depositing 5 cookies: {jar} (Size: {jar.size})")

    # Withdraw 3 cookies
    jar.withdraw(3)
    print(f"After withdrawing 3 cookies: {jar} (Size: {jar.size})")

    # Attempt to deposit 10 cookies, should raise an error due to exceeding capacity
    try:
        jar.deposit(10)
    except ValueError as e:
        print(f"Error: {e}")

    # Withdraw more cookies than in the jar, should raise an error
    try:
        jar.withdraw(10)
    except ValueError as e:
        print(f"Error: {e}")

    # Final state of the jar
    print(f"Final jar: {jar} (Size: {jar.size})")

if __name__ == "__main__":
    main()
