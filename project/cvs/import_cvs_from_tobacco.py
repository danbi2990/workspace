import re
import pandas as pd

directory_path = '/Users/jake/OneDrive - leverage innovative users/Documents/편의점/'
file_name = 'tobacco_raw.xlsx'
file_path = directory_path + file_name

sheet1 = '담배소매업_1'
tobacco1 = pd.read_excel(file_path, sheet1)
len(tobacco1)

cvs_names = [
    '지에스', 'GS', 'LG25', '엘지25',
    '씨유', 'CU', '훼미리마트', '훼밀리마트', '패밀리마트', 'familymart',
    '세븐일레븐', '코리아세븐', '바이더웨이', 'buytheway',
    '이마트24', 'emart24', '위드미',
    '미니스톱', '미니스탑', '대상유통',
    '씨스페이스', '씨스페이시스',
]
cvs_string = '|'.join(cvs_names)

sheet2 = '담배소매업_2'
tobacco = tobacco1.append(pd.read_excel(file_path, sheet2))
print(len(tobacco))

idx_cvs = tobacco['사업장명'].str.contains(cvs_string, flags=re.IGNORECASE, regex=True)


cvs_file_name = 'cvs_from_tobacco4.tsv'
print(len(tobacco.loc[idx_cvs]))
tobacco.loc[idx_cvs].to_csv(directory_path + cvs_file_name, sep='\t', index=False)
