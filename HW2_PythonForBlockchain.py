####Q1 Use input to create an integer variable. Use the variable to print through each item in the below list
#### Use a for loop for this and remeber to make this work you must use type conversion



the_list = ['eth','btc','ada','ltc','dai']

int_var = input('Please input your integer: ')

for i in range(int(int_var)):
    print(the_list[i])



####Q2 Create an if statement to test if the below equation is equal to 9

a = 5*2

if a == 9:
    print("This is nine!")


####Q3 Create a user defined function with no parameters to calculate one ethereum in the denomination of wei
####Use this function to convert the ethereum value that you store in an input statement

eth_store = input("how much eth are you converting?")

def wei_conv():
    wei_to_eth = 10**18
    return wei_to_eth

print(wei_conv()*int(eth_store))


### Q4 Modify your function in Q3 to do conversion based on one or more parameters

def wei_conv(a):
    wei_to_eth = 10**18
    conversion = a*wei_to_eth
    return conversion 

wei_conv(4)