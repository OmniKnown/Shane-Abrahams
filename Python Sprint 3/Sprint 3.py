# Random password generator in Python
# Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols
# Generating a new password every time the code is run resulting in a new password
# The length of the characters should be 12
# Include your code in a main method

import random # usage of a random function
import string # collection of string variables
lower = string.ascii_lowercase # all alphabetical lowercase letters
upper = string.ascii_uppercase # all alphabetical uppercase letters
digits = string.digits # numbers ranging from "0 - 9"
symbols = '!@#$%&?' # special characters

def main(a=3, b=3, c=3, d=3): # Length of password is 12 characters long / assigned 3
    password = []
    [password.append(random.choice(lower)) for x in range(a)] # append() adding the elements of the generated code together {W3schools}
    [password.append(random.choice(upper)) for x in range(b)] # input from the strings
    [password.append(random.choice(digits)) for x in range(c)] # random selection from each
    [password.append(random.choice(symbols)) for x in range(d)] # range of 3 each and 12 in total 
    random.shuffle(password) # random shuffle of the selected characters
    return "".join(password) # generate random password and convert to string

print("Your random generated password is ---> ", main()) # displaying/printing the random generated password from the main function 