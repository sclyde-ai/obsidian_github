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
        \bigcup_{n = 1}^\infty O_n \in \mathcal{O}
        $$
    then, (S, O)を位相空間という。
- 開集合 open set
    $$
    S \in \mathcal{O}, \phi \in \mathcal{O} \\
    \forall O_1, ..., O_n \in \mathcal{O}, \bigcap_{i=1}^n O_i \in \mathcal{O} \\ 
    \forall O_1, ...\in \mathcal{O},
    \bigcup_{n = 1}^\infty O_n \in \mathcal{O} 
    $$
    - 実数の開集合
        $$
        \forall a \in A, \existss \epsilon > 0, (a- \epsilon, a+ \epsilon) \subset A
        $$
    - 距離空間の開集合
    - 例
        - 無限積は開とは限らない
            $$
            A_i = (a-\frac{1}{i}, b+\frac{1}{i})\\
            \bigcap_{i \in \mathbb N} A_i = [a,b]
            $$
- 閉集合 closed set
    $$
    S \in \mathcal{F}, \phi \in \mathcal{F} \\
    \forall F_1, ..., F_n \in \mathcal{F}, \bigcap_{i=1}^n F_i \in \mathcal{F} \\
     \forall F_1, ...\in \mathcal{F}
    \bigcup_{n = 1}^\infty F_n \in \mathcal{F}
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
    \existss U \in \mathcal O, U \subset X, x \in U \subset V
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
        |I| < \infty
        $$
    - 有限開被覆
        $\{A_i\}_{i \in I}$が開被覆かつ有限被覆
        $$
        \{A_i\}_{i \in I} \subset \mathcal O, |I|< \infty
        $$
    - 部分被覆
        $\{A_j\}_{j \in J}\ J \subset I$が被覆の時$\{A_i\}_{i \in I}$の部分被覆という
        $$
        A \subset \{A_j\}_{j \in J}\ J \subset I
        $$
    - 有限部分被覆
        $$
        A \subset \{A_j\}_{j \in J}\ J \subset I, |I| < \infty
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
- 位相空間の例
    - {a, b, c}
    - 離散空間
    - 密着空間
    - 実数空間
    - 特定点位相
    - 除外点位相
    - p乗可積分空間