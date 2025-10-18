



- 完備内積空間 Hilbert space
    完備な内積空間
- 中線定理 parallelogram low
    $$
    \|x+y\|^2 + \|x-y\|^2 = 2(\|x\|^2+\|y\|^2)
    $$
- T_0空間 Kolmogorov space
    - topological space (X, O)
    $$
     \exist \mathcal O_x \subset \mathcal O, x \in \mathcal O_x \land y \notin \mathcal O_x
    \\ \lor \\
     \exist \mathcal O_y \subset \mathcal O, x \notin \mathcal O_y \land y \in \mathcal O_y
    $$
    ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%207.png)
- T_1空間 Frechet space
    - topological space
    $$
     \exist \mathcal O_x \subset \mathcal O, x \in \mathcal O_x \land y \notin \mathcal O_x
    \\ \land \\
     \exist \mathcal O_y \subset \mathcal O, x \notin \mathcal O_y \land y \in \mathcal O_y
    $$
    ![image.png](image%208.png)
    - 一点集合は閉集合
- T_2空間 Hausdoff space
    - topological space (X, O)
    $$
     \exist \mathcal O_x, \mathcal O_y \subset \mathcal O, \mathcal O_x \cup \mathcal O_y = \phi \\ (x \in \mathcal O_x \land y \notin \mathcal O_x)
    \land
    (x \notin \mathcal O_y \land y \in \mathcal O_y)
    $$
    ![image.png](image%209.png)
- Sierpinski space
    $$
    X= \{0, 1\} \\
    \mathcal O = \{\phi, \{0\}, X\}
    $$
- 包含関係
    - 位相空間
        - 距離空間
            - ノルム空間
                - 内積空間
                    - ノルム空間+中線定理=内積
        - T_0空間
        - T_1空間
        - T_2空間
    - 内積空間はノルム空間
    - ノルム空間は距離空間
    - 距離空間は位相空間
- 位相空間の例
    - {a, b, c}
    - 離散空間
    - 密着空間
    - 実数空間
    - 特定点位相
    - 除外点位相
    - p乗可積分空間
- 図形
    - simplex
        ![IMG_7144.jpeg](IMG_7144.jpeg)
    - フラクタル fractal
        - ジルピンスキーの三角形
        - コッホ曲線
        - Weierstrass function
        - 規模一定 scale invariance
            - self-similarity
                $$
                f(\lambda x) = \lambda^\Delta f(x)
                $$
            - stochastic process
                $$
                P(\lambda x) = \lambda^{-\Delta} P(x)
                $$
                \Delta = -1 : pink noise
                \Delta = -2 : brownian noise 
            - tweedie distributions
            $$
            Var(Y) = \sigma^2 E[Y]^p
            $$
    - 多面体の双対
        面の重心を頂点とし辺で接する面同士の重心を辺で結ぶ
        - 正四面体=正四面体
        - 正六面体=正八面体
        - 正十二面体=正二十面体
- 不動点定理
    - ブラウワーの不動点定理
    - 角谷の不動点定理
    - **Borsuk–Ulam theorem**
- 射影幾何学