import json

from . import comissions

async def sell(balance, possition, *args):
    ask, bid = args[0]
    if float(bid) != 0:
        return balance * float(bid) * (1 - comissions.spot_comission[possition])
    else:
        return 0


async def buy(balance, possition, *args):
    ask, bid = args[0]
    if float(ask) != 0:
        return balance / float(ask) * (1 - comissions.spot_comission[possition])
    else:
        return 0


async def withdraw(exchange: str, balance:  float, currience: str, commissions: dict) -> list:
    for key in commissions['Binance'].keys():
        if key == currience:
            for value in commissions['Binance'][key].values():
                if value is not None:
                    return [exchange, (balance - float(value))]



async def main_arbitrage(spot_price: list):
    data_db = []

    start_balance = 100
    start_currience = 'USDT'

    with open('comission.json', 'r') as file:
        withdraw_fee = json.load(file)

    for trade1 in spot_price:
        match trade1:
            case [currience, currience1, *args, position1] if currience == start_currience:
                balance1 = await sell(start_balance, position1, args)
                rate1 = args[1]
            case [currience1, currience, *args, position1] if currience == start_currience:
                balance1 = await buy(start_balance, position1, args)
                rate1 = args[0]
            case _:
                continue

        for key in withdraw_fee.keys():
            match key:
                case exchange if exchange == position1:
                    try:
                        position2, balance2 = await withdraw(exchange, balance1, currience1, withdraw_fee)
                    except TypeError as e:
                        print('ERROR - ', e)
                case _:
                    continue

            for trade3 in spot_price:
                match trade3:
                    case [currience, currience3, *args, position3] if currience == currience1 and position1 != position3:
                        balance3 = await sell(balance2, position3, args)
                        rate3 = args[1]
                    case[currience3, currience, *args, position3] if currience == currience1 and position1 != position3:
                        balance3 = await buy(balance2, position3, args)
                        rate3 = args[0]
                    case _:
                        continue
                if currience3 == start_currience:
                    profit = round((balance3 - start_balance) / start_balance * 100, 2)
                    if 10 > profit > 0:
                        data_db.append([profit, f'{position1}>{position3}', f'{start_currience}>{currience1}>{currience3}',
                                        f'{rate1}>{rate3}', f'{balance1}>{balance3}'])

    data_db = sorted(data_db, key=lambda x: x[0], reverse=True)
    print(data_db)