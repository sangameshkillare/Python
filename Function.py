#function is a block of code use to perform the specific task . types- predefined(min,max,sum,len,short,count,apend,extend,del,clear,remove,pop,del),userdefined(define by programmer),lambda(anomyous or unnamed function),recursive function.
# list=[1,2,34,5,6,7,7]
# str='sangamesh'
# print(min(list))
# print(min(list))
# print(sum(list))
# print(len(list))
# print(min(str))
# print(len(str))
# list.append(11)
# print(list)

# print(list.remove(1))
# print(list)
# list.pop()
# print(list)
# list.clear()
# print(list)
# del list
# print(list)


# def name():
#     print('sangamesh')

# name()


# def add():
#     a=int(input('enter the a :'))
#     b=int(input('enter the b :'))
#     print(a+b)

# add()

# def add(a,b):
#     print(f'addition : {a+b} and subtraction : {a-b}')
#     # return a+b ,a-b
# add(5,5)


# def add(a,b):
#     return f"addition {a+b} and suntraction {a-b}"
# print(add(5,3))

# def add(*num):
#     return f"sum of the numbers :{sum(num)}"
# print(add(1,2,3,4))

# def add(a=1,b=1,c=1):#default ag=rgument
#     return f"multiplication : {a*b*c}"
# print(add(2,3))


# def num(a,b,c):#keyword argument
#     return f"a : {a},b:{b},c:{c}"
# print(num(a=5,b=6,c=7))


# def even_odd (num):
#     if num%2==0:
#         print('num is even.')
#     else:
#         print('num is odd.')

# print(even_odd(3))
# print(even_odd(2))


#wap to find given num is  positive ,negative or 0

# def find(num):
#     if num>0:
#         return('the number is positive .')
#     elif num<0:
#         return('the number is negative')
#     else:
#         return('the number is zero.')



#wap to check even odd list


# def even_odd (num):
#     if num%2==0:
#         print('num is even.')
#     else:
#         print('num is odd.')

# list=[1,2,3,4,5,6,7,8,9,0]
# for i in list:
#     even_odd(i)


#wap to check the year is leap year or not .

def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('The year is a leap year')
    else:
        print('No')

leap(2024)
leap(2000)
leap(1900)
leap(2023)


#to chek greatest of 3 no :


# def major(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return f"{num1} is the greatest"
#     elif num2 > num1 and num2 > num3:
#         return f"{num2} is the greatest"
#     elif num3 > num1 and num3 > num2:
#         return f"{num3} is the greatest"
#     else:
#         return "No single number is strictly greater than the other two."

# print(major(1, 2, 3))
# print(major(3, 1, 2))
# print(major(2, 3, 1))
# print(major(1, 2, 2))
# print(major(3, 3, 1))
    
# print(find(4))
# print(find(-5))
# print(find(0))

# def stdinfo(name,address,age):
#     return f"name of std : {name} , address : {address} age : {age}"

# print('sangamesh','dehu',21)


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




