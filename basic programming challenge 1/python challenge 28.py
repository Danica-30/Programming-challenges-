name_1= input("please enter the first name: ")
name_2= input("please enter the second name: ")
name_3= input("please enter the third name: ")
name_4= input("please enter the fourth name: ")
name_5= input("please enter the fith name: ")
array=[name_1,name_2,name_3,name_4,name_5]
import random
randominteger=random.randint(1,5)
print(f"name chosen: {array[randominteger]}")
