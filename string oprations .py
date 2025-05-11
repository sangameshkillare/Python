
#what is string and what are the diff ways to create string ?
#string is mutable and immutable in nature?
#WAP to print string =" I like Python programming " output ="programmingpythonlikeI"
#what is difference betn capitalize and title in string? with example .
#what are different operation in string explain all syntaxand with their example ?


#Q=1)what is string and what are the diff ways to create string ?


#--> String is the sequense of the charecter enclosed in the qoutes (single,double ,triple,f-string).

#Proof =>
# s1=('sangamesh')
# print(s1)
# s2=("sangamesh")
# print(s2)
# s3=(''' sangamesh 
#     B
#     Killare''')
# print(s3)


# name = "Sangameshwar"
# s5 = f"Hello, {name}!"
# print(s5)  # Output: Hello, Sangameshwar!



#Q=2) string is mutable and immutable in nature?


#-->Strings in Python are immutable, meaning once a string is created, it cannot be changed.

#Proof=>
# s = "Hello"
# s[0] = "J"  # ❌ This will raise an error: TypeError: 'str' object does not support item assignment


##WAP to print string =" I like Python programming " output ="programmingpythonlikeI"

# string =" I like Python programming "
# string2=string[::-1]

# print(string2.lower())






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


