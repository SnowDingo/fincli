import requests

# when using we need to append the currency code
url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies'

def fetchCurrentExchangeRate(old, newcurrency):
    urltemp = url + "/" + old+ ".json"
    response = requests.get(urltemp)
    # res is response in json
    if response.status_code == 200:
        res = response.json()
        return res.get(old).get(newcurrency)
    else:
        print("**DATA FETCH FAILED!!**")
        return

def fetchAllAvailableCurrencies():
    urlnew = url + ".json"
    response = requests.get(urlnew)
    if response.status_code == 200:
        res = response.json()
        keysarr = list(res.keys())
        valarr = list(res.values())
        result = ""
        for i in range(0,len(keysarr)):
            result = result + "\n" + keysarr[i] + ":" + valarr[i]
        return result
    return