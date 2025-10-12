- variable
    - P principal 元本
    - r interest rate 利率
    - V_t deposit balance
- period 期間
    - annually
    - semi-annually
    - quarterly
    - monthly
    - daily
- interest & interest rate 金利と利率
    | interest | 金利 | 実際に受け取れる金額 |
    | --- | --- | --- |
    | interest rate | 利率 | もらえる割合 |
- simple interest 単利
- compound interest 複利
    - preposition 2.10
        m < k
        $$
        (1+\frac{r}{m})^{tm} < (1+\frac{r}{k})^{tk}
        $$
        - proof
            $$
            (1+\frac{r}{m})^m < (1+\frac{r}{k})^k
            $$
            $$
            (1+\frac{r}{m})^m = \sum_{i=0}^m \frac{m!}{i!(m-i)!}(\frac{r}{m})^i \\
            = 1 + r + \frac{1 - \frac{1}{m}}{2!}r^2 + ...+ \frac{(1-\frac{1}{m})\times ...\times(1-\frac{m-1}{m})}{m!}r^m \\
            \leq 1 + r + \frac{1 - \frac{1}{k}}{2!}r^2 + ...+ \frac{(1-\frac{1}{k})\times ...\times(1-\frac{m-1}{k})}{k!}r^k \\
            = (1+\frac{r}{k})^k
            $$
    - continuous compound interest
        $$
        \lim_{m \to \infin} (1+\frac{r}{m})^{tm}P = e^{rt}P
        $$
        - preposition 2.16
            $$
            V_t^c = e^{rt} P \\
            V_t^m = (1+\frac{r}{m})^{tm} P \\
            \Rightarrow \forall m \in \N, V_t^c > V_t^m
            $$
            - proof
                $$
                e^r > (1+\frac{r}{m})^m
                $$
- discount factor 割引率
    $$
    DF(s, t) := \frac{V_s}{V_t}
    $$
- growth factor 成長率
    $$
    \frac{1}{DF(s, t)}
    $$
- return rate
    $$
    K(s, t) := \frac{V_t - V_s}{V_s} 
    $$
- log return rate
    $$
    k(s, t) := \ln \frac{V_t}{V_s}
    $$
    - preposition 2.18
        $$
        k(s, t) + k(t, u) = k(s, u)
        $$
- 利率は暗黙に年率換算
- 例 example
    - unit
        - bps/basis points
            0.0001
            interest rate
    - type
        - fixed/pegged interest rate
            - overnight rate
        - floating interest rate
            - spot rate
            - RFR risk free rate
        - drift/stochastic drift
            the change of the average value of a stochastic process
            - drift rate
                the rate of a stochastic drift
    - interbank
        - LIBOR London InterBank Offered Rate
        - TIBOR Tokyo InterBank Offered Rate
    - overnight
        - SOFR secured overnight financing rate
            FRB of new york
            - link
                [Statement Requesting Public Comment on a Proposed Publication of SOFR Averages and a SOFR Index - FEDERAL RESERVE BANK of NEW YORK](https://www.newyorkfed.org/markets/opolicy/operating_policy_191104)
        - SONIA sterling overnight index average
            BoE
    - collateral
        - TGCR Tri-Party General Collateral Rate
            FRB of new york
        - BGCR Broad General Collateral Rate
            FRB of new york
    - ESTR euro short term rate
        ECB