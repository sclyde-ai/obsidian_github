---
alias:
    ['modern portfolio theory']
---
- 資産 assets
    - 資産 assets
        $$
        N = \{1, 2, ..., n\}
        $$
    - 収益 return
        random variable
        $$
        \{R_i\}_{i \in N}
        $$
    - 期待収益 expected return
        $$
        \mu_i = \mathbb E[R_i]
        $$
        $$
        \mu = (\mu_1, \mu_2,...,\mu_n)^\top
        $$
    - 分散 variance
        $$
        \sigma_i^2 = Var(R_i) = \mathbb E[(R_i - \mu_i)^2]
        $$
    - 共分散 covariance
        $$
        \sigma_{ij} = Cov(R_i, R_j) = \mathbb E[(R_i - \mu_i)(R_j - \mu_j)]
        $$
    - 分散共分散行列 variance covariance matrix
        $$
        \Sigma = (\sigma_{ij})
        $$
- [[portfolio]]
	- weight
	    $$
	    w = (w_1, w_2, ...,w_n)^\top
	    $$
	    $$
	    \sum_{i=1}^n w_i = 1
	    $$
	- expected return
	    $$
	    \mu_p = \mathbb E[R_w] 
	    = \mathbb E[\sum_{i=1}^n w_i R_i] 
	    = \sum_{i=1}^n w_i \mathbb E[R_i] 
	    = \sum_{i=1}^n w_i \mathbb \mu_i
	    $$
	- variance
	    $$
	    \sigma_p^2 = w^\top \Sigma w
	    $$

[[mean-variance optimization]]
[[CAPM capital asset pricing model]]

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
