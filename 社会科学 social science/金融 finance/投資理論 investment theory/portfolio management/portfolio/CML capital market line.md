---
alias:
    ['CML', 'capital market line']
---
$$
\mathbb E[R_P] = r_f + \frac{\mathbb E[R_T] - r_f}{\sigma_T}\sigma_P
$$
- 証明 proof
    安全資産と市場portfolioの組のportfolioの収益率を考える
    $$
    r_p = (1-w)r_f+w r_m $$ 
 $$
    \sigma_p = \sqrt{Var(r_p)} = w  \sqrt{Var(r_m)} = w \sigma_m
    $$
    無リスク資産の期待収益と分散から$w$を消去すると
    $$
    r_p = r_f+ w(r_m-r_f) $$ 
 $$
    r_p = r_f+ \frac{\sigma_p}{\sigma_m}(r_m-r_f)
    $$