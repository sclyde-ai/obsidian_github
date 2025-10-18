
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