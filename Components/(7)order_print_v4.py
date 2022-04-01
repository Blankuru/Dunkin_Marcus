#list to store ordered donuts
order_list = ['Jelly', 'Strawberry Creame','Chocolate Cream','Boston Cream Donuts']

#list to store donut prices
order_cost = [4.50, 5.50, 6.50, 6.50]

cust_details = {'name': 'Mark', 'phone': '324124', 'house': '45', 'street': 'Harry', 'suburb': 'Howick'}



def print_order():
    total_cost = sum(order_cost)
    print ("Customer Details")
    print (f"Customer Name: {cust_details['name']} \nCustomer Phone:{cust_details['phone']} \nCustomer Adress: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print ()
    print ("Order Details")

    count = 0
    for item in order_list:
        print ("Ordered: {} Cost ${:.2f}" .format (item, order_cost[count]))
        count = count+1
    print ()
    print("Total Order Cost")
    print (f"${total_cost:.2f}")

print_order()