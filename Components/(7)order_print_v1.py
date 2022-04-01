#list to store ordered donuts
order_list = ['Jelly', 'Strawberry Creame','Chocolate Cream','Boston Cream Donuts']

#list to store donut prices
order_cost = [4.50, 5.50, 6.50, 6.50]

cust_details = {'name': 'Mark', 'phone': '324124', 'house': '45', 'street': 'Harry', 'suburb': 'Howick'}


#print ("Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}" .format(cust_details['name'], cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb']))

print ("Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}" .format(cust_details['name'], cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb']))


count = 0
for item in order_list:
    print ("Ordered: {} Cost ${:.2f}" .format (item, order_cost[count]))
    count = count+1

