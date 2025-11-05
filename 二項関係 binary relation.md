---
alias:
    ['二項関係', 'binary relation']
---
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