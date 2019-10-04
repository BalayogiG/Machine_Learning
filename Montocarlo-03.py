import random

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

def simple_bettor(funds,inital_wager, wager_count):
    value = funds
    wager = inital_wager

    currentWager = 0

    while currentWager < wager_count:
        if rolldice():
            value += wager
        else:
            value -= wager

        currentWager += 1

    if value < 0:
        value = "Broke!"
    print("Funds: ", value)

x = 0

while x < 100:
    simple_bettor(10000,100,100)
    x += 1
