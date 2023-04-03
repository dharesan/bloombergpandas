# Import necessary libraries 
import pandas as pd 

# Requirements: 
# NEED TO SAVE RBICS FROM SGX IN .csv format, instead of .xlsx, because of Factset formulae 

# Read to Path Directory of Folder 
rbic = pd.read_csv('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/rbic_27Feb2023_fromSGX.csv')

# Read only the "Tradeable Names" sheet from "Sheet1_xlsx" excel workbook 
trader = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Start Sheet_xlsx.xlsx', sheet_name = 'Tradeable Names')

# Remove  SEDOL column containing Factset formulae because original Rbics Document have two SEDOL columns 
column_name = "SEDOL"
rbic = rbic.drop(rbic.columns[rbic.columns.get_loc(column_name)], axis=1)
# Rename SEDOL.1 column to SEDOL for simpliCcity in subsequent usage
rbic = rbic.rename(columns={'SEDOL.1': 'SEDOL'})

# Create Year Column 
rbic['Year'] = pd.to_datetime(rbic['Date']).dt.year 

# Ouput Current RBICs to be used later after Attribution Filter by 30 
rbic.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Rbics with Year(Code7).xlsx', index = False)

# Add Tradeable Region + EM/DM into rbic 
rbic['Primary Exchange Name Copy from BB'] = trader['PRIMARY_EXCHANGE_NAME_COPY']
rbic["Exchange Region"] = trader["Exchange Region"]
rbic["EM/DM"] = trader["EM/DM"]

# Select only the rows where the 'Exchange Region' column is blank
nonTradeableExchanges = rbic[rbic['Exchange Region'].isnull()]

# Output list of non-tradeable exchanges
nonTradeableExchanges.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output1_NonTradeable_Exchanges.xlsx', index=False)

# Remove Rows which are non-tradeable (ie. blanks in "Valid Exchange")
rbic = rbic.dropna(subset=['Exchange Region'])

# Output to a new file 
rbic.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Ouput1_Tradeable_Exchanges.xlsx', index = False)
