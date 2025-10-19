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
    \forall \epsilon \in \R_{++}, \exists N \in \mathbb N, \forall n,m \in \mathbb N, \\ n, m \geq N \Rightarrow d(a_n, a_m) < \epsilon
    $$
    を基本列という
- 完備距離空間 complete metric space
    - 基本列 a_n
    $$
    \lim_{n \to \infty} a_n \in X, \forall \{a_n\}_{n \in \mathbb N}
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
    - $L^\infty$ matrix/Manhattan distance
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