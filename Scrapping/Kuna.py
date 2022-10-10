import requests


async def spot_kuna() -> list:
    url = 'https://api.kuna.io/v3/markets'
    resp = requests.get(url=url)

    pair_list = []
    for pair in resp.json():
        pair_list.append([pair['base_unit'], pair['quote_unit']])

    url_price = 'https://api.kuna.io/v3/tickers?symbols=ALL'
    resp = requests.get(url=url_price)

    spot_kuna = []
    for el in resp.json():
        for pair in pair_list:
            if el[0] == ('').join(pair):
                spot_kuna.append([
                    pair[0].upper(),
                    pair[1].upper(),
                    float(el[3]),
                    float(el[1]),
                    'Kuna'
                ])

    return spot_kuna