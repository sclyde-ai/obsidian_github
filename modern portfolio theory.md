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
    - covariance
        $$
        \sigma_{ij} = Cov(R_i, R_j) = \mathbb E[(R_i - \mu_i)(R_j - \mu_j)]
        $$
    - variance covariance matrix
        $$
        \Sigma = (\sigma_{ij})
        $$
- [[portfolio]]
	
    
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
