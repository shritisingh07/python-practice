str1 = "myself"
str2 = '''shriti'''
str3 = str1 + str2 #concatenation
#we can print in ('single code')or("double code")or("'triple code"')
print(str1)
print(str2)
print(str3)
#for adding gape between line use(\t)and for line change use (\n)
str4 ="Introducing myself Shriti Singh.\nWelcome to my project."
str5 = "Introducing myself Shriti Singh.\tWelcome to my project."
str6 = "Introducing myself Shriti Singh.\t\nWelcome to my project."
print(str4)
print(str5)
print(str6)

#length of str
print(len(str1+str2+str3+str4+str5+str6))
final_str = str1+ str2
print(len(final_str))

#indexing
str = "shriti singh"
ch = str[0]
print(str[3])
print(str[6])
print(ch)

#slicing
#positive
print(str[0:7])
print(str[0:]) #0 to len(str)
print(str[:7]) #0 to 7
#negative
print(str[-6:-1])


