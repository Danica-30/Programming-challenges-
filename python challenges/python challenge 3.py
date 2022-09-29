#python challlenge 3
#def yourpart(yourinput):
    #final_value1 = 99-yourinput
    #return final_value1

def friendpart(friendinput,yourinput):
    final_value1 = 99-yourinput
    value3= (final_value1) +(friendinput)
    r100= (value3)-int(100)
    u1=(r100)+int(1)
    answer= friendinput-(u1)
    return answer

def run():
    value1=int(input("please enter a value between 10 and 49:"))
    value2=int(input("Please enter a value between 50 and 99"))
    final_answer=friendpart(value2,value1)
    print("we are going to play a game. i want you to pick a number then do a series of calculations.i bet i know what the resullt of those calculations will be!")
    print(f"This will be the answer: {value1}")
    print(f"i said the answer was {value1} and the calculation result is {final_answer}")

run()

