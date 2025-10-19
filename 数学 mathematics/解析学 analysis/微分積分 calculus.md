- 定理 theorem
    - 中間値の定理
        閉区間 [a, b], 連続関数f
        $$ \forall k \in [f(a), f(b)], \exists c \in [a,b], f(c) = k $$
        - proof
            - 区間収縮法
                let me define the two sequence
                $$ a_1 = a, b_1 = b\\ f(\frac{a_n + b_n}{2}) \geq k\Rightarrow \\ \left\{ \begin{matrix} a_{n+1} = \frac{a_n + b_n}{2} \\ b_{n+1} = b_n \end{matrix} \right. \\ f(\frac{a_n + b_n}{2}) < k \Rightarrow \\ \left\{ \begin{matrix} a_{n+1} = a_n\\ b_{n+1} = \frac{a_n + b_n}{2} \end{matrix} \right. $$
                then, the following theorem holds
                - (1) $a_1 \leq a_2 \leq ... \leq a_n < b_n \leq ... \leq b_2 \leq b_1$
                - (2) $b_n - a_n = \frac{1}{2^n} (b - a)$
                    $$ b_n - a_n = \\ \left\{ \begin{matrix} b_{n-1}- \frac{a_{n-1}+ b_{n-1}}{2} = \frac{b_{n-1}- a_{n-1}}{2} & f(\frac{a_{n-1}+ b_{n-1}}{2}) \geq k \\ \frac{a_{n-1} + b_{n-1}}{2} - a_{n-1}= \frac{b_{n-1} - a_{n-1}}{2} & f(\frac{a_{n-1}+ b_{n-1}}{2}) < k \end{matrix} \right. \\ = \frac{b_{n-1}- a_{n-1}}{2} $$
                    let’s repeat it n times
                - (3) $f(a_n) \leq k < f(b_n)$
                Every bounded non-decreasing (or increasing) sequence converges
                here is the convergence of the two sequence
                $$ \lim_{n \to \infty} a_n = \alpha \\ \lim_{n \to \infty} b_n = \beta
                $$
                from the theorem (2)
                $$ \lim_{n \to \infty} b_n = \lim_{n \to \infty} (a_n + \frac{1}{2^{n-1}}(b-a)) \\ \lim_{n \to \infty} b_n = \lim_{n \to \infty} a_n + \lim_{n \to \infty }\frac{1}{2^{n-1}}(b-a) \\ \beta = \alpha + 0 \\ \beta = \alpha $$
                then $\beta = \alpha = c$
                $$ \lim_{n \to \infty} f(a_n) = \alpha = f(c) \\ \lim_{n \to \infty} f(b_n) = \beta = f(c) \\ f(c) = k $$
    - 有界性定理
        有界閉区間 [a, b], 連続関数f
        $$ \exists m, M \in \mathbb R m \leq f(x) \leq M, \forall x \in [a, b] $$
    - 最大値最小値原理 ワイエルシュトラウス
        有界閉区間 [a, b], 連続関数f
        $$ \exists c, d \in \mathbb R f(c) \leq f(x) \leq f(d), \forall x \in [a, b] $$
    - ロルの定理
        有界閉区間 [a, b], 連続関数f, fは開区間(a, b)で微分可能
        $$ f(a) = f(b) \Rightarrow \exists c \in (a, b), f'(c)=0 $$
        - proof
            - $\exists t \in [a, b], f(a) < f(t)$
                - 最大値の原理
                    $$ \exists c \in (a, b), \max f(c) $$
    - 平均値の定理
        有界閉区間 [a, b], 連続関数f, fは開区間(a, b)で微分可能
        $$ \Rightarrow \exists c \in (a, b), f'(c) = \frac{f(b)-f(a)}{b-a} $$
    - 積分の平均値の定理
        $$ \exists c \in [a, b], f(c) = \frac{1}{b-a} \int_a^b f(x)dx $$
    - テイラーの定理
        閉区間[a, x], n階微分可能な関数f
        $$ \sum_{k=0}^{n-1} \frac{f^{(l)}(a)}{j!}(x-a)^k + \frac{f^{(n)}(c)}{n!}(x-a)^n $$
    - コーシーの平均値の定理
    - ロピタルの定理
    - テイラーの定理
- 極限 limit
    $$ \lim_{x \to a} f(x) = \alpha $$
    $$ \forall \epsilon>0, \exists \delta >0, \forall x \in \mathbb R \\ 0 < |x-a|< \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
    - 左極限
        $$ \lim_{x \to a-} f(x) = \alpha $$
        $$ \forall \delta>0, \exists \epsilon >0, \forall x \in \mathbb R \\ 0 < a-x < \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
    - 右極限
        $$ \lim_{x \to a+} f(x) = \alpha $$
        $$ \forall \delta>0, \exists \epsilon >0, \forall x \in \mathbb R \\ 0 < x-a < \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
    - theorem
        - 一意性
            $$ a_n = b_n \Rightarrow \alpha = \beta, \forall n \in \mathbb N $$
        - 和
            $$ \alpha + \beta = \lim_{n \to \infty}(a_n + b_n) $$
        - 積
            $$ \alpha \beta = \lim_{n \to \infty} a_n b_n $$
        - 商
            $$ \alpha \ne 0 \Rightarrow \frac{\beta}{\alpha} = \lim_{n \to \infty} \frac{b_n}{a_n} $$
        - 大小関係
            $$ a_n \leq b_n \Rightarrow \alpha \leq \beta $$
- 連続性 continuous
    $$ \lim_{x \to a} f(x) = f(a) $$
    $$ \forall \delta>0, \exists \epsilon >0, \forall x \in \mathbb R \\ 0 < |x-a|< \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
    - 左連続 left-hand
        $$ a \in X \\ \lim_{x \to a+} f(x) \in \mathbb R\\ \lim_{x \to a-} f(x) = f(a) $$
        $$ \forall \delta>0, \exists \epsilon >0, \forall x \in \mathbb R \\ 0 < |x-a|< \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
    - 右連続 right-hand
        $$ a \in X \\ \lim_{x \to a+} f(x) \in \mathbb R\\ \lim_{x \to a+} f(x) = f(a) $$
        $$ \forall \delta>0, \exists \epsilon >0, \forall x \in \mathbb R \\ 0 < |x-a|< \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
- 微分可能性 differentiable
    $$ f'(a) = \frac{df}{dx} (a) = \\ \lim_{h \to 0} \frac{f(a+h)-f(a)}{h} \\ \lim_{x \to a} \frac{f(x)-f(a)}{x-a} $$
    if it exists, f(x) is differentiable at a
    - differentiability class
        - $C^0$級/連続 continuous
            関数fが連続
        - $C^1$級/連続微分可能 continuously differentiable
            関数fが微分可能
            導関数$f^{(1)}$が連続
        - $C^n$級/n階連続微分可能
            関数fが微分可能
            導関数$f^{(n)}$が連続
        - $C^\infty$級/無限回微分可能
            fが何回でも微分可能
        - $C^\omega$級/解析的 analytic
            任意の点aの十分近くでテイラー展開可能
- 微分 differentiate
    - 導関数 derivative function
        $$ f'(x) = \frac{df}{dx} (x) = \frac{d}{dx} f(x) \\ \forall a \in U, \exists f'(a) $$
        f(x) is differentiable on U
    - 演算 operation
        - 線形性
            $$ \{kf(x)+lg(x)\}' = kf'(x)+lg'(x) $$
        - 掛け算
            $$ \{f(x)g(x)\}'=f'(x)g(x)+f(x)g'(x) $$
        - 割り算
            $$ \left\{\frac{f(x)}{g(x)}\right\}' = \frac{f'(x)g(x)-f(x)g'(x)}{\{g(x)\}^2} $$
    - 合成関数の微分
        $$ \frac{df(g(x))}{dx}= \frac{df(g )}{dg}\cdot \frac{dg(x)}{dx} $$
        - proof
            $$ \lim_{a \to b} \frac{f(g(x+h))-f(g(x))}{h} = \lim_{h \to 0} \frac{f(g(x+h))-f(g(x))}{g(x+h)-g(x)} \frac{g(x+h)-g(x)}{h} \\ = \lim_{h \to 0} \frac{f(g(x+h))-f(g(x))}{g(x+h)-g(x)} \lim_{h \to 0} \frac{g(x+h)-g(x)}{h} \\ = \frac{df(g)}{dg} \cdot \frac{dg(x)}{dx} $$
    - 逆関数の微分
        $$ \frac{d y}{dx} = \frac{1}{\frac{d x}{d y}} $$
        - proof
            $$ y =f^{-1}(x) \\ x = f(y) \\ 1 = \frac{\partial f(y)}{\partial y} \frac{\partial y}{\partial x} \\ 1 = \frac{\partial x}{\partial y} \frac{\partial y}{\partial x} \\ \frac{\partial y}{\partial x} = \frac{1}{\frac{\partial x}{\partial y}} $$
    - 商の微分
        $$ \frac{\frac{df(x)}{dx}g(x) - f(x)\frac{dg(x)}{dx}}{\{g(x)\}^2} $$
        - proof
            $$ \lim_{h \to 0} \frac{\frac{f(x+h)}{g(x+h)} - \frac{f(x)}{g(x)}}{h} \\ \lim_{h \to 0} \frac{\frac{f(x+h)g(x)-f(x)g(x+h)}{g(x+h)g(x)}}{h} \\ \lim_{h \to 0} \frac{\frac{f(x+h)g(x) - f(x)g(x) + f(x)g(x )-f(x)g(x+h)}{g(x+h)g(x)}}{h}\\ \lim_{h \to 0} \frac{\frac{(f(x+h)-f(x))g(x) - f(x)(g(x+h)-g(x))}{g(x+h)g(x)}}{h} \\ \xrightarrow{h \to 0 } \frac{f'(x)g(x) - f(x)g'(x)}{\{g(x)\}^2} $$
    - 高階微分
    - 微分公式集
        - log 対数
            $$ \frac{1}{\ln a}\frac{1}{x} $$
            - proof
                $$ \lim_{h \to 0} \frac{\log_a (x+h) - \log_a x}{h} \\ = \lim_{h \to 0} \frac{\log_a (1+\frac{h}{x}) }{h} \\ = \lim_{h \to 0} \log_a (1+\frac{h}{x})^{\frac{1}{h}} \\ = \lim_{h \to 0} \log_a (((1+\frac{h}{x})^{\frac{x}{h}})^{\frac{1}{x}}) \ = \frac{1}{x} \lim_{h \to 0} \log_a (1+\frac{h}{x})^{\frac{x}{h}}) \\ = \frac{1}{x} \log_a e\\ = \frac{1}{\ln a} \frac{1}{x} $$
        - ln 自然対数
            $$ \frac{1}{x} $$
            - proof
                $$ \lim_{h \to 0} \frac{\log (x+h) - \log x}{h} \\ = \lim_{h \to 0} \frac{\log (1+\frac{h}{x}) }{h} \\ = \lim_{h \to 0} \log (1+\frac{h}{x})^{\frac{1}{h}} \\ = \lim_{h \to 0} \log (((1+\frac{h}{x})^{\frac{x}{h}})^{\frac{1}{x}}) \ = \frac{1}{x} \lim_{h \to 0} \log (1+\frac{h}{x})^{\frac{x}{h}}) \\ = \frac{1}{x} $$
        - 分数の対数
- 極値 limit
    - 変曲点
    - 一変数
    - 多変数
        - 臨界点/停留点
            $$ \forall i \in \{1, 2, ..., n\}, f_{x_i} (p_1, ... , p_n) = 0\\ $$
            - 極大
                - neighborhood U
                $f : A \to \mathbb R A \subset \mathbb R$
                $$ \exists a \in A, \exists \delta \in \mathbb R \forall x \in U(a, \delta), f(x) \leq f(a) $$
            - 極小
                - neighborhood U
                $f : A \to \mathbb R A \subset \mathbb R$
                $$ \exists a \in A, \exists \delta \in \mathbb R \forall x \in U(a, \delta), f(x) \geq f(a) $$
            - 鞍点
- 級数 series
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
- 積分 calculus
    - 定積分
    - 原始関数
    - 置換積分
    - 部分積分
        $$ (f(x) g(x))' = f'(x)g(x) + f(x)g'(x) \\ f(x)g(x) = \int f'(x)g(x) + \int f(x)g'(x) $$
    - 部分分数分解
    - 積分公式集
    - 広義積分
        $$ \int_a^{+\infty} f(x)dx = \lim_{c \to +\infty} \int_a^c f(x)dx $$
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
    $$ \exists k \in \mathbb R F_x(a, b, k) = F_y(a, b, k) = F_\lambda(a, b, k) = 0 \\ F(x, y, \lambda) = f(x, y) - \lambda g(x, y) $$
    - how to use
        制約条件gの下でのfの最大/最小化
        $$ \max / \min f(x, y)\ s.t.\ g(x, y) = 0 $$
- Laudau’s notation
    - big O
        $$ \exists M, \delta > 0, |x-a| < \delta \Rightarrow \\ |f(x)| \leq M |g(x)| \\
        $$
    - small o
        $$ \lim_{x \to a} \left|\frac{f(x)}{g(x)}\right| = 0 $$