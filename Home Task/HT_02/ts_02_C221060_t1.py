'''

Home Task #2 
Number Guessing Game with Constraints
Objective: Create a Python program where the user has to guess a randomly chosen number between 1 and 100 within 7 attempts.

Key Requirements:
* Use if-else to compare the guessed number with the correct one.
* Implement a for loop to manage 7 attempts.
* Use break to exit the loop if the user guesses correctly.
* Use continue to skip an attempt if the guess is out of the valid range (1-100).
* Provide feedback if the guess is too high or too low.
* Show a success message if guessed correctly, or display the correct number after 7 attempts if the user fails.

Each operation should be top commented properly.
Each print out should be with proper note.

'''

#at first we have to include random module of python to generate random number in a specific range
import random

#store a random integer number between 1 to 100 in variable called random_number
random_number = random.randint(1, 100)

# the total number of attempt is 7
total_attempt = 7

# declare a variable to track if the user wins the game or not
game_result = False

#initialize a for loop for the attempts
for counter in range(7 , 0 , -1):
    print("You have only ", counter , "chances left.")
    guessed_number = int(input("Guess a number between 1 to 100 : ")) # takes input from the user
    if guessed_number == random_number: # checks if the users guessed number is equal to the generated random number or not
        print("Congratulations! Your guess is correct.")  # prints the message
        game_result = True  # make the boolean variable true which means the player won the game
        break # the loop breaks
    
    elif random_number < guessed_number <= 100: # checks if the guessed number is bigger than the random number
        print("Wrong guess. Guess a small number.") # tells the user to guess a smaller number
        
    elif random_number > guessed_number >= 1:  # checks if the guessed number is less than the random number
        print("Wrong guess. Guess a larger number.") # tells the user to guess a bigger number 
        
    else:
        continue  # if the user guess a number out of range than it skips the operation
        
        
# if the game_result variable is false that means the player loose the game
if game_result == False:  # checks if the game_result variable is false or not
    print("You loose the Game. Better luck next time. :-)") # prints a message for the player
    print("The Number is :" , random_number) # if you loose the game it prints the answer
    
    