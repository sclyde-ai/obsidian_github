- 定義
    集合 X, 演算/写像• : X \times X \to X
    - 結合律 associativity
        $$
        x \cdot (y \cdot z) = (x \cdot y) \cdot z, \forall x,y,z \in X
        $$
    - 単位元 identity
        $$
        \exists e \in X, x \cdot e = e\cdot x=x, \forall x\in X
        $$
    - 逆元 inverse
        $$
        \exists x^{-1} \in X, x\cdot x^{-1} = x^{-1}\cdot x = e, \forall x \in X
        $$
    - 交換律 commutative
        $$
        x \cdot y = y \cdot x, \forall x, y \in X
        $$
- monoid
- 半群 semigroup
- 群 group
    [結合律 associativity](https://www.notion.so/associativity-216ec42dd04b8106a520c3fb451c844a?pvs=21) 
    [単位元 identity ](https://www.notion.so/identity-216ec42dd04b8157b94cf393ea70e686?pvs=21) 
    [逆元 inverse ](https://www.notion.so/inverse-216ec42dd04b817fb6c9dd366379a23f?pvs=21) 
    この時、(X, •)を群という
    - 定理 theorem
        - 単位元の一意性
        - 逆元の一意性
        - 結合後の逆元
        - 逆元の逆元
    - 位数 order
        元の数
    - 部分群 subgroup
        群G, S \subset G
        - 結合律
        - 単位元
        - 逆元
        この時、(S, •)をGの部分群という
        - 必要十分条件 if only if
            H \subset G
            $$
            a, b \in H, ab^{-1} \in H
            $$
            Hは部分群である
            - 証明
                - 必要性
                    $$
                    a \in H, e = aa^{-1} \in H
                    $$
                    $$
                    e, a \in H, a^{-1}= ea^{-1} \in H
                    $$
                    $$
                    a, b \in H, ab = a(b^{-1})^{-1} \in H
                    $$
                - 十分性
        - 定理 theorem
            - GとHの単位元は同じ
            - GとHの逆元は同じ
            - Gが可換群ならばHも可換群
            - 推移律
            - 部分群の積集合
    - 生成される部分群 subset generated
        群G, S \subset G
        $$
        s_1, ..., s_n \in S \\
        a_1, ..., a_n \in \mathbb Q \\
        s_1^{\pm a_1}, ..., s_n^{\pm a_n}
        $$
    - 剰余類 coset
        - 左剰余類 left coset
            G is group, H \subset G
            $$
            gH = \{gh|h \in H\} \subset G
            $$
            をGに対するHの左剰余類
        - 右剰余類 right coset
            G is group, H \subset G
            $$
            gH = \{gh|h \in H\} \subset G
            $$
            をGに対するHの左剰余類
        - 剰余類 coset
        - 剰余集合
        - 定理 theorem
            - 剰余類は同値類
            - 剰余類の濃度は等しい
            - 
        - 剰余群/商群 quotient group
    - 準同型/同型 semihomomorphism/homomorphism
- 可換群 abelian group
![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%206.png)
- 巡回群
- 例
    - 対称群
        集合 {1, 2, …, n}の置換
    - 一般線形群
        n次正則行列
        - 特殊線形群
            行列式が1の一般線形群
    - 直行群
        n次直行行列
        - 特殊直行群
            行列式が1のn次直行行列
    - ユニタリ群
        - 特殊ユニタリ群
            行列式が1
    - 二面体群
    - 連続群 lie group
    - ガリレイ変換
    - ローレンツ群
    - 空間群
    - cayley table