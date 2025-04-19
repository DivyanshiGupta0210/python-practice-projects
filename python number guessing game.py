import random
answer=random.randint(1,100)
guesses=0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between 1 and 100")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        # pass
        guess = int(guess)
        guesses += 1
        if guess < 1 or guess > 100:
            print("The number is out of range")
            print(f"Please select an integer between 1 and 100")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else: 
            print(f"CORRECT! The answer was {answer}!")
            print(f"Numebr of guesses: {guesses}") 
            is_running = False    

    else:
        print("Invalid Guess")
        print(f"Please select an integer between 1 and 100")
                     