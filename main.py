import asyncio

from Scrapping import main_scrapping
from Comissions import main_fee
from Arbitrage import main_arbitrage

async def main():
    spot_price = await main_scrapping()
    # await main_arbitrage(spot_price)

    # await main_fee()


if __name__ == '__main__':
    asyncio.run(main())
