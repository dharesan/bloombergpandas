# import necessary libraries 
import pandas as pd

# read previous output as atrAgg dataframe
atrTotal = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output4.xlsx')

# Filter by "INVALID", i.e. remove those with no data for 2020, 2021, 2022
invalid_rows = atrTotal[atrTotal['Attribution'] == 'INVALID']

# Create list of invalid sedols 
invalid_sedols = list(atrTotal.loc[atrTotal['Attribution'] == 'INVALID', 'SEDOL'].unique())

# Remove rows which contain invalid sedols 
atrTotal = atrTotal[~atrTotal['SEDOL'].isin(invalid_sedols)]

# Output to a new file containing invalid sedol codes
invalid_rows.to_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output5_RemovedList.xlsx', index = False)

# Output to a new file containing valid sedol codes to check for Attribution > 30 in the next step 
atrTotal.to_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output5_KeepList.xlsx', index = False)

            