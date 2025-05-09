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
