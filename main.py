import requests
import json

with open("RUT_1000_tickers.csv", "r") as tickers:
    for ticker in tickers:
        ticker = ticker.strip()

        endpoint = "https://api.schwabapi.com/marketdata/v1/pricehistory?symbol="+ticker+"&periodType=year&period=20&frequencyType=monthly&frequency=1"
        headers = {
            "Authorization": ""}

        candles = requests.get(endpoint, headers=headers).json()

        output = {}

        for x in candles['candles']:
            key = x['datetime']
            del x['datetime']
            output[key] = x

        with open("C:/Users/tyler/OneDrive/Desktop/Financial Statement Analysis/StatementDB/" + ticker + "/" + ticker + "_candles.json", "w+") as test:
            test.seek(0)  # <- This is the missing piece
            test.truncate()
            json.dump(output, test, indent=4, sort_keys=True)

