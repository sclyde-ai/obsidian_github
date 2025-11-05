---
alias:
    ['決定木', 'decision tree']
---
2種類にデータを分割する操作を繰り返してグループを作成
そのグループの平均値を予測値とする
- 不純度 impurity
    - 誤分類率
        $$
        1-\max p
        $$
    - ジニ係数
        $$
        1-\sum p^2
        $$
    - 交差エントロピー誤差
        $$
        -\sum p \log p
        $$
    ![IMG_7366.jpeg](IMG_7366.jpeg)
- 情報利得 information gain
    $$
    IG(D) = I(D)-\sum \frac{N_i}{N}(D_i)
    $$
    D : 分割前の集団
    N : 分割前の集団の大きさ
    D_i : 分割後の集団
    N_i : 分割後の集団の大きさ
- 分類木 classification tree
    - data
        [https___qiita-image-store.s3.amazonaws.com_0_156509_02c831c0-be9a-ca4e-8031-f18bf3710215.avif](https___qiita-image-store.s3.amazonaws.com_0_156509_02c831c0-be9a-ca4e-8031-f18bf3710215.avif)
    - tree
        [https___qiita-image-store.s3.amazonaws.com_0_156509_3ffbd2e4-fbff-5002-7a11-082528cd6a88.avif](https___qiita-image-store.s3.amazonaws.com_0_156509_3ffbd2e4-fbff-5002-7a11-082528cd6a88.avif)
    - model
        [https___qiita-image-store.s3.amazonaws.com_0_156509_9c046a81-9f05-ba3f-5889-02182af29e26.avif](https___qiita-image-store.s3.amazonaws.com_0_156509_9c046a81-9f05-ba3f-5889-02182af29e26.avif)
- 回帰木 regression tree
    - data
        [https___qiita-image-store.s3.amazonaws.com_0_156509_aae21ae1-d0c7-7088-ebf8-60e26f82a9b4.avif](https___qiita-image-store.s3.amazonaws.com_0_156509_aae21ae1-d0c7-7088-ebf8-60e26f82a9b4.avif)
    - tree
        [https___qiita-image-store.s3.amazonaws.com_0_156509_e0ef3c3c-6343-0309-5103-2faf757546d1.avif](https___qiita-image-store.s3.amazonaws.com_0_156509_e0ef3c3c-6343-0309-5103-2faf757546d1.avif)
    - model
        [https___qiita-image-store.s3.amazonaws.com_0_156509_721ffb0e-cc93-2747-efa2-324a93ba2b92.avif](https___qiita-image-store.s3.amazonaws.com_0_156509_721ffb0e-cc93-2747-efa2-324a93ba2b92.avif)
- link
    [[入門]初心者の初心者による初心者のための決定木分析 - Qiita](https://qiita.com/3000manJPY/items/ef7495960f472ec14377)