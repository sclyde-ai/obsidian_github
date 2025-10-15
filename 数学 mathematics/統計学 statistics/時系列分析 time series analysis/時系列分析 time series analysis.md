$$
\{y_t\}_{t \in T}
$$
- T 時間(全順序集合)

    





- 線形模型 linear model
    
    
    - 
    
    - ARIMA AR integrated MA
        階差系列がARMA
        $$
        y_t -y_{t-d}= c + \sum_{k=1}^p \phi_k y_{t-k} + \sum_{k=1}^q \theta_k\epsilon_{t-k} + \epsilon_t
        $$
    - SARIMA seasonal ARIMA
        時系列方向と周期方向にARIMAを用いる
    - ARCH autoregressive conditional heteroscedasticity
        過去の誤差が現在の分散に影響
        $$
        \sigma^2_t = \alpha_0 + \sum_{i=1}^q \alpha_i \epsilon_{t-i}
        $$
    - GARCH generalized autoregressive conditional heteroscedasticity
        過去の誤差と分散が現在の分散に影響
        $$
        \sigma^2_t = \alpha_0 + \sum_{i=1}^q \alpha_i \epsilon_{t-i} + \sum_{j=1}^p \beta_j\sigma_{t-j}
        $$
    - EGARCH exponential GARCH
    - FIGARCH
    - GJR GARCH
    - DCC-GARCH
    - LSTM-GARCH
    - GARCH-M
    - Heston-Nandi GARCH
- 状態空間模型 state space model
    観測できない「状態」が「観測値」に影響を与える
    - 画像 image
        ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image.jpeg)
    - data
        - 観測値 observation
            $$
            y = (y_1, y_2,...)
            $$
        - 状態 state
            $$
            a = (a_1,a_2,...)
            $$
    - 方程式
        - 観測方程式
            観測値と状態の関係式
            $$
            y_t = f(a_t) + \epsilon_t
            $$
        - 状態方程式
            状態の時間経過による関係式
            $$
            a_t = g(a_{t-1}) + \eta_t
            $$
    - 推定
        - filtering
            過去と現在の観測値からnoiseを除去して状態を推定する
            - 画像 image
                ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%201.jpeg)
        - 平滑化 smoothing
            過去、現在、未来の観測値から状態を推定する
            - 画像 image
                ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%202.jpeg)
        - 将来予測 forecasting
            現在の状態から未来の状態を推定する
            - 画像 image
                ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%203.jpeg)
    - 例 example
        - Kalman filter 線形
            - 観測方程式
                $$
                y_t = Z_t a_t + \epsilon_t
                $$
            - 状態方程式
                $$
                a_t = T_t a_{t-1} + \eta_t
                $$
    - website
        [Pythonによるビジネス予測に活かす「状態空間モデル」の基礎と実装例](https://www.salesanalytics.co.jp/datascience/datascience250/)
- 時間周波数解析 time frequency analysis
    - power spectrum analysis
    - DFA detrended fluctional analysis
    - periodogram
        $$
        S_N (f_k) = \frac{|X(f_k)|^2}{N}  = \frac{1}{N}\left|\sum_{n = 0}^{N -1} x[n] \exp(-i2\pi f_k n)\right|^2
        $$
- 正規分布過程 Gaussian process
- Box-Jenkins
- Yule-Walker
- link
    [時系列データ予測の最前線まとめ：機械学習からディープラーニングまで - Qiita](https://qiita.com/ryosuke_ohori/items/6f4d7e8027b0f4797e9f)
    [Websites change. Perma Links don't.](https://perma.cc/)
    [The ARIMAX model muddle – Rob J Hyndman](https://robjhyndman.com/hyndsight/arimax/)