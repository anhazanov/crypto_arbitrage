import requests


async def spot_huobi() -> list:
    url_pair = 'https://api.huobi.pro/v2/settings/common/symbols'
    url_price = 'https://api.huobi.pro/market/tickers'

    resp = requests.get(url=url_pair)
    data_pair = resp.json()['data']
    pair_list = []
    for el in data_pair:
        pair = el['dn']
        pair_list.append([pair, pair.split('/')[0], pair.split('/')[1]])

    resp = requests.get(url=url_price)
    all_price = resp.json()['data']
    spot_price = []
    for el in all_price:
        for pair in pair_list:
            if el['symbol'] == pair[0].replace('/', '').lower():
                spot_price.append([pair[1], pair[2], float(el['ask']), float(el['bid']), 'Huobi'])

    return spot_price
