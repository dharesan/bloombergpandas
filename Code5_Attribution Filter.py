# import necessary libraries 
import pandas as pd

# read previous output as atrAgg dataframe
atrTotal = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output4_Two Years Consecutive_Activity.xlsx')

# Filter by "INVALID"
invalid_rows = atrTotal[atrTotal['Attribution'] == 'INVALID']

# Create list of invalid sedols 
invalid_sedols = list(atrTotal.loc[atrTotal['Attribution'] == 'INVALID', 'SEDOL'].unique())

# Remove rows which contain invalid sedols 
atrTotal = atrTotal[~atrTotal['SEDOL'].isin(invalid_sedols)]

# Output to a new file containing invalid sedol codes
invalid_rows.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output5_RemovedList.xlsx', index = False)

# Output to a new file containing valid sedol codes to check for Attribution > 30 in the next step 
atrTotal.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output5_KeepList.xlsx', index = False)

            