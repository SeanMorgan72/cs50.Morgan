import sys
import requests

def main():
    # Check if the user provided the required command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument.")

    try:
        # Attempt to convert the argument to a float
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number.")

    # URL for the CoinDesk API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        # Query the API for the current Bitcoin price
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Extract the current price of Bitcoin in USD
        bitcoin_price_usd = data["bpi"]["USD"]["rate_float"]

        # Calculate the total cost
        total_cost = bitcoins * bitcoin_price_usd

        # Print the total cost formatted to 4 decimal places with thousands separator
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price from CoinDesk API.")

if __name__ == "__main__":
    main()