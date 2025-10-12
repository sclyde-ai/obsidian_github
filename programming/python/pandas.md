# data型
- datetime
- string
- object
- category
# function
- pd.to_datetime()
    Seriesをdatetime型に変換する
    - 引数一覧
        - format: strftime
            strftimeの形式で文字列を認識する
        - dayfirst: bool
    - 自動で認識する形式
        - YYYY-MM-DD HH:MM:SS
        - YYYY/MM/DD
        - YYYY.MM.DD
- .merge()
    - 引数
        - left_index
# pd.DataFrame()
## property
## method
    - .groupby()
    - .resample(frequency)
        freqencyごとにresamplingする
        - .last()
    - .join()
- .apply()
# accessor
data型固有の属性やmethodをSeriesから直接利用可能にする機能
- .dt
    datetime
    - property
        - .year
        - .month
        - .day
        - .date
        - .weekday
        - .day_name()
        - .quarter
        - .hour
        - .minute
        - .second
    - method
        - .normalize()
            時刻を00:00:00にする
        - 
- .str
    string
- .cat
    category 
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