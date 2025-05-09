
# ##@@ ___________________________________________________PATTERN PROGRAMING__________________________________________________ 

# _____________________________________
# *
# *
# *


# for i in range(5):
#     print("*")


# ____________________________________
# *******

# for i in range(5):
#     print("*",end=" ")


# _____________________________________
# *****
# *****
# *****


#  _____________________# with two while loops 


# n=int(input("Enter a number:"))
# i=1
# while i <=n:
#     j=n
#     while j>=0:
#         print('*',end="")
#         j-=1
#     print()
#     i+=1
    

#_________________________

# while i<=n:
#     print("*"*n)
#     i+=1

#-____________________________

# for i in range(n):
#     print("*"*n)
    



# # __________________________________
# 1111
# 2222
# 3333


# n=int(input("Enter a number:"))
# for i in range(n):
#     print((str(i))*n)



# _______________________________
# 111
# 222
# 333


# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1

# ___________________________________
# 1234
# 1234
# 1234
    
    
# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1


# for i in range(n):
#     for j in range(n):
#         print(j,end="")
#     print()




# ___________________________________
# 4321
# 4321
# 4321


# n=int(input("Enter a number:"))
# i=1
# while i<n:
#     j=n
#     while j>0:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1

# ___________________________________
# *
# **
# ***
# ****







# n=5
# i=1

# while i<=n:
#     j=i
#     while j>0:
#         print(j,end="")
#         j-=1
#     i+=1
#     print()












# n=int(input("Enter a number:"))
# # # i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1


# for i in range(n+1):
#     for j in range(1,i):
#         print("*",end="")
#     print()



# ______________________________________
# 1
# 23
# 456
# 78910

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     p = i
#     while j <= i:
#         print(p, end = '')
#         j = j+1
#         p = p+1
#     print()
#     i = i + 1



# for i in range(n+1):
#     for j in range(1,i):
#         print("*",end="")
#     print()




# _________________________________________
# ABCD
# ABCD
# ABCD


# n=int(input("enetr the number :"))

# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(chr(ord('A')+j-1),end="")
#         j+=1
#     print()
#     i+=1


# ___________________________________________
# ***
# **
# *


n=int(input("Enter a number:"))
i=n
# while i>=0:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i-=1


for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()



# __________________________________
# 1
# 11
# 202
# 3003





# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if i==1 and j==i:
#             print(1,end='')
#         elif j==1:
#             print(j+i-2,end='')
#         elif j==i:
#             print(j-1,end='')
#         else:
#             print(0,end='')
#         j=j+1
#     print()
#     i=i+1



# 1
# 11
# 121
# 1221



# n=int(input("enter the number :"))

# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if i==1 and j==1:
#             print("1",end='')
#         elif j==1:
#             print("1",end='')
#         elif j==i:
#             print("1",end='')
#         else:
#             print("2",end='')
#         j+=1
#     print()
#     i=i+1



# ---*
# --**
# -***
# ****


# n=int(input("enter the number :"))
# i=1
# while i<=n:
#     space=1
#     while space<=n-i :
#         print(' ',end="")
#         space=space+1
#     star=1
#     while star <=i:
#         print("*",end="")
#         star+=1
#     print()
#     i+=1
    
    
    
    
# ***
# **
# *


# n=int(input("NUmber="))
# i=1
# while i<=n:
#     j=n
#     while j>=i:
#         print("*",end="")
#         j-=1
#     print()
#     i+=1
    
    
    
    
# ----1
# ---12
# --123
# -1234
# 12345


# n=int(input("enter the number :"))
# i=1
# while i<=n:
#     space=1
#     while space<=n-i :
#         print(' ',end="")
#         space=space+1
#     star=1
#     while star <=i:
#         if star==1:
#             print("1",end="")
#         else :
#             print(star,end="")
#         star+=1
#     print()
#     i+=1
    
    
    
