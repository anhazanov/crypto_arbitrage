import asyncio
import time

from . import Binance, Whitebit, Huobi, Bybit, OKX, Kucoin, Kuna, Exmo


async def main_scrapping() -> list:
    start = time.time()
    total_spot = []
    total_spot += await Binance.spot_binance()
    total_spot += await Whitebit.spot_whitebit()
    # total_spot += await Huobi.spot_huobi()
    # total_spot += await Bybit.spot_bybit()
    # total_spot += await OKX.spot_okx()
    # total_spot += await Kucoin.spot_kucoin()
    # total_spot += await Kuna.spot_kuna()
    # total_spot += await Exmo.spot_exmo()


    # spot_bitzlato = await Bitzlato.spot_bitzlato() # Don't work

    print('Time: ', (time.time() - start), 'seconds')
    return total_spot
