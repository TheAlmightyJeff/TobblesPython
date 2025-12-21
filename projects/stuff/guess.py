import betterConsole as bc
from random import randint


number = randint(1,10)
bc.write("@yellow-@bold-Welcome to The Guessing Game")
bc.write("@yellow-A game where you guess the number i'm thinking of between 1 and 10!")

guess = bc.ask("@red-Enter you first number... or else ",0.05)


while guess != number:
    bc.write(f"@red-You have entered {guess}")
    guess = bc.ask("@red-Wrong! try again")

bc.write("@gold-Well Done! See you next time")
