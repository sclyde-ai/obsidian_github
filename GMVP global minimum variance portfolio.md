---
alias:
  - GMVP
  - global minimum variance portfolio
parent: "[[mean-variance optimization]]"
---
$$
w_{GVMP} \in \mathbb R
$$
$$
\min_{w} \frac{1}{2} w^\top \Sigma w
$$
$$
\vec 1^\top w = 1
$$
分散が最小となるportfolio
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