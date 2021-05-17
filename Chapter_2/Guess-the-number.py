import random

secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20')
print('You have 6 chances to guess it corectly')
for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break

if guess == secretNumber:
    print(f"Thats right, You guessed it in {guessTaken} tries")
else:
    print(f"Sorry. The number was {secretNumber}")
