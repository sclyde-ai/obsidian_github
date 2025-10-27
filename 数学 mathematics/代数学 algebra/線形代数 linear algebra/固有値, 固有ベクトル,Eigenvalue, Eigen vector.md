---
alias:
    ['固有値', '固有ベクトル', 'Eigenvalue Eigen vector']
---
$$ A \vec x = \lambda \vec x $$
    $\lambda$ is the eigenvalues of A
    x is the eigen vector of A
    - meaning
        - 線形変換Aに対し向きが変化しないベクトルxとその倍率 $\lambda$
    - solution
        $$ \det(A-\lambda I) = 0 $$
        を解くと固有値が求まる
        $$ (A-\lambda I) \vec x = 0 $$
        となるxは $\lambda$ の固有ベクトル
    - theorem
        - trace
        - determinant
        - similar
    - 固有空間 eigen space
        $$ W_\lambda = \{\vec x | A\vec x = \lambda \vec x\} $$
    - 固有多項式 eigen polynomial
        $$ \det(A-\lambda I)=0 $$