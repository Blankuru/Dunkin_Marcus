import sys

#List to store orderd donuts 
order_list=[]
#List to store donuts prices
order_cost=[]

#customer details dictionary
customer_details = {}



print("Do you want to start another Order or Exit")
print ("To start another order enter 1")
print ("To exit the BOT enter 2")
while True:
    try: 
     Confirm = int(input("please enter a number"))
     if Confirm >= 1 and Confirm <= 2:
        if Confirm == 1:
            print ("New Order")
            order_list.clear()
            order_cost.clear()
            customer_details.clear
            break 

        elif Confirm == 2:
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
      print("please enter 1 or 2")


def main():
    print("start again") 