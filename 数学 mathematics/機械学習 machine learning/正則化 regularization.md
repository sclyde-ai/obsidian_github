---
alias:
    ['正則化', 'regularization']
---
過学習を防ぎ、モデルの汎化能力を高めるための手法
a technique to reduce overfitting in machine learning models by adding a penalty to the loss function
$$
\min_w \mathbb E[w] + \lambda R(w)
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