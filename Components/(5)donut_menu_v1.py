donut_names = ['Glazed', 'Chocolate Frosted','Chocolate Glazed','Jelly','Strawberry frosted','Chocolate Kreme','Sugared Rasberry','Glazed Rasberry',
                'Vanilla Kreme','Strawberries and Cream','Double Chocolate','Cookies and Cream']

donut_prices = [3.20, 4.00, 4.00, 4.50, 4.50, 5.50, 5.50, 5.50, 6.00, 6.50, 6.50, 7.00]

number_donuts = 12

print("How many donuts would you like to order? ")
num_donut = int(input())

for count in range (number_donuts):
    print (count+1, donut_names[count], donut_prices[count])