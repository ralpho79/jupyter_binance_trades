# init
#api_key = "ucqMzmbqswWPqo4bfQp4DoPyUTFIV2wO749sXmAPyIqwkA4vKQKSO6CZKAPi3DEA"
#api_secret = "KRQYhVnepPwutIprQmxyDbugCGCNMkr7WL3Cm7zqQoK9GIuGdLJQpoJqIooTqWnY"

from binance.client import Client
client = Client(api_key, api_secret)

# get all order book tickers once 
tickers = client.get_orderbook_tickers()

# Fees vary but I assume 0.075% for all pairs - see Binance for Special Pairs (0%)
fee = 0.00075


def check_triangle(a,b,c):
    # pairs -> AC, BC, BA
    pairs = [a+c, b+c, b+a]
    triangle_data = []

    # get market depths for the triangle pairs; return if one of pairs has no depth
    for i in range(len(pairs)):
        triangle_data += [dict for dict in tickers if dict["symbol"]==pairs[i]]
    
        # print("\n"+pairs[i],'Best bid/ask')
        # print('Ask price:',triangle_data[i]["askPrice"],'Ask volume:',triangle_data[i]["askQty"])
        # print('Bid price:',triangle_data[i]["bidPrice"],'Bid volume:',triangle_data[i]["bidQty"])


    # calculating arbitrage numbers
    spent1 = round(float(triangle_data[0]["askQty"]) * float(triangle_data[0]["askPrice"]),8)
    amount1 = round(float(triangle_data[0]["askQty"]) * (1-fee),8)
    spent2 = round(amount1 / float(triangle_data[2]["askPrice"]),8)
    amount2 = round(spent2 * (1-fee),8)
    spent3 = round(amount2 * float(triangle_data[1]["bidPrice"]),8)
    amount3 = round(spent3 * (1-fee),8)
    outcome1=[spent1,amount3,round(amount3-spent1,8),round((amount3-spent1)/spent1,4),c]

    spent1b = round(float(triangle_data[1]["askQty"]) * float(triangle_data[1]["askPrice"]),8)
    amount1b = round(float(triangle_data[1]["askQty"]) * (1-fee),8)
    spent2b = round(amount1b * float(triangle_data[2]["bidPrice"]),8)
    amount2b = round(spent2b * (1-fee),8)
    spent3b = round(amount2b * float(triangle_data[0]["bidPrice"]),8)
    amount3b = round(spent3b * (1-fee),8)
    outcome2=[spent1b,amount3b,round(amount3b-spent1b,8),round((amount3b-spent1b)/spent1b,4),c]

    # print('\n*** SCENARIO 1 - Parallel: {}->{}, {}->{}, {}->{}'.format(c,a,a,b,b,c))
    # print('Trade 1. Buy',triangle_data[0]["askQty"],a,'for Ask price',triangle_data[0]["askPrice"]+'. Spend',spent1,c+'. Receive',amount1,a)
    # print('Trade 2. Buy',spent2,b,'for Ask price',triangle_data[2]["askPrice"]+'. Spend',amount1,a+'. Receive',amount2,b)
    # print('Trade 3. Sell',amount2,b,'for Bid price',triangle_data[1]["bidPrice"]+'. Spend',amount2,b+'. Receive',amount3,c)
    # print('Invest',spent1,c,'and receive',amount3,c+'. Outcome:',round(amount3-spent1,8),c,"("+str(round((amount3-spent1)/spent1*100,2))+"%)")

    # print('\n*** SCENARIO 2 - Parallel: {}->{}, {}->{}, {}->{}'.format(c,b,b,a,a,c))
    # print('Trade 1. Buy',triangle_data[1]["askQty"],b,'for Ask price',triangle_data[1]["askPrice"]+'. Will spend',spent1b,c+'. Receive',amount1b,b)
    # print('Trade 2. Sell',amount1b,b,'for Bid price',triangle_data[2]["bidPrice"]+'. Will spend',amount1b,b+'. Receive',amount2b,a)
    # print('Trade 3. Sell',amount2b,a,'for Bid price',triangle_data[0]["bidPrice"]+'. Will spend',amount2b,a+'. Receive',amount3b,c)
    # print('Invest',spent1b,c,'and receive',amount3b,c+'. Outcome:',round(amount3b-spent1b,8),c,"("+str(round((amount3b-spent1b)/spent1b*100,2))+"%)")

    
    return [outcome1,outcome2]




if __name__=="__main__":
    # a=check_triangle('ETH','BNB','NGN')
    # a=check_triangle('BTC','ETH','PLN')
    # a=check_triangle('ETH','MATIC','BTC')
    a=check_triangle('BUSD', 'AXS', 'BIDR')
    # a=check_triangle('BUSD','LTC','NGN')

    print(a)
