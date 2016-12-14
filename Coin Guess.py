## basic guessing game. It keeps playing until the player fails a prediction
import random

print("Coin guessing game")
print("Start to throw!")

score = 0

while True:
    sides = random.choice(["heads", "tails"])
    guess = (input("Please predict heads or tails: \n").lower())[0]

    while True:
        if guess != "h" and guess != "t":
            guess = (input("Choose from heads and tails: ").lower())[0]
        else:
            break

    if guess == sides[0]:
        score += 1
        print("It is {}. You are right! Your score is {}. ".format(sides, score))
    else:
        break


