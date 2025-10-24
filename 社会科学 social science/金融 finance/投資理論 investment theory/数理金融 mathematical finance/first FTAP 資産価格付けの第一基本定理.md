裁定機会の非存在とリスク中立確率の存在は必要十分条件
- n=2 金融資産2つ
    - 利益 gain/payoff
        $$
        r_i = \\
        \left\{
        \begin{matrix}
        r_i(u) & X=u \\
        r_i(d) & X=d
        \end{matrix}
        \right.
        $$
        $$
        r(u) = (r_1(u), r_2(u)) \\
        r(d) = (r_1(d), r_2(d))
        $$
        $$
        r = (r_1, r_2) = (r(u), r(d))^\top \\ =
        \begin{pmatrix}
        r_1(u) & r_2(u) \\
        r_1(d) & r_2(d)
        \end{pmatrix}
        $$
    - 出来高 volume
        $$
        x = (x_1, x_2) \in \R^2
        $$
    $$
    R = r \cdot x^\top = \\
    \begin{pmatrix}
    r_1(u) & r_2(u) \\
    r_1(d) & r_2(d)
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\
    x_2
    \end{pmatrix}
    \\
    \begin{pmatrix}
    x_1 r_1(u) + x_2 r_2(u) \\
    x_1 r_1(d) + x_2 r_2(d)
    \end{pmatrix} 
    $$
    $$
    $$
    - risk neutral probability
        $$
        p =(p_u, p_d) \in \R^2 \\
        p_u + q_d =1
        $$
        $$
        p \cdot r = \\ 
        (p_u r_1(u) + p_dr_1(d), \\
        p_u r_2(u) + p_d r_2(d)) \\
        = (0,0)
        $$
    - 裁定 sure win strategy
        $$
        R > \vec 0 \lor R < \vec 0
        $$
