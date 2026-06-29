#list = it store any value(str,int,float,boolean)
marks = [98.8, 97.7, 65.0, 68.7, 79.5, 74.5, 90.8, 86.7, 75.0, 84.0, 62.9, 66.0]
print(type(marks))
print(marks)
#its act like string also
print(len(marks))
print(marks[1])
print(marks[7])
print(marks[9])
#but we can change the value here which is not possible in string
#For example
student = ["shriti",12,66.8,"Jharkhand"]
student[1] = 10
student[0]="choti"
student[2]=84
student[3]="Dhanbad"
print(student)
#so in this case we see it doesnt run
#listslicing (same as str)
print(marks[8:10])
print(marks[:12])
print(marks[0:])
print(marks[-8:-1])

#listmethod
#list.append
list = [40,54,72,25]
list.append(42)
print(list)
#list.sort
#descending
list.sort(reverse = True)
print(list)
#aescending
list.sort()
print(list) 
#reverse.list
list.reverse()
print(list)
#list.insert
list.insert(1,68)#write the position which you want to replace
print(list)
#list.remove(first appearence of the number)
list = [1,2,3,4,6,5,6]
list.remove(6)
print(list)
#list.pop
list.pop(5)
print(list)



