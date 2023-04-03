# import necessary libraries 
import pandas as pd
import datetime

calendarYear = datetime.date.today().year

# read previous output as atrAgg dataframe
atrAgg = pd.read_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output3_Attribution_Filled.xlsx')

# iterate through each unique SEDOL value in SEDOL column 
for sedol in atrAgg['SEDOL'].unique():
    # get the group for the current SEDOL
    group = atrAgg.loc[atrAgg['SEDOL'] == sedol]
    # check if one year before current year exists, if calendarYear = 2023, check 2022 
    if (calendarYear-1) in group['Year'].values:
        continue  # move to the next SEDOL

    # previous year no data, check if previous previous year exists, i.e. if calendarYear = 2023, check for 2021  
    elif (calendarYear-2) in group['Year'].values:
        # get the Attribution value for previous previous year
        attribution_prev = group.loc[group['Year'] == (calendarYear-2), 'Attribution'].iloc[0]
        # create a new row for previous year
        new_row = pd.DataFrame({'SEDOL': [sedol], 'Year': [(calendarYear-1)], 'Attribution': [attribution_prev]})
        # append the new row to the original dataframe
        atrAgg = pd.concat([atrAgg, new_row], ignore_index=True)

    else:
        # no data for previous year and the year before, ie. one year before and two years before today
        # create a new row for previous year with "INVALID" in the Attribution column
        new_row = pd.DataFrame({'SEDOL': [sedol], 'Year': [(calendarYear-1)], 'Attribution': ['INVALID']})
        # append the new row to the original dataframe
        # every SEDOL has a value filled in the calendarYear-1, either a value or 'INVALID'
        atrAgg = pd.concat([atrAgg, new_row], ignore_index=True)


# sort the dataframe by SEDOL and Year
atrAgg = atrAgg.sort_values(['SEDOL', 'Year'])

# Output to a new file (VALID & INVALID)
atrAgg.to_excel('Z:/Shared/Projects/Active/Index/New Index Methodology/Intern/Dha Excel & Codes/Excel Files/Output4_Two Years Consecutive_Activity.xlsx', index = False)