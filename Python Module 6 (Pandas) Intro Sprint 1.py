# Instructions:
# This is an individual exercise
# You will use Pandas and data frames to implement your solution

# Question
# You have been deployed as a data vault manager. As part of your assignment, you are required to create Pandas data list. Using your pandas create a list of Dataframes using Python for the following products:

# Chips: Simba, Lays
# Cooldrinks: Coke, Fanta
# Chocolates: Cadbury, Tex
# Pies: Pepper Steak, Chicken
# Fruit: Pear, Apple, Orange
# Cupcakes: vanilla, chocolate
# Veggies: spinach, cabbage

import pandas as pd  
    
# Table Series 
Table = [['Chips', 'Simba', 'Lays'], ['Cooldrink', 'Coke', 'Fanta'], 
       ['Chocolates', 'Cadbury', 'Tex'], ['Pies', 'Pepper Steak', 'Chicken'],
       ['Fruit', 'Pear', 'Apple'], ['Cupcakes', 'Vanilla', 'Chocolate'], 
       ['Veggies', 'Spinach', 'Cabbage']] 
    
df = pd.DataFrame(Table, columns =['Item', 'Sample 1', 'Sample 2'], dtype = float) 
df