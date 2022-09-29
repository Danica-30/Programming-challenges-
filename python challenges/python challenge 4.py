# python challenge 4

def getwindchill(air_temp,air_speed):
    windchill= 35.74+0.6215*(air_temp)-35.75*(air_speed**0.16)+0.4275*(air_temp)*(air_speed**0.16)
    return windchill
def run():
    mylist=[[10.0,15],[0.0,25],[-10.0,35]]
    for x in mylist:
        print(f"Tempature of {x[0]} and speed of {x[1]} gives windchill of : {getwindchill(x[0],x[1])}")
    user_air_temp= float(input("please enter an air tempeature"))
    user_air_speed= float(input("please enter an air speed"))
    print(f"temperature: {user_air_temp}")
    print(f"speed: {user_air_speed}")
    user_windchill=getwindchill(user_air_temp,user_air_speed)
    print(f"windchill: {user_windchill}")
run()
