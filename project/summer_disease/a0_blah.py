import os

import pandas as pd
pd.set_option('display.expand_frame_repr', False)

PATH = '/Users/jake/OneDrive - leverage innovative users/document/summer_disease/'

files = os.listdir(PATH)
filtered = sorted([f for f in files if f.endswith('.html')])
with open(os.path.join(PATH, filtered[0])) as f:
    content = f.read()
    dfs = pd.read_html(f)

df0 = dfs[0]
print(df0)
