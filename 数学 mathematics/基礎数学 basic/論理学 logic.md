|  | A | 1 | 1 | 0 | 0 |
| --- | --- | --- | --- | --- | --- |
|  | B | 1 | 0 | 1 | 0 |
| 否定 not | ¬A | 0 | 1 | 0 | 1 |
| 論理積 and  | A∧B | 1 | 0 | 0 | 0 |
| 論理和 or | A∨B | 1 | 1 | 1 | 0 |
| 含意 if then | A⇒B
¬A∨B | 1 | 0 | 1 | 1 |
| 同値 if only if | A⇔B
(A⇒B)∧(B⇒A) | 1 | 0 | 0 | 1 |
- 背理法
    A \to Bを証明
    $$
    A \mathbb Rightarrow B \\ 
    \Leftrightarrow \lnot A \lor B \\
    \Leftrightarrow \lnot (A \land \lnot B)
    $$
    Aが真の時、常にBが偽であることを示す
- 様相論理 model logic
    必然性と可能性を扱う論理学
    必然性演算子$\Box$
    可能性演算子$\Diamond$
    - 公理系E
        $$
        P \Leftrightarrow Q \mathbb Rightarrow \Box P \Leftrightarrow \Box Q
        $$
    - 公理系K
        $$
        \Box (P \to Q) \to (\Box P \to \Box Q)
        $$
        - 可能性演算子
            $$
            \Diamond p = \lnot \Box \lnot p
            $$
    - 公理系T
        $$
        \Box P \to P
        $$
        $$
        p \to \Diamond p
        $$
- 論理の双対
    論理和と論理積を全て入れ替え
    全称記号と存在記号を全て入れ替え
    たもの