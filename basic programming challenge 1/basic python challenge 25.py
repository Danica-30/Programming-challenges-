first_name= input("please enter your name: ")
last_name= input("please enter your last name: ")
Gender = input("please enter your gender: ")
form= input("please enter your form: ")
f= open("school_club_user_data.txt","r")
print(f.read())


f= open("school_club_user_data.txt","w")
f.write(f" First name: {first_name}")
f.write(f" Last name: {last_name}")
f.write(f" Gender  :  {Gender}")
f.write(f"form  : {form}")
f.close()

f= open("school_club_user_data.txt","r")
print(f.read())


