    - variable
         $n \in \N$ : the number of data
         $k \in \N$ : the number of means/centroids
         $d \in \N$ : dimension 
        - observations
            $$
            \{x_i \in \R^d :  i \in \{1,...,n\}\}
            $$
        - means/centroids
            $$
            \{\mu_i \in \R^d :  i \in \{1,...,k\}\}
            $$
            it can take any average
        - within-cluster sum of square
            $$
            S =\{S_i \in \R :  i \in \{1,...,k\}\}
            $$
    $$
    \argmin_S \sum_{i=1}^k \sum_{x \in S_i} \|x-\mu_i\|^p
    $$
    - 手順 process
        1. クラスタ数を決めて、その数だけ無作為に点を取る。これをクラスタ点呼ぶ
        2. 全てデータ点に対して最も近いクラスタ点のクラスタを割り当てる
        3. クラスタに属する点の重心を新しいクラスタ点にする
        4. 1, 2, 3繰り返す
    - 欠点 flew
        - 初期値依存
        - 外れ値に弱い
        - クラスタ数を事前に設定
        - 円/球形のクラスタ形を仮定
- k-means++
    初期値依存に対処
    1. 初期値を無作為に変更し複数回試行
    2. 評価関数で最適な結果を選択
    3. 適切な初期値確率的に求める
- k-medoids
    外れ値に対処
- c-means
    データ点に複数のクラスタを割当
- x-means
    最適なクラスタ数にする
- g-means
    最適なクラスタ数にする