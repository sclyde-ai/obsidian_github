 
    - スカラー scalar
        実数
    - ベクトル vector
        線形空間
    - スカラー積 dot product
        $$
        \vec a \cdot \vec b = |\vec a||\vec b|\cos \theta \\ 
        = \sum_{i=1}^n a_i b_i
        $$
    - ベクトル積 cross product
        $$
        \vec a \times \vec b = |\vec a||\vec b|\sin \theta \\ 
        $$
    - ナブラ演算子 labra operator
        $$
        \nabla = (\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z})
        $$
    - 勾配 gradient
        $$
        grad f = \nabla f
        $$
        スカラー場fの変化が最大となるベクトル
    - 発散 divergence
        $$
        div A = \nabla \cdot A
        $$
    - 回転 rotation
        $$
        rot A = \nabla \times  A
        $$
    - ストークスの定理
        回転の面積分は境界の線積分
        $$
        \int_S (\nabla \times A)\cdot n\ dS = \oint_C A\ dr
        $$
        Sは積分範囲の面
        \partial Sは境界の曲線
    - ガウスの発散定理
        $$
        \int_S A \cdot n\ dS = \int_V \nabla \cdot A \ dV
        $$