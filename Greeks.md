the partial differential with respect to the random variable
the sensitivity of the price to changes in the stochastic variable
- main
    [[delta]]
    [[gamma]]
    [[theta]]
    [[Vega]]
    [[rho]]
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