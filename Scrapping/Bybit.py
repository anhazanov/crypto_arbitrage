import requests


async def spot_bybit():
    url_1 = 'https://api.bybit.com/spot/v1/symbols'
    pair_list = []
    resp = requests.get(url=url_1)
    data_pair = resp.json()['result']
    for el in data_pair:
        pair_list.append([el['baseCurrency'], el['quoteCurrency']])

    url_2 = 'https://api.bybit.com/spot/v3/public/quote/ticker/bookTicker'
    resp = requests.get(url=url_2)
    data_price = resp.json()['result']['list']

    spot_bybit = []
    for el in data_price:
        for pair in pair_list:
            if el.get('symbol') == ('').join(pair):
                spot_bybit.append([pair[0], pair[1], float(el['askPrice']), float(el['bidPrice']), 'Bybit'])

    return spot_bybit
