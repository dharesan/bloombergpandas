# import necessary libraries 
import pandas as pd

# read previous output 
atrKeep = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output5_KeepList.xlsx')

# Filter by 2022 in the "Year" column 
atrTotal_2022 = atrKeep[atrKeep['Year'] == 2022]

# check for Attribution value greater than 30
atrBy30_keep = atrTotal_2022[atrTotal_2022['Attribution'] >= 30]
atrBy30_remove = atrTotal_2022[atrTotal_2022['Attribution'] < 30]

# Output List of Removed Rows 
with pd.ExcelWriter('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output6_atrBy30_RemovedList.xlsx') as writer:
    atrBy30_remove.to_excel(writer, index=False)

# Output List of Kept Rows 
with pd.ExcelWriter('C:/Users/dharesan.gk/Desktop/Excel Files/Demo_Output6_atrBy30_KeepList.xlsx') as writer:
    atrBy30_keep.to_excel(writer, index=False)
