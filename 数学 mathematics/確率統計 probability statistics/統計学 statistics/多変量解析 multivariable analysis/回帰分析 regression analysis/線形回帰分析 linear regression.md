- data
    nはデータ数
    pは軸の数
    $$
    x_1 = (x_{11},..., x_{n1}) \\
    x_2 = (x_{12},..., x_{n2}) \\
    \vdots \\
    x_p = (x_{1p},..., x_{np}) 
    $$
    $$
    y = (y_1,..., y_n)
    $$
    - 平均
        $$
        \bar x_j = \frac{\sum_{i=1}^n x_{ij}}{n} \\ \bar y = \frac{\sum_{i=1}^n y_i}{n}
        $$
    - 分散共分散行列
        $$
        S_{jk} = S_{x_j x_k} = \frac{1}{n} \sum_{i=1}^n (x_{ij}-\bar x_j)(x_{ik}-\bar x_k)\\
        S_{jy} = S_{x_j y} = 
        \frac{1}{n}\sum_{i=1}^n (x_{ij}-\bar x_j)(y_i-\bar y)
        $$
        $$
        S_{xx} =
        \begin{pmatrix}
        S_{11} & S_{12} & \cdots & S_{1n}\\
        S_{12} & S_{22} & \cdots & S_{2p} \\
        \vdots & \vdots & & \vdots \\
        S_{1p} & S_{2p} & \cdots & S_{pp}
        \end{pmatrix}
        =
        \begin{pmatrix}
        S_{x_1x_1} & S_{x_1x_2} & \cdots & S_{x_1x_n}\\
        S_{x_1x_2} & S_{x_2x_2} & \cdots & S_{x_2x_p} \\
        \vdots & \vdots & & \vdots \\
        S_{x_1x_p} & S_{x_2x_p} & \cdots & S_{x_px_p}
        \end{pmatrix}
        $$
        $$
        S_{xy} = \begin{pmatrix}
        S_{1y} \\
        S_{2y} \\
        \vdots \\
        S_{py}
        \end{pmatrix} 
        = \begin{pmatrix}
        S_{x_1y} \\
        S_{x_2y} \\
        \vdots \\
        S_{x_py}
        \end{pmatrix}
        $$
    - 相関係数行列
    - p = 2
        $$
        x_1 = (x_{11},..., x_{n1}) \\
        x_2 = (x_{12},..., x_{n2})
        $$
- 単or重回帰模型
    - model
        $$
        y_i = \beta_0  + \beta \cdot x_i + \epsilon_i \\
        = \beta_0  + \sum^p_{j=1} \beta_j x_{ij} + \epsilon_i
        $$
        - 回帰係数 regression coefficient
            $$
            \beta = (\beta_1, ..., \beta_p)
            $$
        - 誤差項 error
            $$
            \epsilon_i \sim N(0, \sigma^2)
            $$
        - p = 1
            $$
            y_i = \beta_0  + \beta_1 x_{i} + \epsilon_i
            $$
        - p = 2
            $$
            y_i = \beta_0  + \beta_1 x_{i1} + \beta_1 x_{i2} + \epsilon_i
            $$
    - solution
        $$
        \hat \beta = S_{xy} \cdot S_{xx}^{-1} \\
        \bar y = \hat \beta_0  + \hat \beta \cdot\bar x
        $$
        - 導出
            1. 残差平方和を最小化
                $$
                \min_{\beta} S_e = \min_{\beta} \sum_{i=1}^n\epsilon_i^2 = \min_{\beta} \sum_{i=1}^n(y_i -\beta \cdot  x_i)^2
                $$
            2. 変数を微分
                $$
                \frac{\partial S_e}{\partial \beta_k} = -2\sum_{i=1}^n x_{ik}(y_i - \beta \cdot x_i)=0 
                $$
                $$
                \sum_{i=1}^n x_{ik}\beta \cdot x_i
                = \sum_{i=1}^n x_{ik} y_i
                \\
                \sum_{i=1}^n x_{ik} \sum^p_{j=1} \beta_j x_{ij}
                = \sum_{i=1}^n x_{ik} y_i
                \\
                \sum_{j=1}^p \beta_j\sum_{i=1}^n  x_{ik}x_{ij} = \sum_{i=1}^n x_{ik} y_i
                $$
            3. 正規方程式
                $$
                \begin{pmatrix}
                n & \sum x_{i1} & 
                \cdots &
                \sum x_{ip} \\ 
                \sum x_{i1} & 
                \sum x_{i1} ^2 & 
                \cdots &
                \sum x_{i1} x_{ip} \\
                \vdots & \vdots & & \vdots\\
                \sum x_{ip} & 
                \sum x_{i1} x_{ip} &
                \cdots & 
                \sum x_{ip} ^2\\
                \end{pmatrix}
                \begin{pmatrix}
                \hat\beta_0 \\
                \hat\beta_1 \\
                \vdots \\
                \hat\beta_p
                \end{pmatrix}
                =
                \begin{pmatrix}
                \sum y_i \\
                \sum x_{i1} y_i \\
                \vdots \\
                \sum x_{ip} y_i 
                \end{pmatrix}
                $$
            4. 式変形
                $$
                \bar y = \hat \beta_0  + \sum^p_{j=1} \hat \beta_j \bar x_j
                \\
                \begin{pmatrix}
                S_{11} & S_{12} & \cdots & S_{1n}\\
                S_{12} & S_{22} & \cdots & S_{2p} \\
                \vdots & \vdots & & \vdots \\
                S_{1p} & S_{2p} & \cdots & S_{pp}
                \end{pmatrix}
                \begin{pmatrix}
                \hat\beta_1 \\
                \hat\beta_2 \\
                \vdots \\
                \hat \beta_n
                \end{pmatrix}
                =
                \begin{pmatrix}
                S_{1y} \\
                S_{2y} \\
                \vdots \\
                S_{py}
                \end{pmatrix}
                $$
                $$
                S_{xx} \cdot \hat \beta = S_{xy} \\
                \hat \beta = S_{xy} \cdot S_{xx}^{-1}
                $$
                $$
                \bar y = \hat \beta_0  + \hat \beta \cdot\bar x \\
                \bar y = \hat \beta_0  + S_{xy} \cdot S_{xx}^{-1}\cdot\bar x 
                $$
        - p = 1
            $$
            \begin{pmatrix}
            \hat\beta_0 \\
            \hat\beta_1
            \end{pmatrix}
            =
            \begin{pmatrix}
            \bar y - \frac{S_{xy}}{S_{xx}} \bar x\\
            \frac{S_{xy}}{S_{xx}}
            \end{pmatrix}
            $$
            - 導出
                1. 残差平方和を最大化
                    $$
                    \min_{\beta_0, \beta_1} S_e = \min_{\beta_0, \beta_1} \sum_{i=1}^n\epsilon_i^2 = \min_{\beta_0, \beta_1} \sum_{i=1}^n(y_i - \beta_0 -\beta_1x_i)^2
                    $$
                2. 変数を微分
                    $$
                    \frac{\partial S_e}{\partial \beta_0} = -2\sum_{i=1}^n(y_i - \beta_0 -\beta_1x_i)=0 
                    $$
                    $$
                    \frac{\partial S_e}{\partial \beta_1} = -2\sum_{i=1}^nx_i(y_i - \beta_0 -\beta_1x_i)=0
                    $$
                3. 正規方程式
                    $$
                    n\hat\beta_0 + \hat\beta_1\sum_{i=1}^n x_i = \sum_{i=1}^n y_i
                    $$
                    $$
                    \hat\beta_0 \sum_{i=1}^n x_i + \hat\beta_1 \sum_{i=1}^n x_i^2  = \sum_{i=1}^n x_i y_i
                    $$
                    $$
                    \begin{pmatrix}
                    n & \sum_{i=1}^n x_i \\
                    \sum_{i=1}^n x_i & \sum_{i=1}^n x_i ^2
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \sum_{i=1}^n y_i \\
                    \sum_{i=1}^n x_i y_i 
                    \end{pmatrix}
                    $$
                4. 式変形
                    $$
                    \begin{pmatrix}
                    \sum_{i=1}^n x_i & \frac{(\sum_{i=1}^n x_i)^2}{n} \\
                    \sum_{i=1}^n x_i & 
                    \sum_{i=1}^n x_i ^2
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \frac{\sum_{i=1}^n x_i 
                    \sum_{i=1}^n y_i}{n} \\
                    \sum_{i=1}^n x_i y_i 
                    \end{pmatrix}
                    $$
                    $$
                    \begin{pmatrix}
                    1 & \frac{\sum_{i=1}^n x_i}{n}  \\
                    0 & 
                    \sum_{i=1}^n x_i ^2 - \frac{(\sum_{i=1}^n x_i)^2}{n}
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \frac{\sum_{i=1}^n y_i}{n} \\
                    \sum_{i=1}^n x_i y_i - \frac{\sum_{i=1}^n x_i 
                    \sum_{i=1}^n y_i}{n}
                    \end{pmatrix}
                    $$
                    $$
                    \begin{pmatrix}
                    1 & \bar x \\
                    0 & 
                    S_{xx}
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \bar y \\
                    S_{xy}
                    \end{pmatrix}
                    $$
                    $$
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \bar y - \frac{S_{xy}}{S_{xx}} \bar x\\
                    \frac{S_{xy}}{S_{xx}}
                    \end{pmatrix}
                    $$
        - p = 2
            $$
            \begin{pmatrix}
            \hat\beta_0 \\
            \hat\beta_1 \\
            \hat\beta_2
            \end{pmatrix}
            =
            \begin{pmatrix}
            \bar y - \hat\beta_1 \bar x_{1} + \hat\beta \bar x_{2} \\
            \frac{S_{11}S_{1y}-S_{12}S_{2y}}{S_{11}S_{22}-S_{12}^2}
            \\
            \frac{-S_{12}S_{1y} + S_{22}S_{2y}}{S_{11}S_{22}-S_{12}^2}
            \end{pmatrix}
            $$
            - 導出
                1. 残差平方和を最小化
                    $$
                    \min_{\beta_0, \beta_1} S_e = \min_{\beta_0, \beta_1} \sum_{i=1}^n\epsilon_i^2 = \min_{\beta_0, \beta_1} \sum_{i=1}^n(y_i - \beta_0 -\beta_1x_{i1} - \beta_2 x_{i2})^2
                    $$
                2. 変数を微分
                    $$
                    \frac{\partial S_e}{\partial \beta_0} = -2\sum_{i=1}^n(y_i - \beta_0 -\beta_1 x_{i1} - \beta_2 x_{i2})=0 
                    $$
                    $$
                    \frac{\partial S_e}{\partial \beta_1} = -2\sum_{i=1}^n x_{i1}(y_i - \beta_0 -\beta_1 x_{i1} - \beta_2 x_{i2})=0 
                    $$
                    $$
                    \frac{\partial S_e}{\partial \beta_2} = -2\sum_{i=1}^n x_{i2}(y_i - \beta_0 -\beta_1 x_{i1} - \beta_2 x_{i2})=0 
                    $$
                3. 正規方程式
                    $$
                    n\hat\beta_0 + 
                    \hat\beta_1 \sum x_{i1} +
                    \hat\beta_2 \sum x_{i2} = 
                    \sum y_i
                    $$
                    $$
                    \hat\beta_0 \sum x_{i1} + \hat\beta_1 \sum x_{i1}^2 +
                    \hat\beta_2 \sum x_{i1}x_{i2} = \sum x_{i1} y_i
                    $$
                    $$
                    \hat\beta_0 \sum x_{i2} + \hat\beta_1 \sum x_{i1}x_{i2} +
                    \hat\beta_2 \sum x_{i2}^2 = 
                    \sum x_{i2} y_i
                    $$
                    $$
                    \begin{pmatrix}
                    n & \sum x_{i1} & 
                    \sum x_{i2} \\ 
                    \sum x_{i1} & 
                    \sum x_{i1} ^2 & 
                    \sum x_{i1} x_{i2} \\
                    \sum x_{i2} & 
                    \sum x_{i1} ^2 & 
                    \sum x_{i2} ^2\\
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1 \\
                    \hat\beta_2
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \sum y_i \\
                    \sum x_{i1} y_i \\
                    \sum x_{i2} y_i 
                    \end{pmatrix}
                    $$
                4. 式変形
                    $$
                    \begin{pmatrix}
                    1 & \frac{\sum x_{i1}}{n} & 
                    \frac{\sum x_{i2}}{n} \\ 
                    0 & 
                    \sum x_{i1}^2 - \frac{(\sum x_{i1})^2}{n} & 
                    \sum x_{i1} x_{i2} - \frac{\sum x_{i1}\sum x_{i2}}{n} \\
                    0 & 
                    \sum x_{i1} x_{i2} - \frac{\sum x_{i1}\sum x_{i2}}{n} & 
                    \sum x_{i2}^2 - \frac{(\sum x_{i2})^2}{n} \\
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1 \\
                    \hat\beta_2
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \frac{\sum y_{i}}{n} \\
                    \sum x_{i1} y_i - \frac{\sum x_{i1}\sum y_{i}}{n}\\
                    \sum x_{i2} y_i - \frac{\sum x_{i2}\sum y_{i}}{n}
                    \end{pmatrix}
                    $$
                    $$
                    \begin{pmatrix}
                    1 & \bar x_1 & \bar x_2 \\
                    0 & S_{11} & S_{12} \\
                    0 & S_{12} & S_{22}
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_0 \\
                    \hat\beta_1 \\
                    \hat\beta_2
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    \bar y \\
                    S_{1y} \\
                    S_{2y}
                    \end{pmatrix}
                    $$
                    $$
                    \begin{pmatrix}
                    S_{11} & S_{12} \\
                    S_{12} & S_{22}
                    \end{pmatrix}
                    \begin{pmatrix}
                    \hat\beta_1 \\
                    \hat\beta_2
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    S_{1y} \\
                    S_{2y}
                    \end{pmatrix}
                    $$
                    $$
                    \begin{pmatrix}
                    \hat\beta_1 \\
                    \hat\beta_2
                    \end{pmatrix}
                    =
                    \begin{pmatrix}
                    S_{11} & S_{12} \\
                    S_{12} & S_{22}
                    \end{pmatrix}^{-1}
                    \begin{pmatrix}
                    S_{1y} \\
                    S_{2y}
                    \end{pmatrix}
                    =
                    \frac{1}{S_{11}S_{22}-S_{12}^2}
                    \begin{pmatrix}
                    S_{11} & -S_{12} \\
                    -S_{12} & S_{22}
                    \end{pmatrix}
                    \begin{pmatrix}
                    S_{1y} \\
                    S_{2y}
                    \end{pmatrix}
                    =
                    \frac{1}{S_{11}S_{22}-S_{12}^2}
                    \begin{pmatrix}
                    S_{11}S_{1y} - S_{12}S_{2y} \\
                    -S_{12}S_{1y} + S_{22}S_{2y}
                    \end{pmatrix}
                    $$
            - 多重共線性
                $$
                S_{11}S_{22}-S_{12}^2 = 0
                $$
                $$
                \frac{S_{12}^2}{S_{11}S_{22}} = r_{x_1 x_2}^2  = 1
                $$
                相関係数が+-1に近い場合、解が不安定になる
    - 予測値
        $$
        \hat y = \{\hat y_1, \hat y_2, ..., \hat y_n\}
        $$
        - theorem1
            $$
            \sum_{i=1}^n (y_i-\hat y_i) = 0 
            $$
        - theorem2
            $$
            \sum_{i=1}^n (y_i-\bar y)(\hat y_i-\bar  y) = \sum_{i=1}^n (\hat y_i-\bar  y)^2 = S_R
            $$
            - proof
                - p=1
                    $$
                    \sum_{i=1}^n (y_i-\bar y)(\hat y_i-\bar  y) \\
                    = \sum_{i=1}^n (y_i-\bar y)(\beta_1(x_i-\bar x)) \\
                    = \beta_1 \sum_{i=1}^n (y_i-\bar y)(x_i-\bar x)
                    $$
        - 観測値の平均と予測値の平均は等しい
            $$
            \bar y = \bar {\hat y}
            $$
            - proof
                最小二乗法より
                $$
                \sum_{i=1}^n (y_i-\hat y_i) = 0 \\
                \sum_{i=1}^n y_i= \sum_{i=1}^n \hat y_i 
                \\
                \frac{1}{n} \sum_{i=1}^n y_i= \frac{1}{n} \sum_{i=1}^n \hat y_i 
                $$
- 回帰統計量
    - 平方和 square sum
        - 全平方和/全変動 SST total sum of square
            $$
            S_T =S_{yy}=\sum(y_i - \bar y)^2 
            $$
        - 回帰平方和/回帰変動 SSR regression sum of square
            $$
            S_R=\sum(\hat y_i - \bar y)^2 
            $$
            - 回帰係数
                $$
                S_R = \hat \beta \cdot S_{xy}  = \sum_{i=1}^p \hat\beta_i S_{iy}
                $$
        - 残差平方和/残差変動 SSE residual sum of square
            $$
            S_e=\sum(y_i - \hat y_i)^2
            $$
            - 最小値
                $$
                S_e =  S_{yy}- \hat \beta \cdot S_{xy} 
                $$
                - p = 1
                    $$
                    S_e = S_{yy}-\hat\beta_1S_{xy}
                    $$
                - p = 2
                    $$
                    S_e = S_{yy}-\hat\beta_1S_{1y}-\hat\beta_2S_{2y}
                    $$
        - 平方和の分解
            $$
            S_T = S_R + S_e
            $$
    - 自由度
        |  | 全変動 | 回帰変動 | 残差変動 |
        | --- | --- | --- | --- |
        | 自由度 | n-1 | p | n-p-1 |
        $$
        \phi_T = \phi_R + \phi_e
        $$
    - 重相関係数 multiple correlation coefficient
        観測値と予測値の相関
        $$
        R  = 
        \frac{\sum_{i=1}^n (y_i-\bar y)(\hat y_i-\bar {\hat y})}
        {\sqrt{\sum_{i=1}^n (y_i-\bar y)^2 
        \sum_{i=1}^n (\hat y_i-\bar {\hat y})^2}}
        \\ =
        \frac{\sum_{i=1}^n (y_i-\bar y)(\hat y_i-\bar  y)}
        {\sqrt{\sum_{i=1}^n (y_i-\bar y)^2 
        \sum_{i=1}^n (\hat y_i-\bar y)^2}}
        \\ = \frac{S_R}{\sqrt{S_R S_T}}
        $$
    - 決定係数/寄与率
        全変動の中の回帰式で説明できる変動の割合
        $$
        R^2 = \frac{S_R}{S_T} = 1-\frac{S_e}{S_T}
        $$
        - 自由度修正済
            $$
            R^{*2} = 1-\frac{S_e/\phi_e}{S_T/\phi_T}
            $$
        - 自由度二重修正済
            $$
            R^{**2} = 1-\frac{\frac{n+p+1}{n-p-1}S_e}{\frac{n+p}{n-1}S_T}
            $$
    - 分散拡大係数 VIF variance inflation factor
- 説明変数の選択（重回帰分析）
    - model 0
        $$
        model[0] : y_i = \beta_0 + \epsilon_i
        $$
        $$
        S_{e(M[0])} = S_{yy}　 \phi_{e(M[0])} = \phi_T
        $$
    - model k
        $$
        model[k] : y_i = \beta_0 + \sum_{j=1}^k \beta_jx_{ij} +  \epsilon_i
        $$
        $$
        model[k+1]_{reg}:y_i = \hat \beta_0 + \sum_{j=1}^k \hat \beta_j x_{ij} + \hat \beta_l x_{il}
        $$
        $$
        F_k = \\
        \frac{S_{R(M[k+1]_{reg})}/\phi_{R(M[k+1]_{reg})}}{S_{e(M[k+1]_{reg})}/\phi_{e(M[k+1]_{reg})}}
        = \\
        \frac{(S_{e(M[k])}-S_{e(M[k+1]_{reg})})/(\phi_{e(M[k])}-\phi_{e(M[k+1]_{reg})})}{S_{e(M[k+1]_{reg})}/\phi_{e(M[k+1]_{reg})}}
        \sim F(\phi_{e(M[0])}-\phi_{e(M[1]_{reg})}, \phi_{e(M[1]_{reg})})
        $$
        $$
        \phi_{e(M[k])}-\phi_{e(M[k+1]_{reg})}=1
        $$
        $$
        F_0 = 
        \frac{(S_{e(M[k])}-S_{e(M[k+1]_{reg})})/1}{S_{e(M[k+1]_{reg})}/\phi_{e(M[k+1]_{reg})}}
        \sim F(1, \phi_{e(M[1]_{reg})})
        $$
        分散比F_kが最大となる変数を取り込む
- 誤差の母分散の推定値
    $$
    Var(\epsilon) = \hat\sigma^2 =\frac{S_e}{\phi_e}
    $$
- 回帰係数の検定と推定
    母平均の検定
    - 回帰係数は正規分布従う
        $$
        \hat \beta_1 \sim N(\beta_1, \frac{\sigma^2}{S_{xx}})
        $$
        $$
        u = \frac{\hat \beta_1 - \beta_1}{\sqrt{\sigma^2/S_{xx}}} \sim N(0, 1^2)
        $$
    - t統計量
        $$
        t = \frac{\hat \beta_1 - \beta_1}{\sqrt{\frac{\hat \sigma^2}{S_{xx}}}}\sim t(\phi_e)
        $$
- 分散
    $$
    (t(\phi, P))^2 = F(1, \phi; P)
    $$
    $$
    F_0 = t_0^2=\frac{\hat \beta_1^2}{\frac{\hat \sigma^2}{S_{xx}}}=\frac{S_R}{\hat \sigma^2} \geq F(1, \phi; \alpha)
    $$
- 残差とテコ比
    - 標準化残差
        $$
        \frac{e_k}{\hat \sigma}
        $$
    - テコ比 leverage
        $$
        h_{kk} = \frac{1}{n} + \frac{D_k^2}{n-1}
        $$