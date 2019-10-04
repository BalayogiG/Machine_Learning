import random

def rolldice():
    roll = random.randint(1,100)
    return roll

x = 0
while x < 100:
    result = rolldice()
    print(result)
    x += 1
