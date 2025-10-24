- setting
    - assets
        $$
        N = \{1, 2, ..., n\}
        $$
    - return
        random variable
        $$
        \{R_i\}_{i \in N}
        $$
    - expected return
        $$
        \mu_i = \mathbb E[R_i]
        $$
    - variance
        $$
        \sigma_i^2 = Var(R_i) = \mathbb E[(R_i - \mu_i)^2]
        $$
    - covariance
        $$
        \sigma_{ij} = Cov(R_i, R_j) = \mathbb E[(R_i - \mu_i)(R_j - \mu_j)]
        $$
    - expected return vector
        $$
        \mu = (\mu_1, \mu_2,...,\mu_n)^\top
        $$
    - variance covariance matrix
        $$
        \Sigma = (\sigma_{ij})
        $$
    - 1 vector
        $$
        \bm 1 = (1, 1, ...,1)^\top
        $$
- portfolio
    - weight
        $$
        w = (w_1, w_2, ...,w_n)^\top \\
        \sum_{i=1}^n w_i = 1
        $$
    - expected return
        $$
        \mu_p = \mathbb E[R_w] 
        \\ = \mathbb E[\sum_{i=1}^n w_i R_i] 
        \\ = \sum_{i=1}^n w_i \mathbb E[R_i] \\
        = \sum_{i=1}^n w_i \mathbb \mu_i
        $$
    - variance
        $$
        \sigma_p^2 = w^\top \Sigma w
        $$
- GMVP global minimum variance portfolio
    $$
    \min_{w} \frac{1}{2} w^\top \Sigma w\\
    s.t. \ \bm 1^\top w = 1
    $$
    - GMVP weight vector
        $$
        w_{GMVP} = \frac{\Sigma^{-1}\rm 1}{\rm 1^\top \Sigma^{-1} \rm 1}
        $$
    - variance
        $$
        w_{GMVP} = \frac{1}{\rm 1^\top \Sigma^{-1} \rm 1}
        $$
        it equals to the Lagrange multiplier 
    - differentiate
        - $\nabla (w^\top \mu) = \mu$
        - $\nabla (w^\top \rm 1) = 1$
        - $\nabla (w^\top \Sigma w) = 2 \Sigma w$
- mean-variance optimization
    $$
    \min_{w} \frac{1}{2} w^\top \Sigma w \\
    s.t. \\ 
    \bm 1^\top w = 1 \\
    \mu^\top w = \mu_T
    $$
    - CML capital market line
        $$
        \mathbb E[R_P] = r_f + \frac{\mathbb E[R_T] - r_f}{\sigma_T}\sigma_P
        $$
        - 証明 proof
            安全資産と市場portfolioの組のportfolioの収益率を考える
            $$
            r_p = (1-w)r_f+w r_m \\
            \sigma_p = \sqrt{Var(r_p)} = w  \sqrt{Var(r_m)} = w \sigma_m
            $$
            無リスク資産の期待収益と分散から$w$を消去すると
            $$
            r_p = r_f+ w(r_m-r_f) \\
            r_p = r_f+ \frac{\sigma_p}{\sigma_m}(r_m-r_f)
            $$
    - tangency portfolio
        the risky asset portfolio maximizing sharpe ratio
        $$
        w_T = \frac{\Sigma^{-1}(\mu - r_f 1)}{1^\top \Sigma^{-1} (\mu - r_f1)}
        $$
    - market portfolio
        tangency portfolioは各危険資産の時価総額の比率と一致する
        これをmarket portfolioと呼ぶ
    - tangency portfolio vs market portfolio
        these are the same in CAPM
    - efficient frontier
    - sharpe ratio
        投資の「燃費」「効率性」
        $$
        \frac{\mathbb E[R_T] - r_f}{\sigma_T}
        $$
- CAPM capital asset pricing model
    - SML security market line
        $$
        \mathbb E[R_i] = r_f + \beta_i (\mathbb E[R_M] - r_f)
        $$
        - proof
            - expectation
                $$
                \mathbb E[R_P] = w \mathbb E[R_i] + (1-w) \mathbb E[R_M]
                $$
            - variance
                $$
                \sigma_P^2 = w^2 \sigma_i^2 + (1-w)^2 \sigma_M^2 + 2w(1-w) \sigma_{iM}
                $$
            - the derivative of r with respect to w
                $$
                \frac{d \mathbb E[R_P]}{d w} = \mathbb E[R_i] - \mathbb E[R_M]
                $$
            - the derivative of sigma^2 with respect to w
                $$
                \frac{d \sigma_P^2}{d w} = 2w \sigma_i^2 -2(1-w)\sigma_M^2 +2\sigma_{iM}-4w\sigma_{iM}
                = 2\sigma_P\frac{d \sigma_P}{d w}
                $$
            - the derivative of sigma with respect to w
                $$
                \frac{d \sigma_P}{d w} =\frac{w \sigma_i^2 -(1-w)\sigma_M^2 +(1-2w)\sigma_{iM}}{\sigma_P}
                $$
            $$
            \frac{\partial \mathbb E[R_P]}{\partial \sigma_P} = \frac{\frac{d \mathbb E[R_P]}{d w}}{\frac{d \sigma_P}{d w}} =\frac{(\mathbb E[R_i] - \mathbb E[R_M])\sigma_P}{w \sigma_i^2 -(1-w)\sigma_M^2 +(1-2w)\sigma_{iM}}
            $$
            plug in $w = 0$ 
            $$
            \left.\frac{\partial \mathbb E[R_P]}{\partial \sigma_P}\right|_{w=0} = \frac{(\mathbb E[R_P] - \mathbb E[R_M])\sigma_M}{-\sigma_M^2 +\sigma_{iM}}
            $$
            it corresponds to capital allocation line 
            $$
            \frac{(r_i - r_m)\sigma_m}{-\sigma_m^2 +\sigma_{im}} = \frac{r_m - r_f}{\sigma_m} \\
            r_i - r_m = (r_m - r_f)(-1 +\frac{\sigma_{im}}{\sigma_m^2})\\
            r_i - r_m + r_m - r_f = (r_m - r_f)\frac{\sigma_{im}}{\sigma_m^2} \\
            r_i - r_f = (r_m - r_f)\frac{\sigma_{im}}{\sigma_m^2} 
            $$
            $$
            \beta_i = \frac{\sigma_{im}}{\sigma_m^2}
            $$
    - beta
        the sensitivity 
        of the return of an asset 
        to the return of the market portfolio
        $$
        \beta_i = \frac{\sigma_{iM}}{\sigma^2_M} = \frac{Cov(R_i, R_M)}{Var(R_M)}
        $$
        $\beta > 1$ : aggressive, high volatility
        $\beta = 1$ : the same to market
        $0 <\beta < 1$ : defensive, low volatility 
        $\beta = 0$ : indifferent to market
    - risk
        $$
        \beta_i^2 \sigma_M^2 + \sigma^2_{\epsilon_i}
        $$
        - systematic risk
            $$
            \beta_i^2 \sigma_M^2 
            $$
        - unsystematic risk
            $$
            \sigma^2_{\epsilon_i}
            $$
    - alpha
        $$
        \alpha_i = \mathbb E[R_i]_{actual}-(r_f + \beta_i (\mathbb E[R_M] - r_f)) 
        $$
        $\alpha_i > 0$ : underestimate
        $\alpha_i < 0$ : overestimate 
        $\alpha_i = 0$ : correct
    - theorical stock price
        $$
        P_0 = \frac{\mathbb E[D_1] + \mathbb E[P_1]}{1 + \mathbb E[R_S]}
        $$
    - models
        - index model
            資産の超過収益と市場の超過収益の相関モデル
            $$
            Y_i = \alpha + \beta X+ e_i \\
            Y_i = r_i - r_f, X = r_m - r_f \\
            r_i - r_f = \alpha + \beta(r_m - r_f) + e_i
            $$
            - 最小二乗法
        - Fama-French three factor model
            |  | cap: small | cap: big |
            | --- | --- | --- |
            | BPR: high | small value | big value |
            | BPR: neutral | small neutral | big neutral |
            | BPR: low | small low | big low |
            - SMB small minus big
                時価総額のrisk factor
                - small size effect 小型株効果
                    anomaly
                - small 小型株
                    時価総額の小さい株
                - big 大型株
                    時価総額の大きい株
            - HML high minus low
                - value effect
                - high/value stock 割安株
                    BPRの高い株
                    PBRの低い株
                - low/growth stock 割高株
                    BPRの低い株
                    PBRの高い株
                - BPR book to price ratio 株価純資産倍率の逆数
                    一株あたり純資産/株価
                - PBR price to book ratio 株価純資産倍率
                    株価/一株あたり純資産
        - zero beta CAPM
        - intemporel CAPM
        - 消費CAPM
    - 資産数を増やすと…
        全ての分散 $\sigma^2$と共分散 $\rho^2$が等しいと仮定する
        $$
        \sigma^2_p = n \left(\frac{1}{n} \right)^2 \sigma^2 + (n^2 -n)\left(\frac{1}{n} \right)^2 \rho^2 \\ = \left(\frac{1}{n} \right)\sigma^2 + \left(1 -\frac{1}{n} \right) \rho^2 \\
        \xrightarrow[n\to\infty]{} \rho^2
        $$
        資産数を増やすと共分散が残ることがわかる
- CML vs SML
    - CML capital market line
        optimizing a portfolio
        $$
        \mathbb E[R_P] = r_f + \sigma_P \left(\frac{\mathbb E[R_M] - r_f}{\sigma_M}\right)
        $$
    - SML security market line
        evaluating an asset
        $$
        \mathbb E[R_i] = r_f + \beta_i (\mathbb E[R_M] - r_f)
        $$
    |  | CML | SML |
    | --- | --- | --- |
    | purpose  | optimizing a portfolio | evaluating an asset |
    | above the line | super-efficient(not exist) | undervalue  |
    | vertical axis  | exp of the portfolio | exp of the asset |
    | under the line | inefficient | overvalue |
    | horizontal axis | total risk(sigma) | systematic risk(beta) |
    | meaning | the most efficient portfolio | the value of market |
- market risk premium
    $$
    \mathbb E[R_M] - r_f
    $$
- risk premium
    rはPを用いて次のように変形できる
    $$
    r_i = (r_m - r_f)\beta + r_f, \beta = \frac{\sigma_{im}}{\sigma_m^2}\\
    r_i = \frac{P_{t+1}}{P_t} -1 \\
    P_t = \frac{P_{t+1}}{r_i + 1} = \frac{P_{t+1}}{(r_m - r_f)\beta + r_f+1} 
    $$
    ここで\betaは
    $$
    \beta=\frac{Cov(\frac{P_{t+1}}{P_t}-1, r_m)}{\sigma_m^2} = \frac{Cov(P_{t+1}, r_m)}{P_t\sigma_m^2}
    $$
    よって
    $$
    P_t = \frac{P_{t+1}}{(r_m - r_f) \frac{Cov(P_{t+1}, r_m)}{P_t\sigma_m^2} + r_f+1}\\
    (r_m - r_f) \frac{Cov(P_{t+1}, r_m)}{\sigma_m^2} + P_t(r_f+1)= P_{t+1} \\
    P_t(r_f +1) - P_{t+1} = -\frac{Cov(P_{t+1}, r_m)}{\sigma_m^2}
    $$
- trainer measure
    $$
    \frac{r_a - r_{f}}{\beta_a}
    $$
    $\beta_a$ : beta of CAPM
- mutual fund separation theorem