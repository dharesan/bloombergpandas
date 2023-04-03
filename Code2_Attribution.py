# Import necessary libraries 
import pandas as pd 

# Read spreadsheets 
tableA = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/tester_Ouput1_Tradeable_Exchanges.xlsx') 

# Attain Sum of Attribution respective to Sedol, in each year 
# Essentially, summing up all sector descriptions in each year unique to each Sedol 
attributionSum = tableA.groupby(['SEDOL','Year'])['Attribution'].sum()

# create Excel writer object
with pd.ExcelWriter('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output2.xlsx') as writer:
    # write result to Excel worksheet
    attributionSum.to_excel(writer, sheet_name = 'PivotRevAgg') # Should call sheet as PivotRevAgg for similarity 