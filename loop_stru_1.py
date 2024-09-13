import random


def roll_dice():
    # Ask the user for the number of dice to roll
    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? "))
            if num_dice <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Initialize the total sum
    total_sum = 0

    # Roll each die and calculate the sum
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        total_sum += roll

    # Print the total sum of the dice rolls
    print(f"Total sum of rolled dice: {total_sum}")


# Call the function to roll the dice
roll_dice()
