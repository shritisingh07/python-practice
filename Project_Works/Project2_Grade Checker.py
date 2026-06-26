#Project of student grade checker

print("Student grade checker")

name = input("Enter your name = ")
student_class = int(input("Enter your class = "))
roll = int(input("Enter your roll = "))
school_name =(input("Enter name of your school = "))

sub1 = int(input("Enter max marks in 1st subject = "))
sub2 = int(input("Enter max marks in 2nd subject = "))
sub3 = int(input("Enter max marks in 3rd subject = "))
sub4 = int(input("Enter max marks in 4th subject = "))
sub5 = int(input("Enter max marks in 5th subject = "))

Total_marks = 500
obtained_marks = sub1+sub2+sub3+sub4+sub5
percentage = obtained_marks/Total_marks*100
Grade = percentage

print("Final result \n --------------")


print("NAME = ",name)
print("CLASS = ",student_class)
print("ROLL = ",roll)
print("NAME OF SCHOOL = ",school_name)
print("MARKS OBTAINED = ",obtained_marks)
print("PERCENTAGE = ",percentage)

if(percentage>=90):
    print("Grade = A+")

elif(percentage>=80):
    print("Grade = A")

elif(percentage>=70):
    print("Grade = B+")

elif(percentage>=60):
    print("Grade = B")
    
else:
    print("Word hard, need more improvment")












