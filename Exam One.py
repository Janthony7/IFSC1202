import random
guessestaken = 0
firstname = input("Hello! What is your name?: ")
print("Alright, " + firstname +", I'm thinking of a number between 1 and 20.")
n = random.randint(1,20)
print(n)
print("What's your number?")
while guessestaken < 6:
    guess = int(input())
    guessestaken = guessestaken + 1      
    if guess < n:
        print("Too low!")
    if guess > n:
            print("Too high!")
    if guess == n:
         break
if guess == n:
    guessestaken = str(guessestaken)
    print("Woohoo! You guessed right!!! " + "You guessed in " + guessestaken + " guesse(s)!")
if guess != n:
    n = str(n)
    print("Sorry, but, nope I was thinking of " + n)