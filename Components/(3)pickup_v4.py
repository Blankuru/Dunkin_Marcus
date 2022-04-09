# Customer details
customer_details = {}

def not_blank(question):
    valid = False
    while not valid:
        response = input (question) #asks the question
        if response != "":
            return response
        else:
            print ("This cannot be blank")





# Basic instruction

#Customer name
question = ("Please enter your name: ") # Question
customer_details['name'] = not_blank(question) # goes off with the function not_blank with the question
print (customer_details['name'])     


#Customer Phone
question = ("Please enter your phone number: ")
customer_details['phone'] = not_blank(question)
print (customer_details['phone']) 