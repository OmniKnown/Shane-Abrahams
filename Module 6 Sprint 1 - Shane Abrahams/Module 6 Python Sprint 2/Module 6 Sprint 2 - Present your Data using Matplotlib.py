# Instructions:
# This is an individual exercise
# You will use Pandas and data frames to implement your solution

# Question
# You have been deployed as a data vault manager. As part of your assignment, 
# you are required to create Pandas data list. Using your pandas create a 
#list of Dataframes using Python for the following products:

# Chips: Simba, Lays
# Cooldrinks: Coke, Fanta
# Chocolates: Cadbury, Tex
# Pies: Pepper Steak, Chicken
# Fruit: Pear, Apple, Orange
# Cupcakes: vanilla, chocolate
# Veggies: spinach, cabbage

import pandas as pd  
    
# Table Series 
Table = [['Chips', 'Simba', 'Lays', '10'], ['Cooldrink', 'Coke', 'Fanta', '20'], 
       ['Chocolates', 'Cadbury', 'Tex', '50'], ['Pies', 'Pepper Steak', 'Chicken', '10'],
       ['Fruit', 'Pear', 'Apple', '30'], ['Cupcakes', 'Vanilla', 'Chocolate', '50'], 
       ['Veggies', 'Spinach', 'Cabbage', '15']] 
    
df = pd.DataFrame(Table, columns =['Products', 'Sample 1', 'Sample 2', 'Sold Items'], dtype = float) 
df

import matplotlib.pyplot as plt

# Monthly average precipitation
Sold_Items = [10, 20, 50, 35, 30, 50, 15]

# Month names for plotting
Products = ["Chips", "Cooldrink", "Chocolates", "Pies", "Fruit", "Cupcakes", "Veggies"]

# Define plot space
fig, ax = plt.subplots(figsize=(10, 6))

# Define x and y axes
ax.plot(Products, 
        Sold_Items)

# Define plot space
fig, ax = plt.subplots(figsize=(10, 6))

# Create scatter plot
ax.scatter(Products, 
        Sold_Items)

plt.show()

# Define plot space
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar plot
ax.bar(Products, 
        Sold_Items)

# Set plot title and axes labels
ax.set(title = "Product Sold for July Week 2",
       xlabel = "Products",
       ylabel = "Total of Sold Items")

plt.show()

# Define plot space
fig, ax = plt.subplots(figsize=(10, 6))

# Define x and y axes
ax.bar(Products, 
       Sold_Items,
       color = 'violet',
       edgecolor = 'darkblue')

# Set plot title and axes labels
ax.set(title = "Product Sold for July Week 2",
       xlabel = "Products",
       ylabel = "Total of Sold Items")

plt.setp(ax.get_xticklabels(), rotation = 45)

plt.show()

# Define plot space
fig, ax = plt.subplots(figsize=(10, 6))

# Define x and y axes
ax.plot(Products, 
        Sold_Items,
        marker = 'o',
        color = 'chartreuse')

# Set plot title and axes labels
ax.set(title = "Product Sold for July Week 2",
       xlabel = "Products",
       ylabel = "Total of Sold Items\n(thousand)")

plt.show()

# Define plot space
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

fig.suptitle("Product Sold for July Week 2", fontsize = 16)

# Define x and y axes
ax1.bar(Products, 
        Sold_Items,
        color = 'cyan', 
        edgecolor = 'darkblue')

# Set plot title and axes labels
ax1.set(title = "Bar Graph",
       xlabel = "Products",
       ylabel = "Total of Sold Items\n(thousands)");

print("")

# Define x and y axes
ax2.plot(Products, 
        Sold_Items,
        marker = 'o',
        color = 'tomato')

# Set plot title and axes labels
ax2.set(xlabel = "Products",
       ylabel = "Total of Sold Items\n(thousand)")

# plt.savefig("average-monthly-precip-boulder-co.png")

plt.show()