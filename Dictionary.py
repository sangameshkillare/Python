#Dict is not mutable nor imutable , values can be changed but keys not keys can not be changed .
dict={"name":"sangamesh","age":21,"education":"B.voc"}
dict2={1:"raj",2:45}
dict3={1:"ram,5,sam"}

# dict2[2]="killare"
# print(dict2)

#dict["location"]="pune"
# dict.update({"location":"pune"})
# print(dict)
 
# dict["color"]="white"
# print(dict)

# a=dict.values()
# print(a)

# a=dict.keys()
# print(a)

# dict.clear()
# print(dict)

# del dict
# print(dict)

# dict.pop("name")
# print(dict)



dict.popitem()
print(dict)

# print({**dict ,** dict2})
# print(dict | dict2)
# dict.update({dict2})
# print(dict)