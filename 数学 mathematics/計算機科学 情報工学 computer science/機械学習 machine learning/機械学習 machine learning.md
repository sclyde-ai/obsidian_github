1. 報酬関数/誤差関数を決める
2. 使う関数を決める
3. 報酬関数/誤差関数を最大化するパラメータを探す(学習)
    
- 模型評価 model assessment/evaluation
    - 汎用性/汎化性能 generalization
        未知の新しいデータに対しても正確な予測や分類を行える能力
    - 過学習 overfitting
        機械学習モデルが訓練データに過剰に適合し、その結果として未知のデータ（検証データ）に対する予測精度が低下してしまう現象
    - 
    - 
    - 
    - bias-variance tradeoff
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
    - PAC probably approximately correct
        $$
        \mathbb P(\mathbb E [])
        $$
    - 表現力と解釈性
        表現力と解釈性は両立不可能
- problem
    - 勾配消失 vanishing gradient
    - no free lunch theorem
        汎用性と最適性は両立不可能
    - 幻覚 hallucination
        事実でない情報や存在しない情報を本物のように出力すること
        - RAG retrieval augmented generation 検索拡張性能
        - fine turning
    - Potemkin understanding
- prompt engineering
    生成AIに期待通りの正確な回答やコンテンツを生成させるために、prompt (AIへの指示文) を設計・最適化する技術や手法
- model tuning/hyper-parameters tuning 模型調整
    - hyper-parameter
    - fine tuning
    - grid search
    - random search
- swarm AI 群集合人口知能
- pre-training
- post-training