import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
df.to_excel("btc.xlsx")

