#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
mov1 = movies.append(input("Enter your first movie = " ))
mov2 = movies.append(input("Enter your second movie = "))
mov3 = movies.append(input("Enter your third movie =  "))

print(movies)

#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = [1,2,3,4,5,6]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")

else:
    print("NOT palindrome")


list2 = [1,2,2,1]
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")

else:
    print("NOT palindrome")

#WAP to count the number of students with the “A” grade in the following tuple

tup =["C" ,"D", "A","A","B","B","A"]
tup.count("A") 
print(tup.count("A"))

#Store the above values in a list & sort them from “A” to “D”
tup =["C" ,"D", "A","A","B","B","A"]
tup.sort()
print(tup)








