# #--------------------factorial



# def fact(n):
#    if n==0:
#       return 1
#    else:
#       return n*fact(n-1)
# print(fact(5))



#-----------------------finonach series


# def fibo(n):
#     if n<=1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

# for i in range(5):
#     print(fibo(i))




#--------------------Sum of N numbers 



# def sum(n):
#    if n<=1:
#       return False
#    else:
#       return n+sum(n-1)
   
# num=int(input("enter the number :"))
# print(f"The sum of N number you enetered is {sum(num)}")






#-------------------GCD by using recusion




# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# print(gcd(48,18))  




#---------------reverse a string using recursion



# def string(r):
#     if len(r)==0:
#         return r
#     else:
#         return r[-1]+string(r[:-1]) 
    
    
# print(string("sangamesh"))



#____________________________power of n numbers



def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 4))  