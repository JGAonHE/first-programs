"""In this program we play with random numbers"""
import random

#create and print a random number
randNum = random.random()
print(f"A random number is {randNum}")

#create and print a random integer from 1 to 10
randGuess = random.randint(1, 10)
print(f"A random integer between 1 and 10 is {randGuess}")