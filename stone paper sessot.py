import random                              # this module will help computer to take random option and play as a AI player
option = ["rock", "paper", "scissors"]     # the options

while True:                                # this is a infinite loop it will work until the match is tie or any of the player won the game
    user = input("choose:- rock, paper or scissors or choose quit") # the options which will be shown to the player
    if user == "quit":                                              # option if the play want to quit
        break
    if user not in option:                                          # if the user chose a option which is not their
        print("choose a valid option")
    AI = random.choice(option)                                      # the code which will allow computer to choose option
    if user == AI:
        print("TIE")                                                # if the both player option came same
    elif(user == "rock" and AI == "scissors") and (user == "paper" and AI == "rock") and (user == "scissors" and AI == "paper"):   # if this result came then the user won
        print("YOU WON !!!!!!")
    else:                                                           # if any other result came the the AI won
        print("YOU LOSE :(")
print("Thank for playing")                                          # made by Rishabh Ghsoh
