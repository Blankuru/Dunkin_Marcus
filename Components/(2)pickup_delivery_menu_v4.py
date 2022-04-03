
# Menu so that the user can choose either pickup or delivery 

print ("Do you want your order to be delivered or picked up?")

print ("For pickup please enter 1") 
print ("For delivery please enter 2")
print ("")


low = 1
high = 2

while True:
    try:
        delivery = int(input("Please enter a number: ")) # The space that the customer will have to input in
        if delivery >= 1 and delivery <= 2:
            if delivery == 1: #if the customer presses d for delivery
                print ("Pickup")
                break

            elif delivery == 2: #if the customer presses p for pickup
                print ("Delivery")
                break
        else:
            print ("The number must be 1 or 2")
            print ("")
    except ValueError:
        print ("That is not a valid number")
        print ("")
        print ("Please pick a number between 1 or 2")