# Instructions:
# This is an individual exercise
# You will use MySQL and Matplotlib to implement your solution

# Question
# You have been deployed as a data vault analyst. As part of your assignment, you are required:

# Import the data from your CSV/Excel file, from sprint 1, using MySQL.
# Using the data from (a) above, add visuals that you have learnt this week to present your data using Matplotlib

import xlrd
import mysqldb
import pandas as pd
import mysql.connector 
import numpy as np
import matplotlib.pyplot as plt


# Open the workbook and define the worksheet
book = xlrd.open_workbook("Data Table.xls")
sheet = book.sheet_by_name("Sheet1")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
heading = """INSERT INTO orders (products, sample1, sample2, sold_items) VALUES (%s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    products = sheet.cell(r,).value
    sample1 = sheet.cell(r,1).value
    sample2 = sheet.cell(r,2).value
    sold_items = sheet.cell(r,2).value

# Assign values from each row
items = (['Chips', 'Simba', 'Lays', '10'], ['Cooldrink', 'Coke', 'Fanta', '20'], 
       ['Chocolates', 'Cadbury', 'Tex', '50'], ['Pies', 'Pepper Steak', 'Chicken', '10'],
       ['Fruit', 'Pear', 'Apple', '30'], ['Cupcakes', 'Vanilla', 'Chocolate', '50'], 
       ['Veggies', 'Spinach', 'Cabbage', '15'])

# Execute sql Query
cursor.execute(heading, items)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()