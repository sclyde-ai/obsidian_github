$$
\mathbb N
$$
- peano axiom
    - 最初の自然数 first natural number
        $$
        0  \in \mathbb N
        $$
    - 同値性 equality relation
        - 反射律 reflexive
            $$
            \forall x \in \mathbb N, x = x
            $$
        - 対称律 symmetric
            $$
            \forall x, y \in \mathbb N, x = y \mathbb Rightarrow y = x
            $$
        - 推移律 transitive
            $$
            \forall x, y, z \in \mathbb N, x = y \land y = z \mathbb Rightarrow x = z
            $$
        - 閉包 closed
            $$
            \forall x, y \in \mathbb N, x \in \mathbb N \land x = y \mathbb Rightarrow y \in \mathbb N
            $$
    - 次写像 successor function
        - 最初 first element
        $$
        0 \in \mathbb N
        $$
        - 閉包 closed
            $$
            \forall n \in \mathbb N, S(n) \in \mathbb N
            $$
        - 単写 injection
            $$
            S(n)=S(m) \mathbb Rightarrow n=m
            $$
        - 非周期性 non-cycle
            $$
            \forall n \in \mathbb N, S(n) \ne 0
            $$
        - 帰納性 induction
            $$
            0 \in K \\
            \forall k \in K, S(k) \in K \\
            \mathbb Rightarrow \mathbb N \subset K
            $$
- 代数構造