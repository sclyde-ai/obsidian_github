# data指定方法
.loc : labelで指定する
.iloc : 座標で指定する
[] : 汎用
    [column]: 列を1つ指定する
    [[column1, column2, ..]] : 列を複数指定する
    [start_number:end_number] ; 行をsliceする
    [bool_series] : Trueの列だけ取得する 
# useful code
- to numeric
    df = df.apply(pd.to_numeric, errors='coerce')
- to datetime
    df= pd.to_datetime(df, format="%Y年%m月%d日", errors='coerce')