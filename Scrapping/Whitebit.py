import requests


async def spot_whitebit() -> list:
    url = 'https://whitebit.com/api/v2/public/ticker'
    resp = requests.get(url=url)

    print(resp.json()['result'][0])
    spot_rates = []
    for el in resp.json()['result']:
        if el['tradesEnabled'] == True:
            stock, money = el['tradingPairs'].split('_')
            spot_rates.append([
                stock, money, float(el['lowestAsk']), float(el['highestBid']), 'Whitebit'
            ])
    return spot_rates


