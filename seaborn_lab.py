# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Create DataFrame
# data = pd.DataFrame({
#     'A': [ 12, 8, 4],
#     'B': [ 8, 2, 8],
#     'C': [ 4, 8, 1]
# })

# print(data)
# corr=data.corr()    #converting matrix into corrliation 
# print(corr)
# # Plot heatmap
# plt.figure(figsize=(6, 5))
# # sns.heatmap(corr,annot=True,  cmap='coolwarm',fmt='.2f', linewidths=0.5)
# sns.heatmap(data,annot=True,  cmap='coolwarm',fmt='.2f', linewidths=0.5)

# plt.title('Heatmap of Data')
# plt.show()