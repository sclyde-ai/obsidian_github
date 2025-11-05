---
alias:
    ['volatility']
---
- volatility skew
    - forward skew
        ![download.jpg](download.jpg)
    - reverse skew
        ![reverse.webp](reverse.webp)
    - volatility smirk
- HV historical volatility
    - time series
        $$
        (S_0, S_1, ..., S_N)
        $$
    - log return
        $$
        R_k = \log S_k - \log S_{k-1} \\
        k \in (1,2,..., N)
        $$
    - sample mean
        $$
        \bar R = \sum_{k=1}^N R_k
        $$
    $$
    \sigma_{HV} = \sqrt{\frac{1}{N-1}\sum_{k=1}^N (R_k -\bar R)^2}
    $$
    - low frequency
    - it’s typically calculated by daily data
- RV realized volatility
    - time series
        $$
        (S_0, S_1, ..., S_N)
        $$
    - log return
        $$
        R_k = \log S_k - \log S_{k-1} \\
        k \in (1,2,..., N)
        $$
    $$
    \sigma_{RV} = \sqrt {\sum_{k=1}^N R_k^2}
    $$
    - high frequency
    - it converges in probability (but there is the problem)
    - micro structure noise
- IV implied volatility
    - market price V^{market}
    $$
    f(\sigma_{IV}) \equiv V^{BS}(S, K, T, r, \sigma_{IV}) - V^{market} = 0
    $$
    - Newton-Raphson/Newton method
        - vega \vega
            $$
            $$
    - term structure
        - contango
        - backwardation
    - surface
    - SVI stochastic volatility inspired
        $$
        w(k) = a +b(\rho (k-m) + \sqrt{(k-m)^2 + \sigma_{svi}})
        $$
    - sticky moneyness
- LV local volatility
    stationary 
    $$
    \frac{dS_t}{S_t} = r(t)dt + \sigma_{LV}(t, S_t)d W_t
    $$
    - Dupire
- SV stochastic volatility
    dynamic
    - Heston
        - variable
            - risk free rate r
            - stock price S_t
            - volatility v_t
            - Wiener process W_t
        $$
        dS_t= rS_tdt + \sqrt v_t S_tdW_t^{(1)}
        $$
        $$
        dv_t = \kappa(\theta-v_t)dt + \xi \sqrt v_t dW_t^{(2)}
        $$
    - SABR stochastic alpha beta rho
        - parameter
            - volatility
            - vol of vol
            - correlation of
        $$
        dF_t = \sigma_t (F_t)^\beta dW_t^F \\
        d\sigma_t = \alpha \sigma_t dW_t^\sigma \\
        dW_t^F dW_t ^\sigma= \rho dt
        $$
    - CEV constant elasticity of variance
        $$
        dS_t = \mu S_t dt + \sigma S_t^\gamma dW_t
        $$
    - Bachelier model
    - BNS Barndorff-Nielsen-Shephard
- VIX
- variance swap
- volatility drag
- contango
- SVI model
- backwardation
- functional ito calculus
- Breeden-Litzenberger
- Fokker-Planck equation
- 資産の分散は3〜5年が多い