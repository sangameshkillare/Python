# def my_function():   #Defining
#     print("Hello from my_function") # block of code
    
# my_function()  #Calling



#___________ARGUMENT  passing a data to function from outside the function


#____________________single argument


# def my_function(fname):   #Defining
#     print(fname) # block of code
    
# my_function("sangamesh")  #Calling and passing single argument
# my_function("yash")




#______________________adding two arguments 


# def my_function(fname,lname):   #Defining
#     print(fname,lname) # block of code
    
# my_function("sangamesh","Killare")  #Calling and passing single argument


#______________________ading 3 arguments


# def my_function(fname,mname,lname):   #Defining
#     print(fname,mname,lname) # block of code
    
# my_function("sangamesh","B.","Killare")  #Calling and passing single argument





# #______________________Arbitary argument 

# if we dont know the how many argument want pass the fuction 



# def function_name(*name):
#     print(*name)
#     print(name) #it will give the elements in tuple formate
# function_name("sonu","monu","chiku")



# def add(*num):
#     return sum(num)
# print(add(3,4,5,3))



#_______________________keyword parameters


# def keyword(name1,name2,name3):
#     print(name1,name2,name3)
    
# keyword("sonu","monu","chiku")



#______________________Defailt parameter

# def nation(nation="norway"):
#     print("country :" + nation)
# nation("india")
# nation()
    
    
    
###__________________-------------+++++++++++ imp question 


# whta is difference between *argu and **argu



# #----------two types of functions -len,split,sort,sorted
# and user defined function




#_____________________

# def add_number(a=4,b=5):
#     print(a+b)
# add_number(a=7)


# def add_number(a=4,b=5):
#     return a+b
# re=add_number(7,7)
# re1=add_number(4,4)
# print(re)
# print(re1)

#_________________del function

# def add_number(a=4,b=5):
#     return a+b
# add_number(a=7)
# # del add_number()
# print(type(add_number()))


#________________________even odd


# def even(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("odd")
        
# num=int(input("enter number :"))
# even(num)


#_______________________leap year


# def leap(year):
#     if year%4==0:
#         print("It is leap year :")
#     else:
#         print("it is normal year :")
# year=int(input("enter year ;"))
# leap(year)



#____________________check positive negative int

# def number(num):
#     if num>0:
#         return "Positive"
#     else:
#         return "negative"
# num=int(input("Enter the number :"))
# print(number(num))


#__________________prime number


# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return "Not prime"
#         else:
#             return "Prime number"
# num=int(input("enter the Number :"))
# prime(prime(num))