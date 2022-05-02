import sys  # Import system
import random  # Imports a random number generator
from random import randint  # from random it would be imported to randint
from tkinter.messagebox import QUESTION  # imports QUESTION from tkinter.messagebox


# Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10


# List of names of the people who will greet the customers
names = ["Shawn", "Karlo", "Louis", "Jodek", "Carlos",
         "Mikara", "Tomas", "Giancarlo", "Joaquin", "Jacob"]


# list of donut names
donut_names = ['Jelly', 'Strawberry Creame', 'Chocolate Cream',
               'Boston Cream Donuts', 'Red Velvet',
               'Glazed', 'Peanut Butter Glazed', 'Apple fritters',
               'Sugared Rasberry', 'Chocolate Coco', 'Chocowhite powder',
               'Pinky Heart']


# list of donut prices
donut_prices = [1.50, 1.50, 1.50, 2.00, 2.00, 2.50, 2.50,
                2.50, 3.50, 3.50, 4.00, 4.00]


# List to store ordered donuts
order_list = []


# List to store donuts prices
order_cost = []

# customer details dictionary
customer_details = {}


# Validate inputs to check if they are blank
def not_blank(question):  # Creates function not_blank
    valid = False  # Valid is false
    while not valid:  # While variable is not valid
        response = input(question)  # Asks question
        if response != "":  # If response is not blank
            return response.title()  # Returns to response with Capitalization
        else:  # If it was printed blank
            print("This cannot be blank")  # Prints error message


def check_string(question):  # Function for inputs that requires letters only
    while True:  # creates loop
        response = input(question)  # Asks question
        x = response.isalpha()  # Only accepts letters
        if x is False:  # If x is false which means that the input are numbers
            print ("Input must only contain letters")  # Prints error message
        else:
            return response.title()  # If input are letters, it returns to response with capitilazation


# Validates inputs to check if there is any integer
def val_int(low, high, question):  # Function for valid integer
    while True:  # While function is true
        try:  # While the function is true it will try to do the code below
            num = int(input(question))  # Asks question
            if num >= low and num <= high:  # If input is low and high
                return num  # Returns and accepts input
            else:  # If input is not 1 or 2
                print(f"Please enter a number between {low} and {high}")  # Asks for input again
        except ValueError:  # If input is a letter
            print ("That is not a valid number")  # Prints error message
            print(f"Please enter a number between {low} and {high}")  # Asks for input again


# Function for inputs that requires phone numbers only
def check_phone(question, PH_LOW, PH_HIGH):  # Creates function for phone number
    while True:  # creates loop
        try:  # While the function is true it will try to do the code below
            num = int(input(question))  # Asks question
            test_num = num  # Variable test_num is num
            count = 0  # Count is equal to 0
            while test_num > 0:  # while test_num is > 0
                test_num = test_num//10  # test_num is equal to test_num divided by 10
                count = count + 1  # count is equal to count + 1
            if count >= PH_LOW and count <= PH_HIGH:  # if count is >= to PH_LOW and <= PH_HIGH
                return str(num)  # returns to str(num)
            else:  # If input is below 7 or above 10 numbers
                print ("NZ phone numbers have between 7 and 10 digits")  # Prints message
        except ValueError:  # If input is blank or letters
            print ("Please enter your number")  # Prints message


# Creates logo function
def logo():
    print ()
    print ("***********************************************************")
    print ("********************** Dunkin Marcus **********************")  # prints logo
    print ("***********************************************************")
    print ()
# creates a function "welcome"
def welcome():
    '''
    Purpose: To generate a random name from the
             list and print out a welcome message
    Parameters: None
    Returns: None
    '''
# random integer which is num
num = randint(0, 9)

# name is the list of names within the list with the
# random integer on it which creates a random name from the list
name = (names[num])

logo()  # prints logo
# prints Welcome to Dunkin Marcus
print ("*** Welcome to Dunkin Marcus ***")
# prints "My name is" and a name from someone in the list
print ("*** My name is", name, "***")
# prints that he/she will be helping with the customer's order
print ("*** I will be here to help your order your delicous donuts ***")


# Menu for pickup and delivery
# Function for type of order whether it is pickup or delivery
def order_type():
    del_pick = ""  # del_pick is <blank>
    print ("Is your order for pickup or delivery? ")  # Asks question
    print ()  # prints blank line
    print ("For pickup please enter 1")  # Asks if it is pickup by entering 1
    print ("For delivery please enter 2")  # Asks if it is delivery by entering 2
    while True:  # creates loop
            try:  # Tries the code below
                delivery = int(input("Please enter a number: "))  # asks to please enter a number
                print ()  # prints blank line
                if delivery >= 1 and delivery <= 2:  # if delivery variable is >= 1 and <= 2
                    if delivery == 1:  # if input is 1
                        print ("Pickup")  # prints pickup
                        pickup_info()  # does pickup_info function
                        del_pick = "Pickup"  # del_pick variable is pickup
                        break  # breaks loop
                    elif delivery == 2:  # if delivery variable is 2
                        print ("Delivery")  # prints delivery
                        delivery_info()  # does delivery_info function
                        del_pick = "Delivery"  # del_pick variable is delivery
                        break  # breaks loop
                else:  # If input is not 1 or 2
                    print ("Number must be 1 or 2")  # asks input to be 1 or 2
            except ValueError:  # If input are letters and <blank>
                print("That is not a valid number")  # prints message
                print ()  # prints blank line
                print("Please enter 1 or 2")  # asks input to be entered 1 or 2
    return del_pick  # returns input to del_pick


# pick up information- name and phone number
def pickup_info():  # Creates pickup info function
    question = ("Please enter your name: ")  # Asks question
    customer_details['Name'] = check_string(question)  # stores name in customer_details also checks if input is in letters
    print (customer_details['Name'])  # prints customer name
    print ()  # prints blank line

    question = ("Please enter your phone number: ")  # asks phone number
    customer_details['Phone'] = check_phone(question, PH_LOW, PH_HIGH)  # stores phone in customer_details also checks if input is in numbers
    print (customer_details['Phone'])  # prints customer phone
    print(customer_details)  # prints customer details
    print ()  # prints blank line


# Delivery information - name address and phone
def delivery_info():  # Creates delivery info function
    question = ("Please enter your name: ")  # asks to enter your name
    customer_details['Name'] = check_string(question)  # stores name in customer details also checks if input is letters
    print (customer_details['Name'])  # prints customer name
    print ()  # prints blank line

    question = ("Please enter your phone number: ")  # asks phone number
    customer_details['Phone'] = check_phone(question, PH_LOW, PH_HIGH)  # stores phone in customer_details also checks if input is in numbers between 7 and 10
    print (customer_details['Phone'])  # prints customer phone
    print ()  # prints blank line

    question = ("Please enter your house number: ")  # asks for house number
    customer_details['House'] = not_blank(question)  # stores house number in customer_details also checks
    print (customer_details['House'])  # prints customer house number
    print ()  # prints blank line

    question = ("Please enter your street name: ")  # asks for street name
    customer_details['Street'] = check_string(question)  # stores street name in customer_details also checks if input is letters
    print (customer_details['Street'])  # prints customer street name
    print ()  # prints blank line

    question = ("Please enter your suburb: ")  # asks for suburb
    customer_details['Suburb'] = check_string(question)  # stores suburb in customer_details also checks if input is letters
    print (customer_details['Suburb'])  # prints customer suburb
    print ()  # prints blank line


# Donut Menu
def menu():  # function for menu
    number_donuts = 12  # total of donuts in the menu

    for count in range(number_donuts):  # for count in range of variable number_donuts
        print ("{} {} ${:.2f}" .format(count+1, donut_names[count],
                                       donut_prices[count]))  # format of menu, which shows list from 1 to 12, donut names, and prices


# Function for ordering donuts
def order_donut():  
    num_donuts = 0  # num_donuts is 0
    while True:  # creates loop
        try:  # tries code below
            print ()  # prints blank line
            num_donuts = int(input("How many donuts do you want to order between 1 and 8? "))  # Asks question
            if num_donuts >= 1 and num_donuts <= 8:  # if num_ donuts is >= 1 and <= 8
                break  # breaks loop
            else:  # if not between 1 and 8
                print ("Your order must be between 1 and 8")  # prints that your order must be between 1 and 8
        except ValueError:  # If input is a letter or <blank>
            print ("That is not a valid number")  # prints error message
            print ("Please enter a number between 1 and 8")  # Asks for input between 1 and 8

# Choose donut from menu
    for item in range(num_donuts):  # for item in range variable num_donuts
        while num_donuts > 0:  # while num_donuts is 0
            while True:  # while variable is true
                try:  # tries code below
                    print ()  # prints blank line
                    donut_ordered = int(input("Please choose your donut by entering the number from the menu: "))  # Asks question in integer
                    if donut_ordered >= 1 and donut_ordered <= 12:  # if donut ordered is >= 1 and <= 12
                        break  # breaks loop
                    else:  # if order is not between 1 and 12
                        print ("Your order must be between 1 and 12")  # prints order must be between 1 and 12
                except ValueError:  # If input is in letters or <blank>
                    print ("This is not a valid number")  # Prints error message
                    print ("Please enter between 1 and 12")  # Asks for input to be between 1 and 12
            donut_ordered = donut_ordered - 1  # donut_ordered is minus 1 per order inputted
            order_list.append(donut_names[donut_ordered])  # order list appending donut names and donut ordered input
            order_cost.append(donut_prices[donut_ordered])  # order cost appending donut prices and donut ordered input
            print("{} ${:.2f}" .format(donut_names[donut_ordered],
                                       donut_prices[donut_ordered]))  # prints in format
            num_donuts = num_donuts - 1  # num_donuts is minus 1 per order it is inputted


# Print order out - Including if order is delivery or pickup and names and prices of each donut - total cost including any delivery charge
def print_order(del_pick):  # creates function
    print()  # prints blank line
    total_cost = sum(order_cost)  # total_cost is sum of order_cost
    print("Customer Details")  # prints Customer Details
    if del_pick == "Pickup":  # if del_pick is pickup
        print("Your order is for pickup")  # prints order is for pickup
        print(f"Customer Name: {customer_details['Name']}")  # prints customer name
        print(f"Customer Phone: {customer_details['Phone']}")  # prints customer phone
    elif del_pick == "Delivery":  # if del_pick is delivery
        print(f"Customer Name: {customer_details['Name']}")  # prints customer name
        print(f"Customer Phone: {customer_details['Phone']}")  # prints customer phone
        print(f"Customer Address: {customer_details['House']} {customer_details['Street']} {customer_details['Suburb']}")  # prints customer address
    print()  # prints blank line
    print("Your Order Details")  # prints order details
    count = 0  # count is 0
    for item in order_list:  # for items in order list
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))  # prints order in format
        count = count + 1  # count gets added by 1
    print()  # prints blank line
    if del_pick == "Delivery":  # if del_pick is delivery
        if len(order_list) >= 5:  # if length of order list is >= 5
            print ("Your order will be free of delivery charge")  # prints order will be free of delivery charge
        elif len(order_list) <= 5:  # if length of order list is <= 5
            print ("There is an additional $9.00 delivery charge")  # prints additional delivery charge of $9.00
            total_cost = total_cost + 9  # adds 9 to total cost

    print("Total Order Cost")  # prints total order cost
    print(f"${total_cost:.2f}")  # total cost in format


# Ability to cancel or proceed with order
def confirm_cancel():  # creates confirm_cancel function
    print("Please confirm your order")  # prints please confirm your order
    print ("To confirm please enter 1")  # prints to enter 1 for confirmation
    print ("To cancel please enter 2")  # prints to enter 2 for cancel
    while True:  # Creates loop
        try:  # tries code below
            confirm = int(input("please enter a number: "))  # asks for input
            if confirm == 1:  # if confirm is 1
                print ("Order confirm")  # prints order is confirmed
                print ()  # prints blank line
                print ("Your delicious donuts will be with you shorlty")  # prints message
                new_exit()  # executes to new_exit function
                break  # breaks loop

            elif confirm == 2:  # if confirm is 2
                print ("Your order has been Cancelled")  # order has been cancelled
                print ()  # prints blank line
                print ("You can restart your order or exit the store")  # prints that you can order or exit the store
                new_exit()  # executes to new_exit function
                break  # breaks the loop
            else:  # if input is not 1 or 2
                print ("Number must be 1 or 2")  # prints error message
        except ValueError:  # if input is letters or <blank>
            print("That is not a valid number")  # prints error message
            print("please enter 1 or 2")  # asks to enter 1 or 2


# Option for new order or to exit
def new_exit():  # creates new_exit function
    print("Do you want to start another Order or Exit")  # prints if you want to start another order or exit
    print ("To start another order enter 1")  # prints to press 1 if you want to start another order
    print ("To exit the store enter 2")  # prints to press 2 if you want to exit the store
    while True:  # creates loop
        try:  # tries code below 
            confirm = int(input("please enter a number: "))  # asks input
            if confirm == 1:  # if confirm is 1
                print ("New Order")  # prints new order
                order_list.clear()  # order list information is cleared
                order_cost.clear()  # order cost information is cleared
                customer_details.clear  # customer details is cleared
                main()  # back to main fucntion
                break  # breaks loop
            elif confirm == 2:  # if confirm is 2
                print ("Exit")  # prints exit
                order_list.clear()  # order list information is cleared
                order_cost.clear()  # order cost information is cleared
                customer_details.clear  # customer details is cleared
                logo()  # prints logo
                sys.exit()  # system exit
            else:  # if input is not 1 or 2
                print ("Number must be 1 or 2")  # prints number between 1 or 2
        except ValueError:  # if input is letters or <blank>
            print("That is not a valid number")  # prints that is not a valid number
            print("please enter 1 or 2: ")  # asks for input
            

# Main function
def main(): 
    '''
    Purpose: To generate a random name from the list and print
             out a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()  # executes welcome function
    del_pick = order_type()  # executes order_type function
    menu()  # executes menu function
    order_donut()  # executes order_donut function
    print_order(del_pick)  # executes print_order function
    confirm_cancel()  # executes confirm_cancel function
    new_exit()  # executes new_exit function

main()  # executes main program
