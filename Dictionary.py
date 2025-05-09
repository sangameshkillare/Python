#Dict is not mutable nor imutable , values can be changed but keys not keys can not be changed .
dict={"name":"sangamesh","age":21,"education":"B.voc"}
dict2={1:"raj",2:45}
dict3={1:"ram,5,sam"}

# dict["name"]="killare" #this is how we can modify and change the element.
# print(dict)

# dict["location"]="pune"
# dict.update({"location":"pune"})  #Add new key and value in dictionaries
# print(dict)
 
# dict["color"]="white" # add new key and value 
# print(dict)

## @ Some improtant method in dictionary 

# a=dict.values()
# print(a)

#dict.remove("name")
# print(dict)

# dict.clear()
# print(dict)

# del dict
# print(dict)

# dict.pop['name']
# dict.pop('name')
# print(dict)


# dict.popitem()
#print(dict.popitem())


## @ how can we add two  dictionaries 

# print({**dict ,** dict2})
# print(dict | dict2) # union
# dict.update({dict2})
# print(dict)

#loop in Dict

# for x in dict.values():#keys and use  items for printing both
#     print(f"{x}")