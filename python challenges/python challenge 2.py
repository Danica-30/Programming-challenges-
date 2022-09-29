#python challenge 2
#rsm=richter scale measurement
def getenergyinjoules(rsm):
    energy=10**((1.5*rsm)+4.8)
    return energy

def getTNT(rsm):
    TNT= getenergyinjoules(rsm)/(4.184*(10**9))
    return TNT

def run():
    richter_values=[1,5,9.1,9.2,9.5]
    print("Richter:  Joules:    TNT: ")
    for x in richter_values:
        print(f" {x}     {getenergyinjoules(x)}      {getTNT(x)}")
    user_rsm= float(input("please enter a richter scale measuremnet: "))
    print(f" Richter value: {user_rsm}")
    print(f" Equivalence in joules:{getenergyinjoules(user_rsm)}")
    print(f" Equivalence in tons of TNT: {getTNT(user_rsm)}")

run()
        
    
