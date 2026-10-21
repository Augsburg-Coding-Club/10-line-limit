import random
winCount = 0
choices = ["rock","paper","scissors"]
print("win 3 games of rock paper scissors!")
while(winCount < 3):
    player = input("type rock paper or scissors")
    i = random.randint(0,2)
    if(player == "scissors" and choices[i] == "paper" or player == "paper" and choices[i] == "rock" or player == "rock" and choices[i] == "scissors"):
        print("+1 point")
        winCount = winCount + 1