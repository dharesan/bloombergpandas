# import necessary libraries 
import pandas as pd
import datetime

# Store value of year in real time 
calendarYear = datetime.date.today().year

# read previous output 
atrKeep = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output5_KeepList.xlsx')

# Filter by previoys year in the "Year" column 
atrTotal_2022 = atrKeep[atrKeep['Year'] == (calendarYear-1)]

# check for Attribution value greater than 30
atrBy30_keep = atrTotal_2022[atrTotal_2022['Attribution'] >= 30]
atrBy30_remove = atrTotal_2022[atrTotal_2022['Attribution'] < 30]

# Output List of Removed Rows 
with pd.ExcelWriter('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output6_atrBy30_RemovedList.xlsx') as writer:
    atrBy30_remove.to_excel(writer, index=False)

# Output List of Kept Rows 
with pd.ExcelWriter('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output6_atrBy30_KeepList.xlsx') as writer:
    atrBy30_keep.to_excel(writer, index=False)
