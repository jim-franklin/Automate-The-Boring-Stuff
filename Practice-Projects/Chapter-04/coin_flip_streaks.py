import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = []  # Initialize an empty list to store the flips

    for i in range(100):  # Perform 100 coin flips
        if random.randint(0, 1) == 0:  # 0 represents 'heads', 1 represents 'tails'
            coin_flips.append("H")
        else:
            coin_flips.append("T")

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak_length = 1  # Initialize streak length to 1

    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            streak_length += 1
        else:
            streak_length = 1  # Reset streak length if streak is broken

        if streak_length == 6:
            numberOfStreaks += 1

# print(numberOfStreaks)
print("Chance of streak: %s%%" % (numberOfStreaks / 100))
