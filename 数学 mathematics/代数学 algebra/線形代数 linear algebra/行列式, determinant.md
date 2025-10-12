$$ \det A = |A| = \sum_{\sigma \in S_n}(sgn\ \sigma) a_{1 \sigma(1)}...a_{n\sigma(n)} $$
- 演算 operation
    - 基本変形
        - ある行/列のc倍他の行/列に加算
            行列式は変化なし
        - 行/列をc倍
            行列式はc倍
        - 行/列を交換
            行列式の符号が反転
    - 多重線形性 linearity
    - 転置 transpose
        $$ \det A = \det A^\top $$
    - 2つの行/列が等しい行列
        $$ \det A = 0 $$
    - 積が可換 abelian
        $$ \det (AB) = \det A \det B $$
    - 正則行列 regular
        $$ \det A \ne 0 $$
        if and only if A is regular
    - 逆行列 inverse
        $$ \det (A^{-1}) = (\det A)^{-1} $$
    - 線形独立 linear independent
        $(\bm a_1, \bm a_2, ..., \bm a_n)$ is linear independent if and only if $\det (A) \ne 0$
- theorem
    $$ A = (\bm a_1, \bm a_2, ..., \bm a_n) \\ \bm a_i = (a_{11}, a_{12}, ..., a_{1n}) $$