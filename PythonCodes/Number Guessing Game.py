#Number Guessing

#Importing the random to have a access to the random integers we can use
import random
number = random.randint(1, 10)

while True:
    #This is the main guess game
 guess = int(input("Guess a number between 1 and 10: "))
 if number == guess:
    print("You guessed right!")
    print("The Number is: " + str(number))
 else:
    print("You guessed wrong!")
    print("The Number is: " + str(number))

    #The loop started
    again = input("Would you like to play again? (y/n): ")
    if again == "y" or again == "Y":
        number = random.randint(0, 100)
    elif again == "n" or again == "N":
        exit()
    else:
        print("Invalid input. Please try again.")






