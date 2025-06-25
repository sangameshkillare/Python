#------it is versatile-support variety of plots , lines,bar scatter
#------coustomization 
#integration -work with pandas, numpy,scipy
#-------interactive enviromnet - compatible with jupyter.vs,kaggle

#----use to perform visualas during EDA ( exploratory data analysis )


import matplotlib.pyplot as plt




# x=[1,2,3,4,5]
# y=[2,4,5,8,5]

# plt.plot(x,y)
# plt.title('line plot')
# plt.grid(True,linestyle='--',alpha=0.8)
# plt.xlabel('work time')
# plt.ylabel('earning in k')
# plt.legend()
# # plt.figure(figsize=(6,4))
# # plt.style.use('ggplot')
# plt.show() 


# x=[1,2,3,4,5]
# y=[2,4,5,8,5]
# plt.plot(x,y,color='green',linestyle=':',marker='*',label='styled line')
# plt.title('line plot')
# plt.grid(True,linestyle='--',alpha=0.8)
# plt.xlabel('work time')
# plt.ylabel('earning in k')
# plt.legend()
# plt.show() 


#-----bar chart
# one catagorica and numeric attribute is must




# x=['a1','a2','a3','a4','a5']
# y=[2,4,5,8,5]

# plt.bar(x,y,color='red')
# plt.title('Bar chart')
# plt.grid(True,linestyle='--',alpha=0.8)
# plt.xlabel('work time')
# plt.ylabel('earning in k')
# plt.legend()
# plt.show() 



#-----scatter

# x=[1,2,5,8,6]
# y=[2,4,5,8,5]

# plt.scatter(x,y,color='red')
# plt.title('scatter chart')
# plt.grid(True,linestyle='--',alpha=0.8)
# plt.xlabel('work time')
# plt.ylabel('earning in k')
# plt.legend()
# plt.show() 




#-----histogram



# import numpy as np

# data=np.random.normal(0,10,100)
# print(data)

# plt.hist(data,bins=5,color='red',alpha=0.8)
# plt.xlabel('work time')
# plt.title('scatter chart')
# plt.ylabel('earning in k')
# plt.legend()

# plt.show() 




#---------


# student={
#     name=['sk','bk','dk','rk','tk'],
    
    
    
# }




# print(plt.style.available)