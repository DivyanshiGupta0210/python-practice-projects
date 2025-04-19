questions = ("How many elements are there in the periodic table? ",
             "Which animal lays the largest eggs? ",
             "What is the most abundant gas in the Earth's atmosphere? ",
             "How many bones are there in the human body? ",
             "Which planet is the hottest in the solar system? ")

options = ("A. 116  B. 117  C. 118  D. 119",
           "A. Whale  B. Crocodile  C. Elephant  D. Ostrich",
           "A. Nitrogen  B. Oxygen  C. Carbon-di-Oxide  D. Hydrogen",
           "A. 206  B.  205  C. 204  D. 203",
           "A. Mercury  B. Venus  C. Earth  D. Mars")

answers = ("C", "D", "A", "A", "B")  # Fixing incorrect string unpacking # answers = ("C D A A B") was generating error
guesses = []
score = 0

for question_num in range(len(questions)):
    print("-----------------------------------------------")
    print(questions[question_num])
    print(options[question_num])  # Displaying the options correctly

    guess = input("Enter (A/B/C/D): ").upper()  # Getting user input #.upper(): to set answer to upper-case by deafult
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is: {answers[question_num]}")

print("----------------------------------------------")
print("                    RESULT                    ")
print("----------------------------------------------")

print("Correct Answers: ", " ".join(answers))
print("Your Answers: ", " ".join(guesses))

score_percentage = int(score / len(questions) * 100)
print(f"Your score is {score_percentage}%")

