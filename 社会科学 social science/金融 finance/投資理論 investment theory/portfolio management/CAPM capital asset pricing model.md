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