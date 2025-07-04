#Dict is  not mutable (keys) nor imutable(values) , values can be changed but keys not keys can not be changed  . dict is collection of hetrogenious  type of data  ,wirtten in keys and values form and seprated by : coln and written in {}.



# dict={"name":"sangamesh","age":21,"education":"B.voc"}
# dict2={1:"raj",2:45}
# dict3={1:"ram,5,sam"}
 
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



# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# for key, value in my_dict.items():
#     print(f"{key} -> {value}")


## @ how can we add two  dictionaries 

# print({**dict ,** dict2})
# print(dict | dict2) # union
# dict.update({dict2})
# print(dict)

#loop in Dict

# for x in dict.values():#keys and use  items for printing both
#     print(f"{x}")

 



# dict={"name":"sangamesh","age":21,"education":"B.voc"}
# have='age' in dict  #membership operator
# print(have)
# len(dict)
# print(dict.keys())
# print(dict.values())

# dict2={1:'mango',2:'apple',3:'grapes',4:'banana',5:'cherry,[pune,cherry.@.com]'}
# # print(dict2[3])   #access the  keys
# dict['name']="Killare"  #changing the value of key
# print(dict) 
# dict3={'list':'[1,2,3,4,5]','set':"{6,7,8,9,0}"}
# dict3['list']=[1,2,3,4,5,6,6]  #change the values of the keys

# print(dict3)
# dict3.clear()
# print(dict3)
# # del dict3
# print(dict3)
# dict2.update(dict3)  #merge the two different dictionaries
# print(dict2)
# print(dict2|dict3)   #also merge with union 
# dict3['list']=[1,2,3,4,5,6,7,78,8,9]
# print(dict3)
# print(dict,dict2,dict3)
# dict4={ 'hot':'mumbai,delhi','cold':'mahabaleshwar',1:'mumbai,delhi'}
# dict5={'name':('sangamesh','raj','viraj','ajay'),1:{1,2,3,4}}
# print(dict5)





d1={'name':'SANGAMESH','marks':99}
d1['age']=40

print(dict.items())


# print(sorted(d1))  
# print(sort(d1)) #not possible 

# del d1['name']
# print(d1)
# d1.pop('age')
# print(d1)




