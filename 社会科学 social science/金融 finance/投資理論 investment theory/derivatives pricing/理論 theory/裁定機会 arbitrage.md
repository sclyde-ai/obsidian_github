- 確率空間 $(\Omega, F, P)$
- 確率変数 X
- 確率過程
$$
\exist t \in T\\
\mathbb P(X_t \geq X_0) = 1 \\
\mathbb P(X_t > X_0) > 0
$$
この時、この確率過程には裁定機会が存在しているという
$$
\forall E \in \mathcal F_t, X_t(E) \geq X_0 \\
\exist E \in \mathcal F_t, X_t(E) > X_0
$$
- non-arbitrage 無裁定
    $$
    \exist E \in \mathcal F_t, X_t(E) < X_0 \\
    \exist E \in \mathcal F_t, X_t(E) > X_0
    $$
    - how to derive
        $$
        \lnot ( \exist t \in T, \\
        (\forall E \in \mathcal F_t, X_t(E) \geq X_0 \\
        \land \\
        \exist E \in \mathcal F_t, X_t(E) > X_0)
        \\ \lor \\
        (\forall E \in \mathcal F_t, X_t(E) \leq X_0 \\
        \land \\
        \exist E \in \mathcal F_t, X_t(E) < X_0)
        $$
        $$
        \forall t \in T, \\
        (\exist E \in \mathcal F_t, X_t(E) < X_0 \\
        \lor \\
        \forall E \in \mathcal F_t, X_t(E))\leq X_0) \\ 
        \land \\
        (\exist E \in \mathcal F_t, X_t(E) > X_0 \\
        \lor \\
        \forall E \in \mathcal F_t, X_t(E) \geq X_0)
        $$
- example1
    dealer A ask $1.62
    dealer B bid $1.60
- example2
    A in NYK buy 1 pond as 1.58 dollar in 1 year
    B in LDN sell 1 pond as 1.60 dollar at this time 
    dollar rate 4%
    pond rate 6%