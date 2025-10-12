- 二項関係 binary relation
    $$
    R \subset A \times A
    $$
    - 同値関係 equivalence relation
        - 定義 def
            - 反射律 reflectivity
                $$
                \forall x \in X, x \leq x
                $$
            - 推移律 trasitivity
                $$
                \forall x, y, z \in X, x \leq y \land y \leq z \Rightarrow x \leq z
                $$
            - 対称律 symmetry
                $$
                \forall x, y \in X, x \leq y \Rightarrow y \leq x
                $$
        - 同値類
        - 商集合
    - 順序関係 ordered relation
        - 前順序関係 preordered relation
            - 反射律 reflective
                $$
                \forall x \in X, x \leq x
                $$
            - 推移律 transitive
                $$
                \forall x, y, z \in X, x \leq y \land y \leq z \Rightarrow x \leq z
                $$
        - 半順序関係 partially ordered relation
            - 反射律 reflectivity
                $$
                \forall x \in X, x \leq x
                $$
            - 推移律 trasitivity
                $$
                \forall x, y, z \in X, x \leq y \land y \leq z \Rightarrow x \leq z
                $$
            - 反対称律 antisymmetry
                $$
                \forall x, y \in X, x \leq y \land y \leq x \Rightarrow x = y
                $$
        - 全順序関係 totally ordered relation
            - 反射律 reflectivity
                $$
                \forall x \in X, x \leq x
                $$
            - 推移律 trasitivity
                $$
                \forall x, y, z \in X, x \leq y \land y \leq z \Rightarrow x \leq z
                $$
            - 反対称律 antisymmetry
                $$
                \forall x, y \in X, x \leq y \land y \leq x \Rightarrow x = y
                $$
            - 完全律 complete
                $$
                \forall x, y \in X, x \leq y \lor y \leq x
                $$
        - 順序同型 order isomorphic
            - 順序保存写像 order preserving
            - 順序同型 order isomorphic
            - 順序同型写像 order isomorphism
        - 例 example
            - 整列集合
                任意の非空部分集合が最小元を持つ
            - 帰納的半順序集合
                任意の全順序部分集合が上界を持つ半順序集合
            - 有向集合
                任意の二元部分集合に上界がある前or半順序集合
            - 束
                任意の二元部分集合に上限と下限が存在する半順序集合
            - 完備束
                任意の非空部分集合に上限と下限が存在する半順序集合
            - 順序体
- 写像 mapping
    - 単写 injective
    - 全射 surjective
    - 全単写 bijective
- 上極限集合/最大極限集合 limit supremum
    $$
    \limsup_{n \to \infin} A_n = 
    \varlimsup_{n \to \infin} A_n = \bigcap_{n=1}^\infin \bigcup_{k=n}^\infin A_k
    $$
    $$
    \{x \in A_k : \forall n \in \N, \exist k \geq n\}
    $$
- 下極限集合/最小極限集合 limit infimum
    $$
    \liminf_{n \to \infin} A_n =
    \varliminf_{n \to \infin} A_n =
    \bigcup_{n=1}^\infin \bigcap_{k=n}^\infin A_k
    $$
    $$
    \{ x \in A_k:\exist n \in \N, \forall k \geq n\}
    $$
- 不等式 inequality
    $$
    \liminf A_n \subset \limsup A_n
    $$
    - proof
        $$
        x \in \liminf A_n \Rightarrow x \in \limsup A_n \\
        \exist n \in \N, \forall k \geq n, x \in A_k 
        \Rightarrow 
        \exist m \in \N, \forall l \geq m, x \in A_l
        $$
        を示す
        $x \in \liminf A_n$より
        $$
        \exist n \in \N, \forall k \geq n, x \in A_k
        $$
        - $\forall m \leq n$
            $$
            \forall k \geq n, x \in A_k 
            \\
            \Rightarrow
            \exist l \geq n, x \in A_l
            \\
            \Rightarrow
            \exist l \geq n \geq m, x \in A_l 
            \\
            \Rightarrow
            \forall m \leq n, \exist l \geq m, x \in A_l
            $$
        - $\forall m > n$
            $$
            \forall k \geq n, x \in A_k 
            \\
            \Rightarrow 
            \forall k \geq n \Rightarrow \exist l \geq m > n \\
            \Rightarrow \exist l \geq m > n, x \in A_l\\
            \Rightarrow \forall m > n, \exist l\geq m,  x \in A_l
            $$
- 極限集合 limit
    $$
    \lim A_n = \liminf A_n = \limsup A_n \\
    $$