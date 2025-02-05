import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

# Load data from Excel file
# Replace the file path with the correct path if needed
df1 = pd.read_excel(r'C:\Users\siddh\OneDrive\Documents\Python\DAX_Dataset.xlsx', sheet_name='Sheet1')  # Adjust 'Sheet1' with your actual sheet name
# df2 = pd.read_excel(r'C:\Users\siddh\OneDrive\Documents\Python\DAX_Dataset.xlsx', sheet_name='Sheet2')  # Adjust as needed for another sheet

# Example: Data Processing (joining, filtering, etc.)
# Merging data from multiple sources (Excel sheets)
df_merged = pd.merge(df1, on='common_column')  # Replace 'common_column' with the actual column name that you want to merge on

# Example of filtering data
df_filtered = df_merged[df_merged['column_name'] > 100]  # Replace with actual column and condition for filtering

# Generating insights and aggregation
df_summary = df_filtered.groupby(['category_column']).agg({'numeric_column': 'sum'}).reset_index()  # Replace with actual columns

# Saving the processed data to a new Excel file
with pd.ExcelWriter(r'C:\Users\siddh\OneDrive\Documents\Python\automated_report_output.xlsx', engine='openpyxl') as writer:
    df_filtered.to_excel(writer, sheet_name='Filtered Data')
    df_summary.to_excel(writer, sheet_name='Summary')

print("Excel report generated successfully!")

# Power BI Visualization
# Create a visualization using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df_summary['category_column'], df_summary['numeric_column'])  # Replace with your actual column names
plt.title('Category-wise Numeric Data')
plt.xlabel('Category')
plt.ylabel('Total Value')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image for Power BI
plt.savefig(r'C:\Users\siddh\OneDrive\Documents\Python\power_bi_visualization.png')
plt.close()

print("Power BI visualization saved as image.")
