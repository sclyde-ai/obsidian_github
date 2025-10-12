1. 報酬関数/誤差関数を決める
2. 使う関数を決める
3. 報酬関数/誤差関数を最大化するパラメータを探す(学習)
- 学習手法 learning method
    - 教師あり学習 supervised learning
    - 教師なし学習 unsupervised learning
    - 回帰 regression
        - 定式化 formulation
            - 入力/説明変数
                $$
                x = (x_1, x_2, ..., x_n) \in \R^n
                $$
            - 出力/目的変数
                $$
                y = (y_1, y_2,...,y_m) = f(x) \in \R^m
                $$
            - 回帰式
                $$
                f : \R^n \to \R^m
                $$
            - 教師データ
                $$
                t = (t_1, t_2,...,t_m)
                $$
    - 分類 clustering/grouping
        - 定式化 formulation
            - 分類数
                $$
                m \in \N
                $$
            - 入力
                $$
                x = (x_1, x_2, ..., x_n)
                $$
            - 出力/label
                $$
                y = (y_1,y_2,..., y_n) \in \{1,2,...,m\}^n
                $$
            - 分類
                $$
                C: \R^n \to \{1,2,...,m\}^n
                $$
            - 教師データ
                $$
                t = (t_1, t_2,...,t_n) \in \{1,2,...,m\}^n
                $$
        - 教師あり学習 supervised learning
        - 教師なし学習 unsupervised learning
            - 階層的
                - ward method
                - 最短距離法
                - 最長距離法
                - 重心法
                - 群平均法
                - dendrogram
            - 非階層的
                - 混合正規模型 GMM Gaussian mixed model
                - DBSCAN
                - meanshift
                - 超体積法
            - 異常値検出
    - models
- 関数 function
    - 活性化関数 activation function
        - ridge function
            $$
            f : \R^d \to \R
            $$
        - step
            $$
            f(x) = 
            \left\{
            \begin{matrix}
            0 & if & x < 0 \\
            1 & if & x \geq0 
            \end{matrix}
            \right.
            $$
        - sigmoid
            $$
            f(x) = \frac{1}{1+\exp(-x)}
            $$
        - identity function 恒等関数
        - step function
        - sigmoid function
            $$
            \sigma(x)= \frac{1}{1+e^{-x}} = \frac{e^x}{1+e^x}
            $$
            ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%203.png)
        - softmax
            $$
            \sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}
            $$
        - tanh
            $$
            \sigma(x)= \frac{e^x-e^{-x}}{e^x+e^{-x}} = \frac{1-e^{-2x}}{1+e^{-2x}}
            $$
            ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%204.png)
        - ReLU Rectified Linear Unit
            $$
            f(x) = 
            \left\{
            \begin{matrix}
            0 & if & x < 0 \\
            x & if & x \geq0 
            \end{matrix}
            \right.
            $$
            $$
            f(x) = \max(0, x) = \frac{x+|x|}{2}
            $$
        - PReLU
        - leakyReLU
        - ELU
        - GELU Gaussian Error Linear Unit
            $$
            f(x) = x \Phi(x)
            $$
            - \Phi 正規分布の累積分布関数
        - Swish
        - Mish
- 模型評価 model assessment/evaluation
    - 汎用性/汎化性能 generalization
        未知の新しいデータに対しても正確な予測や分類を行える能力
    - 過学習 overfitting
        機械学習モデルが訓練データに過剰に適合し、その結果として未知のデータ（検証データ）に対する予測精度が低下してしまう現象
    - 交差検証 CV cross validation
        データを分割して学習と検証を繰り返すこと
        - 排他的 exhaustive
            learn and test on all possible ways to divide the original sample into a training and a validation set
            - leave one out
                1. データを一つ選ぶ
                2. そのデータを検証に使い、他のn-1個を訓練に使う
                3. 全通り(n回)行う
                - gif
                    ![image.gif](image.gif)
            - leave p out
                1. データをp個選ぶ
                2. そのデータを検証に使い、他のn-p個を訓練に使う
                3. 全通り(n!/p!(n-p)!回)行う
        - 非排他的 non-exhaustive
            - 標本分割 holdout
                訓練データと検証データに分割すること
                - 訓練データ train data
                    模型の訓練に使うデータ
                - 検証データ test data
                    模型の検証に使うデータ
            - k-分割交差検証 k-fold cross validation
                1. データをk個に分割
                2. 1つを検証に使い、他のk-1個を訓練に使う
                3. 全通り(k回)行う
                - gif
                    ![image.gif](image%201.gif)
            - repeated random sub-sampling validation
    - 正則化 regularization
        - 意味 meaning
            - 日本語
                過学習を防ぎ、モデルの汎化能力を高めるための手法
            - English
                a technique to reduce overfitting in machine learning models by adding a penalty to the loss function
        $$
        \min_w E(w) + \lambda R(w)
        $$
        - E 誤差項
        - R 正則化項
        - L1正則化/LASSO回帰
            - 正則化項
                $$
                R(w) = \sum_j w_j^2
                $$
            - 解
                $$
                \sum_j w_j^2 =r
                $$
        - L2正則化/Ridge回帰
            - 正則化項
                $$
                R(w) = \sum_j |w_j|
                $$
            - 解
                $$
                \sum_j |w_j|=r
                $$
    - 決定境界 decision boundary
        機械学習の分類問題において、異なるクラスを明確に分けるための境界線や超曲面のこと
        the hypersurface that divides a feature space, separating different classes in a classification model by defining the points where the model switches from predicting one class to another
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