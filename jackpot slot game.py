import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results 
    return [random.choice(symbols) for _ in range(3)]  

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒": 
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0 #always return an integer

def main():
    balance = 100

    print("*************************")
    print(" Welcome to Python Slots ")
    print("Symbol    |     Reward   ")
    print("🍒        |      3  times")
    print("🍉        |      4  times")
    print("🍋        |      5  times")
    print("🔔        |      10 times")
    print("⭐        |      20 times")
    print("*************************")

    while balance > 0:
        print(f"Current Balance: ${balance}")
        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number!")
            continue 
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue
        if bet<=0:
            print("Bet must be greater than 0")
            continue
        balance -= bet 
        if balance == 0:
            print("Current Balance: $0")

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet) #always an integer

        # if payout > 0: #generates error, change position, insert after foloowing loop
        #     print(f"You won ${payout}")
        # else:
        #     print("Sorry you lost this round")

        balance += payout 
        if payout > 0:  
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        play_again = input("Do you want to spin again? (Y/N): ")
        if play_again.upper() != "Y":
            break 

    print("*****************************************")
    print(f"Gamme Over! Your final balance is ${balance}")

if __name__ == "__main__":
    main()