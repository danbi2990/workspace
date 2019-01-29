import os
import unicodedata


directory = '/Users/jake/OneDrive - leverage innovative users/Documents/Temporary/ALIO/'

_list = [unicodedata.normalize('NFC', f) for f in os.listdir(directory)]

with open(directory + _list[0], 'r', encoding='euckr') as f:
    raw = f.read()

print(raw)



