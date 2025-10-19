- 測度論 measure theory
    - 関数空間 functional space
        - $L^0 (X, \mu)$ u-測度可能な関数
        - $L^1 (X, \mu)$ Banach
            - 測度空間 $(X, \mu)$
            - 一般の可測関数の積分
                [一般の可測関数の積分](https://www.notion.so/216ec42dd04b81a88464f953c487d5b6?pvs=21) 
            $$
            \int_X |f| d\mu< \infty
            $$
            この時、fを可積分という
            可積分な関数全体の集合を $L^1$という
            $$
            L^1 = \{f | \int_X |f|d\mu < \infty\}
            $$
        - $L^2 (X, \mu)$ Hirbert
            - 測度空間 $(X, \mu)$
            - 一般の可測関数の積分
                [一般の可測関数の積分](https://www.notion.so/216ec42dd04b81a88464f953c487d5b6?pvs=21) 
            $$
            \int_X |f|^2 d\mu< \infty
            $$
            この時、fを可積分という
            可積分な関数全体の集合を $L^2$という
            $$
            L^2 = \{f | \int_K |f|^2d\mu < \infty\}
            $$
        - $L^p (X, \mu)$ p norm
            - 測度空間 $(X, \mu)$
            - 一般の可測関数の積分
                [一般の可測関数の積分](https://www.notion.so/216ec42dd04b81a88464f953c487d5b6?pvs=21) 
            $$
            \int_X |f|^p d\mu< \infty
            $$
            この時、fを可積分という
            可積分な関数全体の集合を $L^p$という
            $$
            L^p = \{f | \int_K |f|^pd\mu < \infty\}
            $$
        - $L^\infty (X, \mu)$ essential supremum
        - $L^p_{loc} (X, \mu)$ local
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
                ‣ 
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
- ベクトル解析 vector analysis
    - スカラー scalar
        実数
    - ベクトル vector
        線形空間
    - スカラー積 dot product
        $$
        \vec a \cdot \vec b = |\vec a||\vec b|\cos \theta \\ 
        = \sum_{i=1}^n a_i b_i
        $$
    - ベクトル積 cross product
        $$
        \vec a \times \vec b = |\vec a||\vec b|\sin \theta \\ 
        $$
    - ナブラ演算子 labra operator
        $$
        \nabla = (\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z})
        $$
    - 勾配 gradient
        $$
        grad f = \nabla f
        $$
        スカラー場fの変化が最大となるベクトル
    - 発散 divergence
        $$
        div A = \nabla \cdot A
        $$
    - 回転 rotation
        $$
        rot A = \nabla \times  A
        $$
    - ストークスの定理
        回転の面積分は境界の線積分
        $$
        \int_S (\nabla \times A)\cdot n\ dS = \oint_C A\ dr
        $$
        Sは積分範囲の面
        \partial Sは境界の曲線
    - ガウスの発散定理
        $$
        \int_S A \cdot n\ dS = \int_V \nabla \cdot A \ dV
        $$
- フーリエ解析 Fourier transform
    関数を三角関数に分解
    - 三角関数系 trigonometric system
        $$
        \{\cos nx, \sin nx| n \in \mathbb N\} \\
        \{1, \cos x, \sin x, \cos 2x, \sin 2x, ...| n \in \mathbb N\}
        $$
    - フーリエ級数 Fourier series
        $$
        f(x) = \frac{a_0}{2}+ \sum_{n=1}^\infty (a_n \cos nx + b_n \sin nx)
        $$
    - フーリエ級数 Fourier transform
        $$
        \hat f(\xi) = \int_{-\infty}^\infty f(x) e^{-2\pi ix\xi}dx
        $$
    - 逆フーリエ変換 inverse Fourier transform
        $$
        f(x) = \int_{-\infty}^\infty \hat f(\xi) e^{2\pi ix\xi}d\xi
        $$
    - 内積
    - 離散フーリエ変換
        - ナイキスト周波数
            取得したデータの時間間隔により復元できる周期関数の周波数の上限が存在する
        - 標本化定理 sampling theorem
            元の信号をその最大周波数の2倍を超えた周波数で標本化すればよい
    - youtube
        https://youtube.com/watch?v=fGos3wrKeHY&si=u_3Gw6Chsxyge6AS
- 微分方程式 differential equation
    - 変数分離形/一階微分方程式
        $$
        \frac{dy}{dx} = f(x)g(y)
        $$
        - 解法
            $$
            \frac{1}{g(y)}\frac{dy}{dx} = f(x) \\
            \int \frac{1}{g(x)}\frac{dy}{dx}dx = \int f(x)dx
            $$
        - 置換積分
            $$
            \int f(x) dx = \int f(g(t))\frac{dx}{dt}dt
            $$
    - 同次形
        $$
        \frac{dy}{dx} = f(\frac{y}{x})
        $$
    - 一階線形微分方程式
        $$
        \frac{dy}{dx} + p(x)y = g(x)
        $$
    - ベルヌーイの微分方程式
        $$
        \frac{dy}{dx} + p(x)y = g(x)y^\alpha
        $$
    - 完全微分方程式
        $$
        \frac{\partial F(x,y)}{\partial x}dx + \frac{\partial F(x, y)}{\partial y}dy = 0
        $$
    - クレローの微分方程式
        $$
        y = x \frac{dy}{dx} + f(\frac{dy}{dx})
        $$
    - 二階線形同次微分方程式
        $$
        \frac{d^2y}{dx^2} + p(x) \frac{dy}{dx} + g(x)y = 0
        $$
    - 二階線形非同次微分方程式
        $$
        \frac{d^2y}{dx^2} + p(x) \frac{dy}{dx} + g(x)y = f(x)
        $$
    - ルンゲクッタ法
    - 境界値問題 boundary value problem
    - 固有値問題
    - neural OED
- 複素解析 complex number
    $$
    a + bi\\
    i = \sqrt{-1}
    $$
    - exp & tri
        $$
        \exp iz = \cos z + i\sin z
        $$
        - exp
            $$
            \exp z= \sum_{n=0}^\infty \frac{z^n}{n!}
            $$
        - sin
            $$
            \sin z = \sum_{n=0}^\infty \frac{z^{2n+1}}{(2n+1)!}
            $$
        - cos
            $$
            \sin z = \sum_{n=0}^\infty \frac{z^{2n}}{(2n)!}
            $$
        - Eular formula
            $$
            \exp \theta = \cos \theta + i\sin i\theta
            $$
        - Eular equation
            $$
            e^{\pi i} = -1
            $$
    - log
        $$
        w = \ln z
        $$
        $$
        w = u+iv \\
        z = e^w \\
        re^{i\theta} = e^u\cdot e^{iv} \\
        r = e^u \Rightarrow u = \ln r\\
        e^{i\theta} = e^{iv} \Rightarrow v = \theta + 2n\pi
        $$
        $$
        w = \ln z = \ln r +i(\theta + 2n\pi) \\
        w = \ln |z| + i \arg z + 2n\pi i
        $$
    - differential
        $$
        \frac{df(z)}{dz} = \lim_{\Delta z \to 0} \frac{f(z+\Delta z)-f(z)}{\Delta z}
        $$
        - Cauchy Lieman
            - setting
                $$
                z = x+iy \\
                f(z) = u(x,y) +iv(x,y)
                $$
            - CR equation
                $$
                \frac{\partial u}{\partial x}(x, y) = \frac{\partial v}{\partial y}(x, y) \\
                \frac{\partial u}{\partial y}(x, y) = -\frac{\partial v}{\partial x}(x, y)
                $$
            - f(z) が微分可能
            - u(x, y)とv(x, y)が全微分可能かつCRの公式が成立
            上記二つが同値関係
            - 必要条件(上→下)
                $$
                \frac{f(z+\Delta z)-f(z)}{\Delta z} \\ = \frac{(u(x+\Delta x, y + \Delta y) + i v(x+\Delta x, y + \Delta y)) - (u(x, y) + i v(x, y))}{\Delta x + i \Delta y}
                \\ = \frac{(u(x+\Delta x, y + \Delta y) - u(x, y)) + i (v(x+\Delta x, y + \Delta y)+ v(x, y))}{\Delta x + i \Delta y}
                $$
                - 実軸平行
                    $$
                    \frac{df(z)}{dz} = \frac{\partial u}{\partial x}(x,y) + i \frac{\partial v}{\partial x}(x,y)
                    $$
                - 虚軸平行
                    $$
                    \frac{df(z)}{dz} = -i \frac{\partial u}{\partial y}(x,y) + \frac{\partial v}{\partial y}(x,y)
                    $$
            - 十分条件(下→上)
    - calculus
    - pdf
        [kansuron.pdf](kansuron.pdf)
- 超準解析 nonstandard analysis
    - フィルター filter
        定義3.2. F を自然数N の部分集合の集まりとする．F がフィルターであるとは次の条件を
        満たす事である．
        1. F は空集合でない．
        2. A, B ∈ F ならばA ∩ B ∈ F である．
        3. A ∈ F かつA ⊂ B ⊂ N ならばB ∈ F である．
        4. F は空集合を含まない．
        - フレッシェ・フィルター
            自然数の有限部分集合とは，有限個の自然数の集まりの事である．自然数の有限部
            分集合の補集合の集まりをF とすると，これはフィルターである．式で書くと
            F= {Xc | X ⊂ N は有限集合}
        - 超フィルター
            定義3.7. F を自然数N の部分集合の集まりとし，フィルターの条件を満たしているとす
            る．このF が超フィルターであるとは次の条件を満たす事である．
            • もし他のフィルターF ′ がF ⊂ F ′ を満たすならば，F= F ′ である．つまりF より大
            きいフィルターは存在しない
        - 
        命題3.9. フィルターF に対して，次の4 つの条件は同値である．
        1. F は超フィルターである．
        2. どんな部分集合A ⊂ N に対しても，A ∈ F かAc ∈ F のどちらか一つが必ず成立す
        る．（この時両方が成立する事はない．）
        3. 部分集合A, B ⊂ N がA ∪ B ∈ F ならば，A ∈ F かB ∈ F のどちらかが成立する．
        （この時は両方成立してもよい．）
        4. 部分集合A1, . . . , An ⊂ N がA1 ∪ · · · ∪ An ∈ F ならば，あるi に対してAi ∈ F である．
- 局所凸位相ベクトル空間 locally convex topological vector space
- Fréchet derivative
    https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
- holder continuous
- 数値計算
    - 二分法
    - ニュートン法
        - 目的 purpose
            関数 f(x) について f(a) = bとなるaを求めたい
        $$
        x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
        $$
        ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%204.png)
        - 導出
            $$
            x_n-x_{n+1}:f(x_n) = 1:f'(x_n) \\
            f'(x_n)(x_n-x_{n+1}) = f(x_n) \\
            x_n-x_{n+1}= \frac{f(x_n)}{f'(x_n)} \\
            x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)} 
            $$
    - brent法
- website
    [多変数関数の極値判定 - 数学についていろいろ解説するブログ](https://shakayami-math.hatenablog.com/entry/2020/08/08/175457)