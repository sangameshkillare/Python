#{Set} is collection of hetrogenious unorder elements and uniq element .

#union,intersection,diff,simitric difference,sorted, add,update,min,max,del,length,pop,remove,clear,


#proof-->

# set={1,1,2,3,4,5}
# print(set)

# set2={1,3,5,4,2,2,2,2,2}
# print(set==set2)


# whos performance is good , tuple,list or list ?


# set={1,1,2,3,4,5}

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


# ##multiple elementts add in set using update 
# set.update([5,6,7])
# print(set)

# #or

# new=[9,8,90]
# set.update(new)
# print(set)




##clear and del and len function


# s={1,2,3,4,5,5,5,5,5,5,5,6,7,8,9,0}
# s.clear()
# print(len(s))

# del (s)
# print(s)





###union , differnce,intersection


# s={1,2,3,4,5}
# s2={5,7,8,9,2}
# union=s | s2
# print(union)
# intersection= s& s2
# print(intersection)
# diff=s-s2
# print(diff)
# semitric_diff=s ^ s2
# print(semitric_diff)


# s4={'sa','ko','da'}
# s3={'Bmw',"byd"}
# union=s3|s4
# diff=s3-s4
# print(diff)
# intersection=s3&s4
# print(intersection)
# semitric_diff=s3^s4
# print(semitric_diff)


# s={1,2,3,5,4,6,9,8}
# d=sorted(s,reverse=True)
# print(s)
# print(sorted(s))
# print(s.count(1)) #doesnt work because the there is no use of count in set 
# print(min(s))
# print(max(s))
# print(len(s))

# print(sorted(s))
# s.pop()
# print(s)

# s.remove(5)
# print(s)


# s.update(['sa','ka','da'])
# print(s)

#print(sorted(s,reversed=True))