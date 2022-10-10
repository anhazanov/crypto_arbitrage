import requests


async def spot_exmo() -> list:
    url = 'https://api.exmo.com/v1.1/ticker'
    resp = requests.post(url=url)

    spot_exmo = []
    for key, value in resp.json().items():
        spot_exmo.append([
            key.split('_')[0],
            key.split('_')[1],
            value['sell_price'],
            value['buy_price'],
            'Exmo'
        ])

    return spot_exmo
