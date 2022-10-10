import asyncio

import aiohttp
import requests

async def get_price(pair: str, session) -> list:
    url = 'https://www.okx.com/priapi/v5/market/books'
    params = {
        'instId': pair,
        'sz': '10',
    }
    try:
        async with session.get(url=url, params=params) as response:
            data = await response.json()
            return [pair.split('-')[0], pair.split('-')[1], float(data['data'][0]['asks'][0][0]),
                    float(data['data'][0]['bids'][0][0]), 'OKX']
    except Exception as e:
        return [pair.split('-')[0], pair.split('-')[1], 0, 0, 'OKX']


async def spot_okx() -> list:
    url_pair = 'https://www.okx.com/priapi/v5/public/simpleProduct'
    params = {
        't': '1657371154432',
        'instType': 'SPOT',
    }

    spot_pair = []
    resp = requests.get(url=url_pair, params=params)
    data = resp.json()
    for el in data['data']:
        spot_pair.append(el['instId'])

    tasks = []
    async with aiohttp.ClientSession() as session:
        for pair in spot_pair:
            tasks.append(get_price(pair, session))
        spot_okx = await asyncio.gather(*tasks)

    return spot_okx

