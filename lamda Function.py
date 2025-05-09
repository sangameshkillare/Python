# A lambda in Python is a way to create small, anonymous (unnamed) functions in a single line. These functions are defined using the lambda keyword and are often used for short, simple operations where defining a full function using def might feel excessive.

# Characteristics:
# Anonymous: Lambda functions don’t have a name (unless assigned to a variable).
# Single Expression: Limited to one expression, unlike def functions, which can contain multiple statements.
# Compact: Used for small operations, especially in scenarios where brevity is valued.



# #---------------- variable=lambda argument : parameters--------------------
# 10/2=5 reminder=0
# 5/2=2 re=1
# 2/2=1 re=0
# 1/2=0 re =1





#examples

    
# ----------------------------addition and multiplication both  of numbers using binary




# add=lambda x,y: x+y  & x*y 
# print(add(5,6))



#-------------------------addition using lambda


# add=lambda x,y:x+y 
# print(add(3,4))


# add = lambda a,b: a+b 
# print(add(3, 4))




#-----------------

# add=lambda x,y:x+y | x*y 
# print(add(5,6))


# add=lambda x,y:x/y 
# print(add(3,4))





# ------------------write a program to print the squre in list 



# original=[2,4,5,8]
# square=list(map(lambda x : x*x,original))
# print((square))#for store the element .

# original=[2,3,4,5]
# square=list(map(lambda x: x**2 , original))
# print((square))


# -----------------------#write a program to print the cube of unique element  in list 

# numbers=[1,2,4,6]
# square=map(lambda x :x**3,numbers)
# print(list(square))    #for store the element .


#--------------------------even number


# original =[1,2,3,4,5,6,7,8,9]
# even=list(map(lambda x:x%2==0,original))
# print(list(even))

# original =[1,2,3,4,5,6,7,8,9]
# even=list(filter(lambda x:x%2==0,original))
# print(list(even))

# #-------------------------even


# numbers=[1,2,4,6]
# square=list(filter(lambda x :x%2==0,numbers))
# print(list(square))    #for store the element .


# #----------------------------odd


# numbers=[1,2,4,6]
# square=list(filter(lambda x :x%2!=0,numbers))
# print(list(square))  


#---------------sort list using lambda

# city=["mumbai","Banglore","Pune","nashik"]
# sorted_format=sorted(city ,key=lambda city:city.lower(),reverse=True)
# print(sorted_format)

# list1=[1,2,2,3,6,5,4,8,9,6]
# sort=sorted(list1 ,key=lambda list1:list1 )
# print(list1)





#________________lambda function within the fuction


# def multiplier(n):
#     return lambda x:x*n

# a=multiplier(2)
# b=multiplier(3)

# print(a(5))
# print(b(5))
    



#----------------- lambda in dictionary


# operations = {
#     'add': lambda x, y: x + y,
#     'subtract': lambda x, y: x - y,
#     'multiply': lambda x, y: x * y,
#     'divide': lambda x, y: x / y if y != 0 else 'undefined'
# }

# print(operations['add'](10,5))
# print(operations['divide'](10,0))
# print(operations['subtract'](10,5))
# print(operations['multiply'](10,5))



#-----------use lambda to et square of list



# nums=[1,2,3,4,5]
# f=list(map(lambda x : x**2,nums))
# print(f)



# #----------even or odd


# nums=[1,2,3,4,5,6,7,8,9]
# even_odd=list(map(lambda x:x if x%2==0 else "odd",nums))
# print(even_odd)





#----------------------sort list


# nums=[1,2,3,4,5,6,11,22,8,9]
# list=sorted(nums,key=lambda x:x)
# print(list)

# nums=[1,2,3,4,5,6,11,22,8,9]
# list=sorted(nums,key=lambda x:-x)
# print(even_odd)


#---------------sort list with tuple and list element



# list=[[3,4],[5,6],[10,3]]
# sorted_list=sorted(list, key=lambda x:x[0])           #----------------[1 or 0 ] are differs 0 is for 1 st eelement of tuple and 1 is stand for second element.
# print(sorted_list)




#----------------sort list of string using lambda , by length of the string and by alpha sequence 


# words = ["banana", "apple", "cherry","chiku","zen","sanb"]

# sorted_words = sorted(words, key=lambda x:x)
# # sorted_words = sorted(words, key=lambda x:len(x))

# print(sorted_words) 



#--------------sort by last word of string 



# words = ["banana", "apple", "cherry","chiku","zen","sanb"]

# sorted_words = sorted(words, key=lambda x:x[::-1],reverse=True)

# print(sorted_words) 



#---------------sorting by multiple criteria


# pairs = [(1, 3), (4, 1), (2, 3), (4, 3)]
# sorted_pairs=sorted(pairs,key=lambda x:(x[1],x[0]))
# print(sorted_pairs)



#----------------------fibo series


# n=int(input("Enter the number :"))
# for i in range(0,n):
#     n=i
#     fibo=lambda n:n if n<=1 else fibo(n-1) + fibo(n-2)
#     print(f"Fibonacchi of {i} th term is {fibo(n)}")



#____________________________finding sq of list 



# l=[1,2,3,4,5,6]
# l2=list(map(lambda x:x**2,l))
# print(l2)


#_________________________________


# grades = ["A", "B", "C", "D"]
# word=list(map(lambda grade: 4 if grade == "A" else (3 if grade == "B" else 2), grades))
# print(word)




###______________________----------------filter




#------use filter in the lambda for even and odd


# nums=[1,2,3,4,5,6,7,8,9]
# even_odd=list(filter(lambda x:x%2==0 ,nums))
# print(even_odd)



# l1 = [-2, -1, 4, 5, 6]
# l2=list(filter(lambda x:  x < 0, l1))
# print(l2)