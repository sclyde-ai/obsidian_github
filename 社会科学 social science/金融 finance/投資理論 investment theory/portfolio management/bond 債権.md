- ZCB zero coupon bond
    - 満期に額面が
    - 一度だけ
    支払われる債権
    - component 構成要素
        - F face value 額面
        - T maturity 満期
        - r implied rate
- CB coupon bond 利付債
    - 満期日に額面と
    - 一定期間ごとにcouponが
    支払われる債権
    - component 構成要素
        - F face value 額面
        - T maturity 満期
        - r implied rate
        - C coupon
        - $r_c$ coupon rate
    - dirty price
    - accrued interest 経過利息
    - clean price
        dirty price - accrued interest
    - preposition 2.27 (hard)
        $$
        r = r_c \Leftrightarrow F = V_0
        $$
        - proof
            - \Rightarrow
                $$
                \sum_{n = 1}^T \frac{r_c F}{(1+r)^n} + \frac{F}{(1+r)^T} = F
                $$
                - T = 1
                    $$
                    \frac{r_c F}{1+r} + \frac{F}{1+r} \\= \frac{1+r_c}{1+r} F \\
                    = \frac{1+r}{1+r} F \\
                    = F
                    $$
                - T= k
                    T=kで成立すると仮定
                    $$
                    \sum_{n = 1}^{k+1} \frac{r_c F}{(1+r)^n} + \frac{F}{(1+r)^{k+1}} \\ =
                    \sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{r_cF}{(1+r)^{k+1}} + \frac{F}{(1+r)^{k+1}}
                    \\ = 
                    \sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{(1+r_c)F}{(1+r)^{k+1}}
                    \\ = 
                    \sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{(1+r)F}{(1+r)^{k+1}}
                    \\ = 
                    \sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{F}{(1+r)^k}
                    \\ = F
                    $$
            - \Leftarrow
                $$
                F = \sum_{n=1}^{T-1} \frac{r_c F}{(1+r)^n} + \frac{(1+r_c)F}{(1+r)^T} \\
                (1+r)^T = \sum_{n=1}^{T-1} r_c(1+r)^{T-n} + (1+r_c) \\
                x = 1+r \\
                x^T - \sum_{n=1}^{T-1} r_cx^{T-n} -(1+r_c) = 0 \\
                \sum_{n=1}^{T-1} r_cx^{T-n}
                $$
    - par
- unit bond 単位債
    F = 1のZCB
    割引率として機能する
    $$
    B_t^T = B(t, T) = \frac{1}{(1+r)^{T-t}}\\
    B_t^T = B(t, T) = \frac{1}{(1+\frac{r}{m})^{m(T-t)}}\\
    B_t^T = B(t, T) = e^{-r(T-t)}
    $$
    $$
    B_n^N (\omega) = B_n^N(s_n) \\
    B_n^N (\omega) = 1, \forall \omega \in \Omega \\
    B_n^N(s_n u) = B_n^N (s_n d)
    $$
- MMA money market account
    銀行預金
    安全資産として機能する
    $$
    A(t) = A(0)e^{rt}
    $$
- duration
    - PV present value 現在価値
        - PV
            $$
            PV = \sum_{i=0}^n PV_{t_i}
            $$
        - consol/permanent annuity
            $$
            P = \sum_{k=1}^\infin \frac{A}{(1+r)^k} = \frac{A}{r}
            $$
            A : payment every year
            r : rate
            P : present value
        - annuity
            $$
            P = \sum_{k=1}^n \frac{A}{(1+r)^k} = \frac{A}{r}\left(1-\frac{1}{(1+r)^n}\right) 
            $$
            A : payment every year
            r : rate
            P : present value
        - coupon bond
            $$
            P = \frac{F}{(1+\frac{\lambda}{m})^n} + \sum_{k=1}^n \frac{\frac{C}{m}}{(1+\frac{\lambda}{m})^k} = \frac{F}{(1+\frac{\lambda}{m})^n} + \frac{C}{\lambda}\left(1-\frac{1}{(1+\frac{\lambda}{m})^n}\right)
            $$
            P : bond price
            F : face value
            C : coupon per year
            \lambda :YTM  yield to maturity
            m : the number of payment per year
            - use YTM instead of rate in bond
    a measure of the sensitivity of the price of a bond
    $$
    D = -\frac{1}{PV}\frac{d PV}{dy} 
    $$
    - Macaulay duration
        $$
        D = \frac{\sum_{k=1}^n \frac{k}{m} \frac{C_k}{(1+\frac{y}{m})^{k}}}{\sum_{k=1}^n \frac{C_k}{(1+\frac{y}{m})^k}}
        $$
        - parameters
            $C_k$ : coupon of k
            m : the number of payment per year
            n : maturity
            y : yield
    - Macaulay duration (cross form solution)
        $$
        D = \frac{1+y}{my}-\frac{1+y+n(c-y)}{mc[(1+y)^n-1]+my}
        $$
        - parameters
            c : coupon rate
            y : yield
            m : the number of payment per year
            n : maturity
    - modified duration
        the percentage change in a bond’s price for a 1% change in interest rates
        $$
        D_M = \frac{D}{1+\frac{y}{m}}
        $$
        - parameters
            m : the number of payment per year
            y : yield to maturity
    - convexity
        $$
        C = \frac{1}{PV} \frac{d^2PV}{dr^2}
        $$
    - immunization
        minimize the change of portfolio value per the change of rate
        $$
        \Delta P \approx -D_MP\Delta \lambda+\frac{P*C}{2}(\Delta \lambda)^2
        $$
    - BPV basis point value
- 株式 vs ZCB
    |  | 株式・FX | ZCB(unit bond) |
    | --- | --- | --- |
    | 資産数 | 1資産で完結 | 本質的に多資産 |
    | 現時点の情報 | 単一価格 | 複数価格、満期ごとに別資産 |
    | 価格の上限 | なし | 1 |
    | 価格の random  | 恒久的 | 満期で価格確定 |
    | 資産間の相関 | 高い相関は稀 | 近い満期のZCBは高い正相関 |