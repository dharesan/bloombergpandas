import pandas as pd 

# Notes: 
# Write code to directly copy Unique Sedol to fill up bloomberg columns of Sheet 1? 

# Requirements: 
# NEED TO SAVE RBICS FROM SGX IN .csv format, instead of .xlsx, because of Factset formulae 

# rbic = pd.read_csv('C:/Users/Zoe/Desktop/FOLDER OF EXCEL FILE/NAME OF EXCEL FILE.csv')
rbic = pd.read_csv('C:/Users/dharesan.gk/Desktop/Excel Files/rbic_27Feb2023_fromSGX.csv')

# Read only the "Tradeable Names" sheet from "Sheet1_xlsx" excel workbook 
trader = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Sheet 1_xlsx.xlsx', sheet_name = 'Tradeable Names')
tradeableList = pd.read_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Sheet 1_xlsx.xlsx', sheet_name = 'Tradeable Exchange')

# Remove SEDOL column containing Factset formulae 
column_name = "SEDOL"
rbic = rbic.drop(rbic.columns[rbic.columns.get_loc(column_name)], axis=1)

# Rename SEDOL.1 column to SEDOL for simpliCcity in subsequent usage
rbic = rbic.rename(columns={'SEDOL.1': 'SEDOL'})

# Create Year Column 
rbic['Year'] = pd.to_datetime(rbic['Date']).dt.year 

# Include Tradeable Exchange + EM/DM 
for i, row in trader.iterrows(): 
    if trader['PRIMARY_EXCHANGE_NAME_COPY'].isin(tradeableList[['Code','Exchange']].values.flatten()).any():
        temp_df = tradeableList.loc[trader['PRIMARY_EXCHANGE_NAME_COPY'] == row['PRIMARY_EXCHANGE_NAME_COPY'], 'Exchange']
        if not temp_df.empty:
            rbic.loc[i, 'Valid Exchange'] = temp_df.iloc[0]
        
        temp_df = tradeableList.loc[trader['PRIMARY_EXCHANGE_NAME_COPY'] == row['PRIMARY_EXCHANGE_NAME_COPY'], 'DM/EM']
        if not temp_df.empty:
            rbic.loc[i, 'Market Type'] = temp_df.iloc[0]


# Remove Rows which are non-tradeable (ie. blanks in "Valid Exchange")
rbic = rbic.dropna(subset=['Valid Exchange'])

# Output to a new file 
rbic.to_excel('C:/Users/dharesan.gk/Desktop/Excel Files/Test_After_Removing_Empty_Rows.xlsx', index = False)