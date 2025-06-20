#------------------if element is grater than 3 alpha print it



# list=["apple","Grapes","Mango"]
# list2=[]
# for i in list:
    
#     if len(i)>3:
#         list2.append(i)
# print(list2)


#List comprhension

# fruits=[fruit for fruit in list if len(fruit) > 3]
# print(fruits)





# -----------------------evn odd from the list 


# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = []

# for i in num:
#     if i % 2 == 0:
#         list2.append("Even")
#     else:
#         list2.append("Odd")

# print(list2)



#---------------------List comphrention  find the cube root and sqrt

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sqrt=[x**2 for x in range(1,100)]
# print(sqrt)
# cube=[x**3 for x in  range(1,100)]
# print(cube)
# even=[x for x in num if x%2==0]
# odd=[x for x in num if x%2!=0]
# print(even,odd)

# print([x**3 for x in range(1,10)])



#-----------------------store even and odd in dict and tuple



# evn_od = [{x:"even"} if x % 2 == 0 else {x:"odd "} for x in range(1,11)]
# print( [{x:"even"} if x % 2 == 0 else {x:"odd "} for x in range(1,11)])



#=-----------build in functions in list comprehension



#--------------------------upper lowr and length of list using list comprehension



# list=["apple","Grapes","Mango"]

# upper_case=[word.upper() for word in list]
# print(upper_case)





# list=["apple","Grapes","Mango"]

# upper_case=[word.lower() for word in list]
# print(upper_case)



list=["apple","Grapes","Mango"]



# upper_case=[len(word) for word in list]
# print(upper_case)




num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([min(str(x)) for x in num])

#------------add special char after each element in list




# list=["apple","Grapes","Mango"]
# special_char=[ word + "@ "for word in list]
# print(special_char)

# list=["apple","Grapes","Mango"]
# special_char=[ word + " Sangamesh "for word in list]
# print(special_char)







#------------------add 10 in each ele



# list=[23,45,65,67,76]
# list2=[i + 10 for i in list]
# print(list2)