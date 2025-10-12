- what is mathematical finance?
    - quantitively measure the value of a derivative
    - predict the movement of a stock price
    - hedge the risk of portfolio
- 金融市場 financial market
    - 金融工学 financial engineering
        $$
        N = \{1, ..., n\}
        $$
        - return 利益
            $$
            R = (R_1, ..., R_n)
            $$
        - risk 不確実性
            $$
            \sigma = (\sigma_1, ..., \sigma_n)
            $$
        - portfolio
            $$
            w = (w_1, ..., w_n)
            $$
            - variance of portfolio
                $$
                \sigma^2_p = \sum^n_{i = 1} \sum^n_{j = 1} w_i w_j Cov(R_i, R_j) = \\ 
                \begin{pmatrix}
                w_1, \dots , w_n
                \end{pmatrix}
                \begin{pmatrix} 
                  Var(R_1) & \dots  & Cov(R_1, R_n) \\
                  \vdots & \ddots & \vdots \\
                  Cov(R_n, R_1) & \dots  & Var(R_n)
                \end{pmatrix} 
                \begin{pmatrix}
                w_1 \\ \vdots \\ w_n
                \end{pmatrix}
                \\
                = w^t \Sigma w 
                $$
            - return of portfolio
                $$
                r_p = \sum^n_{i=1}w_i r_i = w^t r
                $$
    - FTAP fundamental theorem of asset pricing 資産価格付けの基本定理
        - first FTAP 資産価格付けの第一基本定理
            裁定機会の非存在とリスク中立確率の存在は必要十分条件
            - n=2 金融資産2つ
                - 利益 gain/payoff
                    $$
                    r_i = \\
                    \left\{
                    \begin{matrix}
                    r_i(u) & X=u \\
                    r_i(d) & X=d
                    \end{matrix}
                    \right.
                    $$
                    $$
                    r(u) = (r_1(u), r_2(u)) \\
                    r(d) = (r_1(d), r_2(d))
                    $$
                    $$
                    r = (r_1, r_2) = (r(u), r(d))^\top \\ =
                    \begin{pmatrix}
                    r_1(u) & r_2(u) \\
                    r_1(d) & r_2(d)
                    \end{pmatrix}
                    $$
                - 出来高 volume
                    $$
                    x = (x_1, x_2) \in \R^2
                    $$
                $$
                R = r \cdot x^\top = \\
                \begin{pmatrix}
                r_1(u) & r_2(u) \\
                r_1(d) & r_2(d)
                \end{pmatrix}
                \begin{pmatrix}
                x_1 \\
                x_2
                \end{pmatrix}
                \\
                \begin{pmatrix}
                x_1 r_1(u) + x_2 r_2(u) \\
                x_1 r_1(d) + x_2 r_2(d)
                \end{pmatrix} 
                $$
                $$
                $$
                - risk neutral probability
                    $$
                    p =(p_u, p_d) \in \R^2 \\
                    p_u + q_d =1
                    $$
                    $$
                    p \cdot r = \\ 
                    (p_u r_1(u) + p_dr_1(d), \\
                    p_u r_2(u) + p_d r_2(d)) \\
                    = (0,0)
                    $$
                - 裁定 sure win strategy
                    $$
                    R > \vec 0 \lor R < \vec 0
                    $$
        - second FTAP 資産価格付けの第二基本定理
            金融市場完備性とリスク中立確率の一意性は必要十分条件
    - risk-neutral probability measure リスク中立確率測度
        martingaleとなるような確率測度
        - 確率空間 probability space $(\Omega, \mathcal{F}, \mathbb P)$
        - 確率測度 probability measure $\tilde{\mathbb P}$
        - 確率過程 stochastic process X
        - $\mathbb P = \tilde{\mathbb P}$ is equivalent
        - the discounted stock price is a martingale under $\tilde{\mathbb P}$
        then, $\tilde{\mathbb P}$ is risk-neutral probability measure
    - 金融市場完備性 completeness
        一次独立な収益・損失をもたらす市場の金融資産の数が将来の状態数と等しい
    - 効率的市場仮説 efficient market hypothesis
        情報は即座に市場全体に浸透する
        投資家の反応が正規分布に従う
        - weak-form efficiency
            過去の価格のhistorical dataを全て反映 
        - semi-strong-form efficiency
            会計情報や株式分割情報の公開情報も反映
        - strong-form efficiency
            insider情報や有料情報などの非公開情報も反映
        - Proof That Properly Anticipated Prices Fluctuate Randomly (実証研究)
            市場が効率的であれば価格は酔歩運動に従う
            [investmenttheory.org](https://investmenttheory.org/uploads/3/4/8/2/34825752/paulsamuelson-proof.pdf)
        - Grossman-Stiglitz paradox
            - original article
                [https://www.aeaweb.org/aer/top20/70.3.393-408.pdf](https://www.aeaweb.org/aer/top20/70.3.393-408.pdf)
            - the model
                R : the return of a safe asset
                u : the return of a risky asset 
                $$
                u = \theta + \epsilon
                $$
                \theta : random variable observable at a cost c
                \epsilon : random variable unobservable
                x : the supply of the risky assets
                \lambda : the percentage of informed traders
                 P : price
                $$
                P_\lambda (\theta, x)
                $$
            - conjectures
                1. the more individuals are informed, the more informative is the price system
                2. the more individuals are informed, the lower the ratio of expected utility of the informed to the uninformed
                3. the higher the cost of information, the smaller will be the equilibrium percentage of individuals who are informed 
                4. If the quality of the informed trader's information increases, the more their demands will vary with their information and thus the more prices will vary with \theta
                5. The greater the magnitude of noise, the less informative will the price system be
                6. In the limit, when there is no noise, prices convey all information, and there is no incentive to purchase information.
                7. markets will be thinner under those conditions in which the percentage of individuals who are informed (X) is either near zero or near unity.
            - the securities
                - risk-less asset $M_i$
                - risky asset $X_i$
                $$
                W_{0i} = M_i + PX_i \\
                W_{1i} = RM_i + uX_i
                $$
            - Individual’s utility Maximization
                - assumption
                    all individuals have the same utility function
                $$
                V_i(W_{1i}) = V(W_{1i}) = -e^{-aW_{1i}}, a>0
                $$
                a : the coefficient of absolute risk aversion 
                - informed
                    $$
                    X_I = \frac{\theta - RP}{a \sigma^2_{\epsilon}}
                    $$
                    - proof
                        - \theta, \epsilon : multivariate normal distribution
                            $$
                            \mathbb E[\epsilon] = 0 \\
                            \mathbb E[\theta \epsilon] = 0 \\
                            Var(u^*|\theta) = Var(\epsilon^*) =\sigma^2_\epsilon > 0
                            $$
                        $$
                        \mathbb E[V(W_{1i})| \theta] = -\exp \left((-a)\mathbb E[W_{1i}|\theta] + \frac{(-a)^2}{2}Var[W_{1i}|\theta]\right)
                        $$
                        - expectation & variance
                            $$
                            W_{1i} = R(W_{0i} - PX_i) + uX_i \\
                            $$
                            $$
                            \mathbb E[W_{1i}|\theta] = RW_{0i} +X_I(-RP + \mathbb E[u|\theta]) \\
                            = RW_{0i} +X_I(-RP + \theta) 
                            $$
                            $$
                            Var[W_{1i}|\theta] = X_I^2 \sigma_\epsilon^2
                            $$
                        $$
                        = - \exp \left(-a[RW_{0i} + (\theta - RP)X_I - \frac{a}{2} \sigma_\epsilon^2 X_I^2] \right)
                        $$
                        maximize it with respect to X
                        $$
                        \frac{d \mathbb E[V(W_{1i})| \theta]}{d X_I} = 0 \\
                        (\theta - RP- a \sigma^2_{\epsilon}X_I) \mathbb E[V(W_{1i})| \theta] = 0 \\
                        X_I = \frac{\theta - RP}{a \sigma^2_{\epsilon}}
                        $$
                - uninformed
                    $$
                    X_U = \frac{\mathbb E[u^* | P^*(\theta,x) = P] - RP}{a Var E[u^* | P^*(\theta,x) = P]}
                    $$
            - demand and supply equibalium
            - question
                - budget constraint vs wealth
            - my interpretation
                金融資産の価格に全ての市場参加者の私的情報が反映される
                - proof of preposition
                    A 効率的市場仮説(全ての情報が市場に反映される)
                    B 情報収集に利益が存在する
                    C 情報収集する人が存在する
                    - Aを仮定
                        $$
                        A \Rightarrow \lnot B \\
                        \lnot B \Rightarrow \lnot C \\
                        \lnot C  \Rightarrow \lnot A 
                        $$
                        $$
                        A \Rightarrow \lnot A
                        $$
                        矛盾
                    - ¬Aを仮定
                        $$
                        \lnot A \Rightarrow B \\
                        B \Rightarrow C \\
                        C \Rightarrow A
                        $$
                        $$
                        \lnot A \Rightarrow A
                        $$
                        矛盾
        - 結合仮説問題 joint hypothesis problem
            市場効率性の（証明や反証のような十分な）検証を絶対的に不可能とする説
    - 一物一価の法則/無差別の法則 law of one price
        完全競争市場において、同じ商品は同じ価格で取引される
        - 仮定 assumption
            - 完全競争市場
            - 無差別性
                商品が完全に等しい
            - 為替の無裁定
                為替レート価格差が存在しない(無裁定)
        - バラッサ・サミュエルソン効果 Balassa–Samuelson effect
            一物一価は完全には成立しない
            貿易財部門の生産性上昇率の高い国では、一般物価水準が外国と比べて上昇すると同時に、実質為替相場が増価する効果を意味する。
            - 導出
                1. 貿易財部門の生産性が上昇する
                2. 貿易財価格は所与であるため、生産性の上昇は貿易財部門の賃金を上昇させる
                3. 非貿易財部門から貿易財部門への労働移動圧力が生じる
                4. 非貿易財部門においても賃金が上昇する
                5. 非貿易財部門においては生産性が上昇していないため、賃金の上昇分、非貿易財価格が上昇する
                6. 当該国では一般物価水準が上昇することで、実質為替相場が増価する
    - 条件 condition
        - 負の株価は存在しない
        - 経済活動は和ではなく積である
    - 仮定 assumption
        - 無裁定
        - 取引費用なし
        - 税金なし
        - 株式は無限に分割可能
        - 空売りは制限なし
        - 貸付・借入は金利付きで自由にできる
        - 金利は既知かつ一定
        - 安全資産が存在する
- 金融工学 financial engineering
    - bond 債権
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
    - yield curve
        - yield(zero coupon bond)
            $$
            y_n^N = -\frac{1}{N-n}\log(B_n^N)
            $$
        - yield(coupon bond)
            $$
            P_N = \sum_{m=1}^M B_0^{m} r_c F + B_0^N F
            $$
        - spot rate
            yield at the present time
            $$
            B_0^N = \exp(-y_0^N N)
            $$
            $$
            y_0^N = -\frac{1}{N}\log(B_0^N)
            $$
        - bootstrapping
            B(0, 1) → B(0, 2) → …
            と順番に求める方法
            - prameters
                $F$ : face value
                $r_c$ : coupon rate
                - time series to take coupons
                    $$
                    \{n_m\}_{m \in \{1, 2, ..., M\}}
                    $$
        - forward rate
            $$
            F_k^{n, N}(\omega) = \frac{\log B_k^{N}(\omega) - \log B_n^N(\omega)}{N-n}
            $$
        - momentary forward rate
            $$
            f_k^N(\omega) = F_{k}^{n, n+1}(\omega)
            $$
        - short rate
            $$
            r_n(\omega) = f_n^n (\omega)
            $$
        - how to make yield curve
            - parametric model
                - nelson-Siegel
                    $$
                    f(T) = \beta_0 + \beta_1 e^{-\frac{T}{\tau}} + \beta_2 \frac{T}{\tau}e^{-\frac{T}{\tau}}
                    $$
                - Svensson
                    $$
                    f(T) = \beta_0 + \beta_1 e^{-\frac{T}{\tau_1}} + \beta_2 \frac{T}{\tau_1}e^{-\frac{T}{\tau_1}} + \beta_2 \frac{T}{\tau_2}e^{-\frac{T}{\tau_2}}
                    $$
            - bootstrapping + interpolation
                - pillar
                    カーブを描く為の基準となる期間（時点）
                - bootstrapping
                    $$
                    PV_n - [\sum CF_n(T_i) \times DF_n(T_i)]
                    $$
                    $$
                    \begin{pmatrix}
                    PV_1 & -CF_1(T_1) & 0 & 0 & \dots & 0 \\
                    PV_2 & -CF_2(T_1) & -CF_2(T_2) & 0 & \dots & 0 \\
                    PV_3 & -CF_3(T_1) & -CF_3(T_2) &  -CF_3(T_3) & \dots & 0 \\
                    \vdots & \vdots & \vdots & \ddots &\vdots \\
                    PV_n & -CF_n(T_1) & -CF_n(T_2) &  -CF_3(T_3) & \dots & -CF_n(T_m)\\
                    \end{pmatrix}
                    \begin{pmatrix}
                    1 \\ DF(T_1) \\ DF(T_2) \\ \vdots \\ DF(T_n)
                    \end{pmatrix}
                    = 
                    \begin{pmatrix}
                     0 \\ 0 \\ 0 \\ \vdots \\ 0
                    \end{pmatrix}
                    $$
                - interpolation 補間
                    主にdiscount factorとzero coupon rate
                    - 線形補間
                    - 対数線形補間
                    - spline補間
                    - tension spline
    - modern portfolio theory
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
- 
- バーゼル制御
- class
    - 企業ファイナンス
        - 決算短信が一番株価に影響を与える
        - 時価簿価比率 P/B ratio
            時価総額/自己資本比率
        - 負債自己資本比率 DE ratio