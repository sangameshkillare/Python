List=["Apple","WaterMelone","Papaya","Mango"]

a=len(List)

###insert

# List.insert(3,"Grapes")
# print(List)
# print(a)


###Apend
# List.append("cherry")
# print(List)

###Extend
# List2=["Kevy","Banana"]
# List.extend(List2)
# print(List)

###pop

# List.pop(3)
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
#     i=i+1


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
