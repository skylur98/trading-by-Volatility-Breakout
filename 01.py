import pyupbit
import time
import datetime

def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high']-yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

f = open("upbitkey.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

target = cal_target("KRW-BTC")
op_mode = False
hold = False


while True:
    now = datetime.datetime.now()

    if now.hour == 8 and now.minute == 59 and 50 <= now.second <= 59:
        if op_mode is True and hold is True:
            btc_balance = upbit.get_balance("KRW-BTC")
            upbit.sell_market_order("KRW-BTc", btc_balance)
            hold = False
    op_mode = False
    #time.sleeo(10)

    if now.hour == 9 and now.minute == 0 and 20<= now.second <=30:
        target = cal_target("KRW-BTC")
        op_mode = True

    price = pyupbit.get_current_price("KRW-BTC")

    if op_mode is True and hold is False and price >= target:
        krw_balance=upbit.get_balance("KRw")
        upbit.buy_market_order("KRW-BTC", krw_balance)
        hold = True

    print(f"시간 : {now} 목표가 : {target} 현재가 : {price} 보유상태 : {hold} 동작상태 : {op_mode} ")




    time.sleep(1)

