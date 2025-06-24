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
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['NY', 'LA', 'Chicago']
# }
# df = pd.DataFrame(data)
# print(df)


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


# data=pd.DataFrame([1,2,3],[5,6,7])

# print() 




#---------csv file operations



# file=pd.read_csv('indeks-standar-pencemar-udara-di-spku-dataset.csv')
# # print(file)
# file.rename(columns={'co':'co2'},inplace=True)


# print(file.tail())    #-----first 5
# print(file.head(51))   #----last five
# print(file.columns) 
# print(file.info())
# print(file.iloc[1:10])
# print(file.shape)       #-----size
# print(file.mean)
# print(min('co'))
# print(max('co'))
# print(file.describe)# print(file['co'].count())

#-----delete the column

# print(file.drop(columns=['co2'],inplace=True))
# print(file.columns)

#--------- to check empty cell


# print(file.isnull())
# print(file.isnull().sum())
# print(file['co'].isnull().sum())






# Sample DataFrame to test
file = pd.DataFrame({
    'co': ['India', 'USA', 'India', 'UK', None],
    'co2': [10, 20, 30, 40, 50],
    'val1': [100, 200, 300, None, 500],
    'val2': [1, 2, 3, 4, 5]
})

# 1. Data types of columns
print("Data Types:\n", file.dtypes)

# 2. Count unique values per column
print("\nUnique Values per Column:\n", file.nunique())

# 3. Unique values in 'co'
print("\nUnique values in 'co':\n", file['co'].unique())

# 4. Frequency counts of 'co'
print("\nValue Counts of 'co':\n", file['co'].value_counts())

# 5. Sorted by 'co2'
print("\nSorted by 'co2':\n", file.sort_values(by='co2'))

# 6. Rename column 'co2' to 'carbon'
file.rename(columns={'co2': 'carbon'}, inplace=True)
print("\nRenamed Columns:\n", file.columns)

# 7. Set index to 'co'
file.set_index('co', inplace=True)
print("\nSet 'co' as index:\n", file)

# 8. Reset index
file.reset_index(inplace=True)
print("\nReset Index:\n", file)

# 9. Check for duplicates
print("\nDuplicated Rows:\n", file.duplicated())

# 10. Drop duplicate rows
file.drop_duplicates(inplace=True)

# 11. Fill missing values with 0
file.fillna(0, inplace=True)

# 12. Drop rows with missing values (no effect now, since we filled NaNs)
file.dropna(inplace=True)


# 14. Random sample of 3 rows
print("\nRandom Sample:\n", file.sample(n=3))

# 15. Query where co == 'India'
print("\nQuery for India:\n", file.query('co == "India"'))

# 16. Convert 'co' to uppercase
file['co'] = file['co'].str.upper()
print("\nUppercase 'co':\n", file['co'])

# 17. New column: val1 + val2
file['total'] = file['val1'] + file['val2']
print("\nNew 'total' column:\n", file[['val1', 'val2', 'total']])

# 18. Group by 'co' and take mean
print("\nGroup by 'co':\n", file.groupby('co').mean(numeric_only=True))

# 19. Export to CSV
file.to_csv('output.csv', index=False)  # Will save to current directory

# 20. Concatenate two DataFrames
df2 = pd.DataFrame({'co': ['CANADA'], 'carbon': [60], 'val1': [600], 'val2': [6], 'total': [606]})
combined = pd.concat([file, df2], ignore_index=True)
print("\nConcatenated DataFrame:\n", combined)
