#python challenge 5
#ms=myslayer


def getvaluesforslayer(user_slayer):
    slayer = user_slayer[0]+user_slayer[1]+user_slayer[2]+user_slayer[3]+user_slayer[4]+user_slayer[5]
    layers = user_slayer[1]+user_slayer[2]+user_slayer[3]+user_slayer[4]+user_slayer[5]+user_slayer[0]
    finalslayer= slayer+slayer+slayer
    if finalslayer==layers:
        print("your guess is correct")
        print(f"SLAYER + SLAYER + SLAYER= {finalslayer}")
        print(f"LAYERS = {layers}")
        print("Thaks for playing.")
    else:
        print("your guess is incorrect")
        print(f"SLAYER + SLAYER + SLAYER= {finalslayer}")
        print(f"LAYERS = {layers}")
        print("Thanks for playing.")
        
def run():
    userslayer1= input("please enter a six digit number with -inbetween:eg:(S-L-A-Y-E-R)For what six-digit number SLAYER is the following equation true, where each letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS")
    userslayer2=userslayer1.split("-")
    getvaluesforslayer(userslayer2)
run()
