pは説明変数の数
- data
    nはデータ数
    pは軸の数
    $$
    x_1 = (x_{11},..., x_{n1}) \\
    x_2 = (x_{12},..., x_{n2}) \\
    \vdots \\
    x_p = (x_{1p},..., x_{np}) 
    $$
    - p = 2
        $$
        x_1 = (x_{11},..., x_{n1}) \\
        x_2 = (x_{12},..., x_{n2})
        $$
- 主成分
    - p = 2
        $$
        z_1 = a_1 u_1 + a_2 u_2
        $$
        - 標準化
            $$
            u_1 = \frac{x_1 - \bar{x}_1}{s_1}, \ u_2 = \frac{x_2 - \bar x_2}{s_2}
            $$
        - 分散の最大化
            $$
            \max_{a_1, a_2} Var(z_1) \ s.t. \ a_1^2+a_2^2 =1 
            $$
            $$
            Var(z_1)=
            \frac{1}{n-1} \sum (z_{i1}-\bar{z_1})^2 = \\
            \frac{1}{n-1} \sum z_{i1}^2 = \\
            \frac{1}{n-1} \sum(a_1u_1 + a_2u_2)^2 = \\
            \frac{1}{n-1}\{a_1^2 \sum u_{i1}^2 + 2a_1a_2 \sum u_{i1}u_{i2} + a_2^2 \sum u_{i2}^2\} = \\
            a_1^2+a_2^2 + 2r_{x_1 x_2}a_1 a_2
            $$
            $$
            a_1 + r_{x_1x_2}a_2 - \lambda a_1 = 0 \\
            r_{x_1 x_2} a_1 + a_2 - \lambda a_2 = 0 \\
            r_{x_1x_2}\frac{a_2}{a_1}=\lambda-1 \\
            r_{x_1x_2}\frac{a_1}{a_2}=\lambda-1 \\
            a_1^2 = a_2^2
            $$
            - Lagrange multiplier
            $$
            F(a_1, a_2, \lambda) = a_1^2+a_2^2 + 2r_{x_1 x_2}a_1 a_2 - \lambda(a_1^2 + a_2^2-1)
            $$
- 寄与率・累積寄与率
    - p = 2
- 因子負荷量
- 主成分得点