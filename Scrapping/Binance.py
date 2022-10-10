import requests


async def spot_binance() -> list:
    url_1 = 'https://api.binance.com/api/v3/ticker/bookTicker'
    url = 'https://api.binance.com/api/v3/exchangeInfo'

    price_pair, pair_list = [], []

    resp_pair = requests.get(url=url)
    for el in resp_pair.json()['symbols']:
        if el['status'] == 'TRADING' and 'SPOT' in el['permissions']:
            pair_list.append([el['symbol'], el['baseAsset'], el['quoteAsset']])

    resp_price = requests.get(url=url_1)
    for pair in pair_list:
        for el in resp_price.json():
            if pair[0] == el['symbol']:
                price_pair.append([pair[1], pair[2], float(el['askPrice']), float(el['bidPrice']), float(el['askQty']),
                                   float(el['bidQty']), 'Binance'])
    return price_pair
