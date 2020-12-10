import requests

try:
    while True:
        symbol = input("Enter the symbol of currency:(eg:EUR,JPY,NPR) ").upper()
        url = f"https://api.currencyfreaks.com/latest?apikey=9fc35b0d31f24b21b373045218753cd1&symbols={symbol}"
        res = requests.get(url)
        text = res.json()
        base = text['base']
        rates = text['rates'][f'{symbol}']
        print(f"Base: {base}'1'\nRate: {symbol}'{rates}'")
        usr_inp = input('Again(y/n?)').lower()
        if usr_inp == 'n':
            break
except:
    print("Enter a valid currency symbol!!")