$$
\N
$$
- peano axiom
    - 最初の自然数 first natural number
        $$
        0  \in \N
        $$
    - 同値性 equality relation
        - 反射律 reflexive
            $$
            \forall x \in \N, x = x
            $$
        - 対称律 symmetric
            $$
            \forall x, y \in \N, x = y \Rightarrow y = x
            $$
        - 推移律 transitive
            $$
            \forall x, y, z \in \N, x = y \land y = z \Rightarrow x = z
            $$
        - 閉包 closed
            $$
            \forall x, y \in \N, x \in \N \land x = y \Rightarrow y \in \N
            $$
    - 次写像 successor function
        - 最初 first element
        $$
        0 \in \N
        $$
        - 閉包 closed
            $$
            \forall n \in \N, S(n) \in \N
            $$
        - 単写 injection
            $$
            S(n)=S(m) \Rightarrow n=m
            $$
        - 非周期性 non-cycle
            $$
            \forall n \in \N, S(n) \ne 0
            $$
        - 帰納性 induction
            $$
            0 \in K \\
            \forall k \in K, S(k) \in K \\
            \Rightarrow \N \subset K
            $$
- 代数構造