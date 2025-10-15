
    - マハラノビス距離
    - 誤判別の確率
    - 変数選択
    - fisher線形判別分析
        群間分散/郡内分散の最大化
        $$
        \max_{w}\ \frac{w^T S_B w}{w^T S_W w}\\ s.t.\ w^Tw = 1
        $$
        $$
        \hat w = S^{-1}(\bar x^{(1)}-\bar x^{(2)})
        $$
        - $S_B$ 群間共分散行列
            $$
            (\bar x^{(1)}-\bar x^{(2)})^T(\bar x^{(1)}-\bar x^{(2)})
            $$
        - $S_W$郡内共分散行列
            $$
            S_W = \frac{1}{n_1+n_2-2}((n_1-1)S_1+(n_2-1)S_2)
            $$
        - solution
            $$
            \hat w = S^{-1}(\bar x^{(1)}-\bar x^{(2)})
            $$
            $$
            J(w)=\frac{w^T S_B w}{w^T S_W w}
            $$
            $$
            \frac{\partial J(w)}{\partial w} = 
            $$
        - fisher linear discriminant function
            $$
            f(x)= \hat w^T x - \frac{1}{2}(\bar x^{(1)}-\bar x^{(2)})^TS^{-1}(\bar x^{(1)}-\bar x^{(2)})
            $$