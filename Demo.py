import pandas as pd 

rbic = pd.read_csv('rbics_raw.csv')
classifier = pd.read_csv('tradeable names.csv') #sheet taken from SGX CAI Revenue Classification 

# Create Year column corresponding to Date column
rbic['year'] = pd.to_datetime(rbic['Date']).dt.year 

# Obtain Unique Sedol List 
fullSedolList = rbic['SEDOL2']
value_to_remove = "#N/A" 
uniqueSedolList = fullSedolList[fullSedolList != value_to_remove]
uniqueSedolList = uniqueSedolList.drop_duplicates()

print(uniqueSedolList)

# Paste Unique Sedol List 
rbic["Unique SEDOL"] = uniqueSedolList.reset_index(drop = True)

""" Pseudocode to get Table A 
for each Primary_Exchange_Name:  
    check if it exists in Code (column B) or Exchange (column C)
        if it exists: return Exchange (column C) and EM/DM (column D)
        
        else: return INVALID (dont count it in because #N/A)
"""
# Fill boolean values in new column 
rbic["Validity"] = classifier['PRIMARY_EXCHANGE_NAME_COPY'].isin(classifier[['Code','Exchange']].values.flatten())

#Output to a new file 
rbic.to_excel('materialForTableA.xlsx', index = False)