import random

def rollDice():
    return random.randint(1,6) + random.randint(1,6)

def getWinner():
    if(dice1 == dice2):
        print("Tie!")
    elif dice1 > dice2 :
        print(p1, "Wins!")
    else:
        print(p2, "Wins!")        

p1 = input("Enter player1 name \n");
p2 = input("Enter player2 name \n");

dice1 = rollDice()
dice2 = rollDice()

print(p1,"got", dice1)
print(p2,"got", dice2)

getWinner()

