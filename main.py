import random

while True:
    options = ["R", "P", "S"]
    CPU = random.choice(options)
    player_choice = None

    print("The winning rules of the rock paper scissor game is as follows: \n"
          + "Rock vs Paper -> paper wins \n"
          + "Rock vs Scissors -> Rock wins \n"
          + "Paper vs Scissors -> scissor wins")
    print("Ensure to input your option as follows \n R for Rock, \n P for paper, and \n S for scissor ")

    while player_choice not in options:
        player_choice = input("enter your choice as instructed above = ")

    if player_choice == 'R':
        if CPU == 'R':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("its a tie")
        elif CPU == 'S':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("You win!")
        elif CPU == 'P':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("You Lose!")
    elif player_choice == 'P':
        if CPU == 'P':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("its a tie")
        elif CPU == 'R':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("You win!")
        elif CPU == 'S':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("You Lose!")
    elif player_choice == 'S':
        if CPU == 'S':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("its a tie")
        elif CPU == 'P':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("You win!")
        elif CPU == 'R':
            print('Player', player_choice, ':', 'CPU', CPU)
            print("You Lose!")

    play_again = input("Play Again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")