#----------------------convert string of int into decimal


# import decimal
# string='123445'
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string)))



#-----reverse string


# string="I love python programming"
# print(string[::-1])


#------------count vowels in str


# string="I love python programming"
# count=0
# conso=0
# for i in string:
#     if i in 'aeiouAEIOU':
#         count+=1
#     else:
#         conso+=1
        
# print(conso)
# print(count)



#---------------no of occurance of the char in str

# string="programming"
# char='g'
# count=0
# for i in string:
#     if i == char:
#         break
#     count+=1
# print(count)



#-----------fibo series



# num=int(input('enter the number to get fibo series :'))
# n=0
# print(n)
# n1=1
# print(n1)
# fibo=0
# for i in range(0,num):
#     fibo=n+n1
#     n=n1
#     n1=fibo
#     print(fibo)



#--------finding maximun num in list 



# list=[1,2,3,4,5,97,6]

# current_max=list[0]
# for i in list:
#     if i > current_max:
#         current_max=i
# print(current_max)



#-------------find middel number in list


# list=[1,2,3,4,5,6,7]
# middel=int(len(list)/2)
# print(list[middel])



#----------compaire two strings are anagrams or not



# str1="listen"
# str2="silent"
# str1=str1.replace(" ","").upper()

# str2=str2.replace(" ","").upper()

# if sorted(str1)==sorted(str2):
#     print("YES")
# else:
#     print("NO")



#--------------check string is palindrome



# str="saas"
# str1=str[::-1]
# if str==str1:
#     print("Yes")
# else:
#     print("NO")



#-------------count white spaces in str


# str="i love you"
# print(str.count(" "))



#-----------count list element alpha ,degit of spacial char or spaces



# str="i love python and paandas for 123456 operations on @#!"
# alpha=0
# space=0
# num=0
# special=0
# for i in str:
#     if i.isnumeric():
#         num+=1
#     elif i.isspace():
#         space+=1
#     elif not i.isalnum():
#         special+=1
#     elif i.isalpha():
#         alpha+=1
        
# print(alpha,space,special,num)
    
    
    
    
#---------------