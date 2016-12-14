## A number guessing minigame. How original...
import random

randomNumber=random.randint(0,9)
aux=0##placeholder for the number the player picks

print('Please guess the correct number from 1-10 that has been randomly generated.')
while aux != randomNumber:##it has to be correct first time since randomNumber can't be 0

    aux = int(input('Guess a Number\n'))

    if aux>randomNumber:
        print('the number is lower')

    if aux<randomNumber:
        print('the number is higher')

    if aux==randomNumber:
        print('You guessed correctly!\n')
        print('Thanks for playing')
        break