- 上極限集合/最大極限集合 limit supremum
    $$
    \limsup_{n \to \infty} A_n = 
    \varlimsup_{n \to \infty} A_n = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k
    $$
    $$
    \{x \in A_k : \forall n \in \mathbb N, \exists k \geq n\}
    $$
- 下極限集合/最小極限集合 limit infimum
    $$
    \liminf_{n \to \infty} A_n =
    \varliminf_{n \to \infty} A_n =
    \bigcup_{n=1}^\infty \bigcap_{k=n}^\infty A_k
    $$
    $$
    \{ x \in A_k:\exists n \in \mathbb N, \forall k \geq n\}
    $$
- 不等式 inequality
    $$
    \liminf A_n \subset \limsup A_n
    $$
    - proof
        $$
        x \in \liminf A_n \Rightarrow x \in \limsup A_n \\
        \exists n \in \mathbb N, \forall k \geq n, x \in A_k 
        \Rightarrow 
        \exists m \in \mathbb N, \forall l \geq m, x \in A_l
        $$
        を示す
        $x \in \liminf A_n$より
        $$
        \exists n \in \mathbb N, \forall k \geq n, x \in A_k
        $$
        - $\forall m \leq n$
            $$
            \forall k \geq n, x \in A_k 
            \\
            \Rightarrow
            \exists l \geq n, x \in A_l
            \\
            \Rightarrow
            \exists l \geq n \geq m, x \in A_l 
            \\
            \Rightarrow
            \forall m \leq n, \exists l \geq m, x \in A_l
            $$
        - $\forall m > n$
            $$
            \forall k \geq n, x \in A_k 
            \\
            \Rightarrow 
            \forall k \geq n \Rightarrow \exists l \geq m > n \\
            \Rightarrow \exists l \geq m > n, x \in A_l\\
            \Rightarrow \forall m > n, \exists l\geq m,  x \in A_l
            $$
- 極限集合 limit
    $$
    \lim A_n = \liminf A_n = \limsup A_n \\
    $$