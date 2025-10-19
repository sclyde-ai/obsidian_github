- 定義 def
    集合V、体K
    $$ \forall x, y, z \in V, \forall a, b \in K $$
    - 加法 addition $V \times V \rightarrow V$
        1. 結合律 associativity
            $$ (x+y)+z=x+(y+z) $$
        2. 可換律 commutativity
            $$ x+y = y+x $$
        3. 零元 zero element
            $$ \exists0 \in V, x+0=0+y=0 $$
        4. 逆元 inverse element
            $$ \exists -x \in V, x +(-x) = (-x)+x = 0 $$
    - スカラー倍 scalar multiplation $K \times V \rightarrow V$
        1. スカラー倍 compatibility
            $$ a(b x) = (ab)x $$
        2. 分配則 distributivity
            $$ a(x+y) = ax +by $$
            $$ (a+b)x = ax + bx $$
        3. スカラー単位元
            $$ 1x = x1 = x $$
- 部分ベクトル空間 vector subspace
    $$ a, b \in V' \Rightarrow a+b \in V' \\ k \in \mathbb R a \in V' \Rightarrow ka \in V' $$
- 一次独立 linearly independent
    $$ v_1, ..., v_n \in V, k_1, ..., k_n \in K, \\ k_1v_1+...+k_nv_n = 0 \Rightarrow k_1=...=k_n=0 $$
    - 例1
        $$ \R[x]= \{a_nx^n+...+a_1x+a_0|a_1, ..., a_n \in\R\} $$
    - 例2
        有理数Q上のベクトル空間で
        $$ 1, \sqrt 2 $$
        は独立である
- 一次従属 linearly dependent
    $$ v_1, ..., v_n \in V, \\ \exists k_1, ..., k_n \in K, \\ k_1v_1+...+k_nv_n = 0 \land \forall i \in \mathbb N, k_i \ne 0 $$
- 一次結合 linear combination
    $$ v_1, ..., v_n \in V, \\ k_1, ..., k_n \in K, \\ k_1v_1+...+k_nv_n = 0 $$
- 基底 basis
    1. v_1, …, v_nが一次独立
    2. 任意のv \in Vがv_1, …, v_nの線形結合で表せる
- 次元 dimension
- 例 example
    - n次元ベクトル
        $$ \mathbb R = \{(x_1, x_2, ..., x_n)|x_1, x_2,..., x_n \in \R\} $$
    - 数列
        $$ l(\R) = \{\{a_n\}|a_n \in \mathbb R\} $$
    - 多項式
    - 関数