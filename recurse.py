import random
import os

def roll():
    global verbose
    x = random.randrange(0,999)

    # for bug testing roll chances
    if verbose == True:
        print("Current roll value: {}".format(x))

    return x

def debug():
    # toggles verbose on or off
    global verbose
    verbose = not verbose
    if verbose == True:
        print("############\n# Debug on #\n############")
    else:
        print("#############\n# Debug off #\n#############")

def moneyAvailable():
    global wallet
    return "Cash available: {}".format(wallet)

def widebet(a, b):  # a is money, b is outcome betted on
    global wallet
    # if a > wallet, return error message to input a smaller value
    if a > wallet:
        a = int(input("Yo, that's way more than you actually got. Try again.\n"))
        widebet(a, b)
    else:
        # roll x and see if bet matches
        x = roll()

        # consider doing a class for this response
        wallet -= a
        
        if (x <= 499 and b == "lower") or (x >= 500 and b == "higher"):
            wallet += a*2
            print("Congrats! You won this round. Here's some dough.")
            print("You received {} dollars.".format(a*2))           
            
        else:
            print("Damn son, tough luck huh?")
            print("You lost {} dollars.".format(a))

def ask():
    betoutcome = str(input("Whatcha bettin' on: "))
    betmoney = int(input("Cash amount: "))
    
    widebet(betmoney, betoutcome)

def workRelay():
    global workaddbuff, workmultbuff, wallet
    work(workaddbuff, workmultbuff)
    return "You earned " + str(wallet)

def work(a, b):
    global wallet
    #x = random.randrange(0,100)
    # Write some multiplier or additive function for profit

    # Rewrite work() to pull from dictionary with random amounts of money
    wallet += (10 + a)*b
    return wallet
    
def core():
    global playing, wallet, workaddbuff, workmultbuff, verbose
    switchers = {
        1: ask,
        2: workRelay,
        3: buy,
        4: craft,
        5: moneyAvailable,
        6: save,
        7: load,
        8: exit,
        
        #secret codes
        1974: debug
    }

    print("\n=========================")
    print("How can I help you today?")
    numplace = int(input("  1: Gamble,\n  2: Work,\n  3: Buy,\n  4: Craft,\n  5: Check Wallet,\n  6: Save,\n  7: Load,\n  8: Exit\n"))

    place = switchers.get(numplace, lambda: "\nSorry, I didn't catch that. Come again?")
    print(place())

def buy():
    return "Coming soon!"

def craft():
    return "Coming soon!"

def load():
    # Load the saved file and strip the \n from the variables
    global wallet, workaddbuff, workmultbuff
    f = open("save.txt", "r")
    f = f.readlines()
    f = [x.strip() for x in f]
    wallet, workaddbuff, workmultbuff = f[0], f[1], f[2]
    loadSuccessful = "Save loaded.\n\n" + moneyAvailable() + "\nBuffs values: {}, {}".format(workaddbuff, workmultbuff)
    return loadSuccessful

def save():
    global wallet, workaddbuff, workmultbuff
    f = open("save.txt", "w")
    # Save format will be a list of numbers. In order:
    # [wallet, workaddbuff, workmultbuff] (betaddbuff and betmultbuff will be added later)
    f.write("{}\n{}\n{}".format(wallet,workaddbuff,workmultbuff))
    f.close()
    saveSuccesful = "Game saved."
    return saveSuccesful

# modifiers for gameplay, subject to change, verbose set to false by default
playing = True
verbose = False
wallet = 10
workaddbuff, workmultbuff = 10, 2

while playing == True:
    core()