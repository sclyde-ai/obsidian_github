---
alias:
    ['裁定機会', 'arbitrage']
---
- 確率空間 $(\Omega, F, P)$
- 確率変数 X
- 確率過程
$$
\exists t \in T$$ $$
\mathbb P(X_t \geq X_0) = 1 $$ $$
\mathbb P(X_t > X_0) > 0
$$
この時、この確率過程には裁定機会が存在しているという
$$
\forall E \in \mathcal F_t, X_t(E) \geq X_0 $$ $$
\exists E \in \mathcal F_t, X_t(E) > X_0
$$
- non-arbitrage 無裁定
    $$
    \exists E \in \mathcal F_t, X_t(E) < X_0 $$ $$
    \exists E \in \mathcal F_t, X_t(E) > X_0
    $$
    - how to derive
        $$
        \lnot ( \exists t \in T, $$ $$
        (\forall E \in \mathcal F_t, X_t(E) \geq X_0 $$ $$
        \land $$ $$
        \exists E \in \mathcal F_t, X_t(E) > X_0)
        $$ $$ \lor $$ $$
        (\forall E \in \mathcal F_t, X_t(E) \leq X_0 $$ $$
        \land $$ $$
        \exists E \in \mathcal F_t, X_t(E) < X_0)
        $$
        $$
        \forall t \in T, $$ $$
        (\exists E \in \mathcal F_t, X_t(E) < X_0 $$ $$
        \lor $$ $$
        \forall E \in \mathcal F_t, X_t(E))\leq X_0) $$ $$ 
        \land $$ $$
        (\exists E \in \mathcal F_t, X_t(E) > X_0 $$ $$
        \lor $$ $$
        \forall E \in \mathcal F_t, X_t(E) \geq X_0)
        $$
