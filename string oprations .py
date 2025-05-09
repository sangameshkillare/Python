###String concatention

#string is mutable or immutable 

# s1="Hello"
# s2="World"
# s1 = "h" + s1[1:] 
# print(s1)
# print(s1+" "+s2)



# print(s1)
# #s1=s1+22
# print(s1)


###Slicing

# s1='sangamesh-Bholenath-killare '
# print(s1[5:])
# print(s1[7:5:-1])#here 7 is a starting point of operation and 5th index is end of the operation and -1 is the direction of the operation . 
# print(s1[7:])
# print(s1[:5])
# print(s1[7:-1])
# print(s1[7:0:-1])
# print(s1[::-2 ])
 

# for x in "Sangamesh":
#     print(x)


#===------- membership operators in and no in 
# print('sangamesh '  not in s1)
# print('sangamesh '   in s1)

#----replace function 

# print(s1.replace("sangamesh","Sangameshwar"))
# print(s1)


#----------split function 
# print(s1.split('-'))

# lower,upper,capitalize,title (all first letter of the  str becomes cappital ),concatination (+),length


# name='sangamesh Bholenath killare '
# education='bvoc (sd)'
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.capitalize()+education.title())
# print(len(name))