---
alias:
    ['data_analysis_template']
---
## import template
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib
```
## show all DataFrame
```
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)
```
## get all sheets in a file
```
with pd.ExcelFile("file.xlsx") as xls:
	dfs = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}
```
## get all files in a folder
```
import pandas as pd
import os
folder_path = 'path/to/your/folder'  
dfs = {}
for file in os.listdir(folder_path):
	if file.endswith('.xlsx') or file.endswith('.xls'):
		file_path = os.path.join(folder_path, file)
		df = pd.read_excel(file_path)
		dfs[file] = df
```
## check string in 
```
pd.Series.str.contains(string)
```
## import anything from parent dir
```
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
```
## get all file
```
from pathlib import Path
files = Path('.').rglob('*')
```