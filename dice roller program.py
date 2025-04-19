#using ASCII values and UNICODE characters
#required unicode characters:
# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# ●  ┌  ─  ┐  │  └  ┘
''' BOX
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
'''

print("Select the number of dice and you'll get the sum of their results!")

import random

dice_art = {
    1: ["┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"],

    2: ["┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"],

    3: ["┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"],

    4: ["┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"],

    5: ["┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"],

    6: ["┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"]
}

num_of_dice = int(input("How many dice? "))

dice = [random.randint(1, 6) for _ in range(num_of_dice)]

# Print the dice art row by row
for line in range(5):  # Each dice has 5 lines
    for die in dice:
        print(dice_art[die][line], end="  ")  # Print each line of each die with spacing
    print()  # Move to next line

total = sum(dice)
print(f"\nTotal: {total}")
