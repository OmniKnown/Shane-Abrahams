from random import choice #

print('Welcome to the Dice Simulator Game') # Welcoming text to the simulated game
print(" ") # empty line so that tex does not look conjested 
print('After the number has been given, the program will output each number rolled until target number has been rolled.') # Explination of the game
print(" ") # empty line so that tex does not look conjested 

# input value of yes or no / input account for capitalization using .lower() method
roll_dice = input('Are you ready to roll the dice? Enter Yes or No.').lower() # converts input to lowercase for comparison

die = [1, 2, 3, 4, 5, 6] # The numbers featured on each dice

print('This program rolls two 6-sided dice until their sum is a given target.') # Stating what will be printed

target = 0 # to track the number of times rolled the dice

# the while loop
while target not in range(2,13):  # range of which the answer must consist of
    try:
        target = int(input('Enter the target sum to roll (2-12): ')) # function input number to roll the dice and get a value
    except ValueError:
        print('Please enter a target between 2 and 12') # the input number between 2 to 12 

roll_sum = 0 # sum total of the two dice rolled
roll_count = 0 # number count of times the dice has been rolled

while target != roll_sum: # while statement while the rolled sum is = target function will work

    die_1 = choice(die) # dice_1's random dice choice
    die_2 = choice(die) # dice_2's random dice choice
    roll_sum = die_1 + die_2 # the sum of dice_1 & dice_2
    roll_count += 1 # the roll count number until target is reached
    print('You rolled a total of{}'.format(roll_sum)) # printing the results 

play_again = input("Do you want to restart? Yes or No\n") # new play_again function asking the user if they want to restart the game or not

if play_again == "Yes": # start of if statement asking if the user wants to play again 
    exec(open("./Shane Abrahams Sprint 2.py").read()) # if 'yes' - the exec function will open the ''the file and run the game again.
else:
    print('Thank you for playing') # Messaging saying 'Thank you for playing' - after no was typed. 
