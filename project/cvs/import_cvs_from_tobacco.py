#%%
import pandas as pd
#%%
directory_path = '/Users/jake/OneDrive - leverage innovative users/Documents/편의점/'
file_name = 'tobacco_raw.xlsx'
file_path = directory_path + file_name

#%%
# cvs.columns
sheet1 = '담배소매업_1'
tobacco1 = pd.read_excel(file_path, sheet1)
len(tobacco1)

#%%
# tobacco1.head()
cvs_names = [
    '지에스', 'GS',
    '씨유', 'CU', '훼미리마트', '패밀리마트'
    '세븐일레븐',
    '이마트24', 'emart24',
    '미니스톱',
    '씨스페이스',
]

#%%
big_cvs = pd.DataFrame()
for idx, row in tobacco1.iterrows():
    for name_keyword in cvs_names:
        if name_keyword in row['사업장명']:
            big_cvs = big_cvs.append(tobacco1.loc[idx])

#%%
sheet2 = '담배소매업_2'
tobacco2 = pd.read_excel(file_path, sheet2)
len(tobacco2)

#%%
big_cvs2 = pd.DataFrame()
for idx, row in tobacco2.iterrows():
    for name_keyword in cvs_names:
        if name_keyword in row['사업장명']:
            big_cvs2 = big_cvs2.append(tobacco2.loc[idx])

#%%
big_cvs3 = big_cvs.append(big_cvs2)
len(big_cvs3)

#%%
cvs_file_name = 'tobacco_from_cvs.tsv'
big_cvs3.to_csv(directory_path + cvs_file_name, sep='\t', index=False)

#%%


#%%



















