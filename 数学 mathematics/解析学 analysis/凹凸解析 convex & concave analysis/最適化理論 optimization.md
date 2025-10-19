- 凹凸解析 convex and concave analysis
    - 離散凸解析
        $$
        N = \{1, 2, ..., n\}
        $$
        - supp
            - supp+
                $$
                Supp^+ (z) = \{v \in V|z_v > 0\} \\ z \in \Z^V 
                $$
            - supp-
                $$
                Supp^- (z) = \{v \in V|z_v < 0\} \\ z \in \Z^V
                $$
            - x-y
                $$
                Supp^+ (x-y) = \{v \in V|x_v> y_v\} \\ z \in \Z^V
                $$
                $$
                Supp^- (x-y) = \{v \in V|x_v < y_v\} \\ z \in \Z^V
                $$
        - 近接凸性
            $$
            f(x) + f(y) \leq f(x - \xi(y-x)) + f(y - \xi(y-x))
            $$
            - 指示関数
                $$
                \forall S \subset V \\
                \chi_S(v) = 
                \left\{
                \begin{matrix}
                1 & if & v \in S \\
                0 & otherwise
                \end{matrix}
                \right.
                $$
            - 命題
                fが連続関数である
                ならば
                凹性=近接凹性
                - proof
                    - 有限集合 V
                    $f : z^V \to \mathbb R \cup\{-\infty\}$
        - M凹関数
            - 関数 f
                $$
                f : \Z^V \to \mathbb R \cup\{-\infty\} 
                $$
            $$
            \forall x, y \in dom(f) \\
            \forall u \in Supp^+(x-y) \\
            \existss v \in Supp^-(x-y) \\
            f(x) + f(y) \leq f(x - e_u + e_v) + f(y + e_u - e_v )
            $$
            - 命題1
                fがM凹関数
                ならば
                 $\lnot x, y \in dom(f) \\
                Supp^- (x-y) = \phi$
                - proof
                    $$
                    \forall x, y \in dom(f) \\
                    \sum_{v \in V}x(v) = \sum_{v \in V} y(v)
                    $$
            - 命題2
                $$
                x -e_u + e_v, y + e_u-e_v \in dom\ f
                $$
            - 命題3
                fがM 凹関数ならば
                $$
                dom\ f \subset \{x \in \mathbb R^V | \sum_{v \in V} x(v) = c, c \in \mathbb R\}
                $$
                実行定義域は必ずある超平面上に存在
                成分和は必ず一定
                よって変数 $x \in \Z^V$ の自由度は $|v| -1$ 
                $$
                \existss o \notin V, \hat V = V \cup\{o\} 
                $$
            - example
        - M natural 凹関数
            - 関数 f
                $$
                f : \Z^V \to \mathbb R \cup\{-\infty\} 
                $$
            $$
            \forall x, y \in dom(f) \\
            \forall u \in Supp^+(x-y) \\
            \existss v \in Supp^-(x-y) \\
            f(x) + f(y) \leq f(x - e_u + e_v) + f(y + e_u - e_v ) \\
            \lor \\
            f(x) + f(y) \leq f(x - e_u) + f(y + e_u)
            $$
            - 別表現
                $$
                f : \Z^V \to \mathbb R \cup \{-\infty\} \\
                \existss \hat f \in M, \\
                \hat f : \Z^{\hat V} \to \mathbb R \cup \{-\infty\} \\
                f(x) = \hat f(x, x_0)
                $$
            - 命題1
                $$
                \forall x \in dom\ f, (x, -x_v)\in dom\ \hat f \\
                \forall x \in dom\ f, (x, -x_v)(v) = \sum_{v \in V} x_v - x_v = 0 \\
                dom\ \hat f \subset \{x \in \mathbb R^n|x_v = 0\}
                $$
            - 命題2
                $\hat f$がＭ凹関数 $\Leftrightarrow$ f がM natural 凹関数
                $$
                \hat f: \Z^{\hat V} \to \mathbb R \cup \{-\infty\} \\
                \hat f(x, x_0) = 
                \left\{
                \begin{matrix}
                f(x) & if & x_0 = -x_v \\
                -\infty
                \end{matrix}
                \right.
                $$
            - theorem
                $$
                f : \Z^V \to \mathbb R \cup\{-\infty\} \\
                \forall x, y \in dom(f) \\
                \forall u \in Supp^+(x-y) \\
                \existss v \in Supp^-(x-y)\cup \{o\} \\
                f(x) + f(y) \leq f(x - e_u + e_v) + f(y + e_u - e_v ) 
                $$
            - 関係式
                $$
                f:\Z^V \to \mathbb R \cup \{-\infty\}, M\ natural \{\infty\}
                $$
                必要十分
                $$
                f:\Z^V \to \mathbb R \cup \{-\infty\}, M
                $$
        - L natural 凸集合
        - 層族
            $$
            \mathcal F \subset 2^V, \forall S, T \in \mathcal F,  S \subset T \lor T \subset S \lor S \cap T = \phi
            $$
            Fを層族という
        - 分離凹関数
            $$
            \mathcal F = \{\{v\}_{v \in V}\}
            $$
        - 層凹関数
            $$
            \forall z \in \mathcal F, \existss f_z : \mathbb R \to \mathbb R \cup \{-\infty\} \\f(x) = \sum_{z \in \mathcal F} f_z(x(z)), x(z) = \sum_{v \in z}x_v
            $$
            f_zを層凹関数という
            - 命題
                fが層凹関数ならば
                fはM natural 凹関数
                - proof
                    $$
                    \forall x, y \in dom\ f, \forall u \in Supp^+(f) \\
                    F_u = \{z \in F|u \in z\} \\
                    f(x) = \sum_{z \in F} f_z(x(z)) \\
                    = \sum_{z \notin F_u} f_z(x(z)) + \sum_{z \in F_u} f_z (x(z)) \\
                    = \sum_{z \notin F_u} f_z ((x \pm x_u)(z)) + \sum_{z \in F_u} f_z(x(z))
                    $$
                    - $F_u = \phi$
                        $$
                        f(x) = f(x - x_u) \\
                        f(y) = f(y + x_u)
                        $$
                        よってM natural においてv=0とすればよい
                    - $F_u \ne \phi$
                        1. $\forall z \in F_u, y(z) < x(z)$
                            この時、v = 0とすると
                            $$
                            f(x - x_u) + f(y + x_u) - (f(x) + f(y)) \\
                            = \sum_{z \in F_u} f_z (x(z) - 1) + f_z(y(z) + 1) - (f(x(z)) + f(y(z))) \\
                            \geq 0
                            $$
                            近接凹性を用いた
                        2. $\existss z \in F_u, y(z) \geq x(z)$
                            Fが層族なので
                            $$
                            u \in z_1 \subset z_2 \subset ... \subset z_v
                            $$
                            $$
                            z_k := \min \{z \in \mathcal F | y(z_k) \geq x(z_k)\}
                            $$
        - M凹関数演算最適化
            - theorem1
                $f, g : \Z^V \to \mathbb R \cup \{-\infty\}$ がM natural 凹関数であるとする
                - 正の定数倍
                    $$
                    \hat f(x) = \lambda f(x), \forall x \in \Z^V
                    $$
                - 一次関数の和
                    $$
                    \hat f(x) = f(x) + p \cdot x, \forall x \in \Z^V
                    $$
                    - proof
                        $$
                        px + py = p(x-\xi(x_u + x_v)) + p(y + \xi(x_u -x_v))
                        $$
                        両辺をそれぞれ加えればよい
                - 無限
                    $$
                    a \in (\Z \cup \{-\infty\})^V, b \in \Z \cup \{-\infty\} \\
                    \hat f(x) = 
                    \left\{
                    \begin{matrix}
                    f(x) & if & x \in [a, b] \\
                    -\infty
                    \end{matrix} 
                    \right.
                    $$
                    - proof
                        $$
                        x, y \in [a, b] \\
                        x - x_u + x_v, y +x_u-x_v \in [a, b] 
                        $$
                - 直和
                    $$
                    \hat f(x, y) = f(x) + g(y), x, y \in \Z^V \\
                    f: \Z^V \times \Z ^V \to \mathbb R \{-\infty\}
                    $$
                    - proof
                        $$
                        (x', y'), (x, y) \in dom \hat f 
                        $$
                        - $u \in supp^+ (x'-x)$
                        - $v \in supp^+ (y'-y)$
                \hat f はM natural 凹関数
            - theorem2
                - $f : \Z^V \to \mathbb R \cup \{-\infty\}$ はM natural 凹関数
                - 条件1
                    $$
                    x\in domf, \max_{x \in dom f} f(x)
                    $$
                - 条件2
                    $$
                    f(x) \geq f(x -x_u +x_v), \forall u, v \in V \cup \{o\}
                    $$
                は必要十分条件
                - proof
                    xが後者の条件を満たすが
                    $$
                    \existss x \in dom f, f(y)>f(x)
                    $$
                    であると仮定する
                    $$
                    ||y -x||_1 = \sum_{u \in V} |y_u - x_u|
                    $$
                    が最小となるyをとる
                    $$
                    x \ne y, Supp^+(x-y) \ne \phi \lor Supp^-(x-y) \ne \phi
                    $$
                    - M natural
                        $$
                        f : \Z^V \to \mathbb R \cup\{-\infty\} \\
                        f(x) + f(y) \leq f(x - \xi(y-x)) + f(y - \xi(y-x)) \\
                        \forall x, y \in dom(f) \\
                        \forall u \in Supp^+(x-y) \\
                        \existss v \in Supp^-(x-y) \cup \{o\}
                        $$
                    条件2より $f(x) \geq f(x - x_u + x_v)$ なので
                    $$
                    f(y) \leq f(y + x_u - x_v)
                    $$
                    しかし
                    $$
                    ||x -(y + x_u -x_v)||_1 \leq ||x -y||_1 -1
                    $$
                    よって $f(y) > f(x)$ となり
                    $||x -y||_1$ の最小化に矛盾
            - 離散変数の場合
                集合 $S \subset \Z^V$ がM natural 凸集合
                指示関数 $\delta_S$ がM natural 凸関数
                と定義する
                - 別表現
                    $$
                    \forall x, y \in S,\\
                    \forall u \in Supp^+(x-y) \\
                    \existss v \in Supp^-(x-y) \cup \{o\}\\
                    x - x_u + x_v, y + x_u - x_v \in S
                    $$
                - theorem
                    $f : \Z^V \to \mathbb R \cup \{-\infty\}$ がM natural 凹関数
                    ならば
                    $dom \ f, \argmax\ f$ はM natural 凸集合となる
                    - proof
                        - dom f
                            $$
                            f : \Z^V \to \mathbb R \cup\{-\infty\} \\
                            \forall x, y \in dom(f) \\
                            \forall u \in Supp^+(x-y) \\
                            \existss v \in Supp^-(x-y) \cup \{o\} \\ 
                            f(x - x_u + x_v)), f(y + x_u-x_v) \in \mathbb R\\
                            $$
                            $$
                            x - x_u + x_v, y + x_u -x_v \in dom(f)
                            $$
                        - argmax f
                            dom fと同様
                - 命題
                    $S \subset \Z^V$がM凸集合
                    $$
                    \forall x, y \in S, x(v) = y(v)
                    $$
                    - 注意
                        $$
                        \existss c \in \mathbb R, dom(f) \subset \{x \in \mathbb R^V | x_v = c\}
                        $$
                    - proof
                        $||x-y||_1$ についての帰納法で示す
                        1. $||x - y||_1 = 0$
                            $$
                            x = y , x(v) = y(v)
                            $$
                        2. $||x - y||_1 = 1$
                            $$
                            Supp^+ (x-y) = \phi \lor Supp^-(x -y) = \phi 
                            $$
                            これはSのM凸性に反する
                        3. $||x - y||_1 \geq 2$
                            SのM凸性より
                            $$
                            y' = y + x_u -x_v
                            $$
                            定義より $y'(v) = y(v)$
                            また
                            $$
                            || x - y'||_1 = ||x - y||_1 -2
                            $$
                            よって帰納法の仮定より
                            $$
                            x(v) = y'(v) \\
                            x(v) = y(v)
                            $$
                        4. 
        - 準線形効用
            $$
            u(x) = f(x) - p\cdot x, p \in \mathbb R^V
            $$
            - 命題
                uがM natural 凹関数
                ならば
                uは劣モジュラ関数
                $$
                u(x) + u(y) \geq u(x \lor y) + u(x \land y) \\
                (x \lor y)(v) = \max(u(v), y(v)) \\
                (x \land y)(v) = \max(u(v), y(v)) \\
                \forall v \in V
                $$
                - $x \in \{0, 1\}^V$
                    $f: \{0, 1\}^V \to \mathbb R \cup \{-\infty\}$ は
                    集合値関数 $f:2^V \to \mathbb R \cup \{-\infty\}$
                    とみなせる
                    - 劣モジュラ性
                        $$
                        \forall S, T \subset V, u(S) + u(T) \geq u(S \cup T) + u(S \cap T)
                        $$
                        w = -u と書くとwは凸ゲーム
                        - 凸ゲーム
                            凸ゲームは以下と同値
                            $$
                            u(T \cup\{i \}) - u(T) \geq u(S \cup \{i\}) - u(S) 
                            \\ \lambda \notin S \subset T
                            $$
                        - 消費での解釈
                        - proof
                            $$
                            x, y \in dom(f) \\
                            Supp^+(x-y) = \phi \lor Supp^-(x-y) = \phi \\
                            \lor (x \lor y, x \land y \in dom(f))
                            $$
                            この場合は自明なので
                            $$
                            x, y \in dom(f) \\
                            Supp^+(x-y) \ne \phi \lor Supp^-(x-y) \ne \phi \\
                            \lor (x \lor y, x \land y \in dom(f))
                            $$
                            の場合を考える
                            $$
                            ||x - y||_1 := \sum_{v\in V} |x_v - y_v|
                            $$
                            1. $||x - y|| \leq 2$
                                $$
                                1 = |Supp^+(x - y)| = |Supp^-(x-y)|
                                \\
                                \mathbb Rightarrow x = y + e_u - e_v \\
                                x \lor y = x + e_v = y + e_u \\
                                x \land y = y - e_v
                                $$
                                M natural 条件より
                                $$
                                f(x \lor y) + f(x \land y) = f(y + e_u) + f(y - e_v) \\
                                \leq f(y) + f(y - e_v + e_u) \\
                                = f(x) + f(y)
                                $$
                            2. $||x -y ||_1 \geq 3$
                                $$
                                u \in Supp^+(x-y) \\
                                x' = (x \land y) + e_u \\
                                y' = y + e_u
                                $$
                                ここで
                                $$
                                x' \land y = x \land y \\
                                x' \lor  y = y' \\
                                x \land y' = x'
                                $$
                                dom f がM natural 凸集合なので
                                $$
                                [x \land y, x \lor y] \subset dom(f)
                                $$
                                特に $x' \in dom(f)$ 
                                $$
                                ||x'-y||_1 \leq ||x-y||_1 = 1 \\
                                ||x -y'||_1 \leq ||x-y||_1 = 1
                                $$
                                帰納法の仮定が使える
                                帰納法の仮定より
                                $$
                                f(y) - f (x \land y) \geq f(y+e_u) - f((x\land y)+e_u) \\
                                f(y) - f (x' \land y) \geq f(x'\lor y) - f(x') \\
                                f(y) - f (x' \land y) \geq f(y') - f(x \land y') \\
                                \geq f(x \lor y') - f(x) \\
                                = f(x \lor y) - f(x) \\
                                = f(x \lor y) - f(x) \\
                                \Leftrightarrow f(x) + f(y) \geq f(x\lor y) + f(x \land y)
                                $$
                - 一般に逆は言えない
                    劣モジュラ性を満たすが
                    M natural 凹関数でないものが存在
                - 命題
                    f がM natural 凹関数 
                    $D(f, p)$が $\forall p \in \mathbb R^V$ でM natural 凸集合
                - 需要対応
                    $$
                    D(f, p) = \argmax\{f(x) - p\cdot x|x \in \Z^V\}
                    $$
                    - p
                        $$
                        p(X) = \sum_{v \in V}p(v) \cdot x(v) = \sum_{v \in X} p(v)
                        $$
                - 単調改良性 SI
                    $$
                    X \notin D (f, p) 
                    \\ 
                    \mathbb Rightarrow 
                    \\
                    \existss Y \subset V \\
                    |X|Y|, |Y|X| \leq 1 \\
                    f(X) - p(X) < f(X) -p(Y)
                    $$
                    - 命題
                        $f : \{0, 1\}^V \to \mathbb R \cup \{-\infty\}$
                        局所最適性=最適性
                        よりM natural 凹関数は単調改良性を満たす
                - 粗代替性 GS
                    $$
                    X \in D(f, P), p \leq q 
                    \\
                    \mathbb Rightarrow
                    \\
                    \existss Y \in D(f, q)\\
                    \{v \in X | p(v) = q(v)\} \subset Y
                    $$
                - theorem
                    $f: \{0, 1\}^V \to \mathbb R \cup\{-\infty\}$
                    1. f が M natural 関数
                    2. f が SI を満たす
                    3. f が GS を満たす
                    上記の3つは同値条件
                - LAD 総需要の法則
                    $$
                    X \in D(f, p), p \leq q 
                    \\ 
                    \mathbb Rightarrow 
                    \\
                    \existss Y \in D(f, q), |Y| \leq |X|
                    $$
                    - 命題
                        $f:\{0, 1\}^V \to \mathbb R\cup\{-\infty\}$ がM natural 凹関数
                        ならば
                        f は LADを満たす
                    - 選択の意味での場合
                        $$
                        Y \subset X \mathbb Rightarrow |C(Y)| \leq |C(X)|
                        $$
                        $$
                        C^f(X) = \argmax \{f(Y) | Y \subset X\}
                        $$
                - 選択関数
                    部分集合 $X \subset V$ 最も良い集合を選択
                    $$
                    C : 2^V \to 2^V \\
                    C(X) \subset X
                    $$
                    - Cの合理性
                        $$
                        \forall X, Y \subset V \\
                        Y \subset X \land C(X) \subset Y \\
                        \mathbb Rightarrow \\
                        C(Y) = C(X)
                        $$
                        - アローの公理と等価
                            $$
                            (Y \subset X, C(X) \cap Y \ne \phi, Y \cap C(X) = C(Y))
                            $$
                    - 代替性 sub
                        $$
                        Y \subset X \land C(X) \cap Y \ne \phi
                        \\
                        \mathbb Rightarrow 
                        \\ 
                        \\ Y\cap C(X) \subset C(Y)
                        $$
                        - 条件が成立しない場合
                            $$
                            x \notin C(Y) \land x \in C(X)
                            $$
                            補完的な財（一緒にすると効用が増加）
                            - 別表現 (sen’s $\alpha$, chernoff)
                                $$
                                Y \subset X \mathbb Rightarrow R(Y) \subset R(X) 
                                $$
                                - $R$
                                    $$
                                    R(X) = X/C(X)
                                    $$
                                - 相似条件 (sen’s $\beta$, dual chernoff)
                                    $$
                                    Y \subset X \land C(X) \cap Y \ne \phi \\
                                    \mathbb Rightarrow \\
                                    C(X) \subset Y \cap C(X) 
                                    $$
        - 経済学へのM凹性の応用
            1. 1. M凹性と代替性
                V : 不可分財の集合
                $f : \Z^V \to \mathbb R \cup\{-\infty\}$ : 財の組み合わせに対する満足度
                - 効用関数 u
                    $$
                    u(x) = f(x) - px
                    $$
                    効用 = 純金銭的満足度
                    … 準線形性
                fがM natural 凹関数ならばuもM natural 凹関数
                uがM natural 凹関数ならば次の意味で限界効用逓減の法則が成り立つ
                - theorem
                    uがM natural 凹関数ならば
                    uは劣モジュラ性を満たす
                    - 劣モジュラ性
                        $$
                        \forall x, y \in dom (u), \\
                        u(x) + u(y) \geq u(x \lor y) + u(x\land y) \\
                        (x \lor y)(v) = \max(x(v), y(v)) \\
                        (x \land y)(v) = \min(x(v), y(v))
                        $$
                - 
    - Legendre transform
    - question
        - ラグランジュの証明
        - 極値判定条件の証明
            - 命題1
                ヘッシアンが正かつ第一変数の2階微分が正ならば極小値
                ヘッシアンが正かつ第一変数の2階微分が負ならば極大値
                ヘッシアンが負ならば極値を持たない
            - 命題2
                ヘッセ行列の固有値が全て正ならば極値
            ヘッセ行列が正定値ならば極小
            ヘッシ行列が不定値ならば極大
            偏導関数が全て0の場合
        - 正定値と首座小行列
            首座小行列が全て正
            ならば
            ヘッセ行列は正定値
- 関数解析 function analysis
- Taylor theorem
- minimizer
    - local minimizer
        - neighborhood
            $$
            \mathcal N := \{x \in \mathbb R^n |\ \|x - x^*\|^2 \}
            $$
        $$
        x^* \in \mathcal D, f(x) \geq f(x^*), \forall x \in \mathcal N \cap \mathcal D
        $$
    - global minimizer
        $$
        x^* \in \mathcal D, f(x) \geq f(x^*), \forall x \in \mathcal D
        $$
    - a strict local minimizer
        $$
        x^* \in \mathcal D, f(x) \geq f(x^*), \forall x \in \mathcal D
        $$
    - isolated local minimizer
        $$
        x^* \in \mathcal D, 
        $$
- minimizer condition
    - necessary condition 1
        - $f(x) \in C$ : continuously differentiable
        - local minimizer  x*
        $$
        \nabla f(x^*) = 0
        $$
        - proof
            - $\nabla f(x^*)^\top h \geq 0$
                局所最小点なので
                $$
                f(x^* +th) \geq f(x^*)
                $$
                taylor 
                $$
                f(x^* +th) = f(x^*) + t \nabla f(x^*)^\top h + o(t^2)
                $$
                上記2つを満たすのは
                $$
                t \nabla f(x^*)^\top h + o(t^2) \geq 0
                $$
                の時である。
                よって t → 0のとき
                $$
                \nabla f(x^*)^\top h \geq 0
                $$
            - $\nabla f(x^*)^\top h \leq 0$
                局所最小点なので
                $$
                f(x^* -th) \geq f(x^*)
                $$
                taylor 
                $$
                f(x^* -th) = f(x^*) - t \nabla f(x^*)^\top h + o(t^2)
                $$
                上記2つを満たすのは
                $$
                -t \nabla f(x^*)^\top h + o(t) \geq 0
                \\
                0 \geq t \nabla f(x^*)^\top h + o(t^2) 
                $$
                の時である。
                よって t → 0のとき
                $$
                \nabla f(x^*)^\top h \leq 0
                $$
            よって
            $$
            \nabla f(x^*) = 0
            $$
    - necessary condition 2
        - $f(x) \in C^2$ : twice continuously differentiable
        - local minimizer x*
        $$
        \nabla^2 f(x^*) \succeq 0
        $$
        - proof
            局所最小点なので
            $$
            f(x^* +th) \geq f(x^*)
            $$
            taylor かつ $\nabla f(x^*) = 0$
            $$
            f(x^* +th) = f(x^*) + \frac{t^2}{2} h\nabla f(x^*)^\top h + o(t^3)
            $$
            上記2つを満たすのは
            $$
            \frac{t^2}{2} h\nabla f(x^*)^\top h + o(t^3) \geq 0
            $$
            の時である。
            よって t → 0のとき
            $$
            h\nabla f(x^*)^\top h \geq 0
            $$
    - sufficient condition
        - $f(x) \in C^2$ : twice continuously differentiable
        $$
        \nabla f(x^*) = 0 \land \nabla^2 f(x^*) \succeq 0
        $$
    - KKT condition
        制約付き最適化問題の最適解を求めるための必要条件
        - 問題
            $$
            \min_x f(x) \\
            g_i(x) \leq 0,\ i = 1, ..., m \\
            h_j(x) = 0, \ j = 1, ..., l
            $$
        - 停留条件/定常性条件 stationary
            $$
            \nabla_x \mathcal L(x, \lambda, \mu) = \nabla f(x) + \sum_{i = 1}^m \lambda_i \nabla g_i(x) + \sum_{j = 1}^l \mu_i \nabla h_i(x)=0
            $$
        - 原始実行可能性 primal feasibility
            $$
            g_i(x^*) \leq 0 \\
            h_i(x^*) = 0
            $$
        - 双対実行可能性 dual feasibility
            $$
            \lambda^*_i \ge  0
            $$
        - 相補性条件 complementary slackness
            $$
            \lambda^*_i g_i(x^*) = 0
            $$
- Lipschitz continuous
    $$
    \|\nabla f(y) -\nabla f(x)\| \leq L\|y-x\|
    $$
    - theorem
        $$
        f(y) \leq f(x) + \nabla f(x)^\top (y-x) + \frac{L}{2}\|y -x\|^2 \\
        f(y) - f(x) \leq \nabla f(x)^\top (y-x) + \frac{L}{2}\|y -x\|^2
        $$
        - proof
            - z
                $$
                z(t) = x + t(y-x)
                $$
                $$
                f(y) - f(x) = f(z(1)) - f(z(0)) \\ 
                = \int_0^1 \frac{d}{dt} f(z(t)) dt \\
                = \int_0^1 \nabla f(z(t)) \frac{d z(t)}{dt} dt \\
                =  \int_0^1 \nabla f(z(t)) (y-x) dt \\ 
                $$
            - $\nabla f(z(t))$
                $$
                \nabla f(z(t)) = \nabla f(x) + (\nabla f(z(t)) - \nabla f(x))
                $$
                $$
                = \int_0^1 (\nabla f(x) + (\nabla f(z(t)) - \nabla f(x)))(y-x) dt 
                \\
                = \int_0^1 \nabla f(x)(y-x)dt + \int_0^1 (\nabla f(z(t)) - \nabla f(x))(y-x) dt 
                \\
                = \nabla f(x)(y-x) \int_0^1 dt + \int_0^1 (\nabla f(z(t)) - \nabla f(x))(y-x) dt 
                \\
                = \nabla f(x)(y-x) + \int_0^1 (\nabla f(z(t)) - \nabla f(x))(y-x) dt \\
                $$
            - integral
                $$
                = \int_0^1 (\nabla f(z(t)) - \nabla f(x))(y-x) dt \\
                = (y-x)\int_0^1 (\nabla f(z(t)) - \nabla f(x))dt \\
                \leq (y-x)\int_0^1 L(z(t) - x)dt \\
                = (y-x)\int_0^1 L(x +t(y-x) - x)dt \\
                = \nabla f(x)(y-x) + L(y-x)\int_0^1 t(y-x)dt \\
                = \nabla f(x)(y-x) + L(y-x)^2 \int_0^1 tdt \\
                = \nabla f(x)(y-x) +\frac{L}{2}  (y-x)^2 \\
                $$
    - theorem
        $$
        -LI \preceq \nabla^2 f(x) \preceq LI
        $$
        if and only if Lipschitz continuous 
- Holder continuous    
- 線形計画 linear programming
    - 等式標準系
        $$
        \min c^\top x \\
        s.t.\ Ax = b \\
        x \geq 0
        $$
    - slack variable
        $$
        Gx + s = h
        $$
        不等式を等式に変換するための非負の変数のことをスラック変数という
    - 双対問題 dual problem
        - variable
            $$
            A = 
            \begin{pmatrix}
            a_{11} & a_{12} & \cdots & a_{1m} \\
            a_{21} & a_{22} & \cdots & a_{2m} \\
            \vdots & \vdots & & \vdots \\
            a_{n1} & a_{n2} & \cdots & a_{nm}
            \end{pmatrix}
            \\
            $$
            $$
            b = (b_1, b_2, ..., b_n)^\top 
            $$
            $$
            c = (c_1, c_2, ..., c_m)^\top
            $$
            $$
            y = (y_1, y_2, ..., y_n)^\top
            $$
            $$
            x = (x_1, x_2, ..., x_m)^\top
            $$
        $$
        \min c^\top x \mathbb Rightarrow \max b^\top y
        $$
        - $(Ax, b) \mathbb Rightarrow y$
            $$
            c^\top x \geq c^\top A^{-1} b \geq y^\top b \\
            x \geq A^{-1}b
            $$
            - equal
                $$
                Ax = b \mathbb Rightarrow \forall y \in \mathbb R^n
                $$
                $$
                Ax \geq b \land Ax \leq b \mathbb Rightarrow y \geq 0 \lor y \leq 0
                $$
            - greater
                $$
                Ax \geq b \mathbb Rightarrow y \geq 0 
                $$
            - lower
                $$
                Ax \leq b \mathbb Rightarrow y \leq 0
                $$
        - $x \mathbb Rightarrow (A^\top y, c)$
            $$
            c^\top x \geq c^\top A^{-1} b \geq y^\top b \\
            c^\top A^{-1} \geq y^\top
            $$
            - equal
                $$
                \forall x \in \mathbb R^m \mathbb Rightarrow A^\top y = c
                $$
                $$
                x \geq 0 \lor x \leq 0 \mathbb Rightarrow A^\top y \geq c \land A^\top y \leq c
                $$
            - greater
                $$
                x \geq 0 \mathbb Rightarrow A^\top y \leq c
                $$
            - lower
                $$
                x \leq 0 \mathbb Rightarrow A^\top y \geq c
                $$
        - proof
            $$
            \min c^\top x \\
            s.t.\ Ax \geq b \\
            x \geq 0
            $$
            下界を求める
            $$
            c \geq A^\top y \\
            y \geq 0
            $$
            となるとき
            弱双対定理
            $$
            x^\top c \geq x^\top A^\top y \geq b^\top y
            $$
            が成立する。
            この時
            $$
            \min b^\top x \\
            s.t.\ A^\top y \leq c \\
            y \geq 0
            $$
            は上記の等式標準系の下界となる
            この条件式のことを等式標準系の双対問題という
        - 弱双対定理
        - 強双対定理
    - 単体法 simplex algorithm
        - 標準形
            $$
            \min c^\top x \\
            Ax = b \\
            x \geq 0
            $$
        - 基底行列 A_B
            逆行列が存在する
        - 非基底行列 A_N
        - 基底変数 x_B
        - 非基底変数 x_N
        $$
        A = A_B + A_N \\
        x =x_B + x_A \\
        Ax= 
        \begin{pmatrix}
        A_B & A_N
        \end{pmatrix}
        \begin{pmatrix}
        x_B \\
        x_N
        \end{pmatrix} \\
        = A_B x_B + A_N x_N = b
        $$
        - optimality
            $$
            Ax^* = b
            $$
            $$
            A^\top y^* + s^* = c
            $$
            $$
            x_i^* s_i^* = 0
            $$
            $$
            x^* \geq 0, s^* \geq 0
            $$
    - process
        - 標準形に変換
        - slack変数
        - +-変換
        - pivot列
        - pivot行
        - pivot要素
- 凸最適化 convex optimization
    - 単調性 monotony
        $$
        f(y) \geq f(x) + \nabla f(x)(y-x)
        $$
        $$
        (\nabla f(y) - \nabla f(x))(y-x) \geq 0
        $$
- 降下法 descent direction
    - descent direction
        $$
        d \in f(x + td) < f(x), \forall t > 0
        $$
- problems
    - Weber problem
        $$
        \min_{x,y} \sum_{i=1}^{n} \sqrt {(x_i-x)^2 + (y_i-y)^2}
        $$
    - 最小円問題 smallest/minimum enclosizing circle problem
        $$
        \min_{x, y, r} \pi r^2 \\
        .s.t \\
        (x_i-x)^2 + (y_i-y)^2 \leq r^2 \\
        r \geq 0
        $$
    - network flow problem
        - MF maximum flow problem
            - directed graph
                $$
                G = (V, E)
                $$
            - weight
                $$
                W : E \to \mathbb R \\
                w_{ij} = W((i, j))
                $$
            - capacity constraint
                $$
                x_{ij} \leq u_{ij}
                $$
            - flow conservation
                $$
                \sum_{(i, j) \in E} x_{ij} - \sum_{(j, i) \in E} x_{ji} = 0
                $$
        - minimum cut problem
        - maximum flow minimum cut problem
        - minimum cost flow problem
        - Fold-Fulkerson algorithm
- calculation method
    - Newton method
        $$
        x_{k+1} = x_k - \frac{\nabla f(x_k)}{\nabla^2 f(x_k)}
        $$
    - semi-Newton method
        - DFP
            $$
            \nabla f(x_k + s_k) = \nabla f(x_k) + Bs_k + ...
            $$
- 粒子群最適化 PSO particle swarm optimization
    https://qiita.com/ganyariya/items/ae5a38a3537b06bd3842