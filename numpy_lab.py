import numpy as np
# arr1=np.array([1,2,3,4,5])
# print(type(arr1))


# name1=['sangamesh','akash','yash','ajay']
# print(type(name1))
# arr2=np.array(name1)
# print(type(arr2))
# print(arr2)  



#-----multi dimentional array

# arr=np.array([[1,2,3,7],[1,2,3,6],[4,5,6,8],[4,6,7,8]])
# print(type(arr))
# print(arr)


# arr=np.arange(1,100,3)      #--------arange
# print(arr)



# arr=np.zeros((3,4))   #----------zeros array
# print(arr)


# arr=np.zeros((3,4),dtype=int)
# print(arr)


# arr=np.ones((3,4),dtype=int)             #----------ones array
# print(arr)


# arr=np.eye(4)
# arr=np.eye(4,dtype=int)            #--------identity array  
# print(arr)


# arrr= np.random.rand(3,3)
# print(arrr)

# arrr= np.random.randint(10,15,(2,5))     #--------with in range random array
# print(arrr)



# arr=np.linspace(0,1,5)             #----------divide the aray in specific part 
# print(arr)


 # what is the diff modul and pakages
 #what is list comprensin
 #why list comprension is nessesory why we use it 
 #what are the benefits of list comprension 
 #what is numpy 
 
 
 
 #------------ ARITHMATIC O[ERATIONS IN ARRAY : addition of the array
 
 
# a1= np.array([1,2,4])
# a2= np.array([1,2,4])
# print(a1+a2)

# a1= np.array([1,1,3])
# a2= np.array([1,2,4])
# print(a1-a2)


#------------logical



# b1=np.array([True,False,True])
# b2=np.array([False,True,True])
# print(b1&b2)


# b1=np.array([True,False,True])
# b2=np.array([False,True,True])
# print(b1|b2)



#---------comparison



# a1= np.array([1,1,3])
# a2= np.array([1,2,4])

# print(a1 <a2 )
# print(a1 >a2 )
# print(a1 <=a2 )
# print(a1 >=a2 )
# print(a1 ==a2 )




#-------buildin functions




# main=np.array([1,2,3,4,5])
# print(main.sum())
# print(main.max())
# print(main.min())
# print(main.mean())
# print(np.median(main))




#--------indexing and slicing


# main=np.array([1,2,3,4,5])

# print(main[4])
# print(main[-1])
# print(main[1:3])
# print(main[::-1])
# print(main[::2])






#-----------2d array 



# arr=np.array([[1,2,3],[5,4,7]])
# print(arr[1,2])
# print(arr[0:2])
# print(arr)
# print(arr[0:2,2:3])   #---[col][row]
# print(arr[0:2,2])   #--row


# arr=np.array([[76,85,38],[175,180,170],[256,121,635]])
# print(arr[1:3,1:3])
# print(arr[2:,1:2])
#or
# print(arr[2,1])


import pandas as pd 
data=[1,2,3,4,5]
series=pd.Series