---
alias:
    ['測度論', 'measure theory']
---
- 収束 converge
    - 加法的集合関数
        - 可測空間(X, F)
        $$
        E = \sum_{n=1}^\infty E_n, E_n \in \mathcal F \\ \Rightarrow \Phi(E) = \sum_{n=1}^\infty \Phi(E_n) 
        $$
        $\Phi(E)$をXの上の加法的集合関数という
        - 単調増加
            $$
            \forall E \in \mathcal F, \Phi(E) \geq 0
            $$
            - 理由
                $$
                \Phi(E_1) \leq \Phi(E_2 - E_1) = \Phi(E_2), E_1 \subset E_2
                $$
        - 単調減少
    - 各点収束
        $$
        \lim_{n \to \infty} f_n(x) = f(x), \forall x \in X
        $$
        $$
        \forall \epsilon > 0, \exists N \in \mathbb N, \forall n > N, |f_n(x)-f(x)|<\epsilon, \forall x \in X
        $$
    - 概収束
        - 零集合N
        $$
        \lim_{n \to \infty } f_n(x) = f(x), \forall x \in X/N
        $$
        $$
        \forall \epsilon > 0, \exists N \in \mathbb N, \forall n > N, |f_n(x)-f(x)|<\epsilon, \forall x \in X/N
        $$
    - 上昇列各点収束/増大列各点収束
        $$
        f_n(x) \uparrow f(x), \forall x\in \R
        $$
        - 上昇列/増加列
            $$
            f_1(x) \leq f_2(x) \leq ... 
            $$
        - 各点収束
            [各点収束](https://www.notion.so/216ec42dd04b81e684b6ff950f7a0c43?pvs=21) 
    - 単調収束定理
        - 上昇列各点収束f
            [上昇列各点収束/増大列各点収束](https://www.notion.so/216ec42dd04b8112b7a3e8df0e2dffe1?pvs=21) 
        $$
        \lim_{n \to \infty}\int_A f_n \ d \mu = \int_A f \ d \mu
        $$
        - 証明 proof
            $$
            A(f_1 > t) \subset A(f_2 > t) \subset ... \land \bigcup^\infty_{n = 1} A(f_n > t) = A(f > t)\\
            \lambda_{f_1}(t) \leq \lambda_{f_2}(t) \leq ... \land \lim_{n \to \infty}\lambda_{f_n} (t) = \lambda_f (t)
            $$
            1. $\exists a > 0, \lambda_f (a) = \infty$
                $$
                $$
            2. $\lambda_f (a) < \infty, \forall t > 0$
            - 分布関数
                $$
                A_t = A(f > t) = \{x \in X | f(x) > t\} \\
                \lambda_f (t) = \mu(A_t)
                $$
- 積分 integral
    - 可測関数 measurable function
        - 可測空間(X, F), (Y, G)
            ‣ 
        $$
        f : (X, \mathcal F) \rightarrow (Y, \mathcal G) \\ f^{-1}(G) \in \mathcal F, \forall G \in \mathcal G
        $$
        - Borel mesurable
            F, GがBorel fieldのとき
    - 単関数 simple function
        - Aは互いに素
            $$
            A_1,...,A_n \in \mathcal F, A_i \cap A_j \ne \phi
            $$
        - 可測関数f (域値は実数)
            [可測関数 measurable function ](https://www.notion.so/measurable-function-216ec42dd04b815cac0cd90812258c6f?pvs=21) 
        - 定義関数/指示関数
            $$
            1_A(x)=
            \begin{cases}
            1 \ (x \in A) \\
            0 \ (x \notin A)
            \end{cases}
            $$
        $$
        f(x) = \sum^n_{i=1} a_i 1_{A_i} (x) \\
        a_1, ..., a_n \in \R
        $$
    - 可測関数は単関数で近似可能
        - 非負の場合
            - 可測関数f (域値は実数)
                [可測関数 measurable function ](https://www.notion.so/measurable-function-216ec42dd04b815cac0cd90812258c6f?pvs=21) 
            $$
            \exists \{f_n\}, f_n(x) \uparrow f(x), \forall x\in \R
            $$
            - 上昇列各点収束
                [上昇列各点収束/増大列各点収束](https://www.notion.so/216ec42dd04b8112b7a3e8df0e2dffe1?pvs=21) 
            - 証明 proof
                $$
                f_n(x) = \sum_{k=0}^{n2^n} \frac{k}{2^n} 1_{(\frac{k}{2^n}\leq f(x) < \frac{k+1}{2^n})}(x) \\
                0 \leq f(x) - f_n(x) \leq \frac{1}{2^n} \xrightarrow{n\to\infty} 0
                $$
        - 一般の場合
            - 可測関数f (域値は実数)
                - 可測空間(X, F)
                    ‣ 
                $$
                f : (X, \mathcal F) \rightarrow \mathbb R\\ f^{-1}(G) \in \mathcal F, \forall G \in \mathcal G
                $$
            $$
            \exists \{f_n\}, f_n(x) \to f(x), \forall x\in \R
            $$
            - 証明 proof
                $$
                f^+(x) = \max\{f(x), 0\} \\
                f^-(x) = \max\{-f(x), 0\} \\
                f = f^+ - f^-
                $$
        ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image.png)
    - 非負単関数の積分
        - A_iは有限非交叉
            $$
            a_1, ..., a_n \in \mathbb R A_1,...,A_n \in \mathcal F, A_i \cap A_j \ne \phi, \bigcup_{i = 1}^n A_i = A
            $$
        $$
        \int_A f\ d\mu = \int_A \sum^n_{i=1} a_i 1_{A_i} d\mu=\sum^n_{i=1} a_i \mu(A_i) 
        $$
        ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%201.png)
        - 和
            $$
            \int_S \{a f(x) + b g(x)\} \mu(dx) = a \int_S f(x) \mu(dx) + b \int_S g(x) \mu(dx)
            $$
            - 証明 proof
                $$
                f(x) = \sum^n_{i=1} a_i 1_{A_i} (x) \\ 
                g(x) = \sum^m_{j=1} b_j 1_{B_j} (x)
                \\
                af(x)+bg(x) = a\sum^n_{i=1} a_i 1_{A_i} (x) + b\sum^m_{j=1} b_j 1_{B_j} (x)\\
                = \sum^n_{i=1} aa_i 1_{A_i} (x) + \sum^m_{j=1} bb_j 1_{B_j} (x) \\
                = \sum^n_{i=1}\sum^m_{j=1} aa_i 1_{A_i \cap B_j} (x) + \sum^n_{i=1}\sum^m_{j=1} bb_j 1_{A_i \cap B_j} (x) \\
                = \sum^n_{i=1}\sum^m_{j=1} (aa_i + bb_j) 1_{A_i \cap B_j} (x) \\
                \int_S \{a f(x) + b g(x)\} \mu(dx) \\ = \sum^n_{i=1}\sum^m_{j=1} (aa_i(x) + bb_j (x)) \mu (A_i \cap B_j) \\
                = a\sum^n_{i=1}\sum^m_{j=1} a_i \mu (A_i \cap B_j) + b\sum^n_{i=1}\sum^m_{j=1} b_j \mu (A_i \cap B_j) \\
                = a\sum^n_{i=1} a_i \mu (A_i) + b\sum^m_{j=1} b_j \mu (B_j) \\
                = a \int_S f(x) \mu(dx) + b \int_S g(x) \mu(dx)
                $$
    - 非負可測関数の積分
        - f_nは単調増加かつ収束する単関数
            $$
            \{f_n\}_{n \in \mathbb N}, \\ \forall n \in \mathbb N, 0 < f_n(x) < f_{n+1}(x), \\ \lim_{n \to \infty} f_n (x) = f(x)
            $$
        $$
        \int_A f\ d\mu = \lim_{n \to \infty} \int_A f_n\  d\mu
        $$
        ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%202.png)
    - 一般の可測関数の積分
        $$
        \int_A f\ d\mu = \int_A f_+\ d\mu  - \int_A f_-\ d\mu
        $$
        $$
        f_+(f, 0) = \max\{f, 0\} \\
        f_-(f, 0) = -\min\{f, 0\}
        $$
        ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%203.png)
    - 可積分
        - 測度空間 $(X, \mu)$
        - 一般の可測関数の積分
            [一般の可測関数の積分](https://www.notion.so/216ec42dd04b81a88464f953c487d5b6?pvs=21) 
        $$
        \int_X |f| d\mu< \infty
        $$
        この時、fを可積分という
        可積分な関数全体の集合を $L^1$という
        $$
        L^1 = \{f | \int_K |f|d\mu < \infty\}
        $$
    - 局所可積分
        - 測度空間 $(X, \mu)$
        - compact set K
        $$
        \int_K |f| d\mu< \infty, \forall K \subset X
        $$
        この時、fを局所可積分という。
        局所可積分な関数全体の集合を $L_{loc}^1$という
        $$
        L_{loc}^1 = \{f | \int_K |f|d\mu < \infty, \forall K \subset X\}
        $$
    - fatouの補題
- 微分 differentiate
    - Lebesgue differentiation theorem
        - 一次元
            - 可積分関数f
                $$
                f : \mathbb R\to \mathbb C \\
                \int_{\R} |f|dx < \infty
                $$
            - almost everywhere $x \in \mathbb R$
            $$
            \lim_{h \to 0} \frac{1}{h} \int_x^{x+h} |f(y)-f(x)|dy = 0
            $$
        - 多次元
            - 可積分関数f
                $$
                f : \mathbb R \to \mathbb C \\
                \int_{\mathbb R} |f|dx < \infty
                $$
            - 開球 B(x, r)
            - almost everywhere $x \in \mathbb R$
            $$
            \lim_{r \downarrow 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} |f(y)-f(x)|dy = 0
            $$
    - Radon–Nikodym theorem
        - 可測空間(X, F)
        - σ-有限測度u, v
        - vがuに関して絶対連続
        - $f \in L_{loc}^1$
        $$
        \exists!f \in L_{loc}^1 (\mu), \nu(A) = \int_A f\ d\mu, A \in \mathcal F
        $$
        この時、fをRadon-Nikodym derivativeという
        $$
        f = \frac{dv}{du}
        $$
- link
    https://mathlandscape.com/lebesgue-integral/