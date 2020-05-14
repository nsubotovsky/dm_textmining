import requests as rq
import datetime as dt
import pandas as pd
import numpy as np


class CoinDeskApi( object ):

    _API_LINK = "https://api.coindesk.com/v1/bpi/historical/close.json"

    def __init__(self):
        pass

    def getBetween(self, start=dt.datetime(2020,7,12), stop=None):
        stop = stop or dt.date.today()
        #url = self._buildUrl(start, stop)

        PARAMS = {"start": start,
                  "end": stop}

        r = rq.get(url=self._API_LINK, params=PARAMS)
        return r.json()["bpi"]



def main():
    ca = CoinDeskApi()
    res = ca.getBetween( dt.date(2020,5,1) )
    return res


#
#
#
# start =
# end = dt.now().strftime("%Y-%m-%d")
# URL = API_LINK + "?start=" + start + "&end=" + end
#
# API_Data = rq.get(API_LINK)
#
# PARAMS = {"start":start,
#           "end": end}
# r = rq.get(url = API_LINK, params = PARAMS)
# data = r.json()["bpi"]
#
#
# dates = np.array(list(data.keys()))
# dates = np.vectorize(lambda x: dt.strptime(x, "%Y-%m-%d"))(dates)
# prices = np.array(list(data.values()))
#
# bitcoin_price = pd.DataFrame({"Date": dates, "ClosePrice": prices})
#
# periods = 7
#
# bitcoin_price["Change"] = bitcoin_price["ClosePrice"].pct_change(periods=periods) * 100.0
# bitcoin_price = bitcoin_price.fillna(0)
# bitcoin_price
