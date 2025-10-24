- setting
    - 資産 assets
        $$
        N = \{1, 2, ..., n\}
        $$
    - 収益 return
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
        \mathbb 1 = (1, 1, ...,1)^\top
        $$
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
