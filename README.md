# Stock Price Aggregator

## Description

Aggregate stock prices for companies listed in the Russel 1000 via the Schwab Developer API.

## Instructions

1. Delete temp_ticker.json
2. Copy an index holding csv from the IndexHoldingsAggregator project to the root of this project
3. Login to Schwab Developer Portal with developer account (https://developer.schwab.com)
4. Select 'API Products' tab
5. Locate 'Trader API - Individual' tile
6. Locate 'Market Data Production' tile
7. Click the 'Authorize' button
8. Login with Schwab investment account
9. Retrieve Bearer Token from the CURL command generated by trying out one of the swagger endpoints
10. Place the Bearer Token in main.py

