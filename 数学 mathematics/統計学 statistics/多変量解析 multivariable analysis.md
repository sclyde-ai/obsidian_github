
    - 
    -
    - 
    - 
    - 
- 
- 主成分分析 PCA principal component analysis
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
- 多次元尺度構成法
- 正準相関分析 CCA canonical correlation analysis
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
- 数量化理論 quantification theory
    質的変数を数値化する手法
    - 数量化一類=回帰分析
    - 数量化二類=判別分析
    - 数量化三類=主成分分析
    - 数量化四類=多次元尺度構成法