# Instructions:
# This is an individual exercise
# You will use MongoDB Atlas, GitHub and Python
# Question
# You have been deployed as a Data Scientist. As part of your assignment, you are required to:

# Create a Mongo Database and name it Data Tracker. #DONE
# Add your SPRINT 3 products file to MongoDB you just created. #DONE
# Create a collection for your top 3 products in MongoDB. #Done 
# Insert multiple documents into your collections in question (3) #DONE
# Implement a descending sort to your data in MongoDB. #DONE
# Delete 2 brands from your collection of top 3 products. #DONE
# Update 1 product and its brands from your collection you created in question (3).
# Track (Search/Filter) for the least 5 brands in your products.
# Save your MongoDB data and code to GitHub
# Make your work accessible to your team members on GitHub.

import pymongo
from pymongo import MongoClient

        # Create a Mongo Database and name it Data Tracker.
cluster = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.dug3r.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["data_tracker"]

                # Add your SPRINT 3 products file to MongoDB you just created.

#collection = db["data_tracker"]
#entry1 = {"_id":1, "label": "Chips", "brand1": "Simba", "brand2": "Lays", "Sold_Items": 10}
#entry2 = {"_id":2, "label": "Cooldrink", "brand1": "Coke", "brand2": "Fanta", "Sold_Items": 20}
#entry3 = {"_id":3, "label": "Chocolates", "brand1": "Cadbury", "brand2": "Tex", "Sold_Items": 50}
#entry4 = {"_id":4, "label": "Pies", "brand1": "Pepper Steak", "brand2": "Chicken", "Sold_Items": 10}
#entry5 = {"_id":5, "label": "Fruit", "brand1": "Pear", "brand2": "Apple", "Sold_Items": 30}
#entry6 = {"_id":6, "label": "Cupcakes", "brand1": "Vanilla", "brand2": "Chocolate", "Sold_Items": 50}
#entry7 = {"_id":7, "label": "Veggies", "brand1": "Spinach", "brand2": "Cabbage", "Sold_Items": 15}
#entry8 = {"_id":8, "label": "Sweets", "brand1": "Jelly Tots", "brand2": "Jelly Babies", "Sold_Items": 10}
#entry9 = {"_id":9, "label": "Soup", "brand1": "ButterNut", "brand2": "Noodle", "Sold_Items": 20}
#entry10 = {"_id":10, "label": "Burger", "brand1": "Chicken", "brand2": "Beef", "Sold_Items": 50}
#entry11 = {"_id":11, "label": "Pizza", "brand1": "Margarita", "brand2": "Tica Chicken", "Sold_Items": 20}
#collection.insert_many([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11])

        # Create a collection for your top 3 products in MongoDB.
        # Insert multiple documents into your collections in question

        # Top product 1
#collection = db["Chocolates"] 
#entry1 = {"_id":1, "brand 1": "Cadbury", "Sold_Items": 35}
#entry2 = {"_id":2, "brand 2": "Tex", "Sold_Items": 15}
#entry3 = {"_id":3, "brand 3": "Mars", "Sold_Items": 25}
#entry4 = {"_id":4, "brand 4": "Toblerone", "Sold_Items": 25}
#entry5 = {"_id":5, "brand 5": "Ghirardelli", "Sold_Items": 10}
#entry6 = {"_id":6, "brand 6": "Ferrero Rocher", "Sold_Items": 40}
#collection.insert_many([entry1, entry2, entry3, entry4, entry5, entry6])

        # Top product 2
#collection = db["Cupcakes"]
#entry1 = {"_id":1, "brand 1": "Vanilla", "Sold_Items": 30}
#entry2 = {"_id":2, "brand 2": "Chocolate", "Sold_Items": 20}
#entry3 = {"_id":3, "brand 3": "Lemon With Lavender Frosting", "Sold_Items": 25}
#entry4 = {"_id":4, "brand 4": "Easy Little Pandas", "Sold_Items": 25}
#entry5 = {"_id":5, "brand 5": "Triple Salted Caramel", "Sold_Items": 40}
#entry6 = {"_id":6, "brand 6": "Sprinkles' Strawberry", "Sold_Items": 10}
#collection.insert_many([entry1, entry2, entry3, entry4, entry5, entry6])

        # Top product 3
#collection = db["Burgers"]
#entry1 = {"_id":1, "brand 1": "Chicken", "Sold_Items": 25}
#entry2 = {"_id":2, "brand 2": "Beef", "Sold_Items": 25}
#entry3 = {"_id":3, "brand 3": "Fish", "Sold_Items": 20}
#entry4 = {"_id":4, "brand 4": "Portobello Mushroom", "Sold_Items": 30}
#entry5 = {"_id":5, "brand 5": "Veggie", "Sold_Items": 15}
#entry6 = {"_id":6, "brand 6": "Turkey", "Sold_Items": 35}
#collection.insert_many([entry1, entry2, entry3, entry4, entry5, entry6])


        # Implement a descending sort to your data (via Sold_Items) in MongoDB.
        # sort("name", -1) #descending

collection = db["Burgers"]
mydoc = collection.find().sort("Sold_Items", -1)
for x in mydoc:
  print(x)

print('')

        # Delete 2 brands from your collection of top 3 products.
#collection = db["Chocolates"] 
#print('Documents in Chocolates\n-----------------------')
#for doc in collection.find():
#	print(doc)
#query = {"Sold_Items": 25}
        # delete many document
#collection.delete_many(query)
#print('\nDocuments in Chocolates after delete_many	()\n-----------------------')
#for doc in collection.find():
#	print(doc)

#collection = db["Cupcakes"] 
#print('Documents in Cupcakes\n-----------------------')
#for doc in collection.find():
#	print(doc)
#query = {"Sold_Items": 25}
        # delete many document
#collection.delete_many(query)
#print('\nDocuments in Cupcakes after delete_many	()\n-----------------------')
#for doc in collection.find():
#	print(doc)

#collection = db["Burgers"] 
#print('Documents in Burgers\n-----------------------')
#for doc in collection.find():
#	print(doc)
#query = {"Sold_Items": 25}
        # delete many document
#collection.delete_many(query)
#print('\nDocuments in Burgers after delete_many	()\n-----------------------')
#for doc in collection.find():
#	print(doc)


                # Update 1 product and its brands from your collection you created in question (3).

#collection = db["Chocolates"] 
#query = { "brand 2": "Tex", "Sold_Items": 15}
#newvalues = { "$set": { "Sold_Items": 25 } }
#collection.update_one(query, newvalues)
        # print "Cupcakes" after the update:
#for x in collection.find():
#  print(x)

#collection = db["Cupcakes"] 
#query1 = { "brand 6": "Sprinkles' Strawberry", "Sold_Items": 10}
#newvalues1 = { "$set": { "Sold_Items": 25 } }
#collection.update_one(query1, newvalues1)
     # print "Cupcakes" after the update:
#for x in collection.find():
#  print(x)

#collection = db["Burgers"] 
#query2 = { "brand 5": "Veggie", "Sold_Items": 15}
#newvalues2 = { "$set": { "Sold_Items": 25 } }
#collection.update_one(query2, newvalues2)
      # print ("Burgers") after the update:
#for x in collection.find():
#  print(x)


        # Track (Search/Filter) for the least 5 brands in your products.

collection = db["Chocolates"] 
        #Retrieving data
print("Documents in the collection: ")
for x in collection.find({"Sold_Items":{"$lt":50}}): # Less Than 50 as we only have 5 products
    print(x)

print('')

collection = db["Cupcakes"] 
        #Retrieving data
print("Documents in the collection: ")
for x in collection.find({"Sold_Items":{"$lt":50}}): 
    print(x)

print('')

collection = db["Burgers"]
        #Retrieving data
print("Documents in the collection: ")
for x in collection.find({"Sold_Items":{"$lt":50}}):
    print(x)

        #Save your MongoDB data and code to GitHub
        #Make your work accessible to your team members on GitHub.