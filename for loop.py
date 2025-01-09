## brek ,continu and pass statement 

# for i in [1,2,4,2.3,"sangamesh"]:
#     if i==2.3:
#         break
#     print(i)
# print("exited")


# for i in range(1,11):
#     if i%2==0:
#         continue
#     print (i)
# print("Exited")


# for i in range(20,1,-1):
#     if i%2!=0:
#         pass
#     else:
#         print(i)
        
# print("Exited")


##@@ PATTERN PROGRAMING WHILE LOOP AND FOR LOOP 

# *****
# *****
# *****

# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

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


# *
# **
# ***
# ****


# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1


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



# ***
# **
# *


# n=int(input("Enter a number:"))
# i=n
# while i>=0:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i-=1



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


n=int(input("enter the number :"))
i=1
while i<=n:
    space=1
    while space<=n-i :
        print(' ',end="")
        space=space+1
    star=1
    while star <=i:
        if star==1:
            print("1",end="")
        else :
            print(star,end="")
        star+=1
    print()
    i+=1
    