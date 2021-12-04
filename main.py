import random

PAPER_WIN_MESSAGE = "Paper covers rock,"
ROCK_WIN_MESSAGE = "Rock OBLITERATES scissors,"
SCISSORS_WIN_MESSAGE = "Scissors cuts paper,"

choices = ["rock", "paper", "scissors"]

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Please enter a choice (Rock, Paper, Scissors) or 'q' to exit: ").casefold()

    if user_choice == "q":
        print("Thank you for playing!")
        break

    if user_choice in choices:
        print(f"You chose {user_choice} and the computer chose {computer_choice}")
        if user_choice == computer_choice:
            print(f"Both players chose {user_choice}. It's a draw.\n")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print(PAPER_WIN_MESSAGE, "you lose!\n")
            else:
                print(ROCK_WIN_MESSAGE, "you win!\n")
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print(SCISSORS_WIN_MESSAGE, "you lose!\n")
            else:
                print(PAPER_WIN_MESSAGE, "you win!\n")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print(ROCK_WIN_MESSAGE, "you lose!\n")
            else:
                print(SCISSORS_WIN_MESSAGE, "you win!\n")
    else:
        print(f"\n'{user_choice}' is not a valid choice. Please enter again.\n")