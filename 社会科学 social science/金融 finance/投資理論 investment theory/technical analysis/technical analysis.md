- 傾向 trend
    - MA moving average 移動平均
        near-term
                - 5 days
                - 10 days
                - 20 days
                - 50 days
        long-term
                - 50 days
                - 100 days
                - 200 days
        fibonacci
                - 5
                - 8
                - 13
                - 21
    - EMA exponential moving average 指数的移動平均
            $$
            EMA_k = \frac{1}{k} \sum_{i = n-k+1}^n p_i
            $$
    - parabolic SAR stop and reverse
            $$
            SAR_{n+1} = SAR_n + AF(EP - SAR_n)
            $$
            - EP extreme point
                representing the highest price in an uptrend or the lowest price in a downtrend
            - AF acceleration factor
                which starts at a default value (usually 0.02) and increases incrementally (usually by 0.02) when a new extreme price point (EP) is reached, up to a maximum (often 0.2)
- 振幅 oscillator
    chart indicators that can assist a trader in determining overbought or oversold conditions in ranging market
    data point
            $$
            \{p_1, p_2, ..., p_n\}
            $$
    - MACD moving average convergence divergence
            $$
            MACD = EMA_{12} - EMA_{26}
            $$
    - Bollinger band
            $$
            MA \pm n SD
            $$
        MA moving average 移動平均
        SD standard deviation 標準偏差
    - momentum
            $$
            \frac{\partial^2 S}{\partial t^2}
            $$
        S stock price 株価
        t time 時間
    - RSI relative strength index 相対力指数
            $$
            RSI = \left(1-\frac{1}{1+ RS}\right)\times 100
            $$
    - RS relative strength 相対力
                $$
                RS = \frac{Average\ Gain}{Average\ Loss}
                $$
        overnight (above 70)
            A high RSI (above 70) suggests that a stock's price has risen too quickly and may be due for a correction or pullback.
            When RSI rises above 70 and then crosses back below it, it can signal a potential selling opportunity.
        mid-range (between 30 and 70)
            The RSI is generally neutral when in this range, suggesting that the price movement is neither overbought nor oversold
        oversold (below 30)
            A low RSI (below 30) suggests that a stock's price has fallen too quickly and may be due for a rebound.
            When RSI falls below 30 and then crosses back above it, it can signal a potential buying opportunity.        
    - 平均移動線乖離率
    - phycological line
- S&R
    - support
        A price level where **demand (buying) is strong enough** to prevent further decline.
    - resistance
        A price level where **supply (selling) is strong enough** to prevent further rise.  
- breakout
    when prices pass through and stay through an area of support or resistance
- MA cross
    - golden cross
        短期の移動平均線が長期の移動平均線を下から上に突き抜ける現象のこと
        相場の上昇傾向への転換を示す。
        買い時
    - dead cross
        短期の移動平均線が長期の移動平均線を上から下に突き抜ける現象のこと
        相場の下降傾向への転換を示す。
        売り時
