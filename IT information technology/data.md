- word dictionary
    - data
        - Oxford
        - Cambridge
        - wikipedia
        - IBM
        - etymology
            the plural form of datum
            - datum
                the neuter past participle of “dare”
                - dare
                    to give
            - something given
            - facts that are given
    - data analysis
        - the process
        - using data
        - for decision-making
        - wiki
            the process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making 
        - Cambridge
            the process of examining information, especially using a computer, in order to find something out, or to help with making decisions.
        - cousera
            the process of working with data to derive useful information, which can then be used to make data-informed decisions.
    - data mining
        - extract information
        - from large data
        - wiki
            the process of extracting and finding patterns in massive data sets involving methods at the intersection of machine learning, statistics, and database system
        - Cambridge
            the process of using special software to look at large amounts of computer data in order to find out useful information.
        - Oxford
            the practice of analysing large databases in order to generate new information.
    - data science
        - wiki
            a concept to unify statistics, data analysis, informatics, and their related methods to understand and analyze actual phenomena with data.
        - IBM
            Data science combines math and statistics, specialized programming, advanced analytics, artificial intelligence (AI) and machine learning with specific subject matter expertise to uncover actionable insights hidden in an organization’s data. 
        - cousera
            Data science is the scientific study of data. Data scientists ask questions and find ways to answer those questions with data. They may work on capturing data, transforming raw data into a usable form, analyzing data, and creating predictive models.
    - 統計 statistics
        - 集団の
        - 特性を
        - 数量的に
        - 計ること
        - def (English)
            - Oxford
                **the practice or science of collecting and analysing numerical data in large quantities, especially for the purpose of inferring proportions in a whole from those in a representative sample**
            - Cambridge
                a collection of numerical facts or measurements, as about people, business conditions, or weather
    - data
        - big data
            - 4V
                - volume
                - velocity
                - variety
                - veracity
        - data mining
            仮説を発見
            - CRISP-DM CRoss Industry Standard Process for Data Mining
                - Business Understanding
                - Data Understanding
                - Data Preparation
                - Modeling
                - Evaluation
                - Development
        - 外れ値 outlier
            データの大部分から外れた値
            - 異常値
                原因が特定できる外れ値
        - 欠損値 missing value/data
            - 無作為 random
                - MCAR missing completely at random
                    無作為に発生
                - MAR missing at random
                    欠損値の有無がその変数に非依存
                    - example
                        - 女性の多くが年齢について無回答
            - 非無作為 not random
                - MNAR missing not at random
                    欠損値の有無がその変数に依存
                    - example
                        - 年収が低いほど無回答
            - 処理方法
                - 除外
                    - list wise
                        行単位で除外
                    - pair wise
                        用いる変数のみ着目して除外
                - 補完
                    - 単一代入
                        - 平均/中央値代入
                        - 回帰代入
                        - 確率的回帰代入
                        - 符号化 encoding
                    - 多重代入
                    - フーリエ変換による欠損値補間
        - データ加工 data processing
            - 分析対象データの選択
                - noise data の除外
                - 属性ごとに分類
                - 不均衡データのbalancing
            - 説明変数の追加・除外
                - dummy 変数化
                    - 連続値化 label encoding
                    - 横持ち化 one hot encoding
                - category 化
                - 多重共線性の高い変数の除外
            - 目的変数の変更
            - algorithmの選択
            - 横方向の増減
                - データの統合
            - 縦方向の増減
                - cleansing
                - sampling
        - 構造 structure
            あらかじめ定義された形式
            - 構造化データ structured data
                あらかじめ定義された形式（構造）で整理されたデータ。
                データを人間や機械が効率的に理解・処理できる。
            - 非構造化データ unstructured data
                あらかじめ定義された形式やスキーマ（構造）を持たないデータ。
        - 不均衡データ
            - balancing
                - sampling
                    - under sampling
                    - over sampling
                - weighting
- 実学 practical science
    - fermi problem
    - 医療統計
        - hazard rate
            - N 事象の回数
                $$
                N : 2^T \to \N
                $$
                - T 時間(全順序集合)
                - 入力は時間区間
                - 出力は事象の回数
            $$
            h(t) = \frac{N(t, t+\Delta t)/N(0, t)}{\Delta t} \\
            = \frac{P(t<T<t+\Delta t| T \geq t)}{\Delta t}
            $$
            - Kaplan Meier
                ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%205.png)
            - 生存関数との関係
                - 生存関数 S(t)
                    $$
                    S(t) = P(T>t)
                    $$
                $$
                h(t) = - \frac{d}{dt} \ln S(t)
                $$
            - Cox 回帰/Cox 比例 hazard model
            - Log rank test
            - generalized Wilcoxon test
            - Tarone-Ware test
    - marketing
        - association analysis