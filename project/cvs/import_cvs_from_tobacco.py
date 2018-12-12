#%%
import re
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
    '씨유', 'CU', '훼미리마트', '훼밀리마트', '패밀리마트', 'familymart',
    '세븐일레븐', '코리아세븐', '바이더웨이', 'buytheway',
    '이마트24', 'emart24',
    '미니스톱', '미니스탑'
    '씨스페이스', '씨스페이시스',
]
cvs_string = '|'.join(cvs_names)

#%%
# big_cvs = pd.DataFrame()
# for idx, row in tobacco1.iterrows():
#     for name_keyword in cvs_names:
#         if name_keyword in row['사업장명']:
#             big_cvs = big_cvs.append(tobacco1.loc[idx])

#%%
sheet2 = '담배소매업_2'
tobacco = tobacco1.append(pd.read_excel(file_path, sheet2))
print(len(tobacco))

idx_cvs = tobacco['사업장명'].str.contains(cvs_string, flags=re.IGNORECASE, regex=True)


cvs_file_name = 'cvs_from_tobacco3.tsv'
# big_cvs.to_csv(directory_path + cvs_file_name, sep='\t', index=False)
print(len(tobacco.loc[idx_cvs]))
tobacco.loc[idx_cvs].to_csv(directory_path + cvs_file_name, sep='\t', index=False)

#%%



# big_cvs = pd.DataFrame()
# for idx, row in tobacco.iterrows():
#     for name_keyword in cvs_names:
#         if name_keyword in row['사업장명']:
#             big_cvs = big_cvs.append(tobacco.loc[idx])

#%%
# big_cvs3 = big_cvs.append(big_cvs2)
# len(big_cvs3)

#%%
# cvs_file_name = 'tobacco_from_cvs2.tsv'
# big_cvs.to_csv(directory_path + cvs_file_name, sep='\t', index=False)

#%%


#%%



















