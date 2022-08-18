# Guess the Number Game
import random # imports the random module
print("What's good, homie? What's your name?")
name = input() # name is a variable that stores the user's inputted name
secretNumber = random.randint(1, 20)
print("Well, " + name +  ", I am thinking of a number etween 1 and 20. Take a guess!")

# Debug # print('Debug: Secret Number is ' + str(secretNumber))

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else: break # This condition is for the correct guess!


if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
