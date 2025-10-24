
    $$
    \min_{w} \frac{1}{2} w^\top \Sigma w
    $$
    $$
    s.t. \ \mathbb 1^\top w = 1
    $$
    - GMVP weight vector
        $$
        w_{GMVP} = \frac{\Sigma^{-1}\rm 1}{\rm 1^\top \Sigma^{-1} \rm 1}
        $$
    - expected return
        $$
        \mu_{GMVP} = \frac{\mu^\top \Sigma^{-1}\rm 1}{\rm 1^\top \Sigma^{-1} \rm 1}
        $$
    - variance
        $$
        \sigma^2_{GMVP} = \frac{1}{\rm 1^\top \Sigma^{-1} \rm 1}
        $$
    - differentiate
        - $\nabla (w^\top \mu) = \mu$
        - $\nabla (w^\top \rm 1) = 1$
        - $\nabla (w^\top \Sigma w) = 2 \Sigma w$