#Bug - accepts blank input

print ("Please enter your pickup information")

#Customer name
valid = False
while not valid:
    name = input("Please enter your name: ")
    print ("")
    if name != "":
        print (name)
        break

    else:
        print ("Sorry this cannot be blank") 
        
#Customer phone
valid = False
while not valid:
    phone = int(input("Please enter your phone number: "))
    if phone != "":
        print (phone)
        break
    
    else:
        print ("Sorry this cannot be blank")

