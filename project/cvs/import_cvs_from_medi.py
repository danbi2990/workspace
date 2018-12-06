#%%
import pandas as pd
#%%
directory_path = '/Users/jake/OneDrive - leverage innovative users/Documents/편의점/'
file_name = 'medi_raw.xlsx'
file_path = directory_path + file_name

#%%
# cvs.columns
medi = pd.read_excel(file_path)
len(medi)

#%%
medi.columns

#%%
medi['사업장명']

#%%
cvs_file_name = 'cvs_from_medi.tsv'
medi.to_csv(directory_path + cvs_file_name, sep='\t', index=False)
#%%
#%%
#%%
#%%
#%%


#%%



















