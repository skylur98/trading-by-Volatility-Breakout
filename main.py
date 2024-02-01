import pyupbit
import pprint

f = open("upbitkey.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

balance = upbit.get_balance("KRW")
print(balance)








