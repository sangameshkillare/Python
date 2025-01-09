#{Set} is collection of unorder elements and uniq element .


# set={1,2,3,4,5}
# print(set)
# print(type(set))
# set2={5,4,3,2,1}
# print(set==set2)#Because set is unordered
# set3={"Sangamesh","hello",4,3,2,1}
# print(set3)
# set3.add(5)
# print(set3)


### Add and remove
# set={1,2,3,4,5}
# set.remove(5)##.add  for add
# print(set)


### ele=2 in set ##accecing elements
# print(ele)


# ##multiple elementts add in set
# set.update([5,6,7])
# print(set)

# #or

# new=[9,8,90]
# set.update(new)
# print(set)


###union , differnce,intersection


s={1,2,3,4,5}
s2={7,8,9,2}
new=s ^ s2 ## unionn= | ,diff= -,intersection =& ,semmetric difference=^
print(new)

##clear and del and len function

# #s.clear()
# print(len(s))

# #del (s)
# # print(s)


# s={1,2,3,4,5,6,9,8}
# #d=sorted(s,reverse=True)
# print(min(s))
# print(max(s))
# print(len(s))

# print(sorted(s))
# s.pop()
# print(s)

#print(sorted(s,reversed=True))