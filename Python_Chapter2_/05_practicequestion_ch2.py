#questionpractice
#Grade students based on marks
#marks >= 90, grade = “A”
#90 > marks >= 80, grade = “B”
#80 > marks >= 70, grade = “C”
#70 > marks, grade = “D

marks = 66
if(marks >= 90):
    print("Grade = A")
elif(marks >= 80 and marks < 90):
    print("Grade = B")
elif(marks >= 70 and marks < 80):
    print("Grade = C")
else:
    print("Grade = D ")

#WAP to check if a number entered by the user is odd or even
no = int(input("enter your no ="))

if(no % 2 == 0):
    print("EVEN")

else:
    print("ODD")

#WAP to find the greatest of 3 numbers entered by the user
a = int(input("enter your first num = "))
b = int(input("enter your second num = "))
c = int(input("enter your third num = "))

if(a>=c and a>=b):
    print("first num is largest", a)
elif(b>=c):
    print("second num is largest", b)
else:
    print("third num is largest",c)

#WAP to find the greatest of 4 numbers entered by the user

a = int(input("enter your first num = "))
b = int(input("enter your second num = "))
c = int(input("enter your third num = "))
d = int(input("enter your fourth num = "))

if(a>=c and a>=b and a>=d):
    print("first num is largest", a)
elif(b>=c and b>=d):
    print("second num is largest", b)
elif(c>=d):
    print("third num is largest",c)
else:
    print("fourth num is largest",d)

#WAP to check if a number is a multiple of 7 or not.

number =int(input("enter your number ="))

if(number % 7 == 0):
    print("number is divisible by 7")
else:
    print("Not divisible by 7")










