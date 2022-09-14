def speed(Distance,Time):
    speed= Distance/Time
    return speed
    
distance= int(input("please enter a distance in metres: "))
time= int(input("please enter a time in seconds: "))
answer= speed(distance,time)
print(f" The average speed is : {answer}")
