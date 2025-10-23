- Laspeyres
	$$
	L = \frac{\sum p_t q_0}{\sum p_0 q_0}
	$$
	- CPI consumer price index
- Passhe
	$$
	P = \frac{\sum p_t q_t}{\sum p_0 q_t}
	$$
	- GDP deflator
- fisher
	LaspeyresとPaasheの幾何平均
	$$
	F = \sqrt {L\times P}
	$$
- 株価/時価総額 stock price/market cap
    - Dow divisor(divisor)
        number of stock (basically)
        - algorithm
            $$
                \frac{sum_{old}}{divisor_{old}} = \frac{sum_{new}}{divisor_{new}}
            $$
            $$
                divisor_{new} = \frac{divisor_{new}\times sum_{new}}{sum_{old}}
            $$
    - 株価 stock price
        - DJIA Dow jones industrial average
            $$
            \frac{sum\:of\:stock\:price\:of\:top\:30}{divisor}
            $$
        - Nasdaq composite index
            tech heavy
    - 時価総額 market cap
        - S&P 500 index
            $$
            \frac{sum\:of\:market\:cap\:of\:top\:500}{divisor}
            $$
- 物価 price
    - 消費者物価指数 CPI consumer price index
        $$
        CPI_t = \frac{C_t}{C_0}*100
        $$
        $C_t$  : cost of market in current period
        $C_0$  : cost of market in base period
        - 日本の消費者物価指数
            家計調査の今年度と一年前の平均1ヶ月の1世帯当たり品目別消費支出金額
            https://www.stat.go.jp/data/cpi/2020/kaisetsu/pdf/1.pdf
        - core CPI
    - 生産者物価指数 PPI producer price index
        - US
            published by bureau of labor statistics 
        - core CPI
    - PCE personal consumption expenditure
        - US
            published by bureau of labor statistics 
        - core CPI
- 国民経済計算 national account
    - 国内総生産 GDP gross domestic product
        the value produced in the country
        - formula
            GDP = C + I + G + EX - IM
        - variables
            - C 消費 Consumption
            - I 投資 Investment
            - G 政府支出 Government Expenditure
            - EX 輸出 Export
            - IM 輸入 Import
        - 実質 real GDP
        - 名目 nominal GDP
        - GDP deflator
            nominal GDP/real GDP*100
            - inflation rate
                GDP deflatorの前年比変化率
                $$
                \frac{GDP\ deflator_t}{GDP\ deflator_{t-1}}
                $$
            - chained weighted method
        - green GDP
    - 国民総生産 GNP gross net product
        the value produced by the residents
        GNP = GDP 
        + Net Income Inflow from Foreign Countries 
        – Net Income Outflow to Foreign Countries
    - 国民総所得 GNI dross national income
        the total income earned by residents
        GNI = GDP + EX_FS - IM_FS
    - NNP national net product
    - NI national income
    - NNW national net wealth
- 為替 foreign exchange