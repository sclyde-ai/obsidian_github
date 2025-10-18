
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