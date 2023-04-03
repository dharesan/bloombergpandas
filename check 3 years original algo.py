# iterate over each unique SEDOL value
for sedol in atrAgg['SEDOL'].unique():
    # get the group for the current SEDOL
    group = atrAgg.loc[atrAgg['SEDOL'] == sedol]
    # check if 2022 exists
    if 2022 in group['Year'].values:
        continue  # move to the next SEDOL
    # check if 2021 exists
    if 2021 in group['Year'].values:
        # get the Attribution value for 2021
        attribution_2021 = group.loc[group['Year'] == 2021, 'Attribution'].iloc[0]
        # create a new row for 2022
        new_row = pd.DataFrame({'SEDOL': [sedol], 'Year': [2022], 'Attribution': [attribution_2021]})
        # append the new row to the original dataframe
        atrAgg = pd.concat([atrAgg, new_row], ignore_index=True)
    elif 2020 in group['Year'].values:
        # get the Attribution value for 2020
        attribution_2020 = group.loc[group['Year'] == 2020, 'Attribution'].iloc[0]
        # create new rows for 2021 and 2022
        new_row_2021 = pd.DataFrame({'SEDOL': [sedol], 'Year': [2021], 'Attribution': [attribution_2020]})
        new_row_2022 = pd.DataFrame({'SEDOL': [sedol], 'Year': [2022], 'Attribution': [attribution_2020]})
        # append the new rows to the original dataframe
        atrAgg = pd.concat([atrAgg, new_row_2021, new_row_2022], ignore_index=True)

    else:
        # no data for 2022, 2021, 2020 
        # create a new row for 2022 with "INVALID" in the Attribution column
        new_row = pd.DataFrame({'SEDOL': [sedol], 'Year': [2022], 'Attribution': ['INVALID']})
        # append the new row to the original dataframe
        atrAgg = pd.concat([atrAgg, new_row], ignore_index=True)
