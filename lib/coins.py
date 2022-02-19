import cryptocompare as cc


def Return_List_Of_Types():
    return cc.get_coin_list()

def GetPrice(coinMod:str,ToModCoin='USD'):
    return cc.get_price(coinMod,ToModCoin)
def Get_Info_From_Coin(coinMod:str):
    return cc.get_avg(coinMod)
def GetOnlinePriceNow(coinMod:str,ToModCoin='USD'):
    return cc.get_historical_price(coinMod,ToModCoin)
def GetOnlinePriceDay(coinMod:str,ToModCoin='USD'):
    return cc.get_historical_price_day(coinMod,ToModCoin)
def GetOnlinePriceHour(coinMod:str,ToModCoin='USD'):
    return cc.get_historical_price_hour(coinMod,ToModCoin)
def GetOnlinePriceMinute(coinMod:str,ToModCoin='USD'):
    return cc.get_historical_price_minute(coinMod,ToModCoin)
def GetExchanges():
    return cc.get_exchanges()
def GetExchangesInfo():
    return cc.get_pairs()



def GetStdPrice():
    best = ['BTC','ETH','BCH','LTC','BCH','DOT','ADA','DOGE','HEX','BNB']
    syntax = '''\t\t10 اپدیت جدید
نوع ارز  \t قیمت(USDT) \t روزانه \t هفتگی
1-{} \t {} \t {} \t {} 
2-{} \t {} \t {} \t {} 
3-{} \t {} \t {} \t {} 
4-{} \t {} \t {} \t {} 
5-{} \t {} \t {} \t {} 
6-{} \t {} \t {} \t {} 
7-{} \t {} \t {} \t {} 
8-{} \t {} \t {} \t {} 
9-{} \t {} \t {} \t {} 
10-{} \t {} \t {} \t {} 
'''
    print(syntax)
