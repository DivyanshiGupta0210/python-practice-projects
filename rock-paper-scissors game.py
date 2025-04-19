import random

options = ("rock", "paper", "scissors")

running = True
while running:
    player = None  # Reset player's choice

    # Get valid input
    while player not in options:
        if player is not None:
            print("Invalid choice! Only enter rock, paper, or scissors.")
        player = input("Enter a choice (rock/paper/scissors): ").lower()

    # Computer makes a new choice each round
    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Ask for replay
    play_again = None
    while play_again not in ("y", "n"):
        if play_again is not None:
            print("Invalid choice! Only enter 'y' for Yes or 'n' for No.")
        play_again = input("Play again? (y/n): ").lower()
    if play_again not in "y": #OR if play_again != "y":
        running = False

print("Thanks for playing!")
