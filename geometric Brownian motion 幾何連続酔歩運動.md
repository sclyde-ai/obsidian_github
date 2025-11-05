---
alias:
    ['geometric Brownian motion', '幾何連続酔歩運動']
---
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