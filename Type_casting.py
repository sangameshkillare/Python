# print("Hello Sangamesh its your new laptop .")


#@int->float
# x=45
# new_x=float(x)
# print(new_x)
# print(type(new_x))

# #@float to str
# x=5.5
# new_x=str(x)
# print(new_x)
# print(type(new_x))


#@str to float 
# x="56.37"
# new_x=float(x)
# print(new_x)
# print(type(new_x))

# x="4443"
# new_x=int(x)
# print(new_x)
# print(type(new_x))





#LIST TO SET OR WRITE A PROGRAM FOR A LIST AND COVERT INTO UNIQUE ELEMENTS
# list =(1,2,3,4,5,6,6,7,8,8,9,4)
# list1=set(list)
# print(list1)
# print(type(list1))


# list =(1,2,3,4,5,6,6,7,8,8,9,4)
# list1=tuple(list)
# print(list1)
# print(type(list1))


# list =(1,2,3,4,5,6,6,7,8,8,9,4)
# list1=str(list)
# print(list1)
# print(type(list1))


# list =(1,2,3,4,5,6,6,7,8,8,9,4)
# list1=set(list)
# print(list1)
# print(type(list1))
# set=list(list1)
# set1=(1,2,3,4,5)
# set=list(set1)
# print(set)
# print(type(set))


# t=(1,2,3,4,5)
# string=set(t)
# print(string)
# print(type(string))

# set={1,2,3,4,5}
# list=list(set)
# print(list)
# print(type(list))

# set={1,2,3,4,5}
# list=dict(set)
# print(list)
# print(type(list))


# dict={1:"wwe",2:"eew"}
# set=set(dict)
# print(set)
# print(type(set))

# #int +float
# x=3
# y=3.5
# z=x+y
# print(z)
# print(type(z))


# int +bool
# x=True
# y=3
# z=x+y
# print(z)

#int +complex
# x=3
# y=(3+k)
# z=x+y
# print(z)


# #float +bool
# x=True
# y=3.5
# z=x+y
# print(z)


# #float +int
# x=4
# y=3.5
# z=x+y
# print(z)

# #float +complex
# x=7.5
# y=(7+8j)
# z=x+y
# print(z)


# #bool+int
# x=True
# y=3
# z=x+y
# print(z)


# #bool+float
# x=True
# y=3.5
# z=x+y
# print(z)

# #bool+complex
# x=True
# y=(7+9j)
# z=x+y
# print(z)


#append ,extend , and insert


# list=[1,2,3,4]
# list.extend([7,8])
# print(list)

# list=[1,2,3,4]
# list.insert(2,8)
# print(list)


list=[1,2,3,4]
list.append(8)
print(list)


# list=[1,2,2,3,4]
# list.remove(2)
# print(list)


# list=[1,2,3,4,]
# list.clear()
# print(list)



# list1=[1,2,3,4,]
# del(list1)
# #print(list)
# print(list1)


# list2=[1,2,3,4,5,6]
# to_remove=(2,3,4)

# for i in to_remove:
#     if i in list2:
#         list2.remove(i)
# print(list2)

#@count function
# list=[1,1,2,3,4,5]
# print(list.count(1))

#@Length function
# list=[1,1,2,3,4,5]
# a=len(list)
# print(a)

# list=[1,7,2,3,4,5]
# listr=sorted(list,reverse=True)
# print(listr)



# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# to_remove = [3, 5, 7]
# for i in to_remove:
#     if i in my_list:
#         my_list.remove(i)
# print(my_list)  


num=int(input("enter the number for factorial :"))

print(num)
i=1
fact=1
while i <= num:
    fact*=i
    i+=1
    
print(fact)    