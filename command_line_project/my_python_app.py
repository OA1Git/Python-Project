import random

#Initialise the list of numbers that the computer will choose from and a dictionary to define this based on the payers choice
num_range = []
difficulty = {
    "Easy": 100, 
    "Medium": 10,
    "Hard": 5
}
d_choice = input("Choose your difficulty level: Easy, Medium or Hard? ")

#Function to build the list of possible numbers based on difficulty set
def diff_func(d_choice):
  for j in range(1, difficulty[d_choice] + 1):
    num_range.append(j)

#Set the random number, number of guesses allowed and initialise the counter of guesses left
diff_func(d_choice)

#Using this chosen method, the number of guesses allowed will be easier with a larger range of possible numbers
#To improve the game, the number of guesses allowed should scale non-linearly with the range of possible numbers
num = random.choice(num_range)
guesses_allowed = int(len(num_range) / 3)
guess_left = guesses_allowed

print("I'm thinking of a number between " + str(num_range[0]) + " and " + str(num_range[-1]) + ", can you guess it in " + str(guesses_allowed) + " guesses? ") 

for i in range(guesses_allowed):
    
    guess = int(input("What's your guess? "))
    
    #Check win condition first
    if guess == num:
        print("You win, my number was indeed " + str(num))
        break
    
    #Check lose condition
    elif guess_left == 1:
        print("You've failed, my number was " + str(num))
        break
    
    #Guide the players next guesses
    elif guess < num:
        guess_left = guess_left - 1
        print("That's too low try again, you've got " + str(guess_left) + " guesses left")
    elif guess > num:
        guess_left = guess_left - 1
        print("That's too high try again, you've got " + str(guess_left) + " guesses left")
