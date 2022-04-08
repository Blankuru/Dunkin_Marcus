import sys
import random
from random import randint


#Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10


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



#List to store orderd donuts
order_list=[]


#List to store donuts prices    
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




def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print ("Input must only contain letters")
        else:
            return response.title()



# Validates inputs to check if there is any integer
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}")
        except ValueError:
            print ("That is not a valid number")
            print(f"Please enter a number between {low} and {high}")





def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                print(num)
                return str(num)
            else:
                print ("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print ("Please enter your number")







#Welcome Function
def welcome():
    ''' 
    Purpose: To generate a random name from the list and print out 
    a welcome message
    parameter: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dunkin Marcus***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious donuts***")




#Menu for pickup and delivery 
def order_type(): 
 del_pick= ""
 print ("Is your order for pickup or delivery?")
 print ("For pickup please enter 1")
 print ("For delivery please enter 2")
 while True:
    try: 
     delivery = int(input("Please enter a number: "))
     if delivery >= 1 and delivery <= 2:  
        if delivery == 1:
            print ("pickup") 
            pickup_info()
            del_pick = "pickup"
            break
        
        elif delivery == 2:
            print ("delivery")
            delivery_info()
            del_pick = "delivery" 
            break 
     else:
         print ("Number must be 1 or 2")
    except ValueError:
      print("That is not a valid number")
      print("please enter 1 or 2")
 return del_pick 

















#pick up information- name and phone number 
def pickup_info():
    question = ("Please enter your name: ")
    customer_details['name'] = check_string(question )
    print (customer_details['name']) 
        
    question = ("Please enter your phone number: ")
    customer_details ['phone'] = check_phone(question, PH_LOW, PH_HIGH )
    print (customer_details ['phone'])
    print(customer_details)

# Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name: ")
    customer_details['name'] = check_string(question )
    print (customer_details['name']) 
        
    question = ("Please enter your phone number: ")
    customer_details ['phone'] = check_phone(question, PH_LOW, PH_HIGH )
    print (customer_details ['phone'])

    question = ("Please enter your house number: ")
    customer_details ['house'] = not_blank(question )
    print (customer_details['house'])

    question = ("Please enter your street name: ")
    customer_details ['street'] = check_string(question )
    print (customer_details['street'])

    question = ("Please enter your suburb: ")
    customer_details ['suburb'] = check_string(question )
    print (customer_details['suburb'])




#Donut Menu
def menu():
    number_donuts = 12

    for count in range (number_donuts):
        print ("{} {} ${:.2f}" .format(count+1, donut_names[count], donut_prices[count]))



# Ask for total number of donuts for order
def order_donut():
    num_donuts = 0
    while True:
        try:
            num_donuts = int(input("How many donuts do you want to order? "))
            if num_donuts >= 1 and num_donuts <= 5:
                break
            else:
                print ("Your order must be between 1 and 5")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")

    #Choose donut from menu 
    for item in range(num_donuts):
        while num_donuts > 0:
            while True:
                try:
                    donut_ordered = int(input("Please choose your donut by entering the number from the menu: "))
                    if donut_ordered >= 1 and donut_ordered <=12:
                        break
                    else:
                        print ("Your order must be between 1 and 12")
                except ValueError:
                    print ("This is not a valid number")
                    print ("Please enter 1 or 12")
            donut_ordered = donut_ordered - 1
            order_list.append(donut_names[donut_ordered])
            order_cost.append(donut_prices[donut_ordered])
            print("{} ${:.2f}" .format(donut_names[donut_ordered],donut_prices[donut_ordered]))
            num_donuts = num_donuts - 1


#Print order out - Including if order is delivery or pickup and names and prices of each donut - total cost including any delivery charge 
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer_Details")
    if del_pick =="pickup":
         print("Your order is for pickup")
         print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
         print("Your order is for delivery a $5.00 delivery charge applies")
         total_cost = total_cost + 5
         print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Deatils")
    count= 0  
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}") 


#Ability to cancel or proceed with order 
def confirm_cancel():
    print("Please confirm Your Order")
    print ("To confirm please enter 1")
    print ("To Cancel please enter 2")
    while True:
        try: 
            confirm = int(input("please enter a number: "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Order confirm")
                    print ("Your order has been sent to our kitchen")
                    print ("Your delicious donuts will be with you shorlty")
                    new_exit()
                    break 

                elif confirm == 2:
                    print ("Your Order has been Cancelled")
                    print ("Your can restart your order or exit the BOT")
                    new_exit()
                    break 
            else:
                print ("Number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("please enter 1 or 2")


# Option for new order or to exit 
def new_exit():
    print("Do you want to start another Order or Exit")
    print ("To start another order enter 1")
    print ("To exit the BOT enter 2")
    while True:
        try: 
          confirm = int(input("please enter a number: "))
          if confirm >= 1 and confirm <= 2:  
            if confirm == 1:
                print ("New Order")
                order_list.clear()
                order_cost.clear()
                customer_details.clear
                main()
                break 
            
            elif confirm == 2:
                print ("Exit")
                order_list.clear()
                order_cost.clear()
                customer_details.clear
                sys.exit()
                break 
          else:
            print ("Number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("please enter 1 or 2: ")



#Main function
def main():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None 
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_donut()
    print_order(del_pick)
    confirm_cancel()




main()

