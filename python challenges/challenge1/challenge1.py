# Rod conversions
def getmetres(rods):
    metres= rods*5.0292
    return metres

def getfeet(rods):
    foot=getmetres(rods)/0.3048
    return foot

def getmiles(rods):
    miles=getmetres(rods)/1609.34
    return miles

def getfurlongs(rods):
    furlongs=rods/40
    return furlongs

def gettime(rods):
    speed=3.1
    time=(getmiles(rods)/speed)*60
    return time

def run():
    rod1=float(input("input rods: "))
    print(f" your input {rod1}")
    print("conversions: ")
    print(f"meters: {getmetres(rod1)}")
    print(f"feet: {getfeet(rod1)}")
    print(f"miles: {getmiles(rod1)}")
    print(f"furlongs: {getfurlongs(rod1)}")
    print(f"minutes to walk: {gettime(rod1)}")

run()
