# Add the following to your sprint 2 MySQL data using Python:
# Add more products and their brands
# Create more columns to your products. 
# Create separate tables for each product
# Save your MySQL data and code to GitHub
# Make your work accessible to your team members on GitHub. (Sprint1, Sprint 2, Sprint3)

import csv
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas.io.sql
import pyodbc
import xlrd

connection = mysql.connector.connect(host='localhost',
    user='root',
    passwd='2222',
    db='databasename1'
    ) # create Connection and Cursor objects

cursor = connection.cursor()
cursor = connection.cursor(buffered=True,dictionary=True)

data = pd.read_excel('Data Table.xlsx') # read data

data = data.rename(columns={'Products': 'Products',
                            'Sample1': 'Sample1',
                            'Sample2': 'Sample2'}) # rename columns

book = xlrd.open_workbook("Data Table.xlsx")
sheet = book.sheet_by_name("Sheet1") # Open the workbook and define the worksheet

query1 = """
CREATE TABLE DATA (
    Products varchar(255),
    Sample1 varchar(255),
    Sample2 varchar(255),
    )"""

query = """
INSERT INTO DATA (
    Products,
    Sample1,
    Sample2
) 
VALUES (%s, %s, %s)"""

try:
    cursor.execute(query1)
    connection.commit()
except mysql.connector.ProgrammingError:
    pass # execute create table

for r in range(1, sheet.nrows):
    Products = sheet.cell(r,0).value
    Sample1 = sheet.cell(r,1).value
    Sample2 = sheet.cell(r,2).value

    values = (Products, Sample1, Sample2) # Assign values from each row

    cursor.execute(query, values) # Execute sql Query

connection.commit() # Commit the transaction

cursor.execute("SELECT Products from DATA") # checking if all rows are imported
result = cursor.fetchone()

connection.commit() # the connection is not autocommited by default. So we must commit to save our changes.

cursor = connection.cursor()
sql = "INSERT INTO DATA (Products,Sample1,Sample2) VALUES (%s,%s,%s)"
val = [ 
    ("Sweets","Jelly Tots","Jelly Babies"),
    ("Soup","ButterNut","Noodle"),
    ("Burger","Chicken","Beef"),
    ("Pizza","Margarita","Tica Chicken")
]
cursor.executemany(sql, val)

connection.commit()

query2 = """
INSERT INTO DATA (
    Sold_Items
) 
VALUES ("10"), ("20"), ("50"), ("10"), ("30"), ("50"), ("15"), ("10"), ("20"), ("50"), ("10")"""
connection.commit()

query3 = """ALTER TABLE 'DATA'
    (ADD Amount_Left varchar(40) NOT NULL 
        AFTER Sold_Items) VALUES (100), (200), (500), (100), (300), (500), (150), (100), (200), (500), (100)"""

connection.commit()

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS chips (id INT AUTO_INCREMENT PRIMARY KEY, simba VARCHAR(255), lays VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS cooldrink (id INT AUTO_INCREMENT PRIMARY KEY, coke VARCHAR(255), fanta VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS chocolates (id INT AUTO_INCREMENT PRIMARY KEY, cadbury VARCHAR(255), tex VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS pies (id INT AUTO_INCREMENT PRIMARY KEY, pepper_steak VARCHAR(255), chicken VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS fruit (id INT AUTO_INCREMENT PRIMARY KEY, pear VARCHAR(255), apple VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS cupcakes (id INT AUTO_INCREMENT PRIMARY KEY, vanilla VARCHAR(255), chocolate VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS veggies (id INT AUTO_INCREMENT PRIMARY KEY, spinach VARCHAR(255), cabbage VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS sweets (id INT AUTO_INCREMENT PRIMARY KEY, jelly_tots VARCHAR(255), jelly_babies VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS soup (id INT AUTO_INCREMENT PRIMARY KEY, butternut VARCHAR(255), noodle VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS burgers (id INT AUTO_INCREMENT PRIMARY KEY, chicken VARCHAR(255), beef VARCHAR(255))")

cursor.execute("CREATE TABLE IF NOT EXISTS pizza (id INT AUTO_INCREMENT PRIMARY KEY, margarita VARCHAR(255), tica_chicken VARCHAR(255))")
cursor = connection.cursor()

connection.close() # Close the database connection
