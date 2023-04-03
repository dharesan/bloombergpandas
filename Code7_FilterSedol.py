# import relevant libraries
import pandas as pd

# Read Outpyt6_atrBy30_KeepList & Rbics with Year(Code7)
relevantSedol = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output6_atrBy30_KeepList.xlsx')
editedRbics = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Rbics with Year(Code7).xlsx')

# Give me a list of all the SEDOL which I still want after Attribution Filter by 30 
uniqueSedolList = relevantSedol['SEDOL']

# Filter relevant rows from rbics given from SGX according to the SEDOL which we had at first 
filteredRbics = editedRbics[editedRbics['SEDOL'].isin(uniqueSedolList)]

# Output Rbics after filtering out all irrelevant rows 
filteredRbics.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output7_Rbics_Final.xlsx', index = False)
