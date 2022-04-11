
question = ("enter house number")


def check_int(question):
    while True:
        try:
            num = int(input(question))
            return num
        except ValueError:
            print ("Please enter a valid house number")