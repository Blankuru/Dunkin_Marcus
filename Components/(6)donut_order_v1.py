#list of donut names
donut_names = ['Glazed', 'Chocolate Frosted','Chocolate Glazed','Jelly','Strawberry frosted','Chocolate Kreme','Sugared Rasberry','Glazed Rasberry',
                'Vanilla Kreme','Strawberries and Cream','Double Chocolate','Cookies and Cream']

#list of donut prices
donut_prices = [3.20, 4.00, 4.00, 4.50, 4.50, 5.50, 5.50, 5.50, 6.00, 6.50, 6.50, 7.00]

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

num_donuts = int(input("How many donuts do you want to order? "))

print(num_donuts)


#choose pizza from menu 
print ("Please choose your donuts by entering the number from the menu: ")
for item in range(num_donuts):
    while num_donuts > 0:
        donut_ordered = int(input())
        order_list.append(donut_names[donut_ordered])
        order_cost.append(donut_prices[donut_ordered])
        num_donuts = num_donuts - 1

print (order_list)
print (order_cost)







#countdown until all donuts are ordered



#print order