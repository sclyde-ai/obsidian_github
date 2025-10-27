---
alias:
    ['金融市場', 'financial market']
---
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
        \sigma^2_p = \sum^n_{i = 1} \sum^n_{j = 1} w_i w_j Cov(R_i, R_j) = $$ 
 $$ 
        \begin{pmatrix}
        w_1, \dots , w_n
        \end{pmatrix}
        \begin{pmatrix} 
          Var(R_1) & \dots  & Cov(R_1, R_n) $$ 
 $$
          \vdots & \ddots & \vdots $$ 
 $$
          Cov(R_n, R_1) & \dots  & Var(R_n)
        \end{pmatrix} 
        \begin{pmatrix}
        w_1 $$ 
 $$ \vdots $$ 
 $$ w_n
        \end{pmatrix}
        $$ 
 $$
        = w^t \Sigma w 
        $$
    - return of portfolio
        $$
        r_p = \sum^n_{i=1}w_i r_i = w^t r
        $$