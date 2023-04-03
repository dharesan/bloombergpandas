import pandas as pd
 
atrChecker = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output2.xlsx')

# Attempt 3: Slicing 
# Fill every row with Sedol:Year:Attribution
# If dont have year, then leave it 

# use the explode function to ungroup the data in "SEDOL"
atrChecker = atrChecker.explode('SEDOL')

# Fill every row in "SEDOL" column with unique SEDOL 
atrChecker['SEDOL'] = atrChecker['SEDOL'].fillna(method='ffill')

# Output to a new file 
atrChecker.to_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output3.xlsx', index = False)
