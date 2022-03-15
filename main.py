import requests
import json
from datetime import datetime

class Stock:

    def __init__(self, symbol):
        self.symbol = symbol

    def out(self,symbol):
        url1=f"https://finnhub.io/api/v1/quote?symbol={self.symbol}&token=c8nqqc2ad3iep4jecnt0" #url for all numerical data required
        url2=f"https://finnhub.io/api/v1/stock/profile2?symbol={self.symbol}&token=c8nqqc2ad3iep4jecnt0" #url for name of the compmany
        r1=requests.get(url1)
        r2=requests.get(url2)

        r3=json.loads(r2.text)
        r4 = json.loads(r1.text)

        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Current date and time =", dt_string)
        print(r3["name"])
        print(str(r4["c"]) + " " + str(r4["d"]) + '('+str(r4["dp"])+'%'+')')

s = input("Enter Stock symbol: ")

try:
    x = Stock(s)
except Exception as e:
    print(e)
x.out(s)