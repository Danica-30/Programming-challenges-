def cm_to_in(number):
    return number*0.393700787
def in_to_cm(number):
    return number*2.54
    
    
value= float(input("please input a number to convert: "))
print("menu")
print("1 cm to in")
print("2 in to cm")

choice=input("please choose a type of conversion: (1/2)")
if choice == "1":
    output1 = cm_to_in(value)
    print(f"{value}cm is {output1}inches")
elif choice == "2":
     output2 = in_to_cm(value)
     print(f"{value}inches is {output2}cm")
    
    
    

    

             

