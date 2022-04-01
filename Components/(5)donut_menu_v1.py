donut_names = ['Jelly', 'Strawberry Creame','Chocolate Cream','Boston Cream Donuts','Red Velvet','Glazed','Peanut Butter Glazed','Apple fritters',
                'Sugared Rasberry','Chocolate Coco','Chocowhite powder','Pinky Heart']

donut_prices = [4.50, 5.50, 6.50, 6.50, 7.50, 7.50, 8.50, 9.50, 9.50, 10.50, 13.50, 13.50]

number_donuts = 12

print("How many donuts would you like to order? ")
num_donut = int(input())

for count in range (number_donuts):
    print (count+1, donut_names[count], donut_prices[count])