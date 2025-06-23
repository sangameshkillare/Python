import pandas as pd 
import numpy as np
# data=[1,2,3,4,5]
# series=pd.Series 

# -----------------Create Series:

# From list
# s = pd.Series([10, 20, 30])
# print(s)

# # With custom index
# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s)

# # From dictionary
# d = pd.Series({'a': 1, 'b': 2, 'c': 3})
# print(d)




#----------DataFrame (2D)



# # From dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)


#------accessing the dataframes


# print(df['Name'])             # single column
# print(df[['Name', 'Age']])             # single column
# print(df[['Name', 'Age']])    # multiple columns
# print( df.iloc[0])             # first row (by index)
# print(df.loc[0])              # row with label 0
# print(df.iloc[0, 1])          # specific cell



# data={
#     'name':['alice','bob','charlies'],
#     'age':[10,20,30],
#     'address':['pune','mumbai','delhi']
# }

# df=pd.DataFrame(data)
# print(df)
# print(data)



#----------array

# data=np.array([[1,2,3],[4,5,6]])
# print(data)

# print()
# df=pd.DataFrame(data,columns=['A','B','C'])
# print(df)

# name=pd.Series(['A','B','C'])
# data=pd.Series(name,index=[0,2,1])
# # print(name['A'])
# # print(data[2])
# print(data)
# print(data[1])
# # for i in name:
# #     print(name[i] )
    

# data=pd.Series([10,20,30,40,50], index=['a','b','c','d','e']) 
# print(data[1:5])   
# print(data[::-1])

# print(data['b':'e'])


data=pd.DataFrame([1,2,3],[5,6,7])

print() 