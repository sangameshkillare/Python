#Write a program to take an input from the user and print its data type.

# a=int(input("enter somthing else:"))
# print(type(a))


#Accept two numbers from the user and perform addition, subtraction, multiplication, and division.

# n1=int(input("enter first number:"))
# n2=int(input("enter second number:"))

# print(n1+n2)
# print(n1/n2)
# print(n1-n2)
# print(n1*n2)

#4. Write a program that checks if a number entered by the user is even or odd.

# num=int(input("Enter the number :"))
# if num%2==0 :
#     print("even")
# else:
#     print("odd")


#5. Accept a character from the user and determine whether it is a vowel or a consonant.

# charecter=input("enter any charecter:")
# if charecter in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("consonent")


# 6. Grade Calculator: Input a percentage and output a grade according to the following:
#    - 90-100: A
#    - 80-89: B
#    - 70-79: C
#    - 60-69: D
#    - Below 60: F



# percent=int(input("enter the percentage :"))
# if percent<60:
#     print("Fail")
# elif percent<69:
#     print("D")
# elif percent<79:
#     print("C")
# elif percent<89:
#     print("B")
# elif percent<=100:
#     print("A")
# else:
#     print("error")



# 7. Write a program to calculate the sum of all elements in a list.


# list=[1,2,3,4,5]
# i=1
# bg=0
# while i in list:
#     bg+=i
#     i+=1
# print(bg)


#8. Find the largest number in a list without using built-in functions.


# list=[1,2,3,4,5]
# i=list[0]
# cm=0
# while i in list :
#     if i>= cm :
#         cm=i
#     i+=1
# print(f"largest is {cm}")
    
    
    
#9. Reverse a given list without using built-in methods.


list=[1,2,3,4,5]
re_list=[]

# length=len(list)-1
# print(length)
# i=length


# for i in list[::-1]:
#     re_list.append(i)
# print(re_list)

##________or________

# while i>=0:
#     re_list.append(list[i])
#     i-=1
# print(re_list)
    



# 10. Write a program to remove duplicates from a list.


# num=["sangamesh",1,2,3,2,1,3,"sangamesh"]
# print(num)
# num1=set(num)
# print(num1)

# 11. Write a program to check if a given key exists in a dictionary.


# dict={"name":"Sangamesh","marks":99}

# if "name" in dict:
#     print("exist")
# else:
#     print("Nothing")




# 12. Combine two dictionaries into one.


# dict={"name":"Sangamesh","marks":99}
# dict2={"education":"B.voc","status":"studing"}

# dict3=dict | dict2
# print(dict3)



# 13. Count the frequency of each character in a given string and store it in a dictionary.



# string="sangamesh"

# frequency={}

# for char in string:
#     if char in frequency :
#        frequency[char]+=1
#     else:
#         frequency[char]=1 
    
# print(frequency)
    


# 14. Create a dictionary where keys are student names, and values are their marks. Write a program to find the student with the highest marks.



# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 88,
#     "David": 95,
#     "Eva": 89
# }

# highest_marks=0
# topper=''
# for student,marks in students.items():
#     if marks>highest_marks:
#         highest_marks=marks
#         topper=student
# print(f"{topper}:{highest_marks}") 




# 15. Write a program to calculate the factorial of a given number using a for loop.



# num=int(input("enter the number for factorial :"))

# print(num)
# i=1
# fact=1
# while i <= num:
#     fact*=i
#     i+=1
    
# print(fact)   



# 16. Print the multiplication table of a number entered by the user.


# num=int(input("enter the number:"))


# for i in range(0,11):
#     print(num*i)







# 23.Print the Digits of a Number in Reverse Orded.



# num=12345

# num2=int(str(num)[::-1])
# print(num2)



# 25.WAP To Keep Multiplying a Number by 2 Until It Becomes Greater Than 1000**




# num=int(input("enter number "))
# res=num*2
# while res<1000:
#     print(res)
#     res=res*2




