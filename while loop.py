#we use while loop when we dont want no of iteration.

#WAP to print 1-10


# i=1
# while i<=10:
#     print(i)
#     i+=1


#WAP to print even no 1-10

# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1


#WAP to print odd no 1-10


# i=1
# while i<=10:
#     if i%2!=0:
#         print(i)
#     i+=1



#WAP to print 50-1 


# i=50
# while i>=0:
#     print(i)
#     i-=1

#wap to print 50-1 even no.

# i=50
# while i>=1:
#     if i%2==0:
#         print(i)
#     i-=1



#wap to print 50-1 odd no.

# i=50
# while i>=1:
#     if i%2!=0:
#         print(i)
#     i-=1


#WAP to print sum of first  50 num 

# i=50
# sum=0
# while i>=1:
#     sum=sum+i
#     i-=1
# print(sum)

#wap to print cumalative sum

# i=5
# sum=0
# while i>=1:
#     sum=sum+i
#     i-=1
#     print(sum)



#wap to print sum of 1-15 even no




# i=15
# sum=0
# while i>=1:
#     if i%2==0:
#       sum=sum+i
#     i-=1
# print(sum)



#wap to print sum of odd num 1-15



# i=5
# sum=0
# while i>=1:
#     if i%2!=0:
#       sum=sum+i
#     i-=1
# print(sum)



#WAP to print table 


# num=int(input("enter the number to print table :"))
# i=1
# a=0
# while i<=10:
#     print(f"{num}*{i}={a}")
    
    
    
    
    
    
#Reverse a Number Using a While Loop


# n=int(input("enter the nuber :"))

# reverse=int(str(n)[::-1])
# print(reverse)





#Print a Countdown From 10 to 1



# i=10

# while i>=0:
#     print(i)
#     i-=1





#Generate the Fibonacci Sequence Until a Specified Number



# n=int(input("enter the number :"))
# num=0
# num2=1

# i=1
# # while i<=n:
# #     print(num)
# #     num,num2=num2,num+num2
# #     i+=1
# print(num,num2,end=" ")
    
# while i<n:
#     result=num+num2
#     print(result,end=" ")
#     num=num2
#     num2=result
#     i+=1






# Keep Taking Input From the User Until They Enter 'exit'

# n=5
# i=0
# while i<=n:
#     str=input("enter the string :")
#     if str.lower()=="exit":
#         break
#     else:
#         n+=1
#         i+=1



# #Calculate the Power of a Number Without Using the  Operator



# base=int(input("enter the base :"))
# exponent=int(input("enter the exponent:"))
# result=1
# count=(abs(exponent))
# while count > 0:
#     result*=base
#     count-=1
#     if exponent<0:
#         result=1/result
       
# print(result)
    
    
    
    
    
#Keep Multiplying a Number by 2 Until It Becomes Greater Than 1000



# n=int(input("enter the number :"))
# result=n*2
# while result <=1000:
#     print(result)
#     result=result*2




#gcd



# num1=int(input("enter the num 1 :"))

# num2=int(input("enter the num 2 :"))

# div1=[]
# div2=[]

# for i in range(1,num1):
#     if num1%i==0:
#         div1.append(i)
# for i in range(1,num2):
#     if num2%i==0:
#         div2.append(i)
    
# print(div1)
# print(div2)

# common=list(set(div1) & set(div2))

# gcd=max(common)

# print(gcd)





# Simulate a Basic Password Check That Limits to 3 Attempts




# set_password=int(input("set the password :"))
# attempt=3

# while attempt >0:
#     password=int(input("Enter the password : "))
#     if password==set_password:
#         print("you entered right password , Access Granted : ")
#         break
#     else:
#         attempt-=1
#         print("You entered invalid password , please enter right password :")

# if attempt==0:
#     print("Device lock for 30 sec .")
# else:
#     print("Devise unlock.")      



