- data
    nはデータ数
    pは軸の数
    $$
    X = (x_1,..., x_p) \\
    x_1 = (x_{11},..., x_{n1}) \\
    x_2 = (x_{12},..., x_{n2}) \\
    \vdots \\
    x_p = (x_{1p},..., x_{np})
    $$
    $$
    Y = (y_1,..., y_p) \\
    y_1 = (y_{11},..., y_{n1}) \\
    y_2 = (y_{12},..., y_{n2}) \\
    \vdots \\
    y_p = (y_{1p},..., y_{np}) 
    $$
    - 係数
        $$
        a = (a_1,..., a_p) \\
        b = (b_1,..., b_p)
        $$
    - 分散共分散行列
        $$
        S_{xx} = \frac{1}{n}X\cdot X^\top \\
        S_{yy} = \frac{1}{n}Y\cdot Y^\top \\
        S_{xy} = \frac{1}{n}X\cdot Y^\top
        $$
$$
\max\ a^\top S_{xy}b\ \\ 
s.t.\\ a^\top S_{xx}a = 1\\
b^\top S_{yy}b=1
$$
- 意味 meaning
    2つの変数群の相関係数を最大化
    $$
    r_{xy} = \frac{a^\top S_{xy}b}{\sqrt{a^\top S_{xx}a\ b^\top S_{yy}b}}
    $$
    aとbはいくらでも大きく出来るので
    $$
    a^\top S_{xx}a = 1 \\
    b^\top S_{yy}b=1
    $$
    を制約条件とする
- 解法 solution
    Lagrange multiplier 
    $$
    F(a, b, \lambda_1, \lambda_2) = a^\top S_{xy}b-\frac{\lambda_1}{2}(a^\top S_{xx}a-1)-\frac{\lambda_2}{2}(b^\top S_{xx}b-1)
    $$
    $$
    \frac{\partial F}{\partial a} = S_{xy}b -\lambda_1S_{xx}a = 0 \\
    \frac{\partial F}{\partial b} =
    S_{xy}^\top a -\lambda_2S_{yy}b = 0
    $$