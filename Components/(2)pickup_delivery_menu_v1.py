# Menu so that the user can choose either pickup or delivery 

print ("Do you want your order to be delivered or picked up?")

print ("For delivery press d, for Pickup press p")


# The space that the customer will have to input in
delivery = input()

#if the customer presses d for delivery
if delivery == "d":
    print ("Delivery")

#if the customer presses p for pickup
elif delivery == "p":
    print ("Pickup")

#if inputed something else then it will print out the one shown below
else:
    print("That is not an option, press d for delivery or p for pickup")

