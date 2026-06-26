#project to build calculator
#select of operation
print("Selected operation are: \n 1.addition \n 2.substraction \n 3.multiplication \n 4.divide")

a = input("please select your operation:") 

Num1 = float(input("Please select your first number = "))
Num2 = float(input("Please select your second number = "))

if(a == "addition"):
    print(Num1+Num2)

elif(a == "substraction"):
    print(Num1-Num2)

elif(a == "multiplication"):
    print(Num1*Num2)

elif(a == "divide"):
    print(Num1%Num2)

else:
    print("Invalid,Please try again.")




