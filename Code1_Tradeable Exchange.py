import pandas as pd 

# Notes: 
# Write code to directly copy Uique Sedol to fill up bloomberg columns of Sheet 1? 

# Requirements: 
# NEED TO SAVE RBICS FROM SGX IN .csv format, instead of .xlsx, because of Factset formulae 

# rbic = pd.read_csv('C:/Users/Zoe/Desktop/FOLDER OF EXCEL FILE/NAME OF EXCEL FILE.csv')
rbic = pd.read_csv('C:/Users/dharesan.gk/Desktop/Excel Files/rbic_27Feb2023_fromSGX.csv')

# Read only the "Tradeable Names" sheet from "Sheet1_xlsx" excel workbook 
trader = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Start Sheet_xlsx.xlsx', sheet_name = 'Tradeable Names')
#tradeableList = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Start Sheet_xlsx.xlsx', sheet_name = 'Tradeable Exchange')

# Remove  SEDOL column containing Factset formulae
column_name = "SEDOL"
rbic = rbic.drop(rbic.columns[rbic.columns.get_loc(column_name)], axis=1)

# Rename SEDOL.1 column to SEDOL for simpliCcity in subsequent usage
rbic = rbic.rename(columns={'SEDOL.1': 'SEDOL'})

# Create Year Column 
rbic['Year'] = pd.to_datetime(rbic['Date']).dt.year 

# Add Tradeable Region + EM/DM into rbic 
rbic['Primary Exchange Name Copy from BB'] = trader['PRIMARY_EXCHANGE_NAME_COPY']
rbic["Exchange Region"] = trader["Exchange Region"]
rbic["EM/DM"] = trader["EM/DM"]

#print(rbic.head())

# Creates an entire list of all rows as per rbics with #N/A, valid exchanges by using Vlookup - done w start sheet alr 

# Select only the rows where the 'Exchange Region' column is blank
nonTradeableExchanges = rbic[rbic['Exchange Region'].isnull()]
# Need to add the exchange column to show is invalid because of geographical location

# Output list of non-tradeable exchanges
nonTradeableExchanges.to_excel('C:/Users/dharesan.gk/Desktop/Excel Files/tester_Output1_NonTradeable_Exchanges.xlsx', index=False)

# Remove Rows which are non-tradeable (ie. blanks in "Valid Exchange")
rbic = rbic.dropna(subset=['Exchange Region'])

# Output to a new file 
rbic.to_excel('C:/Users/dharesan.gk/Desktop/Excel Files/tester_Ouput1_Tradeable_Exchanges.xlsx', index = False)


# Output a list of all those which I drop showing their exchange 

# Include Tradeable Exchange + EM/DM 
# for i, row in trader.iterrows(): 
#     if trader['PRIMARY_EXCHANGE_NAME_COPY'].isin(tradeableList[['Code','Exchange']].values.flatten()).any():
#         temp_df = tradeableList.loc[trader['PRIMARY_EXCHANGE_NAME_COPY'] == row['PRIMARY_EXCHANGE_NAME_COPY'], 'Exchange']
#         if not temp_df.empty:
#             rbic.loc[i, 'Valid Exchange'] = temp_df.iloc[0]
        
#         temp_df = tradeableList.loc[trader['PRIMARY_EXCHANGE_NAME_COPY'] == row['PRIMARY_EXCHANGE_NAME_COPY'], 'DM/EM']
#         if not temp_df.empty:
#             rbic.loc[i, 'Market Type'] = temp_df.iloc[0]

