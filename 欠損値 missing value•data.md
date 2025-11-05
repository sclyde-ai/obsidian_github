---
alias:
    ['欠損値', 'missing value data']
---
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