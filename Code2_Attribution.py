# Import necessary libraries 
import pandas as pd 

# Read spreadsheets 
tableA = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Ouput1_Tradeable_Exchanges.xlsx') 

# Attain Sum of Attribution respective to Sedol, in each year 
# Essentially, summing up all sector descriptions in each year unique to each Sedol 
attributionSum = tableA.groupby(['SEDOL','Year'])['Attribution'].sum()

# create Excel writer object
with pd.ExcelWriter('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output2_Attribution_Sum.xlsx') as writer:
    # write result to Excel worksheet
    attributionSum.to_excel(writer, sheet_name = 'PivotRevAgg') 