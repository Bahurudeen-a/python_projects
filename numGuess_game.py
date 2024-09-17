import random

print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the game. Let's start the game")

number_to_guess = random.randrange(100)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please Enter the Number: "))
    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and You found it rigth!! in the {guess_counter} attempt") 
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops sorry, The number is {number_to_guess}, better luck next time")
    elif my_guess > number_to_guess:
        print("Your Guess is very high")
    elif my_guess < number_to_guess:
        print("Your Guess is very low")