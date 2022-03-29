from  tkinter.messagebox import QUESTION


def order_type(low, high, question): 
 while True:
    try: 
        num = int(input)
        if num >= low and num <= high:
            return num
        else:
            print(f"Please enter a number between {low}, "and", {high}")
    except ValueError:
        print("That is not a valid number")
        print(f"Please enter a number between {low}, "and", {high}")

LOW = 1
HIGH = 12
QUESTION(f"Enter a number between {LOW}, "and", {HIGH}")

answer = order_type(LOW, HIGH, QUESTION)

print(answer)