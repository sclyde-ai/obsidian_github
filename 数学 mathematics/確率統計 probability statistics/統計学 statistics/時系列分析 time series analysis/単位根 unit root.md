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