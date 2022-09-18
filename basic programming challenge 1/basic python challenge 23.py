radius1=float(input("what is the raidus of the flower bed: "))
length_of_garden=float(input("what is the length of your garden"))
width_of_garden=float(input("what is the width of your garden"))
def area_of_rectangle(length,width,radius):
    import math
    area= length*width
    flowerbed=radius*(math.pi)
    total_area= area-flowerbed
    return total_area
answer=area_of_rectangle(length_of_garden,width_of_garden,radius1)
print(f"the total amount of turf needed: {answer}")
