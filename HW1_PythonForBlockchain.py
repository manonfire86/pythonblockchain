#### Please only use the material covered in lesson 1





### Below is are two variables, number of bitcoins in circulation and bitcoin price


# Bitcoins in circulation: 18,856,450
# Bitcoin Price: 59,109.74

### Q1: Please calculate the Bitcoin Market cap. Formula: Price x Bitcoins in Circulation

a = 18856450
b = 59109.74

print(a*b)



### Q2: Below is a list of token strings, market caps, and prices. Please index the lists,
### calculate the individual coins in circulation, and place them in a print statement.
### REMEBER YOU CAN CONCATENATE STRINGS AND CONVERT DATATYPES


tickers = ['ETH','BTC','ADA']
market_caps = [471095868313,1110007454929,64443565023]
prices = [3988.79,59109.74,1.94]

eth_coins = market_caps[0]/prices[0]
btc_coins = market_caps[1]/prices[1]
ada_coins = market_caps[2]/prices[2]

print(tickers[0]+': '+str(eth_coins)+", "+tickers[1]+": "+str(btc_coins)+", "+tickers[2]+": "+str(ada_coins))

### Q3: Ethereum has 13 blockchain transactions per second. Please calculate the total
### number of transactions in a month. Please also calculate the annual average.

block_tx = 13
seconds_in_year = 60*1440*365
seconds_in_month = 60*1440*(365/12)

tx_year_average = (block_tx * seconds_in_year)/12

tx_month = block_tx*seconds_in_month

print(tx_month)
print(tx_year_average)

### Q4: What is the value of b^2 − 5 when b = 5. 
### Convert your answer to a float and check the data type.

b =5

solution = (b**2)-5

print(float(solution))

type(solution)
