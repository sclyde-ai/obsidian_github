- 
- 
- 
- 形状 shape
    - 
    - 
    - 
- 代数的 algebra
    - 
    - 
    - 
- 性質 property
    - 
    - 
    - 
    - 
- 固有 Eigen
    - 
- 決定 determinant
    - 余因子行列 cofactor
- 凸凹 convex/concave
    - 定値行列 defined
        - 半正定値 positive semi-defined matrix
            $$ A \succeq 0 \\ x^TAx \geq 0, \forall x \in \R^n $$
            Aを半正定値行列という
            - 同値条件
                - 固有値が全て非負
                    $$ v^\top Av = \lambda v^\top v = \lambda \|v\|^2 \geq 0 \\ \lambda \geq 0 $$
                - 主小行列式が全て正
        - 正定値 positive defined matrix
            $$ A \succ 0 \\ x^TAx > 0, \forall x \in \R^n, $$
            Aを正定値行列という
            - 同値条件
                - 固有値が全て正
                    $$ v^T Av = \lambda v^Tv = \lambda \|v\|^2 > 0 \\ \lambda > 0 $$
                - 首座小行列式が全て正
            - theorem
                - 対称性
                    $$ A = A^T $$
        - 半負定値 negative semi-defined matrix
            $$ \forall x \in \R^n, x^TAx \leq 0 $$
            Aを半正定値行列という
            - 同値条件
                - 固有値が全て非正
                - 主小行列式が全て非正
        - 負定値 negative defined matrix
            $$ A \prec 0\\ x^TAx < 0, \forall x \in \R^n $$
            Aを正定値行列という
            - 同値条件
                - 固有値が全て負
                    $$ v^T Av = \lambda v^Tv = \lambda \|v\|^2 \geq 0 \\ \lambda \geq 0 $$
                - 首座小行列式が全て負
            - theorem
                - 対称性
                    $$ A = A^T $$