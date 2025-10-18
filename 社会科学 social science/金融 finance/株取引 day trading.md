- 専門用語 expertise
    - 相場 market price
            商品が取引される、その時その時の値段
    - 時価 market value
    - 健玉 position
         - 買い建玉/買建玉 long position
                - buy side
                - buy and own an asset (not right)
                - buy first, sell later
                - expecting the price will rise
                - profit from holding long-term
            - 売り建玉/売建玉 short position
                - sell side
                - sell and borrow an asset (not right)
                - sell first, buy later
                - expecting the price will fall
                - profit form holding short-term
            - neutral position
                a position does not change much in value if the price of the underlying instrument rises or falls
            - 持ち高/持高position size
                the number of units invested in a particular security by an investor or trader
            - open position
                buy, in a market
            - close position
                sell, exit a market
            - entry
                - entry point/price
                    the price at which an investor buys or sells a security
            - exit
            - overnight
            - RTP reserve tranche position
        - 買値 bid
            the highest price a buyer is willing to pay for an asset
            - 買い気配 bid interest/pressure
                買い注文が売り注文より多く、売買が成立しない状態
        - 売値 ask/offer
            the lowest price at which a seller is willing to accept for an asset
            - 売り気配 ask interest/pressure
                売り注文が買い注文より多く、売買が成立しない状態
        - 出来高 volume
        - 含み益 unrealized gain
        - 含み損 unrealized loss
        - spread
            difference or gap between two related values.
            - bid-ask spread
                the difference between the highest price that a buyer is willing to pay for an asset and the lowest price that a seller is willing to accept
            - interest rate spread
            - credit spread
        - 注文 order
            - order book
            - market order
            - limit order
            - stop order
            - stop loss
            - trailing stop
            - IFD order
            - OCO order
        - 板/ローソク足 candlestick
            ![image.png](学問%20academics/notion/economics/ExportBlock-5173355a-40b0-4550-b453-181e6713355d-Part-1/image%201.png)
            - 見せ板
            - 板読み
        - 一目均衡表
            - 時間論
            - 波動論
            - 水準論/値幅観測論
            - 歩み値 time and sales/trade log
                取引時間中の約定の履歴を時系列で表示したもの。時刻、価格、数量が表示される
                - 約定
                    成立した売買注文
                    - 約定単位 tick
                - 約定時刻
                - 約定価格/値段
                - 約定数量
        - calibration
            adjusting a model's parameters to ensure its outputs (like prices) match observed market data as closely as possible, essentially making the model's predictions align with real-world prices
        - backtesting
            a method of testing a trading strategy on historical data to assess its potential performance before risking real capital
    - 戦略 strategy
        - algorithmic trading
        - 損切り loss cut
            含み損を損失として確定させて売却すること
        - in & out
            短期間で大量の売り買いを行う
            buy and sell multiple times over a short period
        - scalping
        - ドテン売買 reversal trading
        - redemption
    - 市場 market
        - 状態 situation
            - range market 往来相場/レンジ相場/ボックス相場
                価格が一定の値幅の中で上下を繰り返す相場
                a trading environment where an asset's price fluctuates within a defined high and low price range, without a clear trend in either direction
            - volatile market
            - market sentiment/investor attention
                - bullish
                - bearish
        - 現象 phenomena
            - flash crash
                an extremely rapid decline in the price of one or more commodities or securities, typically one caused by automated trading
                ![image.png](学問%20academics/notion/economics/ExportBlock-5173355a-40b0-4550-b453-181e6713355d-Part-1/image%202.png)
            - slippage
                急激な価格変動
            - swing
            - break
            - ダマシ fake out
            - グランビルの法則
    - FX構造解析ラボ
        - website
            [FX構造解説ラボ｜note](https://note.com/fx_structure2025)
- technical analysis
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
    - stochastics
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
        短期の移動平均線が長期の移動平均線を下から上に突き抜ける現象
        相場の上昇傾向への転換を示す買いシグナル        
    - dead cross
        短期の移動平均線が長期の移動平均線を上から下に突き抜ける現象
        相場の下降傾向への転換を示す売りシグナル
- drawdown
    the investment loss experienced from a high point to a low point