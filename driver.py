# coding: utf-8

import sys
from Bot import MarketWatchBot

if(len(sys.argv) > 1):
    if(sys.argv[1] == '-a'):
        file = open(sys.argv[2], 'r')
        username = file.readline().strip('\n')
        password = file.readline().strip('\n')
        game_name = file.readline().strip('\n')
        path = file.readline().strip('\n')
        
else:
    username = input("Enter username: ")

    password = input("Enter account password: ")

    #ADD FEATURE THAT LOGS IN, AND THEN LETS YOU PICK A GAME FROM LIST OF GAMES
    game_name = input("Enter the game name: ")

    path = input("Enter your chromedriver path: ")

#chrome_path = '/Users/matthewlacayo/Desktop/Stocky Botty/chromedriver'



bot1 = MarketWatchBot(username, password, game_name, path)

bot1.login()

print("SUCCESSFULLY LOGGED IN")



###	MOVE BELOW TO ANOTHER FILE	###
###	CODE FOR GUI	###

import tkinter as tk



master = tk.Tk() 

l1v = tk.StringVar().set('Net Worth')
l2v = tk.StringVar().set('Today\'s Gains')
l3v = tk.StringVar().set('Overall Returns')
l4v = tk.StringVar().set('Cash Remaining')


def update_1():
    v1.configure(text=bot1.getNetWorth())

def update_2():
    v2.configure(text=bot1.getTodaysGains())

def update_3():
    v3.configure(text=bot1.getOverallReturns())

def update_4():
    v4.configure(text=bot1.getCashRemaining())

l1 = tk.Label(master, text='Net Worth').grid(row=0, column = 0) 
l2 = tk.Label(master, text='Today\'s Gains').grid(row=1, column = 0) 
l3 = tk.Label(master, text='Overall Returns').grid(row=2, column = 0)  
l4 = tk.Label(master, text='Cash Remaining').grid(row=3, column = 0) 


v1 = tk.Label(master, text=bot1.getNetWorth())
v1.grid(row=0, column = 1) 
v2 = tk.Label(master, text=bot1.getTodaysGains())
v2.grid(row=1, column = 1) 
v3 = tk.Label(master, text=bot1.getOverallReturns())
v3.grid(row=2, column = 1) 
v4 = tk.Label(master, text=bot1.getCashRemaining())
v4.grid(row=3, column = 1) 



b1 = tk.Button(master, text="Update", command=update_1).grid(row=0, column = 2)
b2 = tk.Button(master, text="Update", command=update_2).grid(row=1, column = 2)
b3 = tk.Button(master, text="Update", command=update_3).grid(row=2, column = 2)
b4 = tk.Button(master, text="Update", command=update_4).grid(row=3, column = 2)


master.mainloop() 