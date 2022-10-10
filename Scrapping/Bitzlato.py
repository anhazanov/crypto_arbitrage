import asyncio

import requests
import aiohttp


async def get_price(pair: str, session) -> list:
    url = f'https://bitzlato.bz/api/v2/peatio/public/markets/{pair}/order-book'
    try:
        async with session.get(url=url) as response:
            data = await response.json()
            print(data)
            return [pair.split('-')[0].upper(), pair.split('-')[1].upper(),
                    float(data['asks'][0]['price']),
                    float(data['bids'][0]['price']), 'Bitzlato']
    except Exception as e:
        print(e)


async def spot_bitzlato() -> list:
    url_pair = 'https://bitzlato.bz/api/v2/peatio/public/markets/tickers'
    response = requests.get(url=url_pair)

    pair_list = []
    for pair in response.json().keys():
        pair_list.append(pair)


    tasks = []
    async with aiohttp.ClientSession() as session:
        for pair in pair_list:
            tasks.append(get_price(pair, session))
        spot_bitzlato = await asyncio.gather(*tasks)

    print(spot_bitzlato)

    # url_price = 'https://bitzlato.bz/api/v2/peatio/public/markets/btc_usdt/order-book'
    # resp = requests.get(url=url_price)
    # all_price = resp.json()
    # print(all_price)


    # spot_bitzlato = []
    # for key, value in all_price.items():
    #     spot_bitzlato.append([
    #         key.split('_')[0].upper(),
    #         key.split('_')[1].upper(),
    #         float(value['ticker'].get(''))
    #     ])