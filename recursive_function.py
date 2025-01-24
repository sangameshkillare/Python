# #--------------------factorial


def factorial(n):
    if n==0:
       return 1
    else:
       return n * factorial(n-1)


print(factorial(5))


#-----------------------finonach series


# def fibo(n):
#     if n<=1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

# for i in range(5):
#     print(fibo(i))