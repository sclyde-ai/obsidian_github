入力ｘから有限個の離散値の出力yを推定する
- 二値分類 binary classification
- 多値分類 
分類 classification
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