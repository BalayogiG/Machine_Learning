#Importing required packages
import random
import matplotlib.pyplot as plt

#Rolling dice function generate random dice value
def rolldice():
    roll = random.randint(1,100)

    if roll == 100:
        print(roll,"Roll was 100, you lose, Play again")
        return False
    elif roll <= 50:
        print(roll,"Roll was 1-50, you lose")
        return False
    elif 100 > roll >= 50:
        print(roll,"Roll was 51-99, you win")
        return True

#Betting Function
def simple_bettor(funds,inital_wager, wager_count):
    value = funds
    wager = inital_wager

    wx = []
    wy = []

    currentWager = 1

    while currentWager <= wager_count:
        if rolldice():
            value += wager
            wx.append(currentWager)
            wy.append(value)
        else:
            value -= wager
            wx.append(currentWager)
            wy.append(value)

        currentWager += 1

    #Plotting graph
    plt.plot(wx,wy)

x = 0
while x<100:
    simple_bettor(10000,100,100)
    x += 1


plt.xlabel("Wager Count")
plt.ylabel("Account Value")
plt.show()
