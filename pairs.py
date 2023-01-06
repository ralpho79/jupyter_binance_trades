# Get more info on https://python-binance.readthedocs.io/en/latest/general.html

# init
import csvfile
import time
#import os
from binance.client import Client

api_key = "ucqMzmbqswWPqo4bfQp4DoPyUTFIV2wO749sXmAPyIqwkA4vKQKSO6CZKAPi3DEA"
api_secret = "KRQYhVnepPwutIprQmxyDbugCGCNMkr7WL3Cm7zqQoK9GIuGdLJQpoJqIooTqWnY"

client = Client(api_key, api_secret)
# This master list collects dictionaries - pair symbols with base and quote assets
my_pairs = []
    
def load_pairs():

    ### STEP 1: Load all Binance pairs

    all_tickers = client.get_all_tickers()

    for info in all_tickers:
        my_pairs.append(dict(symbol=info['symbol']))
        
    print(len(my_pairs), 'Binance pairs found and loaded.')


def update_pairs():

    ### STEP 2: for each pair call Binance again for quote+asset base and status, and add to my_pairs
    ##Risk here - breaching 1200 api calls per minute.....
    ##Risk here - some pairs return None type - ask Binance why :)

    lag = 0.1 # lag for not hitting Binance API 1200/min threshold
    
    print('Loading base and quote currencies, and statuses...')
    for i in range(len(my_pairs)):
        time.sleep(lag)
        details = client.get_symbol_info(my_pairs[i]['symbol'])
        if details is not None:
            my_pairs[i]['baseAsset'] = details['baseAsset']
            my_pairs[i]['quoteAsset'] = details['quoteAsset']
            my_pairs[i]['status'] = details['status']
            if i % 500 == 0: print(time.ctime(),'|| Loaded:',i)
    print('Finished loading base and quote assets, and status.')
    csvfile.lod_to_csv(my_pairs,'my_pairs.csv')

if __name__ == "__main__":
    load_pairs()
    print("This was run as a script. Only loading pairs.")
