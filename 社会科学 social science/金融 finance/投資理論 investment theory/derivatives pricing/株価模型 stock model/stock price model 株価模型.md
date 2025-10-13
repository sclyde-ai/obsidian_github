
        
        - random walk 酔歩運動
            - 
            - 
        - Brownian motion 連続酔歩運動
            - Brownian motion 連続酔歩運動
                - probability space
                - def 定義
                    - initial condition 初期値
                        $$
                        W_0= 0
                        $$
                    - independent increment 独立増分
                        $$
                        \forall s_1,t_1,s_2,t_2 \in T, \\ 
                        s_1 \leq t_1 \leq s_2 \leq t_2 \Rightarrow \\ \mathbb P[X_{t_1}-X_{s_1} \cap X_{t_2}-X_{s_2}] = \mathbb P[X_{t_1}-X_{s_1}] \mathbb P[X_{t_2}-X_{s_2}]
                        $$
                        the increments are independent on each other 
                    - normal/gaussian increment 正規増分
                        $$
                        \forall s,t \in T, X_t - X_s \sim N(0, t-s)
                        $$
                        Each of these increments is normally distributed 
                    - alternative characterization of Brownian motion
                - increment 増分
                    $$
                    W_{t_1}-W_{t_0}\\
                    W_{t_2}-W_{t_1}\\ 
                    ..., W_{t_m}-W_{t_{m-1}} \\
                    t_0 < t_1 < ... < t_m
                    $$
                    is independent and normally distributed
                    - expectation
                        $$
                        \mathbb E[W_{t_{i+1}}-W_{t_i}] = 0 
                        $$
                    - variance
                        $$
                        Var[W_{t_{i+1}}-W_{t_i}] = t_{i+1}-t_i
                        $$
                - filtration
                    - information accumulates
                        $$
                        \forall s, t \in T, s < t \Rightarrow \mathcal F_s \subset \mathcal F_t
                        $$
                    - adaptivity
                        Brownian motion W_t at the time t is F_t-measurable
                        $$
                        \{\omega \in \Omega: W_t(\omega) \in B, \forall B \in \mathcal B(\R)\} \in \mathcal F(t)
                        $$
                    - independence future increments
                        the increment W_t - W_s is independent of F_t
                        $$
                        \forall F \in \mathcal F_t
                        $$
                        F and W_t - W_s are independent 
                - property 性質
                    - martingale
                        $$
                        \mathbb E[W_t|\mathcal F_s] = W_s, \forall s, t \in T
                        $$
                        almost surely
                        - proof
                            $$
                            \mathbb E[W_t|\mathcal F_s] \\ 
                            = \mathbb E[W_s + (W_t-W_s)|\mathcal F_s] \\ 
                            = \mathbb E[W_s| \mathcal F_s] + \mathbb E[(W_t-W_s)|\mathcal F_s] \\
                             =W_s + 0
                            $$
                    - Markov property
                        - Borel measurable func f, g
                        $$
                        \mathbb E[f(W_t)|\mathcal F_s] = g(W_t)
                        $$
                        - proof
                            $$
                            \mathbb E[f(W_t)|\mathcal F_s] =
                            \mathbb E[f(W_t - W_s) + W_s|\mathcal F_s] =
                            $$
                    - not differential
                        $$
                        W(t+h) - W(t) \sim N(0, h)
                        $$
                        $$
                        \frac{W(t+h)-W(t)}{h} = \frac{\sqrt h Z}{h} = \frac{Z}{\sqrt h}
                        $$
                    - fractal
                        - self-similarity
                            $$
                            W(ct) \stackrel{\mathrm{d}}{=} \sqrt c W(t)
                            $$
                        - holder continuity
                            $$
                            |W_t-W_s| \leq C|t-s|^\alpha
                            $$
                - moment 積率
                    - the moment-generating function
                    - expectation 期待値
                        $$
                        \mathbb E[X_t] = 0
                        $$
                        - proof
                            $$
                            X_t = X_t -X_0 \sim N(0, t-0) = N(0, t) \\ \Rightarrow \mathbb E[X_t] = 0
                            $$
                    - variance 分散
                        $$
                        \mathbb E[(X_t-\mu)^2] = t
                        $$
                        - proof
                            $$
                            X_t = X_t -X_0 \sim N(0, t-0) = N(0, t) \\ \Rightarrow \mathbb E[X_t^2] = t
                            $$
                    - covariance 共分散
                        $$
                        Cov(W_s, W_t) = \mathbb E[W_sW_t] = \min(s, t)
                        $$
                        - proof
                            $$
                            \mathbb E[W_sW_t] \\
                            = \mathbb E[W_s(W_s+W_t-W_s)] \\
                            = \mathbb E[W_s^2] + \mathbb [W_s(W_t-W_s)] \\ 
                            = s
                            $$
                        - covariance matrix
                            $$
                            \bm{\Sigma} = \mathbb{E}\left[\begin{pmatrix}(X_1 - \mathbb{E}[X_1])^2 & (X_1 - \mathbb{E}[X_1])(X_2 - \mathbb{E}[X_2]) & \cdots & (X_1 - \mathbb{E}[X_1])(X_n - \mathbb{E}[X_n]) \\(X_2 - \mathbb{E}[X_2])(X_1 - \mathbb{E}[X_1]) & (X_2 - \mathbb{E}[X_2])^2 & \cdots & (X_2 - \mathbb{E}[X_2])(X_n - \mathbb{E}[X_n]) \\\vdots & \vdots & \ddots & \vdots \\(X_n - \mathbb{E}[X_n])(X_1 - \mathbb{E}[X_1]) & (X_n - \mathbb{E}[X_n])(X_2 - \mathbb{E}[X_2]) & \cdots & (X_n - \mathbb{E}[X_n])^2\end{pmatrix}\right]
                            $$
                - quadratic variation
                    $$
                    [W, W](T) = T
                    $$
                    - proof
                        $$
                        Q_\Pi = \sum_{j=0}^{n-1}(W(t_{j+1}) - W(t_j))^2
                        $$
                        $$
                        \mathbb E[(W(t_{j+1})-W(t_j))^2] = Var [W(t_{j+1})-W(t_j)] = t_{j+1} - t_j
                        $$
                        $$
                        \mathbb E[Q_\Pi] = \sum_{j=0}^{n-1}\mathbb E[(W(t_{j+1})-W(t_j))^2] = \sum_{j=0}^{n-1} t_{j+1} - t_j = T
                        $$
                        $$
                        Var[]
                        $$
            - athematic Brownian motion 算術連続酔歩運動
                - SDE stochastic differential equations
                    $$
                    dS_t = \mu dt + \sigma dW_t
                    $$
            - geometric Brownian motion 幾何連続酔歩運動
                - SDE stochastic differential equations
                    $$
                    d S_t = \mu S_t dt + \sigma S_t d W_t
                    $$
                - solution
                    $$
                    S_t = S_0 \exp \left(\sigma W_t +\left(\mu-\frac{1}{2}\sigma^2\right)t\right)
                    $$
                    - how to derive
                        $$
                        dS_t = \mu S_t dt + \sigma S_t dW_t
                        $$
                        $$
                        \frac{d S_t}{S_t} = d\ln S_t = \mu dt + \sigma dW_t
                        $$
                        伊藤の公式‣
                        $$
                        dh(x, t) = \left(\frac{\partial h}{\partial t} + f \frac{\partial h}{\partial x} + \frac{1}{2}g^2 \frac{\partial^2 h}{\partial x^2} \right)dt + g \frac{\partial h}{\partial x}d\omega
                        $$
                        $$
                        x = S_t, h(S_t, t) = \ln S_t \\
                        \frac{\partial \ln S_t}{\partial S_t} = \frac{1}{S_t} \\
                        \frac{\partial^2 \ln S_t}{\partial S_t^2} = -\frac{1}{S_t^2} \\
                        \frac{\partial \ln S_t}{\partial t} = 0
                        $$
                        $$
                        d \ln S_t= \left(0 + \mu S_t\frac{1}{S_t} + \frac{1}{2}(\sigma S_t)^2 (-\frac{1}{S_t^2})\right)dt + \sigma S_t\frac{1}{S_t}d\omega \\
                        = \left(\mu - \frac{1}{2}\sigma^2\right)dt+\sigma d\omega
                        $$
                        $$
                        S_t = S_0 \exp \left(\left( \mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)
                        $$
                - assumption 仮定
                    - frictionless market
                        - no transaction cost and tax
                        - lend and borrow with risk-free interest rate
                    - perfect and complete market
                        - price taker
                        - infinite divisibility
                        - not limit short selling
                        - any payoff is replicable
                    - risk-free asset
                        risk-free asset exists 
                        interest rate is known and constant
                    - efficient market
                        no-arbitrage
                - option
                    - call
                        - SDE
                            $$
                            \frac{\partial C_t}{\partial t}+ rS_t \frac{\partial C_t}{\partial S_t}+\frac{1}{2}\sigma^2S_t^2 \frac{\partial^2 C_t}{\partial S_t^2} -rC_t=0
                            $$
                            - how to derive
                                - portfolio
                                    - 一物一価の法則
                                        $$
                                        C(t) = p(t)S(t) + q(t)B(t)
                                        $$
                                    - 自己資本充足
                                        $$
                                        dpS + dqB = 0
                                        $$
                                    一物一価の法則より
                                    $$
                                    C(t) = p(t)S(t) + q(t)B(t)
                                    $$
                                    全微分をすると
                                    $$
                                    dC = dpS + pdS + dpB + qdB 
                                    $$
                                    自己資本充足より
                                    $$
                                    dC = pdS + qdB \\
                                    = (paS + qrB)dt + p\sigma S d\omega
                                    $$
                                - 伊藤の公式
                                    $$
                                    dC = \left(\frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} \right)dt + \sigma S \frac{\partial C}{\partial S}d\omega
                                    $$
                                dtとdwの係数比較すると
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  = paS + qrB
                                $$
                                $$
                                \sigma S \frac{\partial C}{\partial S}
                                = p\sigma S
                                $$
                                第二式を変形すると
                                $$
                                \frac{\partial C}{\partial S} = p
                                $$
                                一物一価の法則より
                                $$
                                rC = rpS+rqB \\
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - paS = qrB = rC - rpS
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - \frac{\partial C}{\partial S}aS =rC - r\frac{\partial C}{\partial S}S
                                $$
                                $$
                                \frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  =rC
                                $$
                        - solution
                            $$
                            C_0 = \Phi (d_1)S_0 - \Phi (d_2)Ke^{-rt} \\
                            d_1 = \frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\
                            d_2 = \frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\ 
                            \Phi(d) = \frac{1}{2\pi} \int^d_{- \infin} e^{- \frac{x^2}{2}} dx
                            $$
                            - how to derive
                                $$
                                C_0 = e^{-rt}\mathbb E_\mathbb Q[\max(S_t-K, 0)] 
                                \\
                                = e^{-rt} \mathbb E_\mathbb Q[(S_t-K)\cdot1_{K\leq S_t}] 
                                \\
                                = 
                                e^{-rt} (\mathbb E_\mathbb Q[S_t\cdot 1_{K\leq S_t}] - \mathbb E_\mathbb Q[K\cdot 1_{K\leq S_t}])
                                $$
                                - $\mathbb E_\mathbb Q[S_t\cdot1_{K\leq S_t}]$
                                    - 測度変換をすると
                                        $$
                                        \frac{d\mathbb Q^S}{d\mathbb Q} = \frac{S_t}{S_0e^{rt}}
                                        $$
                                    $$
                                    = \mathbb E_\mathbb Q[S_0 e^{rt} \frac{d\mathbb Q^S}{d\mathbb Q}\cdot 1_{K \leq S_t}] \\
                                    = S_0 e^{rt}\mathbb E_\mathbb Q[\frac{d\mathbb Q^S}{d\mathbb Q}\cdot 1_{K \leq S_t}] 
                                    $$
                                    - 期待値の計算より
                                    $$
                                    = S_0 e^{rt}\mathbb E_{\mathbb Q^S}[1_{K \leq S_t}] \\
                                    = S_0 e^{rt} \mathbb Q^S(K \leq S_t) 
                                    $$
                                    - Girsanovの定理より
                                        $$
                                        W_t^{\mathbb Q^S} = W_t^\mathbb Q - \sigma t
                                        $$
                                    $$
                                    \ln S_t = \ln S_0 + \left(r- \frac{\sigma^2}{2}\right)t + \sigma W_t^\mathbb Q \\
                                    = \ln S_0 + \left(r + \frac{\sigma^2}{2}\right)t + \sigma W_t^{\mathbb Q^S}
                                    $$
                                    株価S_tは対数正規分布に従うので
                                    $$
                                    \ln S_t \sim N(\mu, \sigma^2t) \\
                                    \mu = \ln S_0 + \left(r+\frac{\sigma^2}{2}\right)t
                                    $$
                                    標準化すると
                                    $$
                                    \frac{\mu - \ln K}{\sigma\sqrt t} =  \frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}
                                    $$
                                    $$
                                    \mathbb Q^S(K \leq S_t) = \mathbb Q^S(\ln K \leq \ln S_t) = \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                    上記より
                                    $$
                                    \mathbb E_\mathbb Q[S_t\cdot1_{K\leq S_t}]
                                    = S_0 e^{rt} \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                - $\mathbb E_\mathbb Q[K\cdot 1_{K\leq S_t}]$
                                    $$
                                    = K \cdot \mathbb E_\mathbb Q[1_{K\leq S_t}]
                                    \\ = K\cdot \mathbb Q(K\leq S_t)
                                    $$
                                    株価S_tは対数正規分布に従うので
                                    $$
                                    \ln S_t \sim N(\mu, \sigma^2t) \\
                                    \mu = \ln S_0 + \left(r-\frac{\sigma^2}{2}\right)t
                                    $$
                                    標準化すると
                                    $$
                                    \frac{\mu - \ln K}{\sigma\sqrt t} =  \frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}
                                    $$
                                    $$
                                    \mathbb Q(K \leq S_t)
                                    \\ 
                                    = \mathbb Q(\ln K \leq \ln S_t) 
                                    \\ 
                                    = \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                    上記より
                                    $$
                                    \mathbb E_\mathbb Q[K\cdot 1_{K\leq S_t}] 
                                    = K \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                $$
                                C_0 = e^{-rt}(S_0 e^{rt} \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)- K \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right))
                                \\
                                =S_0 \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)- K e^{-rt} \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right))
                                $$
                    - put
                        - SDE
                            $$
                            \frac{\partial P_t}{\partial t}+ rS_t \frac{\partial P_t}{\partial S_t}+\frac{1}{2}\sigma^2S_t^2 \frac{\partial^2 P_t}{\partial S_t^2} -rP_t=0
                            $$
                            - how to derive
                                - portfolio
                                    - 一物一価の法則
                                        $$
                                        C(t) = p(t)S(t) + q(t)B(t)
                                        $$
                                    - 自己資本充足
                                        $$
                                        dpS + dqB = 0
                                        $$
                                    一物一価の法則より
                                    $$
                                    C(t) = p(t)S(t) + q(t)B(t)
                                    $$
                                    全微分をすると
                                    $$
                                    dC = dpS + pdS + dpB + qdB 
                                    $$
                                    自己資本充足より
                                    $$
                                    dC = pdS + qdB \\
                                    = (paS + qrB)dt + p\sigma S d\omega
                                    $$
                                - 伊藤の公式
                                    $$
                                    dC = \left(\frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} \right)dt + \sigma S \frac{\partial C}{\partial S}d\omega
                                    $$
                                dtとdwの係数比較すると
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  = paS + qrB
                                $$
                                $$
                                \sigma S \frac{\partial C}{\partial S}
                                = p\sigma S
                                $$
                                第二式を変形すると
                                $$
                                \frac{\partial C}{\partial S} = p
                                $$
                                一物一価の法則より
                                $$
                                rC = rpS+rqB \\
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - paS = qrB = rC - rpS
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - \frac{\partial C}{\partial S}aS =rC - r\frac{\partial C}{\partial S}S
                                $$
                                $$
                                \frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  =rC
                                $$
                        - solution
                            $$
                            P_t = \Phi (-d_2)Ke^{-rt}- \Phi (-d_1)S_0 \\
                            d_1 = \frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\
                            d_2 = \frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\ 
                            \Phi(d) = \frac{1}{2\pi} \int^d_{- \infin} e^{- \frac{x^2}{2}} dx
                            $$
                            - how to derive
                                $$
                                P_0 = D_t \mathbb E_\mathbb Q[\max(K-S_t, 0)] \\
                                = D_t \mathbb E_\mathbb Q[(K -S_t)\cdot1_{S_t\leq K}] \\
                                = D_t (\mathbb E_\mathbb Q[K\cdot 1_{S_t\leq K}] -\mathbb E_\mathbb Q[S_t\cdot1_{S_t\leq K}])
                                $$
                                - $\mathbb E_\mathbb Q[K\cdot 1_{S_t\leq K}]$
                                - $\mathbb E_\mathbb Q [S_t\cdot1_{S_t\leq K}]$
                    - 熱伝導方程式 heat equation
                        $$
                        \frac{\partial u}{\partial \tau} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2} \\
                        \tau = T-t \\
                        u = Ce^{r\tau} \\
                        x = \frac{y+(r-\frac{1}{2}\sigma^2)\tau}{\sigma}
                        $$
                        - how to derive
                - log return
                    $$
                    \log \frac{S_{t_{j+1}}}{S_{t_j}} = \sigma(W_{t_{j+1}}-W_{t_j}) +\left(a-\frac{1}{2}\sigma^2\right)(t_{j+1}-t_j)
                    $$
                - realized volatility
                    $$
                    \log \frac{S_{t_{j+1}}}{S_{t_j}} = \sigma(W_{t_{j+1}}-W_{t_j}) +\left(a-\frac{1}{2}\sigma^2\right)(t_{j+1}-t_j)
                    $$
                    $$
                    \sum_{j=0}^{m-1}\left(\log \frac{S_{t_{j+1}}}{S_{t_j}} \right)^2 
                    = \sigma^2 \sum_{j=0}^{m-1} (W_{t_{j+1}}-W_{t_j})^2 
                    + \sigma \left(a-\frac{1}{2}\sigma^2\right) \sum_{j=0}^{m-1} (W_{t_{j+1}}-W_{t_j}) (t_{j+1}-t_j)
                     + \left(a-\frac{1}{2}\sigma^2\right)^2 \sum_{j=0}^{m-1} (t_{j+1}-t_j)^2
                    \\ \xrightarrow{\| \Pi \| \to 0}
                    \sigma^2(T_2 - T_1)
                    $$
                - Jensen’s inequality
                    $$
                    \mathbb E[\ln S_t] \leq \ln \mathbb E[S_t]
                    $$
                    $$
                    \mathbb E[\ln S_t] = \ln S_0 +  \left( \mu - \frac{\sigma^2}{2}\right)t \\
                    \ln \mathbb E[S_t] = \ln S_0 + \mu t
                    $$
            - fractional Brownian motion 非整数連続酔歩運動
                - 定義 def
                    - 初期値0
                        $$
                        B(0) = 0 
                        $$
                    - 期待値0
                        $$
                        \mathbb E[B(t)] = 0
                        $$
                    - 自己相関
                        $$
                        Cov(B(t), B(t +\tau)) = \frac{1}{2}(t^{2H} + (t+\tau)^{2H}-\tau^{2H})
                        $$
                    - Hurst parameter
                        $$
                        0< H<1
                        $$
                - 定常増分性
                    $$
                    B(t+\tau) -B(t) \sim B(\tau)
                    $$
                - 自己相似性
                    $$
                    B(at) = a^H B(t)
                    $$
                - 長期依存性
                    $$
                    \sum_{k=1}^\infin Cov(X_1, X_{1+k}) = \infin \\
                    X_i = B(i) - B(i-1)
                    $$
            - CEV constant elasticity of variance model
                $$
                dS_t = \sigma S_t^\beta dW_t
                $$
            - jump diffusion model 跳躍拡散模型
                - merton
                    $$
                    dS_t = (\mu -\lambda \cdot k)S_t dt + \sigma S_t dW_t + S_t dJ_t
                    $$
                    - diffusion part 拡散項
                        $$
                        \sigma S_t dW_t
                        $$
                        - standard Wiener process
                    - jump part 跳躍項
                        $$
                        S_t d J_t
                        $$
                        - compound Poisson process
        - my model
            - 直近の上下動の回数に比例して上か下かの確率が変動するmodel
            - probability space
                - event space
                    $$
                    \Omega = \{H, T\}^N=\{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{1,2,...,N\}\}
                    $$
                - filtration
                    $$
                    \mathcal F_0 = \{\phi, \Omega\}\\
                    \mathcal F_2= \{\phi, H\{H, T\}^{N-1}, T\{H, T\}^{N-1}, \Omega\} \\
                    \mathcal F_1 = \{\phi, 
                    HT\{H, T\}^{N-2}, HT\{H, T\}^{N-2}, TH\{H, T\}^{N-2}, TT\{H, T\}^{N-2}, \Omega\}
                    \\ \vdots \\
                    \mathcal F_n =\{ \phi, 
                    \{\omega_1\omega_2...\omega_n\{H, T\}^{N-n}| w_i \in \{H, T\}, \forall i \in \{1,2,...,n\}\}, \Omega\}
                    $$
                    $$
                    \omega_n =\omega_1\omega_2...\omega_n = \omega_1\omega_2...\omega_n\{H, T\}^{N-n} = \{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{n+1,n+2,...,N\}\}
                    $$
                - probability measure
                    $$
                    P_n(\omega_n) =  p^{H_n}q^{T_n} \\
                    n = H_n + T_n
                    $$
            $$
            S_n(\omega_1\omega_2...\omega_n\{H, T\}^{N-n}) = S_0 u^{H_n}d^{T_n} \\
            n = H_n + T_n
            $$
            $$
            p = f(\omega_1\omega_2...\omega_n) \\
            q = f^{-1}(\omega_1\omega_2...\omega_n)\\
            p+q=1
            $$