###Tuple in Imutable means it cannot be changed once decleared , it is similer to the list , it is writen in () brasses,ordered (index ,position  matters). , allow  duplicates .
##insert, append , replce can not be used here 
#we can acsses the element the element .





#what is tuple , with their example .
#tuple ordered or unordered collection of elements ? if ordered then why  if not then why ?
#is it possible to print reverse the tuple , why?
#what is tuple unpacking ?
#where we use tuple in real world ?



#Q=1) what is tuple , with their example .

# -->Tuple just like the list which stores the multiple elements,ordered(each element have their unique index) and written in () brasses , but there is only on key dffierence is the elements in tuple is can not be modified, remove ,and cannot add any element in the tuple . 

# tuple=(1,1,3,2,5,7,9,3)

# tuple.append(6) 
# print(tuple)
# tuple.remove(3)
# print(tuple)
# tuple.insert(2,"3")
# print(tuple)


#Q=2)tuple ordered or unordered collection of elements ? if ordered then why  if not then why ?

#-->Tuple is ordered collection of element because each element in the tuple have there unique and own index position . 
# proof =>  
# t1=(1,2,3,4,5)
# t2=(1,2,3,4,5)
# print(t1==t2)  

# Result is true because the all elements in t1 and t2 are same in the sense the element on index positions of the both tuple is same .

# t2=(1,2,3,4,5,6)  # here we are reasigning the tuple t2 thats why the value is 6 is getting add in the tuple 
# print(t1==t2)
# print(t2)
 
# The result is false because the  elements on the index position are mis matched . t1 == t2 is  wrong statement  beacause of new element is  add in the t2  thats why false got printed . 



#Q=3)Is it possible to print reverse the tuple , why?

#--> We cant print the tuple in reverse using the buildin fuctions (reverse), But Yes with using the slicing  we can print  the tuple in reverse .  


#proof=>
 
# tuple=(1,3,2,5,7,9,3)
# # print(tuple.reverse())
# print(tuple[::-1])


# Q=4) what is tuple unpacking ?


# tuple=(1,3,2,5,7,9,3)
# print(tuple[4])
# print(tuple[::-1])
# print(tuple[0:6:2])
# print(tuple.reverse())

# tuple.append(6) 
# print(tuple)

# tuple.sort()
# print(tuple)
# list=(2,3)

# tuple.extend(list)
# print(tuple)
 
# tuple.remove(3)
# print(tuple)

# del tuple
# print(tuple)

# a=len(tuple)
# print(a)

#a=min(tuple)
# print(min(tuple))
# b=max(tuple)
# print(b)


# a=tuple.count(3)
# print(a)

# a=sorted(tuple)
# print(a)
# t1=(1,3,2,5,7,9,3)
# t2=sorted(t1)
# print(tuple(t2))

#_____in the situation where  add  of element is important in tuble needs to perform concate ation


# t1=(1,2,3,4)
# t2=(5,6,7,7)
# print(t1+t2)


# multidimentional tuple



# t3=(1,2,3,4,(4,3,"python"),55)

# print(t3)
# print(t3[4][2])


