the partial differential with respect to the random variable
the sensitivity of the price to changes in the stochastic variable
- main
    - delta (stock)
        $$
        \Delta_V =\frac{\partial V}{\partial S}
        $$
        stock price
        - call
            $$
            \Delta_C =\frac{\partial C}{\partial S} = N(d_1)
            $$
        - put
    - gamma (change of stock)
        stock price^2
        $$
        \Gamma = \frac{\partial \Delta}{\partial S} = \frac{\partial^2 V}{\partial S^2}
        $$
        - call & put
            $$
            \frac{N'(d_1)}{S\sigma\sqrt{T}}
            $$
        - call
            $$
            \Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{N'(d_1)}{S \sigma \sqrt{T -t}}
            $$
        - put
        - long gamma
            $$
            \Gamma > 0
            $$
        - short gamma
            $$
            \Gamma < 0
            $$
    - theta
        time
        - call
            $$
            \Theta = \frac{\partial C}{\partial t}
            $$
        - put
    - Vega
        volatility
        $$
        \nu = \frac{\partial V}{\partial \sigma}
        $$
    - rho
        interest rate
        $$
        \rho = \frac{\partial V}{\partial r}
        $$
- minor
    - lambda
        $$
        \frac{\partial V/V}{\partial S/S}
        $$
    - Vanna
        $$
        \frac{\partial \Delta}{\partial \sigma} = \frac{\partial^2 V}{\partial S \partial \sigma}
        $$
    - charm
        $$
        \frac{\partial \Delta }{\partial t} = - \frac{\partial^2 V}{\partial S \partial t}
        $$
    - Vomma
        $$
        \frac{\partial \nu}{\partial \sigma} = \frac{\partial^2 V}{\partial \sigma^2}
        $$
- normal distribution
    $$
    N(x) = \frac{1}{\sqrt {2\pi}} \int_{-\infin}^x e^{-\frac{y^2}{2}}dy
    $$
    $$
    N'(d_1)= \frac{1}{\sqrt {2\pi}} e^{-\frac{x^2}{2}}
    $$
- hedge by greeks
    - delta hedging/delta neutral
        dynamic rebalance 
        - call
            - portfolio
                $$
                \Pi = -C + \Delta_C S
                $$
            - sell
            - buy
        - put
    - gamma trading
        $$
        \Delta _{new} = \Delta_{old} + \Gamma \Delta S
        $$
        - long gamma
            $$
            \Gamma >0
            $$
            payoff
        - short gamma
            $$
            \Gamma < 0
            $$
            premium
        - gamma scalping
    - cross gamma