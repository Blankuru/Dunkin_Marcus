import random
from random import randint

#List of names of the people who will greet the customers
names = ["Shawn", "Karlo", "Louis", "Jodek", "Carlos", "Mikara", "Tomas", "Giancarlo", "Joaquin", "Jacob"]

#random integer which is num
num = randint(0,9) 

# name is the list of names within the list with the random integer on it which creates a random name from the list
name = (names[num]) 

#prints Welcome to Dunkin Marcus
print ("*** Welcome to Dunkin Marcus ***")
#prints "My name is" and a name from someone in the list
print ("*** My name is", name, "***")
#prints that he/she will be helping with the customer's order
print ("***I will be here to help your order your delicous donuts***")