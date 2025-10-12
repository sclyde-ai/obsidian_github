- 相等 equivalent
    $$ A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix} B = \begin{pmatrix} b_{11} & b_{12} & \dots & b_{1n} \\ b_{21} & b_{22} & \dots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{m1} & b_{m2} & \dots & b_{mn} \end{pmatrix} \\ A = B, a_{i, j} = b_{i, j} $$
- 和と差
    $$ A \pm B = \begin{pmatrix} a_{11}+b_{11} & a_{12}+b_{12} & \dots & a_{1n}+b_{1n} \\ a_{21}+b_{21} & a_{22}+b_{22} & \dots & a_{2n}+b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}+b_{m1} & a_{m2}+b_{m2} & \dots & a_{mn}+b_{mn} \end{pmatrix} $$
- scalar multiplication
    $$ kA = \begin{pmatrix} ka_{11} & ka_{12} & \dots & ka_{1n} \\ ka_{21} & ka_{22} & \dots & ka_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ ka_{m1} & ka_{m2} & \dots & ka_{mn} \end{pmatrix} $$
- 形状 shape
    - 正方行列 square
        $(n, n)$ 型行列をn次正方行列という
    - 三角行列 triangular matrix
        - 上三角行列 upper
            $$ \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ & a_{22} & \dots & a_{2n} \\ & & \ddots & \vdots \\ \text{\huge{0}} & & & a_{nn} \end{pmatrix} $$
        - 下三角行列 lower
            $$ \begin{pmatrix} a_{11} & & & \text{\huge{0}} \\ a_{21} & a_{22} \\ \vdots & & \ddots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix} $$
        - 対角行列 diagonal
            $$ \begin{pmatrix} a_{11} \\ & a_{22} & & \text{\huge{0}} \\ & & \ddots \\ & \text{\huge{0}} & & \ddots \\ & & & & a_{nn} \end{pmatrix} $$
    - 転置行列 transpose
        $$ A^\top = \begin{pmatrix} a_{11} & a_{21} & \dots & a_{m1} \\ a_{12} & a_{22} & \dots & a_{m2} \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n} & a_{2n} & \dots & a_{mn} \end{pmatrix} $$
        転置行列は $(n, m)$ 型行列である
        - 性質
            $$ (AB)^\top = B^\top A^\top $$
- 代数的 algebra
    - 零行列 null
        $$ \begin{pmatrix} 0 & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & 0 \end{pmatrix} $$
    - 単位行列 identity
        $$ \begin{pmatrix} 1 & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & 1 \end{pmatrix} $$
    - 正則行列 regular
        $$ AX = XA = I $$
        A is a regular matrix
        X is the inverse matrix of A
        - theorem
            - uniqueness
            - inverse of inverse
                $$ (A^{-1})^{-1} = A $$
                - proof
                    - right
                        $$ (A^{-1})^{-1} A^{-1} = I $$
                        multiple it on the right by A
                        $$ (A^{-1})^{-1} A^{-1} A = I A\\ (A^{-1})^{-1} I = A \\ (A^{-1})^{-1} = A $$
                    - left
                        $$ A^{-1} (A^{-1})^{-1} = I $$
                        multiple it on the right by A
                        $$ A^{-1} (A^{-1})^{-1} = I \\ AA^{-1} (A^{-1})^{-1} = AI \\ (A^{-1})^{-1} = A $$
            - inverse of association
                $$ (AB)^{-1} = B^{-1} A^{-1} $$
                in other words, AB is regular if A & B are regular
                - proof
                    - right
                        $$ (AB)^{-1} AB = I \\ (AB)^{-1} AB B^{-1} = IB^{-1}\\ (AB)^{-1} AI = B^{-1}\\ (AB)^{-1} AA^{-1} = B^{-1}A^{-1}\\ (AB)^{-1} I = B^{-1}A^{-1}\\ (AB)^{-1} = B^{-1}A^{-1}\\
                        $$
                    - left
                        $$ AB(AB)^{-1} = I $$
            - inverse of transpose
                $$ (A^\top)^{-1} = (A^{-1})^\top $$
            - scaler multiplication
                $$ (kA)^{-1} = \frac{1}{k} A^{-1}, k \ne 0 $$
            - qdeterminant of inverse
                $$ \det (A^{-1}) = (\det A)^{-1} $$
            - determinant is not zero
                $$ \det A \ne 0 $$
                if and only if A is regular
            - eigenvalues of inverse
                the eigenvalues of A are $\lambda_1, \lambda_2, ..., \lambda_n$
                then
                the eigenvalues of $A^{-1}$ are $\lambda_1^{-1}, \lambda_2^{-1}, ..., \lambda_n^{-1}$
- 性質 property
    - 対称行列 symmetric
        $$ A^\top = A $$
    - エルミート行列 Hermitian matrix
        $$ \overline A^\top = A $$
        - 随伴行列/エルミート転置 adjoint matrix/Hermitian transpose
            $$ \overline A^\top = \\ A^* = A^\dagger = \begin{pmatrix} \bar a_{11} & \bar a_{21} & \dots & \bar a_{m1} \\ \bar a_{12} & \bar a_{22} & \dots & \bar a_{m2} \\ \vdots & \vdots & \ddots & \vdots \\ \bar a_{1n} & \bar a_{2n} & \dots & \bar a_{mn} \end{pmatrix} $$
        - 性質 property (Hermitian matrix)
            - 正方行列
                $$ A + A^* \\ AA^* $$
                はHermitian行列になる
            - 内積
                $$ \braket {Ax, y} = \braket {x, Ay} $$
            - 行列式は実数
            - 固有値は実数
        - 性質 property (Hermitian transpose)
            - vector
                $$ (A^_)^_ = A \\ (A+B)^* = A^_+B^_ \\ (kA)^* = \bar k A^* $$
            - 正方行列
                - 固有値は元の行列の複素共役
                    $$ \det (\lambda I - A^_) \\ = \det ((\bar \lambda I)^_ - A^_) \\ = \det (\bar \lambda I - A)^_ \\ = \overline{\det(\bar\lambda I - A)^T} \\ = \overline{\det(\bar\lambda I^T - A^T)} \\ = \overline{\det(\bar\lambda I - A^T)} $$
                - 内積
                    $$ \langle Av, w\rangle = \langle v, A^*w \rangle $$
                - 逆行列
                    $$ (A^_)^{-1} = (A^{-1})^_ $$
    - 直交行列 orthogonal
        $$ A^\top = A^{-1} $$
        $$ AA^\top = A^\top A = I $$
    - ユニタリ行列 unitary
        $$ \overline U^\top = U^{-1} $$
        $$ UU^* = U^* U = I_n $$
- 固有 Eigen
    - 相似 similar
        $$ B = P^{-1} A P, \exist P $$
        A and B are similar
        - equivalence relation
            - reflexivity
                $$ A \sim A $$
            - symmetry
                $$ A \sim B \Leftrightarrow B \sim A $$
            - transivity
                $$ A \sim B \land B \sim C \Rightarrow A \sim C $$
                - proof
                    $$ B = P^{-1} A P, C = P^{-1}B P \\ \Rightarrow C = P^{-1} P^{-1}B PP
                    $$
                    P is regular, then PP & P^-1 P^-1 are regular
        - theorem
            - determinant is equivalent
            - rank is equivalent
            - trace is equivalent
            - eigenvalue is equivalent
            - factorial is similar
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