import requests


async def spot_kucoin() -> list:
    url = 'https://api.kucoin.com/api/v1/market/allTickers'
    response = requests.get(url=url)
    data = response.json()

    spot_kucoin = []
    for pair in data['data']['ticker']:
        ticker = pair['symbol']
        spot_kucoin.append([ticker.split("-")[0], ticker.split("-")[1], float(pair['sell']), float(pair['buy']),
                            'Kucoin'])
    return spot_kucoin
