# list of donut names
donut_names = ['Margherita', 'Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']


# list of donut prices
donut_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered donuts
order_list = []

#list to store donut prices
order_cost = []



def menu():
    number_donuts = 12

    for count in range (number_donuts):
        print ("{} {} ${:.2f}" .format(count+1, donut_names[count], donut_prices[count]))

menu()  




def order_donut():
    # ask for total number of donuts for order
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

    #choose donut from menu 
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

menu()
order_donut()