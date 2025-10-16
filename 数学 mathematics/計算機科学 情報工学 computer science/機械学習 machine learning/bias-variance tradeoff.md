
        汎化誤差はbiasとvarianceとerrorに分解できる
        |  | overfitting | underfitting |
        | --- | --- | --- |
        | bias | low | high |
        | variance | high | low |
        - 設定 setting
            - dataset
                $$
                D = \{d_i\}_{i = 1}^m \\
                d_i = ((x_1,y_1),(x_2, y_2),...,(x_n, y_n))
                $$
            - 真のmodel
                $$
                y = f(x)+ \epsilon \\
                \epsilon \sim N(0, \sigma^2)
                $$
            - 予測model
                $$
                \hat f (x; D)
                $$
        - bias
            $$
            Bias[\hat f(x)] = \mathbb E[\hat f(x)] -f(x)
            $$
            予測模型の平均と真の模型の差を表す指標
        - variance
            $$
            Var[\hat f(x)] = \mathbb E[\hat f(x)^2] - \mathbb E[\hat f(x)]^2
            $$
            訓練dataによるばらつきを表す指標
        - bias-variance decomposition
            $$
            \mathbb E[(y-\hat y)^2] 
            =\mathbb E[(y-\hat f)^2] 
            =\mathbb E[(f+\epsilon -\hat f)^2]
            \\
            = \mathbb E[(f+\epsilon -\hat f + \mathbb E[\hat f]- \mathbb E[\hat f])^2]
            \\ 
            = \mathbb E[((f-\mathbb E[\hat f]) + (-\hat f + \mathbb E[\hat f])+\epsilon)^2]
            \\ 
            = \mathbb E[
            (f- \mathbb E[\hat f])^2] 
            + 
            \mathbb E[
            (-\hat f+ \mathbb E[\hat f])^2] 
            + 
            \mathbb E[\epsilon^2] 
            +
            \mathbb E[(f- \mathbb E[\hat f])(-\hat f+ \mathbb E[\hat f])] 
            +
            \mathbb E[\epsilon (f - \mathbb E[\hat f)]] 
            + 
            \mathbb E[\epsilon (- \hat f + \mathbb E[\hat f])]
            \\
            $$
            - $\mathbb E[
            (f- \mathbb E[\hat f])^2]$
                $$
                \mathbb E[
                (f- \mathbb E[\hat f])^2] 
                = (f- \mathbb E[\hat f])^2
                = (\mathbb E[\hat f]-f)^2
                = Bias(\hat f)
                $$
            - $\mathbb E[
            (-\hat f+ \mathbb E[\hat f])^2]$
                $$
                \mathbb E[
                (-\hat f+ \mathbb E[\hat f])^2]=\mathbb E[
                (\hat f- \mathbb E[\hat f])^2] = Var(\hat f)
                $$
            - $\mathbb E[(f- \mathbb E[\hat f])(-\hat f+ \mathbb E[\hat f])]$
                $$
                \mathbb E[(f- \mathbb E[\hat f])(-\hat f+ \mathbb E[\hat f])] \\
                =
                (f- \mathbb E[\hat f])\mathbb E[-\hat f+ \mathbb E[\hat f]] \\
                =
                (f- \mathbb E[\hat f])(-\mathbb E[\hat f]+ \mathbb E[\hat f])
                = 0
                $$
            - $\mathbb E[\epsilon (f - \mathbb E[\hat f])]$
                $$
                \mathbb E[\epsilon (f - \mathbb E[\hat f])]
                =
                \mathbb E [\epsilon]\mathbb E[(f - \mathbb E[\hat f)]] 
                = 0
                $$
            - $\mathbb E[\epsilon (- \hat f + \mathbb E[\hat f])]$
                $$
                \mathbb E[\epsilon (- \hat f + \mathbb E[\hat f])]
                =
                \mathbb E[\epsilon ]\mathbb E[(- \hat f + \mathbb E[\hat f])]
                = 0
                $$
            $$
            = \mathbb E[
            (f- \mathbb E[\hat f])^2] + \mathbb E[
            (-\hat f+ \mathbb E[\hat f])^2] + \mathbb E[\epsilon^2] +
            (f- \mathbb E[\hat f])\mathbb E[(-\hat f+ \mathbb E[\hat f])] 
            +
            \mathbb E[\epsilon]\mathbb E[(f - \mathbb E[\hat f)]] + \mathbb E[\epsilon]\mathbb E[(- \hat f + \mathbb E[\hat f])]
            \\
            = 
            (f- \mathbb E[\hat f])^2 + \mathbb E[
            (\hat f- \mathbb E[\hat f])^2] + \mathbb E[\epsilon^2] +
            (f- \mathbb E[\hat f])(-\mathbb E[\hat f]+ \mathbb E[\hat f]]) 
            \\ 
            = Bias^2(\hat f) + \sigma^2 + Var[\hat f]
            $$