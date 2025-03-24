import requests
import json

# Period Type
# Available values : day, month, year, ytd
period_type = 'year'

# Period
# day - valid values are 1, 2, 3, 4, 5, 10
# month - valid values are 1, 2, 3, 6
# year - valid values are 1, 2, 3, 5, 10, 15, 20
# ytd - valid values are 1
period = '20'

# Frequency Type
# Available values : minute, daily, weekly, monthly
# If the periodType is
# day - valid freq type value is minute
# month - valid freq type values are daily, weekly
# year - valid freq type values are daily, weekly, monthly
# ytd - valid freq type values are daily, weekly
frequency_type = 'monthly'

# Frequency
# If the frequencyType is
# minute - valid values are 1, 5, 10, 15, 30
# daily - valid value is 1
# weekly - valid value is 1
# monthly - valid value is 1
frequency = '1'

with open("RUT_1000_tickers.csv", "r") as tickers:
    for ticker in tickers:
        ticker = ticker.strip()
        endpoint = f"https://api.schwabapi.com/marketdata/v1/pricehistory?symbol={ticker}&periodType={period_type}&period={period}&frequencyType={frequency_type}&frequency={frequency}"
        headers = {"Authorization": ""}

        candles = requests.get(endpoint, headers=headers).json()

        json_output = {}

        for x in candles['candles']:
            key = x['datetime']
            del x['datetime']
            json_output[key] = x

        file_path = "data/" + ticker + "_candles.json"

        with open(file_path, "w+") as output_file:
            output_file.seek(0)  # <- This is the missing piece
            output_file.truncate()
            json.dump(json_output, output_file, indent=4, sort_keys=True)

