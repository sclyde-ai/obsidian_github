---
alias:
    ['級数', 'series']
---
- マクローリン級数 Maclaurin series
    - 一変数
        $$ \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}x^n $$
    - 多変数
        $$ \sum_{n=0}^\infty \frac{1}{n!} (x \frac{\partial}{\partial x} + y \frac{\partial}{\partial y})^n f(\vec0) $$
    - 有限マクローリン展開（剰余項 reminder）
- テイラー級数 Taylor series
    $$ \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n $$
    - 有限テイラー展開（剰余項 reminder）
        - Lagrange
            $$ \frac{f^{(n)}(c)}{n!}(x-a)^n $$
        - Cauchy
            $$ \frac{f^{(n)}(c)}{(n-1)!} (x-c)^{n-1}(x-a) $$
        - Peano
            $$ \frac{f^{(n)}(c)}{n!}(x-a)^n +o(|x-a|^n) $$
        - Integral
            $$ \frac{1}{(n-1)!}\int_a^x (x-t)^{n-1}f^{(n)}(t)dt $$
- 整級数/冪級数 power series
    $$ \sum_{n=0}^\infty a_n (x-c) $$
    - 漸近展開
    - 収束半径
    - 各点収束
    - 一様収束
- 正項級数
    $$ \sum_{n=0}^\infty a_n, a_k \geq 0, \forall n \in \mathbb N $$
- 交代級数
    $$ \sum_{n=0}^\infty (-1)^{n}< \infty $$
- 優級数
- 絶対収束性
    $$ \sum_{n=1}^\infty|a_n| < \infty $$
    - 絶対収束すれば収束
        $$ \left|\sum_{n=1}^\infty a_n \right| < \sum_{n=1}^\infty|a_n| < \infty $$
- convergence test 収束判定条件
    - ratio test/d’Alembert
        $$ r = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n}\right|
        $$
        0 \leq r \leq 1 : absolute convergence
        r > 1 : divergence
    - root test/cauchy
        $$ r = \limsup_{n \to \infty} \sqrt[n]{|a_n|} $$
        0 \leq r < 1 : absolute convergence
        r > 1 : divergence
    - direct comparision test
        $$ |a_n| \leq |b_n|, \sum_{n=0}^\infty |b_n|<\infty $$
    - integral test
    - abel
    - dirichlet
    - cauchy condensation test
    - raabe
    - gauss
    - berteand
- landauの記号