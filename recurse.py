import random

def roll():
    x = random.randrange(0,999)
    return x

def widebet(a, b):  # a is money, b is outcome betted on
    global wallet
    
    # if a > wallet, return error message to input a smaller value
    if a > wallet:
        a = int(input("Yo, that's way more than you actually got."))
        widebet(a, b)
    else:
        # roll x and see if bet matches
        x = roll()

        # consider doing a class for this response
        wallet -= a
        
        if x <= 499 and b == "lower":
            wallet += a*2
            print("Congrats! You won this round. Here's some dough.")
            print("You received {} dollars.".format(a*2))
            print("You currently have {} in your wallet.".format(wallet))
            
        elif x >= 500 and b == "higher":
            wallet += a*2
            print("Congrats! You won this round. Here's some dough.")
            print("You received {} dollars".format(a*2))
            print("You currently have {} in your wallet.".format(wallet))
            
        else:
            print("Damn son, tough luck huh?")
            print("You lost {} dollars.".format(a))
            print("You currently have {} in your wallet.".format(wallet))

wallet = 10

while wallet > 0:
    widebet(1, "higher")
