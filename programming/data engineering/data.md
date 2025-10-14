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
    
        - data mining
            
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