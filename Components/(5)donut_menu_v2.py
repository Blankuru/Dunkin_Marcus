donut_names = ['Margherita', 'Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']

donut_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]



print("How many donuts would you like to order? ")
num_donut = int(input())

def menu():
    number_donuts = 12

    for count in range (number_donuts):
        print ("{} {} ${:.2f}" .format(count+1, donut_names[count], donut_prices[count]))
        
menu()