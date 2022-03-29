donut_names = ['Margherita', 'Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']

donut_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

number_donuts = 12

print("How many pizzas would you like to order? ")
num_donut = int(input())

for count in range (number_donuts):
    print (count+1, donut_names[count], donut_prices[count])