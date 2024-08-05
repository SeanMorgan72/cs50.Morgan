import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression to match a valid IPv4 address
    pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")

    # Check if the input matches the pattern
    if pattern.match(ip):
        # Split the input into octets
        octets = ip.split(".")

        for octet in octets:
            # Check each octet to ensure it's between 0 and 255
            if not (0 <= int(octet) <= 255):
                return False
        return True
    return False


if __name__ == "__main__":
    main()