---
alias:
    ['交差検証', 'CV', 'cross validation']
---
データを分割して学習と検証を繰り返すこと
- 排他的 exhaustive
    learn and test on all possible ways to divide the original sample into a training and a validation set
    - leave one out
        1. データを一つ選ぶ
        2. そのデータを検証に使い、他のn-1個を訓練に使う
        3. 全通り(n回)行う
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
    - repeated random sub-sampling validation
- wikipedia
  https://ja.wikipedia.org/wiki/%E4%BA%A4%E5%B7%AE%E6%A4%9C%E8%A8%BC