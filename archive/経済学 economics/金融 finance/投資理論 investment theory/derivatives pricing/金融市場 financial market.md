---
alias:
    ['金融市場', 'financial market']
---
- 株価 stock
    $$
    S_t 
    $$
    - 無作為性 randomness
        Sは確率変数
    - 正値性 positive
        $$
        S_t > 0
        $$
- 安全資産 safety asset
    $$
    A_t
    $$
    - 正値性 positive
        $$
        A_t > 0
        $$
- 金融派生商品 derivative
    $$
    H_t
    $$
    - 支払能力 solvency
        $$
        V_t \geq 0
        $$
- portfolio
    $$
    V_t = x_t S_t + y_t A_t
    $$
    - 分割性 divisibility
        完備性
        $$
        x, y \in \R
        $$
    - 流動性 liquidity
        無限を含む
        $$
        x, y \in \R \cap \{\infin\}
        $$
    - 空売り可能 short selling
        負値をとる
        $$
        x, y < 0
        $$
    - 許容可能 admissible
        - 自己資金調達 self-financing
            $$
            dV_t = x_t dS_t + y_t A_t
            $$
        - 非負性 non-negative
            $$
            V_t \geq 0
            $$
