$$
\{y_t\}_{t \in T}
$$
- T 時間(全順序集合)
- data/series
    - panel data
    - time series data
        $$
        \{ y_t\}_{-\infin}^\infin
        $$
        特定の対象
        複数の時間
    - cross section data
        複数の対象
        特定の時間
    - 対数系列 logarithm
    - 差分系列・階差系列 differential
    - 対数差分系列 logarithm differential
    - 季節調整済み系列 seasonally adjusted
    - 変動成分 components of time series
        - trend 傾向
            長期的傾向
        - seasonality 季節変動
            1年周期の規則的変動
        - cycle 周期性
            trendより短期、季節変動より長期な、周期的な変動
        - anomaly 不規則変動
            noise
- 自己相関 autocorrelation
    - 自己共分散 autocovariance
    - 自己相関係数 autocorrelation
    - 偏自己相関
    - 検定 test
        - Ljung-box test
            - Box-Pierce
            - Ljung-box
            - link
                [Ljung-Box 検定](https://hkawabata.github.io/technical-note/note/Math/statistics/hypothesis-testing/ljung-box-testing.html)
        - Durbin-Watson test
- 定常性 stationary
    時間的な不変性をもつ
    - 弱定常性 weak stationary
        - 期待値一定 the expectation is constant
            $$
            \mathbb E[y_t] = \mu 
            $$
        - 共分散が時間差に依存 the covariance depends on only the time span
            $$
            cov(y_t, y_{t-k}) = \mathbb E[(y_t-\mu)(y_{t-k}-\mu)] = \gamma_k
            $$
    - 強定常性 strong stationary
- 内生性 endogeneity
    $$
    Cov(X, \epsilon) \ne 0
    $$
    - 検定 test
        - Weak instrument
        - Wu-Hausman
        - Sargan
- 単位根 unit root
    差分が定常である非定常過程
    non-stationary process that differencing is stationary 
    - 単位根検定 unit root test
        - DF Dickey-Fuller test
            - model
                $$
                y_t = \rho y_{t-1} +\epsilon_t
                $$
                $\rho = 1$ :  非定常、単位根あり non-stationary, it has a unit root
                $|\rho| < 1$ : 定常 stationary
                $|\rho| > 1$ : 指数的 exponential
            $$
            \Delta y_t = y_t - y_{t-1}
            \\ = (\rho -1)y_{t-1} + \epsilon_t \\ = \gamma y_{t-1} + \epsilon_t
            $$
            - 帰無仮説 $H_0$ :  $\gamma = 0$
            - 対立仮説 $H_1$ :  $\gamma < 0$
        - ADF Augmented Dickey-Fuller test
            $$
            \Delta y_t = \alpha + \beta t + \gamma y_{t-1} + \sum_{i=1}^p \delta_i \Delta y_{t-i} + \epsilon_t
            $$
            - $\Delta y_t$ : 差分 differential
            - $\alpha$ : 定数 constant
            - $\beta t$ :  時間傾向 time trend
            - $\gamma y_{t-1}$ :  単位根検定 unit root test
            - $\sum_{i=1}^p \delta_i \Delta y_{t-i}$  :  lag (correct autocorrelation)
        - KPSS Kwiatkowski-Phillips-Schmidt-Shin
            $$
            y_t = r_t + \beta t + \epsilon_t
            $$
            - $r_t = r_{t-1} + u_t$ : 酔歩運動 random walk
            - $u_t$ : 白色雑音 white noise
            - $\beta t$ : 線形傾向 linear trend
            - $\epsilon_t$ : 誤差 error
            - test statistics
                1. estimate time series with a regression model
                    - level stationary
                        $$
                        y_t = \alpha + \epsilon_t
                        $$
                    - trend stationary
                        $$
                        y_t = \alpha + \beta t +  \epsilon_t
                        $$
                    - 
                2. cumulative sum 
                3. test statistics
        - PP Phillips-Person test
- 白色雑音 white noise
    - 期待値は0 the expectation is 0
        $$
        \mathbb E[\epsilon_t] = 0
        $$
    - 分散は一定 the variance is constant
        $$
        Var(\epsilon_t) = \mathbb E[\epsilon_t^2] = \sigma^2 
        $$
    - 自己共分散は0 the autocovariance is 0
        $$
        \gamma_k = \mathbb E[\epsilon_t \epsilon_{t-k}] = 0
        $$
    - 白色光との類似性が語源
    - power spectrumが一定のnoise
    - gaussian white noise
- 線形模型 linear model
    - MA moving average model 移動平均模型
        過去の誤差が現在の値に影響
        - white noise $\epsilon_t$
        $$
        y_t= \mu + \epsilon_t + \sum_{k=1}^q \theta_k\epsilon_{t-k}
        $$
        - 期待値
            $$
            \mathbb E [\hat y_t] = \mu
            $$
        - 分散
            $$
            (1+ \theta_1^2 + ...+ \theta_q^2)\sigma^2
            $$
    - AR autoregressive model 自己回帰模型
        過去の値が現在の値に影響
        - white noise $\epsilon_t$
        $$
        y_t = c + \sum_{k=1}^p \phi_k y_{t-k} + \epsilon_t
        $$
        - 期待値
            $$
            \mathbb E[\hat y_t] = \frac{c}{1 - \sum_{i = 1}^p \phi_i}
            $$
        - 分散
            $$
            var (\hat y_t) = \frac{\sigma^2}{1 - \sum_{i = 1}^p \phi_i \rho_i}
            $$
        - 定常性条件
            $$
            1 -\sum^p_{i=1} \phi_i z^i = 0
            $$
    - VAR vector autoregressive model 複数列自己回帰模型
        - vector $\bm y_t$
        - coefficient matrix $A_k$
        - error/shock/innovation $\epsilon_t$
        $$
        \bm y_t = c + \sum_{k=1}^p A_k \bm y_{t-k} + \bm \epsilon_t
        $$
        - 定常性条件 stationary
            $$
            \det(I_k -\sum^p_{i=1} A_i z^i) = 0
            $$
        - 予測誤差分散分解 FEVD Forecast Error Variance Decomposition
            - 移動平均表現 MA version
                $$
                y_t = \mu + \sum_{h=0}^\infin \psi_h  \epsilon_{t-h}
                $$
                - impulse response coefficient matrix
                    $$
                    \psi_h = \frac{\partial y_{t+h}}{\partial\epsilon_{t}}
                    $$
                    - how to calculate
                        $$
                        \psi_0 = I \\
                        \psi_h = \sum_{j=1}^{\min(h, p)} A_j \psi_{h-j}
                        $$
            - 分散共分散行列 variance covariance matrix
                $$
                \Sigma = \frac{1}{T-k} \sum_{t =1}^T \epsilon_t \times \epsilon_t
                \\ = (\sigma_{ij})_{i \in \{1, ... ,p\}, j \in \{1, ..., T\}}
                $$
                - outer product $\times$
            - Cholesky decomposition
                $$
                \Sigma = LL^\top
                $$
                - modified Cholesky decomposition
                    $$
                    \Sigma = LDL^\top
                    $$
            - 直行化誤差 orthogonalized shock
                $$
                u_t = L^{-1} \epsilon_t
                $$
            - IRF impulse response function
                $$
                IRF_{i, j, h } = (\psi_h L)_{i, j}
                $$
                - normalized IRF
                    $$
                    IRF_{i, j, h}^{normalized} = (\psi_h L)_{i, j} \sqrt{\sigma_{j j}}
                    $$
            - 予測誤差分散 forecasting error variance
                $$
                Var(y_{i, t+h}) = \sum_{s=0}^{h-1} (\psi_s  L\Sigma L^\top \psi_s^\top)_{i, i}
                $$
            - 寄与度 contribution ratio
                $$
                CR_{i, j, h} 
                = \frac{\sum_{s = 0}^{h-1} (IRF_{i, j, s}^{normalized})^2}{Var(y_{i, t+h}) } \\
                = \frac{\sum_{s = 0}^{h-1}(\psi_s L)^2_{i, j} \sigma^2_{j j}}{\sum_{s=0}^{h-1} (\psi_s  L\Sigma L^\top \psi_s^\top)_{i, i}}
                $$
                the contribution ratio of j for i
        - SVAR structure VAR
        - granger causality
    - ARMA autoregressive moving average model 自己回帰移動平均模型
        過去の値と誤差が現在の値に影響
        $$
        y_t = c + \sum_{k=1}^p \phi_k y_{t-k} + \sum_{k=1}^q \theta_k\epsilon_{t-k} + \epsilon_t
        $$
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