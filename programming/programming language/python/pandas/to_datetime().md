---
alias:
    ['to_datetime()']
---
```
pd.to_datetime(df)
```
# useful code
```
df = pd.to_datetime(df, format="%Y年%m月%d日", errors='coerce')
```
```
df = pd.to_datetime(df, format="%Y/%m/%d/", errors='coerce')
```
