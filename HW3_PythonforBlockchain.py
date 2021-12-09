
###Q1: Create an empty list. Dynamically append to this empty list and then
### dynamically print the contents of the list.

##Note: Dynamically means that if you change a variable in your code or new data
##is received the resulting calculation will automatically adjust


empty_list = []

for i in range(1,10):
    empty_list.append(i)
    
for i in range(len(empty_list)):
    print(empty_list[i])


###Q2: Create a function with three variables that uses either a for loop, elif
### statement, or while loop to calculate any crypto currencys market cap

### THIS IS THE FORMULA FROM HW 1


def mkt_func(price,volume,marketcap):
    if price == '':
        p = (marketcap/volume)
        mktcap_p = p * volume
        return mktcap_p
    elif volume=='':
        v = (marketcap/price)
        mktcap_v = v*price
        return mktcap_v
    elif marketcap == '':
        mktcap_m = price*volume
        return mktcap_m


mkt_func('',20000,20000000)

###Q3: Use your function from Q2 to dynamically calculate and print a collection of data
### I want you to find five currencies that you follow with their associated price and volume
### store them in a list and run your function on this list. This process should be dynamic

#https://coinmarketcap.com/currencies/multi-collateral-dai/

btc = [56673.11,18888275.00,'']
ada = [1.54,33310000000,'']
eth = [4548.04,118567151.12,'']
dai = [0.9994,6470000000,'']
stx = [2.80,1290000000,'']


currencies = [btc,ada,eth,dai,stx]

for i in currencies:
    print(mkt_func(i[0],i[1],i[2]))


###Q4: Calculate the transaction sum and average from the below blocks. Convert the values
### to a denomination of wei


eth_blocks = [['Dummy 1','11/15/2021','ETH',7.875],['Dummy 2','11/18/2021','ETH',2.375],['Dummy 3','11/15/2021','ETH',4.575],['Dummy 4','11/15/2021','ETH',9.3475]]

tx_vals = []
for i in eth_blocks:
    tx_vals.append(i[3])
    
print(sum(tx_vals))
print(sum(tx_vals)/len(tx_vals))