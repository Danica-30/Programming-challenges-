
name = input("enter name: ")

def maths_quiz_q1(x_1):
    if x_1== int(-2):
        Q1_mark=int(3)
    else:
        Q1_mark=int(0)
    mark1 = Q1_mark
    return mark1

def maths_quiz_q2(x_2):
    if x_2== int(-10):
        Q2_mark=int(3)
    else:
        Q2_mark=int(0)
    mark2= Q2_mark
    return mark2
       

def maths_quiz_q3(x_3):
    if x_3== int(3):
        Q3_mark=int(3)
    else:
        Q3_mark=int(0)
    mark3=Q3_mark
    return mark3

def file_test_data():
    print("please solve for x:")
    print("x^2 + 4x + 4")
    firstx=int(input("x = "))
    print("please solve for x:")
    print("x^2 + 20x + 100")
    secondx=int(input("x = "))
    print("please solve for x:")
    print("x^2 - 6x + 9")
    thirdx= int(input("x = "))
    total_mark= (maths_quiz_q1(firstx))+ (maths_quiz_q2(secondx))+ (maths_quiz_q3(thirdx))
    f=open("student_test_result.txt","w")
    f.write(f"Name: {name}")
    f.write("\n")
    f.write(f" Question 1 mark: {maths_quiz_q1(firstx)}")
    f.write("\n")
    f.write(f" Question 2 mark:{maths_quiz_q2(secondx)}")
    f.write("\n")
    f.write(f" Question 3 mark: {maths_quiz_q3(thirdx)}")
    f.write("\n")
    f.write(f"total mark = {total_mark} out of 9")
    f.close()

file_test_data()
f= open("student_test_result.txt","r")
print(f.read())
