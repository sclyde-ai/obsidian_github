---
alias:
    ['fractional Brownian motion', '非整数連続酔歩運動']
---
- 定義 def
    - 初期値0
        $$
        B(0) = 0 
        $$
    - 期待値0
        $$
        \mathbb E[B(t)] = 0
        $$
    - 自己相関
        $$
        Cov(B(t), B(t +\tau)) = \frac{1}{2}(t^{2H} + (t+\tau)^{2H}-\tau^{2H})
        $$
    - Hurst parameter
        $$
        0< H<1
        $$
- 定常増分性
    $$
    B(t+\tau) -B(t) \sim B(\tau)
    $$
- 自己相似性
    $$
    B(at) = a^H B(t)
    $$
- 長期依存性
    $$
    \sum_{k=1}^\infin Cov(X_1, X_{1+k}) = \infin \\
    X_i = B(i) - B(i-1)
    $$