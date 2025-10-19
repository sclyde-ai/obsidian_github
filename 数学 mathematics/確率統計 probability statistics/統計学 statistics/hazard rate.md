- N 事象の回数
    $$
    N : 2^T \to \mathbb N
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