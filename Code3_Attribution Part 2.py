import pandas as pd

# Read Excel Workbooks
atrChecker = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output2_Attribution_Sum.xlsx')

# Ungroup the data in "SEDOL"
atrChecker = atrChecker.explode('SEDOL')

# Fill every row in "SEDOL" column with unique SEDOL 
atrChecker['SEDOL'] = atrChecker['SEDOL'].fillna(method='ffill')

# Output to a new file 
atrChecker.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output3_Attribution_Filled.xlsx', index = False)
