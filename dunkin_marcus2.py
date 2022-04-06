import random
from random import randint

#List of names of the people who will greet the customers
names = ["Shawn", "Karlo", "Louis", "Jodek", "Carlos", "Mikara", "Tomas", "Giancarlo", "Joaquin", "Jacob"]
#list of donut names
donut_names = ['Jelly', 'Strawberry Creame','Chocolate Cream','Boston Cream Donuts','Red Velvet','Glazed','Peanut Butter Glazed','Apple fritters',
                'Sugared Rasberry','Chocolate Coco','Chocowhite powder','Pinky Heart']
#list of donut prices
donut_prices = [4.50, 5.50, 6.50, 6.50, 7.50, 7.50, 8.50, 9.50, 9.50, 10.50, 13.50, 13.50]
#creates a function which is "welcome"
def welcome ():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
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

#List to store orderd pizzas 
order_list=[]
#List to store pizzas prices    
order_cost=[]

#customer detalis dictionary
customer_details = {}

#Validate inputs to check if they are blank
def not_blank(question):
    valid = False 
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")







def main():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
    welcome()





main()

