#---> 1. Reverse a String
#==>



# str='sangamesh B killare'
# reverse=str[::-1]
# print(reverse)


# withjoin=''.join(reversed(str))
# print(withjoin)


#---. 2. Check if a String is a Palindrome

# str2=input("enter the set of charecters to check the is it palindrome : ")
# reverse_str2=''.join(reversed(str2))
# if str2==reverse_str2:
#     print(f'{str2} is palindrome .')
# else:
#     print('Try again .')
    
    
#---> 3. Count the Number of Vowels in a String

# str3='I am the python expert'
# i=0
# consonents=0
# vowel=0
# while i < len(str3):
#     if str3[i] in "aeiouAEIOU":
#         vowel+=1
#     else:
#         consonents+=1
#     i+=1
# print(f"Total count of vowel in {str3} = {vowel}")
# print(f"Total count of consonents in {str3} = {consonents}")


# str3='I am the python expert .'
# vowel=0
# for i in str3:
#     if i in 'aeiouAEIOU':
#         vowel+=1
# print(f"Total count of vowel in {str3} = {vowel}") 

# -->4. Find the Frequency of Characters in a String

# str4='boolen'
# i=0
# while i < len(str4):
#     currunt_char=str4[i]
#     count=0
    
#     for j in str4:
#         if j==currunt_char :
#             count+=1
#     print(f' count of { currunt_char} = {count}')
#     i+=1        
    
          
# text = "hello world"
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# print(frequency)

        
# 5. Check if Two Strings are Anagrams


# --> 6. Remove Duplicate Characters from a String


str5='sangamesh'
print(set(str5))
# new=''
# for i  in str5:
#     if i not in new:
#         new+=i
# print(f"the new string without duplicates is = ",new)    
    

# -->7. Check if a String Contains Only Digits


# str6='123ssssss'
# for i in str6:
#     if i in "1234567890":
#         print("Detected degit ")
#     else:
#         print("Detected charecters .")

# str6='1457632'
# only_digit=True

# for i in str6:
#     if i not in '1234567890':
#         only_digit=False
        
# if  only_digit:
#     print("contains only digit ")
# else:
#     print('contains cherecters also .')


#--> 8. Convert the First Letter of Each Word to Uppercase



# str7= 'i am the best programmer'

# print(str7.title())



# ---> 1.Reverse a List Without Using Built-in Functions


# list=[1,2,3,4,5,6,7,8,9]
# reverse=list[::-1]
# print(reverse)


# 2. Find the Largest and Smallest Elements in a List


# list=[1,2,3,4,5,6,7,8,9]

# print(min(list))
# print(max(list))





# 3. Remove Duplicates from a List


# list=[1,1,2,3,4,5,2,3,4,5,6,7,8,9]
# # print(set(list))
# list2=[]
# for i  in  list:
#     if i not in list2:
#         list2.append(i)
# print(list2)



# 4. Check if a List is Empty


# list=[]
# iterations =0
# for i in list :
#     iterations+=1

# if iterations<=0:
#     print('list is empty ')
# else:
#     print('list have elements .')
    




# 5. Find the Second Largest Element in a Listmax

list=[1,1,2,3,4,5,2,3,4,5,6,7,8,9]

cnt_max=list[0]
cnt_snd_max=list[1]
# print(f"current max is = {cnt_max}")

for i in list :
    if i <= cnt_max and i >= cnt_snd_max :
        cnt_snd_max=list[i]
        


# 6. Count the Frequency of Each Element in a List
# 7. Flatten a Nested List
# 8. Merge Two Lists and Remove Duplicates
# 9. Find the Intersection of Two Lists
# 10. Rotate a List by `n` Positions
# 11. Check if Two Lists are Identical
# 12. Split a List into Even and Odd Numbers
# 13. Find the Cumulative Sum of a List
# 14. Sort a List Without Using the `sort()` Method
# 15. **Find All Pairs in a List