---
alias:
    ['凸集合', 'convex set']
---
$$
\forall x \in S \land \forall y \in S \Rightarrow \\  \lambda x + (1-\lambda)y \in S, \forall \lambda \in [0, 1]
$$
- other description
    $$
    \lnot(\forall x \in S \land y \in S) \lor \\  (\lambda x + (1-\lambda)y \in S, \forall \lambda \in [0, 1])
    $$
- 指示関数
    $$
    \delta_S : \mathbb R \to \R\cup\{\infty\} \\
    \delta_S(x) = 
    \left\{
    \begin{matrix}
    1 & if & x \in S \\
    \infty & otherwise
    \end{matrix}
    \right.
    $$
    - theorem
        $\delta_S : \mathbb R \to \R\cup\{\infty\}$ 
        が凸関数 
        必要十分条件
        $S \subset \mathbb R$ が凸集合
        - proof
            $$
            A = \forall x \in S \land \forall y \in S \\
            B = \lambda x + (1-\lambda)y \in S, \forall \lambda \in [0, 1] \\
            C = \forall x \in \mathbb R, \forall \lambda \in[0, 1],\\ f(\lambda x + (1- \lambda)y) \leq \lambda f(x)+ (1-\lambda)f(y)
            $$
            - \Rightarrow
                $$
                \lnot C \lor (\lnot A \lor B) = T\\
                C \land \lnot (\lnot A \lor B) = F \\
                C \land A \land \lnot B = F
                $$
                $C \land A$ より
                $$
                \delta_S(\lambda x + (1-\lambda)y) \\ 
                \leq
                \lambda \delta_S(x) + (1-\lambda)\delta_S(y) \\
                = \lambda \cdot 1 + (1-\lambda)\cdot 1 \\
                = 1
                $$
                しかし、 $\lnot B$ より
                $$
                \lambda x + (1-\lambda)y \notin S, \exists \lambda \in [0, 1] \\
                \Leftrightarrow \\
                \delta_S(\lambda x + (1-\lambda)y) = \infty, \exists \lambda \in [0, 1]
                $$
                よって矛盾
            - \Leftarrow
                $$
                \lnot (\lnot A \lor B) \lor C = T\\
                (\lnot A \lor B) \land \lnot C = F
                $$
                $A \Rightarrow  B$ と仮定すると
                $$
                \lambda \delta_S(x) + (1-\lambda)\delta_S(y) \\
                = \lambda \cdot 1 + (1-\lambda)\cdot 1 \\
                = 1
                \\ \Rightarrow \delta_S(\lambda x + (1-\lambda)y) = 1
                $$
                が成立する。ただし
                $$
                \lnot C \\
                \delta_S(\lambda x + (1-\lambda)y) >
                \lambda \delta_S(x) + (1-\lambda)\delta_S(y) \\
                1 > 1
                $$
                により矛盾
- 実行定義域
    関数 $f: \mathbb R \to \mathbb R\cup\{\infty\}$
    - dom
        $$
        dom(f) = \{x \in \mathbb R|f(x)< \infty\}
        $$
    - argmin
        $$
        \argmin(f) = \{x \in \mathbb R | f(y) \geq f(x), \forall y \in \mathbb R  \}
        $$
    - theorem
        $f : \mathbb R \to \R\cup\{\infty \}$ を凸関数とする
        この時、 $dom(f), \argmin(f)$ 
        は凸集合
        - proof
            - dom
                $$
                \forall x, y\in dom(f), \forall \lambda \in [0, 1] \\
                \infty > \lambda f(x) + (1-\lambda)f(y) \geq f(\lambda x+ (1-\lambda)y) \\
                \lambda x + (1-\lambda ) \in dom(f)
                $$
            - argmin
                $\argmin(f) \ne \phi$
                $\alpha = \min_{x \in \mathbb R} f(x)$
                $$
                \forall x, y\in dom(f), \forall \lambda \in [0, 1] \\
                \alpha = \lambda f(x) + (1-\lambda)f(y) \geq f(\lambda x+ (1-\lambda)y) \geq \alpha \\
                f(\lambda x+ (1-\lambda)y)=\alpha \\
                \lambda x + (1-\lambda ) \in \argmin(f)
                $$
- 凸多面体 convex polyhedron
    $$
    P = \{x \in M_{n, 1}(\R)| Ax \leq b\}
    $$
    - 超平面 hyperplane
        - vector a
        - scalar b
        $$
        H(a, b) = \{x \in M_{n, 1}(\R)|a^t x = b\}
        $$
    - 半空間 half space
        - 下半空間 lower
            - vector a
            - scalar b
            $$
            H^-(a, b) = \{x \in M_{n, 1}(\R)|a^t x \leq b\}
            $$
        - 上半空間 upper
            - vector a
            - scalar b
            $$
            H^+(a, b) = \{x \in M_{n, 1}(\R)|a^t x \geq b\}
            $$
        - theorem
            半空間同士の共通部分は多面体