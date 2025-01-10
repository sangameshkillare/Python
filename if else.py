# # W.a.p for grade system 


# marks=int(input("enter the markes to get grades : "))
# print(f"You entered : {marks}")
# if marks <= 35:
#     print("You are Failed ")
# elif marks <50:
#     print("D")
# elif marks < 70:
#     print("c")
# elif marks < 90:
#     print("B")
# else:
#     print("A")
    


# # w.a.p to chect no is positive or negative

# num=int(input("Enter any number you want : "))
# print(num)
# if num >= 0:
#     print(f"The number {num} is positive")
# else:
#     print(f"the number {num} is negative .")



##w.a.p to check no is odd or even

# num=int(input("Enter any number you want : "))
# print(num)

# if num %2==0 and num >=0:
#     print(f"Numer {num} is Even")
# else:
#     print(f"It is odd .")


## W.a.p to find grater of 3 number.

# num=int(input("Enter any number you want But positive: "))

# num1=int(input("Enter any number you want : "))

# num2=int(input("Enter any number you want : "))
# print(num,num1,num2)



# if num > num1 :
#     if num1 > num2 :
#         print(f"{num} is grater than others .")
# elif num1 > num2 :
#     if num2 > num :
#         print(f"{num1} is grater than others .")
# elif num2 > num1 :
#     if num1 > num :
#         print(f"{num2} is grater than others .")



## Write a program to check if a student has passed or failed based on a mark of 40.


# mrk=int(input("Enter the markes :"))

# print(mrk)

# if mrk >= 40 :
#     print("Pass")
# else:
#     print("Fail")


##. Write a program to check if a person is eligible to vote (age >= 18).  


# age=int(input("Enter the age of person :"))
# print(age)

# if age>18:
#     print(" the persone is eligible for vote .")
# else:
#     print("not eligible for vote .")



##Write a program to classify a number as positive, negative, or zero.  

# num=int(input("enter the number :"))

# print(num)

# if num >0:
#     print("Positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")



##Write a program to check if a number is divisible by both 3 and 5. 

# num=int(input("enter the number :"))
# print(num)
# if num / 3==0 and num /5==0 :
#     print(f"The number you have entered {num} is divisible by 3 and 5")
# elif num /5:
#     print(f"number is divisible by 5.")
# elif num / 3:
#     print(f"number is divisible by 3")
# else :
#     print("error")


##Write a program to check if three given sides can form a triangle.  



# s1=int(input("enter s1 ::"))
# s2=int(input("enter s2 ::"))
# s3=int(input("enter s3 ::"))

# if s1+s2 > s3 and s2+s3>s1  and s3+s1>s2 :
#     print(f"This sides can form a triangle .")
# else :
#     print("Error")


##/// Write a program to check if a character entered is an alphabet or not.  

# alfa=input("enter the alfabets :")
# print(alfa)

# if alfa.isalpha() :
#     print("it is alphabet.")
# else:
#     print("It is not alphabet")



## Write a program to check if an entered character is a vowel or consonant.  



# alfa=input("enter the alfa :")
# vowel="aeiou"
# if alfa in vowel:
#     print("It is vowel")
# else:
#     print("It is consonent ")
    
    
##Write a program to calculate a discount based on the purchase amount (e.g., 10% for purchases above $100).


# purchase=float(input("enter the amout to get discouted amount :"))

# discount_per=10/100

# if purchase >= 100:
#     print("You are eligible for 10% discount .")
#     discounted_amount=purchase*discount_per
#     print(f"Discount on purchase value = {discounted_amount}")
    
#     print(purchase-discounted_amount)
# else :
#     print(f"total payable amout ={purchase}")




##Write a program to perform addition, subtraction, multiplication, or division based on the user’s choice.


# num1=int(input("Enter 1st number :"))

# num2=int(input("Enter 2st number :"))

# print(num1 , num2 )

# print("1) add ,2) sub, 3) div,4)mult")
# choise=int(input("enter the coise :"))

# if choise ==1:
#     print(num1+num2)
# elif choise==2:
#     print(num1-num2)
# elif choise==3:
#     print(num1/num2)
# elif choise== 4:
#     print(num1*num2)
