#list of donut names
donut_names = ['Jelly', 'Strawberry Creame','Chocolate Cream','Boston Cream Donuts','Red Velvet','Glazed','Peanut Butter Glazed','Apple fritters',
                'Sugared Rasberry','Chocolate Coco','Chocowhite powder','Pinky Heart']

#list of donut prices
donut_prices = [4.50, 5.50, 6.50, 6.50, 7.50, 7.50, 8.50, 9.50, 9.50, 10.50, 13.50, 13.50]

#list to store ordered donuts
order_list = []

#list to store donut prices
order_cost = []



def menu():
    number_donuts = 12

    for count in range (number_donuts):
        print ("{} {} ${:.2f}" .format(count+1, donut_names[count], donut_prices[count]))

menu()  





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


print(num_donuts)


#choose donut from menu 
print ("Please choose your donuts by entering the number from the menu: ")
for item in range(num_donuts):
    while num_donuts > 0:
        donut_ordered = int(input())
        donut_ordered = donut_ordered - 1
        order_list.append(donut_names[donut_ordered])
        order_cost.append(donut_prices[donut_ordered])
        print("{} {} ${:.2f}" .format(donut_names[donut_ordered], donut_prices[donut_ordered]))
        num_donuts = num_donuts - 1