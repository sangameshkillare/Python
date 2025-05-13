# 1.	What will be printed and why? Explain each slicing step.
# lst = list(range(20))
# #lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# print(lst[::-2][5:10])
# #lst[::-2] = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
# #[5:10]=[9, 7, 5, 3, 1]



# 2.	Predict the output and explain how both positive and negative indexing interact in a nested structure.
# lst = [[i for i in range(5)] for j in range(5)]
# lst[0][0] = 100
# print(lst[-5][-5])

## lst = [
##    [100, 1, 2, 3, 4],  -5=100
##    [0, 1, 2, 3, 4],  
##    [0, 1, 2, 3, 4],  
##   [0, 1, 2, 3, 4],  
##   [0, 1, 2, 3, 4]   
##]


# 3.	What will be the output? Why does this slicing work?
# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(lst[::-1][1::3])



# 4.	What is the output and what happens if 40 is not in the list?
# lst = [10, 20, 30, 40,50, 60]
# i = lst.index(40)
# print(lst[i - 3:i + 2])



# 5.	What will the list look like after this assignment? Explain how both the left and right slices are evaluated.
# lst = [1, 2, 3, 4, 5]
# lst[1:-1] = lst[-2:0:-1]
# print(lst)
#priginal list prints here



# 6.	What will be printed? What slice is created by lst[::2]?
# lst = list('abcdefghij')
# a, b, *c, d = lst[::2]#concept of python unpacking a=1st,b=2nd,c=middle elementes in [] and createes the list of moddle elements ,d=last elements
# print(a, b, c, d)



# 7.	What element is accessed? How can this be generalized for circular index logic?
# lst = ['a', 'b', 'c', 'd', 'e']
# i = -7   #-7%5=3
# print(lst[i % len(lst)])



# 8.	Why does a remain unchanged? How does slicing impact list mutability?
# a = list(range(10))
# b = a[2:7]
# b[0] = 99
# print(a)
# ________________________________________
# 9.	Write a function custom_slice(lst, start, stop, step) that mimics Python's slicing behavior, including support for negative indices.
# (No code provided — user must implement this.)
# ________________________________________
# 10.	What is the output? Why must the start, stop, and step values be arranged this way?
# lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
# print(lst[-2:-7:-2])
# ________________________________________
# 11.	Why does appending to one sublist seem to affect all others? How would you avoid this?
# lst = [[]] * 3
# lst[0].append(100)
# print(lst)
# ________________________________________
# 12.	Why do append and extend produce different results?
# a = [1, 2]
# b = [3, 4]
# a.append(b)
# print("After append:", a)
# a = [1, 2]
# a.extend(b)
# print("After extend:", a)
# ________________________________________
# 13.	What causes the shared change across elements? How can this be fixed using a list comprehension?
# lst = [[0]] * 3
# lst[1][0] = 7
# print(lst)
# ________________________________________
# 14.	Why are the two sorts different? What is the role of the key parameter?
# names = ['bob', 'Alice', 'dave', 'Carol']
# names.sort()
# print(names)
# names.sort(key=lambda x: x.lower())
# print(names)
# ________________________________________
# 15.	What happens when insert is used with an index beyond the list size?
# lst = [1, 2, 3]
# lst.insert(10, 999)
# print(lst)
# ________________________________________
# 16.	Why does remove raise an error? How could you avoid this in production code?
# lst = [1, 2, 3]
# try:
#     lst.remove(4)
# except ValueError as e:
#     print("Caught:", e)
# ________________________________________
# 17.	Why does print(rev) return None? How can you get a reversed version without modifying the original list?
# lst = [1, 2, 3, 4]
# rev = lst.reverse()
# print(rev)
# ________________________________________
# 18.	Why does clearing a also affect b? What would you do if you want to keep b unchanged?
# a = [1, 2, 3]
# b = a
# a.clear()
# print("a:", a)
# print("b:", b)
# ________________________________________
# 19.	Why does it not remove all the 2s? How can this be fixed?
# lst = [1, 2, 2, 2, 3]
# for i in lst:
#     if i == 2:
#         lst.remove(i)
# print(lst)
# ________________________________________
# 20.	What happens here? Why can inserting while iterating cause unexpected behavior?
# lst = [1, 2, 3]
# for i in range(len(lst)):
#     lst.insert(i,5)
# print(lst)




## what is diff betwen list tuple ,set dict
#what are the diffrent datatype in python and 15 operations on each


#Q-1)

#-->



# | Type      | Ordered | Mutable | Duplicates Allowed      | Syntax Example               | Use Case                                       |
# | --------- | ------- | ------- | ----------------------- | ---------------------------- | ---------------------------------------------- |
# | **List**  | Yes     | Yes     | Yes                     | `my_list = [1, 2, 3]`        | Store ordered items, often with duplicates     |
# | **Tuple** | Yes     | No      | Yes                     | `my_tuple = (1, 2, 3)`       | Fixed collections of items (e.g., coordinates) |
# | **Set**   | No      | Yes     | No                      | `my_set = {1, 2, 3}`         | Unique items, like tags or categories          |
# | **Dict**  | Yes     | Yes     | Keys: No<br>Values: Yes | `my_dict = {'a': 1, 'b': 2}` | Key-value pairs (e.g., name → age)             |


#Q-2)

#--> 
#1) list 
# 15 Common Operations:
# lst.append(5)

# lst.extend([6, 7])

# lst.insert(1, 10)

# lst.remove(3)

# lst.pop() / lst.pop(2)

# lst.index(2)

# lst.count(2)

# lst.sort()

# lst.reverse()

# len(lst)

# sum(lst)

# min(lst) / max(lst)

# lst[1] – Indexing

# lst[1:3] – Slicing

# for item in lst: – Looping


#2) tuple

# 15 Common Operations:
# tup.count(2)

# tup.index(3)

# tup[0] – Indexing

# tup[1:3] – Slicing

# len(tup)

# min(tup) / max(tup)

# sum(tup)

# 2 in tup

# for i in tup: – Loop

# sorted(tup) – Returns a list

# tuple([1,2]) – Convert list to tuple

# tup + (4, 5)

# tup * 2

# any(tup) / all(tup)

# enumerate(tup)



#3)set

# 15 Common Operations:
# s.add(4)

# s.remove(2)

# s.discard(5) – No error if not found

# s.pop()

# s.clear()

# s.union({4, 5})

# s.intersection({2, 3})

# s.difference({1})

# s.symmetric_difference({3, 4})

# len(s)

# 2 in s

# set([1, 2, 2]) – Convert list to set

# s.isdisjoint({10, 11})

# s.issubset({1,2,3,4})

# s.issuperset({1,2})

# 4) dict

# 5 Common Operations:
# d["a"] – Access value

# d.get("b")

# d["c"] = 3 – Add/update

# d.update({"d": 4})

# d.keys()

# d.values()

# d.items()

# d.pop("a")

# d.popitem() – Removes last

# "b" in d

# len(d)

# d.clear()

# dict.fromkeys(["x", "y"], 0)

# for k, v in d.items(): – Loop

# del d["b"]



#5)int

# 15 Common Operations:
# + Addition

# - Subtraction

# * Multiplication

# / Division

# // Floor Division

# % Modulus

# ** Exponentiation

# abs(a) – Absolute value

# round(b) – Round to nearest integer

# int(b) – Convert to integer

# float(a) – Convert to float

# complex(a, b) – Create complex number

# a > b, a < b, etc. – Comparisons

# divmod(a, b) – Returns quotient and remainder

# pow(a, b) – a to the power of b



# 6) Strting


# 15 Common Operations:
# s.upper()

# s.lower()

# s.title()

# s.capitalize()

# s.strip() – Trim spaces

# s.replace("hello", "hi")

# s.find("world")

# 'world' in s

# s.count("l")

# len(s)

# s.split(" ")

# " ".join(["hi", "there"])

# s[0] – Indexing

# s[0:5] – Slicing

# s.endswith("d") / s.startswith("h")

