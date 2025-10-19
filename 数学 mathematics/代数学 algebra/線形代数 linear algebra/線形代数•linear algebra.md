    - 直接法
        - LU分解
            $$ A = LU $$
            - L 下三角行列
            - U 上三角行列
            - 分解可能条件
                - 行列Aが正則
                - 首座小行列が非ゼロ
            - ガウス消去法/Doolittle method
            - Cholesky分解
            - Crout method
        - ガウス消去法
        - ヤコビ消去法
        - クリノフ部分空間
    - 行列ベクトルの演算の計算量
        - ベクトルの内積 O(n)
        - 行列ベクトル積 O(n^2)
        - 行列積 O (n^3)
        - ベクトル和 O(n)
    - 定常反復法
        - ヤコビ法
        - Gausss-Seide法
        - SOR法
        - SSOR法
    - 非定常反復法
        - 共益勾配
        - 相共益勾配
        - 一般最小残差
    - stream
        ```mermaid
        graph TB
        減少 --> 数理モデル-->近似方程式-->近似解-->理解予測
        数理モデル-->厳密解-->理解予測
        ```
- 
- 
- 
- ベクトル空間の双対
    - vector space V
    $$ V^* := \{f : V \to \R^n| f: linear\ mapping\} \\ (f+g)(x) = f(x) + g(x) \\ (\alpha f)(x) = \alpha f(x) $$
    V^* is a linear space
    - proof
        - 加法
            - 結合律
                $$ (f + (g + h))(x) = ((f + g) + h)(x) $$
                $$ (f + (g + h))(x) = f(x) + (g+h)(x) \\ = f(x) + g(x) + h(x) \\ = (f+g)(x) + h(x) $$
            - 単位元
            - 逆元
            - 交換律
        - scalar倍
            - 結合律
            - 分配律1
            - 分配律2