import sys  # Import system
import random  # Imports a random number generator
from random import randint  # from random it would be imported to randint
from tkinter.messagebox import QUESTION


# Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10


# List of names of the people who will greet the customers
names = ["Shawn", "Karlo", "Louis", "Jodek", "Carlos",
         "Mikara", "Tomas", "Giancarlo", "Joaquin", "Jacob"]


# list of donut names
donut_names = ['Jelly Box', 'Strawberry Creame Box', 'Chocolate Cream Box',
               'Boston Cream Donuts Box', 'Red Velvet Box',
               'Glazed Box', 'Peanut Butter Glazed Box', 'Apple fritters Box',
               'Sugared Rasberry Box', 'Chocolate Coco Box', 'Chocowhite powder Box',
               'Pinky Heart Box']


# list of donut prices
donut_prices = [4.50, 5.50, 6.50, 6.50, 7.50, 7.50, 8.50,
                9.50, 9.50, 10.50, 13.50, 13.50]


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

# prints Welcome to Dunkin Marcus
print ("*** Welcome to Dunkin Marcus ***")
# prints "My name is" and a name from someone in the list
print ("*** My name is", name, "***")
# prints that he/she will be helping with the customer's order
print ("***I will be here to help your order your delicous donuts***")


# Menu for pickup and delivery
# Function for type of order whether it is pickup or delivery
def order_type():
    del_pick = ""  # del_pick is <blank>
    print ("Is your order for pickup or delivery? ")  # Asks question
    print ("For pickup please enter 1")  # Asks if it is pickup by entering 1
    print ("For delivery please enter 2")  # Asks if it is delivery by entering 2
    while True:  # creates loop
            try:  # Tries the code below
                delivery = int(input("Please enter a number: "))  # asks to please enter a number
                if delivery >= 1 and delivery <= 2:  # if delivery variable is >= 1 and <= 2
                    if delivery == 1:  # if input is 1
                        print ("pickup")  # prints pickup
                        pickup_info()  # does pickup_info function
                        del_pick = "pickup"  # del_pick variable is pickup
                        break  # breaks loop
                    elif delivery == 2:  # if delivery variable is 2
                        print ("delivery")  # prints delivery
                        delivery_info()  # does delivery_info function
                        del_pick = "delivery"  # del_pick variable is delivery
                        break  # breaks loop
                else:  # If input is not 1 or 2
                    print ("Number must be 1 or 2")  # asks input to be 1 or 2
            except ValueError:  # If input are letters and <blank>
                print("That is not a valid number")  # prints message
                print("please enter 1 or 2")  # asks input to be entered 1 or 2
    return del_pick  # returns input to del_pick


# pick up information- name and phone number
def pickup_info():
    question = ("Please enter your name: ")  # Asks question
    customer_details['name'] = check_string(question)  # customer details 
    print (customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])
    print(customer_details)


# Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name: ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])

    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name: ")
    customer_details['street'] = check_string(question)
    print (customer_details['street'])

    question = ("Please enter your suburb: ")
    customer_details['suburb'] = check_string(question)
    print (customer_details['suburb'])


# Donut Menu
def menu():
    number_donuts = 12

    for count in range(number_donuts):
        print ("{} {} ${:.2f}" .format(count+1, donut_names[count],
                                       donut_prices[count]))


# Ask for total number of donuts for order
def order_donut():
    num_donuts = 0
    while True:
        try:
            num_donuts = int(input("How many donuts do you want to order between 1 and 8? "))
            if num_donuts >= 1 and num_donuts <= 8:
                break
            else:
                print ("Your order must be between 1 and 8")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter a number between 1 and 8")

# Choose donut from menu
    for item in range(num_donuts):
        while num_donuts > 0:
            while True:
                try:
                    donut_ordered = int(input("Please choose your donut by entering the number from the menu: "))
                    if donut_ordered >= 1 and donut_ordered <= 12:
                        break
                    else:
                        print ("Your order must be between 1 and 12")
                except ValueError:
                    print ("This is not a valid number")
                    print ("Please enter 1 or 12")
            donut_ordered = donut_ordered - 1
            order_list.append(donut_names[donut_ordered])
            order_cost.append(donut_prices[donut_ordered])
            print("{} ${:.2f}" .format(donut_names[donut_ordered],
                                       donut_prices[donut_ordered]))
            num_donuts = num_donuts - 1


# Print order out - Including if order is delivery or pickup and names and prices of each donut - total cost including any delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_pick == "pickup":
        print("Your order is for pickup")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery a $9.00 delivery charge applies")
        total_cost = total_cost + 9
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")


# Ability to cancel or proceed with order
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
                    print ("")
                    print ("Your order has been sent to our kitchen")
                    print ("Your delicious donuts will be with you shorlty")
                    new_exit()
                    break

                elif confirm == 2:
                    print ("Your Order has been Cancelled")
                    print ("")
                    print ("You can restart your order or exit the BOT")
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


# Main function
def main():
    '''
    Purpose: To generate a random name from the list and print
             out a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_donut()
    print_order(del_pick)
    confirm_cancel()
    new_exit()

main()
