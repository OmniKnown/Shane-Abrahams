# Calculator in Python
# The calculator must be able to perform the following operations
# Addition
# Subtraction
# Multiplication
# Division
# Exit 


def welcome(): # Welcome function
    print("Welcome to the Python Calculator. ") # print welcome
    print(" ")
    option = input("""Please type what you would like to do
    Y to proceed, N for exit:
    """)
    if option.upper() == 'Y': # if the user selects Y, then call calculate
# we can make the program accept Y or y by adding the .upper()
        calculate()
    elif option.upper() == 'N': # if the user types N, say thanks and goodbye
        print("You did not even bother to try my Calculator, Bye. ") # we can make the program accept N or n by adding the .upper()
        exit() # N or n will exit the program 
    else:welcome() # any other option will continue using the calculator

def calculate():
    choice = input(""" please type in the mathametical function you will like to run...
+ for addition
- for subtraction
* for multiplication
/ for division
""") # list of input options
    num_1 = float(input("Your first number?\n")) # first chosen number
    num_2 = float(input("Your second number?\n")) # second chosen number 

    if choice == '+': # addition
        print("{} + {} = ".format(num_1, num_2))
        print(num_1 + num_2 )

    elif choice =='-': # subtraction
        print("{} - {} = ".format(num_1, num_2))
        print(num_1 - num_2 )

    elif choice =='*': # multiplication
        print("{} * {} = ".format(num_1, num_2))
        print(num_1 * num_2 )

    elif choice =='/': # Division
        print("{} / {} = ".format(num_1, num_2))
        print(num_1 / num_2 )

    else:print("Operation not Supported, please run through the program again. ")
    again() # we add the again function to the calculate as a loop


def again(): # to make the calculator continuous we define another variable for continuity called again

    calc_again = input(""" please type if you want to use the calculate again 
    say Y for Yes and N for No
    """) # we will need to take input form user

    if calc_again.upper() == 'Y': # we can make the program accept Y or y by adding the .upper()
        calculate() # if the user selects Y, then call calculate

    elif calc_again.upper() == "N": # we can make the program accept N or n by adding the .upper()
        print("Thanks for using My Calculator, have a great day. ") # if the user types N, say thanks and have a great day 
        exit()

    else: # if the user types any other key aside N, call calculate
        again() 

welcome() # Call the function Welcome
calculate() # Call calculate() outside of the function