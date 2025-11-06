---
parent: "[[現金 cash]]"
---
[[ZCB zero coupon bond]]

-
- unit bond 単位債
    F = 1のZCB
    割引率として機能する
    $$
    B_t^T = B(t, T) = \frac{1}{(1+r)^{T-t}}\\
    B_t^T = B(t, T) = \frac{1}{(1+\frac{r}{m})^{m(T-t)}}\\
    B_t^T = B(t, T) = e^{-r(T-t)}
    $$
    $$
    B_n^N (\omega) = B_n^N(s_n) \\
    B_n^N (\omega) = 1, \forall \omega \in \Omega \\
    B_n^N(s_n u) = B_n^N (s_n d)
    $$
- MMA money market account
    銀行預金
    安全資産として機能する
    $$
    A(t) = A(0)e^{rt}
    $$
- 株式 vs ZCB
    |  | 株式・FX | ZCB(unit bond) |
    | --- | --- | --- |
    | 資産数 | 1資産で完結 | 本質的に多資産 |
    | 現時点の情報 | 単一価格 | 複数価格、満期ごとに別資産 |
    | 価格の上限 | なし | 1 |
    | 価格の random  | 恒久的 | 満期で価格確定 |
    | 資産間の相関 | 高い相関は稀 | 近い満期のZCBは高い正相関 |p