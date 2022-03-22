# Customer details
customer_details = {}

def not_blank(question):
    valid = False
    while not valid:
        response = input (question) #asks the question
        if response != "":
            return response.title()
        else:
            print ("This cannot be blank")

# Basic instruction

def pickup():
#Customer name
    question = ("Please enter your name: ") # Question
    customer_details['name'] = not_blank(question) # goes off with the function not_blank with the question
    print (customer_details['name'])     

    #Customer Phone
    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])  

    #Customer house number
    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])  

    #Customer street name
    question = ("Please enter your street name: ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])  

    #Customer suburb
    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb']) 

pickup()