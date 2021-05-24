from random import randint

# create a list of play options
table = ["rock", "paper", "scissors"]

# le CPU choisit une option au hasard
computer = table[randint(0, 2)]

player = None
wantsToQuit = False

while not wantsToQuit:
    # set player to true
    player = input("rock, paper, scissors?")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print(computer, "covers", player, ", you lose :( !")
        else:
            print(player, "crushes", computer, ", you win :D !")
    elif player == "paper":
        if computer == "scissors":
            print(computer, "lashes", player, ", you lose :( !")
        else:
            print(player, "covers", computer, ", you win :D !")
    elif player == "scissors":
        if computer == "rock":
            print(computer, "breaks", player, "to pieces. You lose :( !")
        else:
            print(player, "cuts", computer, ", you win :D !")
    else:
        print("You only are allowed to play rock, paper or scissors !")
        print(" Check your spelling !")
    player == input("Want to quit ?")
    if player == "yes":
        print("Thanks for having played :)")
        wantsToQuit = True
    else:
        wantsToQuit = False
        computer = table[randint(0, 2)]
        print("Awesome ! Let's play some more")
        player = input("rock, paper, scissors?")
