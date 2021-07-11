import random
import os

def roll():
    x = random.randrange(0,999)
    return x

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

def ask():
    betoutcome = str(input("Whatcha bettin' on: "))
    betmoney = int(input("Cash amount: "))
    
    widebet(betmoney, betoutcome)

def work(a, b):
    global addbuff, multbuff
    global wallet
    x = random.randrange(0,100)
    # Write some multiplier or additive function for profit

    if x > 0 and x <= 40:
        # Write something about line of work and how much you're getting paid
        # Make sure to insult the player for working just to gamble :)
        print("You tap danced with a rat for 10 dollars.")
        wallet += 10
        print("You currently have {} in your wallet.\n".format(wallet))
        
    elif x > 40 and x <= 80:
        print("You won rock paper scissors against an amputee for 15 dollars.")
        wallet += 15
        print("You currently have {} in your wallet.\n".format(wallet))

    elif x > 80 and x <= 90:
        print("You licked Warren Buffett's shoe for 20 dollars.")
        wallet += 20
        print("You currently have {} in your wallet.\n".format(wallet))

    else:
        print("You trolled the IMF for 25 dollars.")
        wallet += 25
        print("You currently have {} in your wallet.\n".format(wallet))
    
def core():
    global playing, wallet, workaddbuff, workmultbuff
    switchers = {
        1: "Gamble",
        2: "Work",
        3: "Buy",
        4: "Craft",
        5: "Check Wallet",
        6: "Save",
        7: "Load",
        8: "Exit"
    }

    print("\n=========================")
    print("How can I help you today?")
    numplace = int(input("  1: Gamble,\n  2: Work,\n  3: Buy,\n  4: Craft,\n  5: Check Wallet,\n  6: Save,\n  7: Load,\n  8: Exit\n"))

    place = switchers.get(numplace)

    if place == "Gamble":
        ask()
    elif place == "Work":
        work(workaddbuff, workmultbuff)
        pass
    elif place == "Buy":
        print("Coming soon!")
        pass
    elif place == "Craft":
        print("Coming soon!")
        pass
    elif place == "Check Wallet":
        print("\nYou currently have {} in your wallet.".format(wallet))
        pass
    elif place == "Save":
        f = open("save.txt", "w")
        # Save format will be a list of numbers. In order:
        # [wallet, workaddbuff, workmultbuff] (betaddbuff and betmultbuff will be added later)
        f.write("{}\n{}\n{}".format(wallet,workaddbuff,workmultbuff))
        f.close()
    elif place == "Load":
        # Load the saved file and strip the \n from the variables
        f = open("save.txt", "r")
        f = f.readlines()
        f = [x.strip() for x in f]
        wallet, workaddbuff, workmultbuff = f[0], f[1], f[2]
    elif place == "Exit":
        print("\nSee ya next time, chief!")
        playing = False
    else:
        print("\nSorry, I didn't catch that. Come again?")
        pass

def buy():
    pass
    

playing = True
wallet = 10
workaddbuff, workmultbuff = 0, 1

while playing == True:
    core()