- 同一確率空間上の確率変数列 $\{X_n\}$
- probability 0 version
    $$ \forall \epsilon > 0, \lim_{n \rightarrow \infin} P(|X_n-X| \geq \epsilon\}) = 0 $$
    - strict def
        $$ \forall \epsilon > 0, \forall \delta > 0, \exist N \in \N, \forall n > N, \\ |\mathbb P(\{\omega \in \Omega: |X_n(\omega)-X(\omega)| \geq \epsilon\})| < \delta $$
- probability 1 version
    $$ \forall \epsilon > 0, \lim_{n \rightarrow \infin} P(|X_n-X| < \epsilon) = 1 $$
    - strict def
        $$ \forall \epsilon > 0, \forall \delta > 0, \exist N \in \N, \forall n > N, \\ |\mathbb P(\{\omega \in \Omega: |X_n(\omega)-X(\omega)| < \epsilon\})-1| < \delta $$
この時、確率変数列 $\{X_n\}$は確率変数Xへ確率収束する
- 表記
    $$ X_n \to X\ c.p. \\ X_n \stackrel{p}{\to} X $$
確率変数Xを確率変数列 $\{X_n\}$の確率極限という