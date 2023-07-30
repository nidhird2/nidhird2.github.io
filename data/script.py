import pandas as pd


counties = pd.read_csv("us-counties-2020.csv")
temp = counties[counties['state'] == 'Illinois']
temp2 = temp.max()
cases_2020 = temp[temp.date == temp.date.max()]
print(cases_2020.head())



mask_use = pd.read_csv("mask-use-by-county.csv")
mask_use.rename(columns={'COUNTYFP': 'fips'}, inplace=True)

cases_with_masks = cases_2020.merge(mask_use, on='fips')

colleges = pd.read_csv("colleges.csv")
colleges = colleges[colleges['state'] == 'Illinois']
aa = colleges.groupby('county', as_index=False)['cases'].sum()
aa.rename(columns={'cases': 'college_cases'}, inplace=True)

cases_with_masks_uni = cases_with_masks.merge(aa, on='county', how = 'left')

prisons = pd.read_csv("facilities.csv")
prisons = prisons[prisons['facility_state'] == 'Illinois']
bb = prisons.groupby('facility_county', as_index=False)['total_inmate_cases'].sum()
bb.rename(columns={'facility_county': 'county'}, inplace=True)


all = cases_with_masks_uni.merge(bb, on='county', how = 'left')



print(len(cases_with_masks_uni))
print(len(all))

print(all.head())


all.to_csv("hydrated_all.csv", index=False)