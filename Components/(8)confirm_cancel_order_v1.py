print("Please Confirm Your Order")
print ("To Confirm please enter 1")
print ("To Cancel please enter 2")
while True:
    try: 
     Confirm = int(input("please enter a number"))
     if Confirm >= 1 and Confirm <= 2:
        if Confirm == 1:
            print ("Order Confirm")
            print ("Your order has been sent to our kitchen")
            print ("Your delicious donuts will be with you shorlty")
            break 

        elif Confirm == 2:
            print ("Your Order has been Cancelled")
            print ("Your can restart your order or exit the BOT")
            break 
     else:
         print ("Number must be 1 or 2")
    except ValueError:
      print("That is not a valid number")
      print("please enter 1 or 2")