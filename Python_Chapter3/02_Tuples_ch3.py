#tuples
#The value of tuples are also not changeable like string 
tup = (8,6,4,3)
print(type(tup))
tube = (1,) #it is mandatory in tuple for one element to put ,(koma)
print(type(tube))
tuk = (1,4,6,7) #For more than one element it was not mandatory to put koma, its shows tuple always.
#it works almost the same as string and list.

#tuple method
#tup.index = gives the position of the number
tup = (3,6,4,2,8)
tup.index(6)
print(tup.index(6))

tup = (3,6,4,2,8,6)
tup.index(6)
print(tup.index(6))#in the case of double number it give the index of the first appearence number

#tup.count()= it gives the total times of a particular no. present in a tuple
tup.count(6)
print(tup.count(6))

#slicing (works same as list and string)
print(tup[1:4])

