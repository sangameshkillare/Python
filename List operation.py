# List=["Apple","Apple","WaterMelone","Papaya","Mango"]


# a=len(List)
# print(a)


###insert

# List.insert(2,"grapes")
# print(List)
# # print(a)


# ##Apend
# List.append("cherry")
# print(List)

###Extend
# List2=["Kevy","Banana"]
# List.extend(List2)
# print(List)

###pop

# List.remove("Apple")
# print(List)

###Remove

# List.remove("Apple")
# print(List)

###clear

# List.clear()
# print(List)

###Del

# del List
# print(List)


###loop in List

# for i in List:
#     print(i)

#while looop

# i=0
# while i < a:
#     print(List[i])



#wap to print list in reverse order


list=[1,2,3,4,5,6,7,8,9,0]
# i=len(list)-1

# for i in list[::-1]:
#     print(i)

# for i in range(len(list)-1,-1,-1):
#     print(i)




#build in function 


list=[1,2,2,3,4,5,9,4,7]
print(list.reverse())
# print(sum(list))
# list.append(55)
# print(list)

# list2=[9,8,7]
# list2.extend(list)
# print(list2)


# print(max(list))
# print(min(list))
# set1=set(list)
# print(set1)
# list.pop(5)
# # print(list)
# del list
# # print(list)
# list.clear()
# print(list)


# list.insert(5,11)
# print(list)

# length=len(list)
# print(length)

# list.remove(1)
# print(list)
# print(list.count(1))
# print(sum(list))
# index=list.index(3)
# print(list.reverse())
# list2=list.copy()
# print(list2)
# print(type(list))
# sort=sorted(list)
# print(sort)




# x=list(map(int,input("enter list : ").split(',')))
# print(x)

# x = eval(input("Enter dictionary as key:value pairs (e.g., {1:10, 2:20}): "))
# print(x)


# p=eval(input("enter list: "))
# print(p)



# p=eval(input("enter set : "))
# print(p)

#----------- topic-concatination,indexing,1d,2d,3d list,slicing

#indexing 


# list=[1,2,3,4,5,6,7,8,9,10]
# print(list[3])
# print(list[10])

#slicing

# list=[1,2,3,4,5,6,7,8,9,10]


# print(list[1:5])
# print(list[0:])
# print(list[:])#all
# print(list[1::2])#even
# print(list[0::2])#odd

#-----with using buildin functions

# list.reverse()
# print(list)

#-------without using build in functions

# print(list[::-1])#reverse

# print(list[5::-1])
# print(list[::-2])

#--------------



# print(list[4:5])#print 5
# print(list[1:3:2])


#------------------examples of indexing in multi dimentional list


# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(numbers[8:0:-3])


# Number = [1,2,3,[4,5,["Richa","Vaishnavi",34,["it",["It-python"],23,54],6]]]
# tin=Number[3][2][3][1][:]
# #tin=Number[3[2[1:4]]]
# print(tin)

# print(Number[3][4::-1])


# List = [23, 43, 54, [45, 65, 43, (45, 65, 76, [75, 54, [45, 76, 87, "Python", 43, 65], 65, 8], 45, 43), 54, 65, "Raj"]]

# python = List[3][3][3][2][3]
# print(python)

# for element in python:
#     if element == "Python":
#         print(element)
#         break