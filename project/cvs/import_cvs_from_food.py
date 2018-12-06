#%%
import pandas as pd
#%%
directory_path = '/Users/jake/OneDrive - leverage innovative users/Documents/편의점/'
file_name = 'food_raw.xlsx'
file_path = directory_path + file_name

#%%
# cvs.columns
sheet1 = '휴게음식점_1'
cvs1 = pd.read_excel(file_path, sheet1)
idx_cvs1 = cvs1['업태구분명'] == '편의점'
len(cvs1.loc[idx_cvs1])


#%%
sheet2 = '휴게음식점_2'
cvs2 = pd.read_excel(file_path, sheet2)
idx_cvs2 = cvs2['업태구분명'] == '편의점'
len(cvs2.loc[idx_cvs2])


#%%
cvs3 = cvs1.loc[idx_cvs1].append(cvs2.loc[idx_cvs2])
len(cvs3)

#%%
cvs3.index

#%%
cvs_file_name = 'cvs.tsv'
cvs3.to_csv(directory_path + cvs_file_name, sep='\t', index=False)

#%%


#%%



















