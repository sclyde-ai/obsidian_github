- 位相空間 topological space
    - 定義 def
        set S、family O
        - 全体集合と空集合
            $$
            S \in \mathcal{O}, \phi \in \mathcal{0}
            $$
        - 有限積
            $$
            \forall O_1, ..., O_n \in \mathcal{O}, \bigcap_{i=1}^n O_i \in \mathcal{O} 
            $$
        - 無限和
            $$
            \forall O_1, ...\in \mathcal{O},
            \bigcup_{n = 1}^\infin O_n \in \mathcal{O}
            $$
        then, (S, O)を位相空間という。
    - 開集合 open set
        $$
        S \in \mathcal{O}, \phi \in \mathcal{O} \\
        \forall O_1, ..., O_n \in \mathcal{O}, \bigcap_{i=1}^n O_i \in \mathcal{O} \\ 
        \forall O_1, ...\in \mathcal{O},
        \bigcup_{n = 1}^\infin O_n \in \mathcal{O} 
        $$
        - 実数の開集合
            $$
            \forall a \in A, \exist \epsilon > 0, (a- \epsilon, a+ \epsilon) \subset A
            $$
        - 距離空間の開集合
        - 例
            - 無限積は開とは限らない
                $$
                A_i = (a-\frac{1}{i}, b+\frac{1}{i})\\
                \bigcap_{i \in \N} A_i = [a,b]
                $$
    - 閉集合 closed set
        $$
        S \in \mathcal{F}, \phi \in \mathcal{F} \\
        \forall F_1, ..., F_n \in \mathcal{F}, \bigcap_{i=1}^n F_i \in \mathcal{F} \\
         \forall F_1, ...\in \mathcal{F}
        \bigcup_{n = 1}^\infin F_n \in \mathcal{F}
        $$
        - 実数の閉集合
        - 距離空間の閉集合
        - 例
            - 一点集合
            - 整数集合
            - 有限集合
    - 近傍 neighborhood
        Xを位相空間、$x \in X$、 $V \subset X$
        $$
        \exist U \in \mathcal O, U \subset X, x \in U \subset V
        $$
        Vを近傍という
        - 開近傍 open
            $$
            V \in \mathcal O
            $$
        - 閉近傍 closed
            $$
            V \in \mathcal F
            $$
        - 基本近傍系 neighborhood base
            近傍集合族 $\mathcal U$
            $$
            \forall V \in \mathcal U, U \in \mathcal U, U \subset V
            $$
            - 距離空間の基本近傍系
                $$
                \mathcal U_x = \{B(x, r)|r > 0\}
                $$
    - 被覆 covering
        - 定義
            集合S、部分集合族$\{A_i\}_{i \in I}$
            $$
            A \subset \bigcup_{i \in I} A_i
            $$
            $\{A_i\}_{i \in I}$をAの被覆という
        - 開被覆
            $\{A_i\}_{i \in I}$が開集合の時、開被覆という
            $$
            \{A_i\}_{i \in I} \subset \mathcal O
            $$
        - 有限被覆
            $\{A_i\}_{i \in I}$の $I$ が有限集合の時、有限被覆という
            $$
            |I| < \infin
            $$
        - 有限開被覆
            $\{A_i\}_{i \in I}$が開被覆かつ有限被覆
            $$
            \{A_i\}_{i \in I} \subset \mathcal O, |I|< \infin
            $$
        - 部分被覆
            $\{A_j\}_{j \in J}\ J \subset I$が被覆の時$\{A_i\}_{i \in I}$の部分被覆という
            $$
            A \subset \{A_j\}_{j \in J}\ J \subset I
            $$
        - 有限部分被覆
            $$
            A \subset \{A_j\}_{j \in J}\ J \subset I, |I| < \infin
            $$
        - コンパクト
            Rの部分集合Aの任意の開被覆 $\{A_i\}_{i \in I}$に対し有限部分被覆が必ず存在するとき、SをR上のコンパクト集合という
            $$
            A \subset \R
            $$
        - ハイネボレルの被覆定理
            実数の位相空間の任意の有界閉集合はコンパクト
    - 連続写像 continuous map
        写像 f : X \to Y
        $$
        \forall V \in \mathcal O_Y, f^{-1} (V) \in \mathcal O_X
        $$
    - 同相写像 homeomorphism
        位相空間 $(X, \mathcal O_X)$,、 $(Y, \mathcal O_Y)$、 $f:X \to Y$
        - 全単射
        - 連続
        - 逆写像 $f^{-1}$ も連続
    - 直積位相
        $$
        X = X_1 \times ... \times X_n
        $$
        - 射影
            $$
            p_i : X \rightarrow X_i
            $$
    - link
        https://old.math.jp/wiki/%E5%85%A5%E9%96%80%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%80%8C%E4%BD%8D%E7%9B%B8%E7%A9%BA%E9%96%93%E8%AB%96%E3%80%8D
        https://www1.econ.hit-u.ac.jp/kawahira/courses/kiso/03-isou.pdf
- 距離空間 metric space
    - 定義 def
        set X
        - 距離 metric  $X \times X \to \R$
            - 正値
                $$
                d(x,y) \geq 0
                $$
            - 零
                $$
                d(x, y) = 0 \Leftrightarrow x = y 
                $$
            - 対称性
                $$
                d(x,y) = d(y, x)
                $$
            - 三角不等式
                $$
                d(x,z) \leq d(x,y) + d(y,z)
                $$
    - theorem
    - 開球体 open ball
        $$
        B_d(x, r) = \{y \in X | d(x,y) < r\}
        $$
    - 閉球体 closed ball
        $$
        \bar{B}_d(x, r) = \{y \in X | d(x,y) \leq r\}
        $$
    - 基本列/コーシー列 cauchy sequence
        $$
        \{a_n\} \subset X \\
        \forall \epsilon \in \R_{++}, \exist N \in \N, \forall n,m \in \N, \\ n, m \geq N \Rightarrow d(a_n, a_m) < \epsilon
        $$
        を基本列という
    - 完備距離空間 complete metric space
        - 基本列 a_n
        $$
        \lim_{n \to \infin} a_n \in X, \forall \{a_n\}_{n \in \N}
        $$
        を満たす距離空間を完備距離空間という
    - example
        - $L^1$ matrix/Chebyshev distance
            $$
            d(x, y) = x+y
            $$
        - $L^2$ matrix/Euclid distance
            $$
            d(x,y) = \sqrt {x^2+y^2}
            $$
        - $L^\infin$ matrix/Manhattan distance
            $$
            d(x, y) = \max(x,y)
            $$
        - mahalanobis distance
            $$
            d(x, y) = \sqrt{(x-y) \Sigma^{-1}(x-y)}
            $$
        - post office matrix/rail matrix
            $$
            d(x, y) = 
            \begin{equation}
              \begin{cases}
            |x-y| & (x = ky, \forall k \in \R) \\
            |x| + |y| & others
              \end{cases}
            \end{equation}
            $$
        - 離散距離 discrete matrix
            $$
            d(x, y) = 
            \begin{equation}
              \begin{cases}
            1 & (x = y)\\
            0 & (x \ne y)
              \end{cases}
            \end{equation}
            $$
        - 球面距離
- 基準空間 norm space
    - vector space V on K
    - norm $V \rightarrow \mathbb R$
        - 正値
            $$
            \| x \| > 0
            $$
        - 零
            $$
            \| x \| = 0 \Leftrightarrow x = 0
            $$
        - 斉次性
            $$
            \|kx\| = |k| \|x\|
            $$
        - 三角不等式
            $$
            \| x+y \| \leq \|x\| + \|y\|
            $$
    - theorem
    - example
        - $L^p$ norm
            $$
            \|x \|_p = \sqrt[p]{\sum x_i^p}
            $$
        - $L^1$ norm
            $$
            \|x \|_1 = \sum |x_i|
            $$
        - $L^2$  norm
            $$
            \|x \|_2 = \sqrt[2]{\sum x_i^2}
            $$
        - $L^\infin$ norm
            $$
            \|x \|_\infin = \sqrt[\infin]{\sum x_i^\infin} = \max(|x_1|, ...)
            $$
- 完備基準空間 Banach space
    完備なノルム空間
- 内積空間 metric vector space
    K上ベクトル空間
    - 内積 V \times V \to \R
        - 正値
            $$
            \langle x, x \rangle \geq 0
            $$
        - 零
            $$
            \langle x, x \rangle = 0 \Leftrightarrow x=0 
            $$
        - 自己随伴対称性
            $$
            \langle x, y \rangle = \overline{ \langle y, x \rangle}
            $$
        - 線形性
            $$
            \langle kx+ly, z \rangle = k \langle x, z \rangle + l\langle y, z \rangle 
            $$
    内積が定義されたベクトル空間を内積空間という
    - 性質 property
        - 反線形性 antilinear
    - 例 example
- 完備内積空間 Hilbert space
    完備な内積空間
- 中線定理 parallelogram low
    $$
    \|x+y\|^2 + \|x-y\|^2 = 2(\|x\|^2+\|y\|^2)
    $$
- T_0空間 Kolmogorov space
    - topological space (X, O)
    $$
     \exist \mathcal O_x \subset \mathcal O, x \in \mathcal O_x \land y \notin \mathcal O_x
    \\ \lor \\
     \exist \mathcal O_y \subset \mathcal O, x \notin \mathcal O_y \land y \in \mathcal O_y
    $$
    ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%207.png)
- T_1空間 Frechet space
    - topological space
    $$
     \exist \mathcal O_x \subset \mathcal O, x \in \mathcal O_x \land y \notin \mathcal O_x
    \\ \land \\
     \exist \mathcal O_y \subset \mathcal O, x \notin \mathcal O_y \land y \in \mathcal O_y
    $$
    ![image.png](image%208.png)
    - 一点集合は閉集合
- T_2空間 Hausdoff space
    - topological space (X, O)
    $$
     \exist \mathcal O_x, \mathcal O_y \subset \mathcal O, \mathcal O_x \cup \mathcal O_y = \phi \\ (x \in \mathcal O_x \land y \notin \mathcal O_x)
    \land
    (x \notin \mathcal O_y \land y \in \mathcal O_y)
    $$
    ![image.png](image%209.png)
- Sierpinski space
    $$
    X= \{0, 1\} \\
    \mathcal O = \{\phi, \{0\}, X\}
    $$
- 包含関係
    - 位相空間
        - 距離空間
            - ノルム空間
                - 内積空間
                    - ノルム空間+中線定理=内積
        - T_0空間
        - T_1空間
        - T_2空間
    - 内積空間はノルム空間
    - ノルム空間は距離空間
    - 距離空間は位相空間
- 位相空間の例
    - {a, b, c}
    - 離散空間
    - 密着空間
    - 実数空間
    - 特定点位相
    - 除外点位相
    - p乗可積分空間
- 図形
    - simplex
        ![IMG_7144.jpeg](IMG_7144.jpeg)
    - フラクタル fractal
        - ジルピンスキーの三角形
        - コッホ曲線
        - Weierstrass function
        - 規模一定 scale invariance
            - self-similarity
                $$
                f(\lambda x) = \lambda^\Delta f(x)
                $$
            - stochastic process
                $$
                P(\lambda x) = \lambda^{-\Delta} P(x)
                $$
                \Delta = -1 : pink noise
                \Delta = -2 : brownian noise 
            - tweedie distributions
            $$
            Var(Y) = \sigma^2 E[Y]^p
            $$
    - 多面体の双対
        面の重心を頂点とし辺で接する面同士の重心を辺で結ぶ
        - 正四面体=正四面体
        - 正六面体=正八面体
        - 正十二面体=正二十面体
- 不動点定理
    - ブラウワーの不動点定理
    - 角谷の不動点定理
    - **Borsuk–Ulam theorem**
- 射影幾何学
- website
    https://mathlandscape.com/t0-sp/
    https://old.math.jp/wiki/%E4%BD%8D%E7%9B%B8%E7%A9%BA%E9%96%93%E8%AB%961%EF%BC%9A%E4%BD%8D%E7%9B%B8%E7%A9%BA%E9%96%93