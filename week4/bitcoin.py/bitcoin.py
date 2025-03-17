import requests
import sys

URL = f'https://api.coincap.io/v2/assets/bitcoin'


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(bitcoin_price(n))
        except ValueError:
            sys.exit('Command-line argument is not a number!')
    else:
        sys.exit('Missing command-line argument')


def bitcoin_price(num):
    try:
        response = requests.get(URL)
        result = response.json()
        price = result["data"]["priceUsd"]
        total = float(price) * num
        return f"${total:,.4f}"
    except requests.RequestException:
        return None

if __name__ == '__main__':
    main()
