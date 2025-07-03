import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Enter player1's name: ")
    player2 = input("Enter player2's name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

if __name__ == "__main__":
    main()