###Tuple in Imutable means it cannot be changed once decleared , it is similer to the list , it is writen in () brasses . 
##insert, append , replce can not be used here 
#we can acsses the element the element .


tuple=(1,3,2,5,7,9,3)

# tuple.append(6)
# print(tuple)

# tuple.sort()
# print(tuple)
# list=(2,3)

# tuple.extend(list)
# print(tuple)

# tuple.remove(3)
# # print(tuple)

# del tuple
# print(tuple)

# a=len(tuple)
# print(a)

# a=min(tuple)
# print(a)
# b=max(tuple)
# print(b)


# a=tuple.count(3)
# print(a)

# a=sorted(tuple)
# print(a)

##@ Can we modify or add tuple . The answer is no but using serval methodes  we can modify it 
# 1) change it into list 2) Modify it 3) change it into tuple

# list=list(tuple)
# print(list)
# list.append(28)

# tu=tuple(list)
# print(tu)

# Original tuple
original_tuple = (1, 2, 3)

# Convert the tuple to a list
temp_list = list(original_tuple)

# Add the new value to the list
temp_list.append(4)

# Convert the list back to a tuple
updated_tuple = tuple(temp_list)  # Ensure no variable is named `tuple`

# Print the updated tuple
print(updated_tuple)
