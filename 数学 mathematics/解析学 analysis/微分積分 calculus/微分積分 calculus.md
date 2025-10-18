- 定理 theorem
    
    
    
    
    
    
    


- 極値 limit
    - 変曲点
    - 一変数
    - 多変数
        - 臨界点/停留点
            $$ \forall i \in \{1, 2, ..., n\}, f_{x_i} (p_1, ... , p_n) = 0\\ $$
            - 極大
                - neighborhood U
                $f : A \to \R, A \subset \R^n$
                $$ \exist a \in A, \exist \delta \in \R, \forall x \in U(a, \delta), f(x) \leq f(a) $$
            - 極小
                - neighborhood U
                $f : A \to \R, A \subset \R^n$
                $$ \exist a \in A, \exist \delta \in \R, \forall x \in U(a, \delta), f(x) \geq f(a) $$
            - 鞍点
- 級数 series
    - マクローリン級数 Maclaurin series
        - 一変数
            $$ \sum_{n=0}^\infin \frac{f^{(n)}(0)}{n!}x^n $$
        - 多変数
            $$ \sum_{n=0}^\infin \frac{1}{n!} (x \frac{\partial}{\partial x} + y \frac{\partial}{\partial y})^n f(\vec0) $$
        - 有限マクローリン展開（剰余項 reminder）
    - テイラー級数 Taylor series
        $$ \sum_{n=0}^\infin \frac{f^{(n)}(a)}{n!}(x-a)^n $$
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
        $$ \sum_{n=0}^\infin a_n (x-c) $$
        - 漸近展開
        - 収束半径
        - 各点収束
        - 一様収束
    - 正項級数
        $$ \sum_{n=0}^\infin a_n, a_k \geq 0, \forall n \in \N $$
    - 交代級数
        $$ \sum_{n=0}^\infin (-1)^{n}< \infin $$
    - 優級数
    - 絶対収束性
        $$ \sum_{n=1}^\infin|a_n| < \infin $$
        - 絶対収束すれば収束
            $$ \left|\sum_{n=1}^\infin a_n \right| < \sum_{n=1}^\infin|a_n| < \infin $$
    - convergence test 収束判定条件
        - ratio test/d’Alembert
            $$ r = \lim_{n \to \infin} \left| \frac{a_{n+1}}{a_n}\right|
            $$
            0 \leq r \leq 1 : absolute convergence
            r > 1 : divergence
        - root test/cauchy
            $$ r = \limsup_{n \to \infin} \sqrt[n]{|a_n|} $$
            0 \leq r < 1 : absolute convergence
            r > 1 : divergence
        - direct comparision test
            $$ |a_n| \leq |b_n|, \sum_{n=0}^\infin |b_n|<\infin $$
        - integral test
        - abel
        - dirichlet
        - cauchy condensation test
        - raabe
        - gauss
        - berteand
    - landauの記号
- 積分 calculus
    - 定積分
    - 原始関数
    - 置換積分
    - 部分積分
        $$ (f(x) g(x))' = f'(x)g(x) + f(x)g'(x) \\ f(x)g(x) = \int f'(x)g(x) + \int f(x)g'(x) $$
    - 部分分数分解
    - 積分公式集
    - 広義積分
        $$ \int_a^{+\infin} f(x)dx = \lim_{c \to +\infin} \int_a^c f(x)dx $$
        - 収束判定条件1
        - 収束判定条件2
    - 三角置換積分
- Lagrange multiplier
    - C^1 級関数 f(x, y) g(x, y)
    - 条件1
        - 判別式 $D_f(a, b)$
        $$ g(x, y)=0 \Rightarrow D_f(a, b)>0 $$
    - 条件2
        $$ g_x(a, b)\ne 0 \land g_y(a, b) \ne 0 $$
    $$ \exist k \in \R, F_x(a, b, k) = F_y(a, b, k) = F_\lambda(a, b, k) = 0 \\ F(x, y, \lambda) = f(x, y) - \lambda g(x, y) $$
    - how to use
        制約条件gの下でのfの最大/最小化
        $$ \max / \min f(x, y)\ s.t.\ g(x, y) = 0 $$
- Laudau’s notation
    - big O
        $$ \exist M, \delta > 0, |x-a| < \delta \Rightarrow \\ |f(x)| \leq M |g(x)| \\
        $$
    - small o
        $$ \lim_{x \to a} \left|\frac{f(x)}{g(x)}\right| = 0 $$