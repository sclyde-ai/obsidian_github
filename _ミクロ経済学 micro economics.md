---
alias:
    ['ミクロ経済学', 'micro economics']
---
- 消費者理論
        - 財 goods
            $$
            x = (x_1, x_2, ... , x_N) \in \R^N \\
            X \subset \R^N
            $$
            - 完全補完財 perfect complements
            - 完全代替財 perfect substitutes
        - 選好関係 preference relation
            $$
            \succeq \ \subset X \times X
            $$
            - 広義選好関係 weak
                $$
                x \succeq y  
                $$
            - 狭義選好関係 strict
                $$
                x \succ y
                $$
                - def
                    $$
                    x \succeq y \land \lnot(y \succeq x)
                    $$
            - 無差別関係 indifference
                $$
                x \sim y
                $$
                - def
                    $$
                    x \succeq y \land y \succeq x
                    $$
            - 合理性
                - 完備性
                    $$
                    \forall x, y \in \R^l_+, x \succeq y \lor y \succeq x
                    $$
                - 推移性
                    $$
                    \forall x, y, z \in \R^l_+, x\succeq y \land y \land z \Rightarrow x \succeq z 
                    $$
                上記2つを満たす時、選好は合理的という
        - 効用関数 utility function
            $$
            u : X \to \R \\
            u(x) \geq u(y) \Leftrightarrow x \succeq y
            $$
            - 危機回避 risk aversion
            - 危機中立 risk neutral
            - 危機愛好 risk
            - 命題
                選好 $\succeq$ を表現する効用関数が存在するとする
                このとき選好 $\succeq$ は完備性と推移性を満たす
            - 効用最大化
                - 予算制約
                    $$
                    p \cdot x  = p_1x_1 + ...+ p_nx_n \preceq I 
                    $$
                    - 価格ベクトル
                        $$
                        p \in \R_+^l
                        $$
                    - 所得
                        $$
                        I \in \R_+
                        $$
                - 効用最大化問題
                    $$
                    \max\ \ u(x)\ \  s.t.\ \ p \cdot x \leq I, x \in \R^l_+
                    $$
                    - 解
                        $$
                        x (P, I) \in \R_+^l
                        $$
                - 所得効果
                    $$
                    $$
                - 価格効果
                - 代替効果
        - 期待効用理論 expected utility hypothesis
            $$
            \mathbb E[U] =
            $$
            - 確実性等価 CE certainty equivalent
            - risk premium
            - 
- 生産者理論
    - 生産関数 production function
        - ゴブダグラス型生産関数
            $$
            f(x) = kx_1^{a_1}...x_N^{a_N} \\
            \sum_{i=1}^n a_i = 1
            $$
            $$
            Y = A\ L^\alpha K^{1-\alpha}
            $$
        - レオンチェフ型生産関数 Leontief Production Function
            $$
            f(x) = min\{a_1x_1, ..., a_Nx_N\}
            $$
        - CES型生産関数 Constant Elasticity of Substitution
            $$
            f(x) = k (a_1x_1^\rho...a_Nx_N^\rho)^{\frac{1}{\rho}} \\
            \sum_{i=1}^n a_i = 1
            $$
            $$
            Y = A \left[ \alpha K^{\rho} + (1-\alpha) L^{\rho} \right]^{\frac{1}{\rho}}
            $$
        - 線形生産関数 Linear Production Function
    - ゲーム理論 game theory
        - game index
            - 2 players 2 goods
                - player
                    $$
                    \{1, 2\}
                    $$
                - goods
                    $$
                    x, y \in \R
                    $$
                - consumer vector
                    $$
                    z_i = (x_i, y_i) \in \R^2_+
                    $$
                - 効用関数 utility function
                    $$
                    u_i : \R^2_+ \to \R
                    $$
                    - linear utility
                        $$
                        u_i (z_i) = q_{ix}x_i + q_{iy}y_i \\ q_{ix}, q_{iy} > 0 \\
                        q_{ix} + q_{iy} = 1 
                        $$
                    - the combination of preference
                        $$
                        \mathcal D = \mathcal D_1 \times \mathcal D_2
                        $$
                - 効率性 effectivity
                    $$
                    \lnot \exist z' \in X \\ 
                    u_i (z_i' ) \geq u_i(z_i), \forall i = 1, 2 \\
                    u_j (z_j' ) > u_j(z_j), \exist j = 1, 2 
                    $$
                    then, $z \in X$ is effective
                - 個人合理性 individual rationality
                    $$
                    u_i (z_i) \geq u_i(\omega_i), \forall i = 1, 2
                    $$
                - 対戦略性 strategy-proofness
                - Hurwicz theorem
                    二財に消費者の純粋交換経済において
                    効率性、個人合理性、耐戦略性
                    を満たす選択関数は存在しない
                - Arrow’s impossibility theorem
                    定義域の無制限性 $\mathcal D = \mathcal R^n$
                    社会厚生関数 $F : \mathcal D\to \mathcal R$
                    pareto 
                    二項独立性
            - Nash bargaining solution
                - 交渉問題
                    $$
                    P = (\alpha_A, d_A, \alpha_B, d_B, \pi)
                    $$
                - ナッシュ交渉解
                    $$
                    \max_{x_A, x_B} (x_A-d_A)(x_B-d_B)\ .s.t\ \alpha_A x_A+\alpha_Bx_B = \pi
                    $$
                    - 導出
                        - ラグランジュ
                            $$
                            x_B - d_B -\alpha_A \lambda = 0
                            $$
                            $$
                            x_A - d_A -\alpha_B \lambda = 0
                            $$
                            $$
                            \alpha_A x_A+\alpha_Bx_B = \pi
                            $$
                        $$
                        \alpha_A x_A - \alpha_A d_A = \alpha_B x_B - \alpha_B d_B
                        $$
                        $$
                        2\alpha_A x_A - \pi = \alpha_A d_A- \alpha_B d_B
                        $$
                - 公理
            - Shapley value
                the center of weber set
                the average of contributing distribution
                the centroid of core
                $$
                f_i^{Sh}(v)=\frac{1}{n!}\sum_\pi x(\pi, i)
                $$
                - efficiency E
                    $$
                    \sum_{i \in N}f_i^{Sh} = v(N)
                    $$
                - addictivity A
                    $$
                    f_i^{Sh}(v+u)  = f_i^{Sh}(v) + f_j^{Sh}(u)
                    $$
                - symmetry S
                    $$
                    \forall i, j \notin S \subset N, \\ 
                    \Delta^i(v, S) = \Delta^j(v, S)
                    \\
                    \Rightarrow f_i^{Sh}(v) = f_j^{Sh}(v)
                    $$
                - null player N
                    $$
                    \forall i \notin S \subset N,
                    \\ \Delta^i(v, S) = 0 \Rightarrow f_i^{Sh} = 0
                    $$
            - strategy-proof
                - obviously strategy-proof
        - game type
            - cooperative/coalition or not
                - cooperative/coalitional game 協力ゲーム
                    $$
                    (N, v) 
                    $$
                    - player
                    $$
                    N = \{1, 2, ..., n\}
                    $$
                    - 特性関数
                    $$
                     v: S \subset N \to \R
                    $$
                    - 優加法性
                        $$
                        \forall S, T \subset N,\ \\S\cap T = \phi \Rightarrow v(S \cup T) \geq v(S) + v(T)
                        $$
                    - 凸性
                        $$
                        \forall S, T \subset N, 
                        \\ v(S \cup T)+v(S \cap T) \geq 
                        v(S) + v(T)
                        $$
                        - 同値条件
                            $$
                            \forall i  \in N, S \subset T \subset N/\{i\} 
                            \\v(T \cup\{i\})-v(T) \geq
                            v(S \cup\{i\})-v(S)
                            $$
                            - 導出
                                - 上 → 下
                                    $$
                                    v(S \cup T)- v(T) \geq 
                                    v(S) - v(S \cap T)
                                    $$
                                    $$
                                    T  = T, S = S \cup \{i\}
                                    $$
                                    と置くと成立。
                                - 下→ 上
                                    $$
                                    T/S = \{i_1, ..., i_k\}, S\cup T = R
                                    $$
                    - 配分
                        $$
                        \mathcal{I}(v) = \{x \in \R^n |\\ x_i \geq v(\{i\}) \land \\
                        \sum_{i=1}^nx_i = v(N) \}
                        $$
                        - 個人合理性
                        $$
                        x_i \geq v(\{i\})
                        $$
                        - 全体合理性
                        $$
                        \sum_{i=1}^nx_i = v(N)
                        $$
                    - コア
                        $$
                        \forall S \subset N, \sum_S x_i \geq v(S)
                        $$
                        - 命題
                            $$
                            v\ is \ convex \Rightarrow\forall\pi, x(\pi) \in C(v)
                            $$
                    - 貢献度
                        $$
                        x(\pi, i)=
                        v(P(\pi, i)\cup\{i\})-v(P(\pi, i))
                        $$
                        - 順列
                        $$
                        \pi: N \rightarrow\N
                        $$
                        - 前列集合
                        $$
                        P(\pi, i) = \{j \in N | \pi(j) < \pi(i)\}
                        $$
                        - 貢献度配分
                        $$
                        x(\pi) = (x(\pi, 1), ..., x(\pi, n))
                        $$
                    - weber set
                        貢献度配分の重み付き和
                        $$
                        \mathcal{W}(v) = \{x \in \R^n | \\ x=\sum_{\pi \in \Pi_N} \alpha(\pi)x(\pi), \\ \alpha(\pi) \geq 0, \\ \sum_{\pi \in \Pi_N}\alpha(\pi)=1\}
                        $$
                    - 不満
                        $$
                        e(S, x) = v(S)- \sum_{i \in S} x_i
                        $$
                        - コア配分
                            $$
                            \forall S \subset N, e(S, x) \leq 0
                            $$
                        - 不満ベクトル
                            不満の大きい順に並べたもの
                            $$
                            sort\ x
                            $$
                            ```python
                            def sort(x): 
                               for i in range(n):
                                  for j in range(i, n):
                                     if(x[i] < x[j]):
                                        temp = x[i]
                                        x[i] = x[j]
                                        x[j] = temp
                            ```
                    - 仁
                        受容的な配分が存在しない配分
                        $$
                        \forall y \in \mathcal{I}(v), \lnot(y\ accept\ x)
                        $$
                        - 受容的な配分
                            最初に異なる成分がより小さい配分
                            $$
                            x\ accept\ y
                            $$
                            ```python
                            def accept(x, y): 
                               for i in range(n)
                                  if(x[i] > y[i]):
                                     return x;
                                  elif(x[i] < y[i]):
                                     return y;
                            ```
                        - 計算algorithm
                            ```python
                            v = {
                                "ABC": 
                                "AB":
                                "BC":
                                "CA":
                                "A":
                                "B":
                                "C":
                            }
                            ```
                    - voting game
                        $$
                        (q; w_1, ..., w_n)
                        $$
                        - player
                        $$
                        N = \{1, 2, ..., n\}
                        $$
                        - 票数
                            $$
                            w_i
                            $$
                        - 可決数
                            $$
                            q
                            $$
                        - 勝利提携
                            $$
                            S \subset N, \sum_{i \in S} w_i \geq q
                            $$
                        - Shapley–Shubik 指数
                        - pivot
                            $$
                            v(P(\pi, i)\cup\{i\})=1,\ v(P(\pi, i))=0
                            $$
                        - 拒否権player
                            $$
                            v(S) = 1 \Rightarrow i \in S
                            $$
                    - TU transferable utility game
                        $$
                        v: 2^N  \to \R
                        $$
                        - payoff vector
                            $$
                            \phi : \mathcal G^n \to \R^n
                            $$
                        - shapley value
                            the center of weber set
                            the average of contributing distribution
                            the centroid of core
                            $$
                            f_i^{Sh}(v)=\frac{1}{n!}\sum_{T \subset N, i. \in T} \frac{\lambda_T^v}{|T|}
                            $$
                            - general axiom
                                - efficiency E
                                    $$
                                    \sum_{i \in N}f_i^{Sh} = v(N)
                                    $$
                                - addictivity A
                                    $$
                                    f_i^{Sh}(v+u)  = f_i^{Sh}(v) + f_j^{Sh}(u)
                                    $$
                                - symmetry S
                                    $$
                                    \forall i, j \notin S \subset N, \\ 
                                    \Delta^i(v, S) = \Delta^j(v, S)
                                    \\
                                    \Rightarrow f_i^{Sh}(v) = f_j^{Sh}(v)
                                    $$
                                - null player N
                                    $$
                                    \forall i \notin S \subset N,
                                    \\ \Delta^i(v, S) = 0 \Rightarrow f_i^{Sh} = 0
                                    $$
                            - gain-loss axiom
                                - gain-loss GL
                                    $$
                                    v(N) = w(N) \land \exist i \in N, \phi_i(v)>\phi_i(w) \Rightarrow \exist j \in N, \phi_j(v)>\phi_j(w)
                                    $$
                                - 
                        - unanimity game
                            $$
                            u_T(S) = \left\{ 
                            \begin{alignedat}{} 
                            1 & & T \subset S \\
                            0 & & otherwise
                            \end{alignedat} 
                            \right.
                            $$
                            $$
                            \lambda_T^v = \left\{ 
                            \begin{alignedat}{} 
                            0 && |T| > 1\\
                            v(i) && otherwise
                            \end{alignedat} 
                            \right.
                            $$
                            - unanimity game is the basis of TU
                                $$
                                v = \sum_{T \subset N, T \ne \phi} \lambda_T^v u_T
                                $$
                        - marginal contribution
                            $$
                            \Delta^i(v, S) = v(S \cup i)-v(S)
                            $$
                        - dummy player D
                            $$
                            i \in N, \Delta^i(v, S) = v(i), \forall S \subset N/i
                            $$
                        - inessential game IG
                            $$
                            v(S) = \sum_{i \in S} v(i), \forall S \subset N
                            $$
                        - null game NG
                            $$
                            0 \in \mathcal G^N, 0(S) = 0, \forall S \subset N
                            $$
                        - sign
                            $$
                            sign(a)= \left\{ 
                            \begin{alignedat}{} 
                            1 & & a>0 \\
                            0 & & a=0\\
                            -1 & & a<0
                            \end{alignedat} 
                            \right.
                            $$
                        - marginality M
                            $$
                            \Delta^i(v, S) = \Delta^i(w, S), \forall S \subset N
                            $$
                        - differential marginality DM
                            $$
                            \Delta^i(v-w, S) = \Delta^j(v-w, S), \forall S \subset N
                            $$
                        - sign differential marginality DM_
                            $$
                            sign(\Delta^i(v-w, S)) = sign(\Delta^j(v-w, S)), \forall S \subset N
                            $$
                        - pdf
                            [EZW2023.pdf](EZW2023.pdf)
                    - NTU non-transferable utility game
                        $$
                        (N, X, V, \mathcal{P})
                        $$
                        - player
                            $$
                            N = \{1, ..., n\}
                            $$
                        - 結果集合
                            $$
                            X = \{x_1, ..., x_m\}
                            $$
                        - 実現可能集合
                            ある提携の実現可能な集合
                            $$
                            S \subset N, V(S) \subset X \\
                            V(N) = X
                            $$
                        - 選好集合
                            $$
                            \mathcal{P} = (\succeq_i)_{i \in N}
                            $$
                        - block/支配
                            全てのplayerがxよりyがいい
                            $$
                            y\ dom_S\ x: y \succ_i x, \forall i \in S \\
                            \lnot (y\ dom_S\ x): \lnot (y \succ_i x), \exist i \in S
                            $$
                            $$
                            y\ dom\ x : \exist S \subset N, y\ dom_S x
                            $$
                            - コア
                                ブロックされない結果の集合
                                $$
                                C = \{x \in V(N)=X| \\
                                \forall S \subset N, \\
                                \forall y \in V(S), \\ 
                                \lnot (y\ dom_S\ x) \}
                                $$
                    - NTU voting game
                        - 勝利提携
                            $$
                            N \in \mathcal{W} \\
                            S \in \mathcal{W}, S \subset T \Rightarrow T \in \mathcal{W} \\
                            S \in \mathcal{W} \Rightarrow S^c \notin \mathcal{W}
                            $$
                        - コア
                            $$
                            C = \{x \in X| \\
                            \forall S \in \mathcal{W}, \\
                            \forall y \in X, \\ 
                            \lnot (y\ dom_S\ x) \}
                            $$
                        - サイクル
                            $$
                            \exist x_1, ..., x_m \in X, \\ x_mdom\ x_{m-1}dom\ ...\ dom\ x_1\ dom \ x_m
                            $$
                        - 命題
                            支配関係がサイクルを持たないとき、コアは非空
                            - 証明
                                コアが空であると仮定する。
                                $$
                                \forall x \in X, \exist y \in X, \exist S \in \mathcal{W}, \\ y\ dom_S\ x \\
                                \Leftrightarrow \\ \forall x \in X, \exist y \in X,  y\ dom\ x
                                \\ \Leftrightarrow \\
                                \exist x_1, ..., x_m \in X, 
                                \\ 
                                x_mdom\ x_{m-1}dom\ ...\ dom\ x_1\ dom \ x_m
                                $$
                        - 中村number
                            共通部分が空集合になる勝利提携の族の要素の最小値
                            $$
                            v(G) = min\{|\sigma|\ |\sigma \in  \Sigma \}
                            $$
                            $$
                            \Sigma =\{\sigma | \sigma = (S_j)_{j=1}^k \subset \mathcal{W}, \\
                            \cap_{j=1}^k S_j =\phi\}
                            $$
                    - 非分割財の交換
                        $$
                        (N, \mathcal{P})
                        $$
                        - player
                            $$
                            N = \{1, ..., n\}
                            $$
                        - 選好集合
                            $$
                            \mathcal{P} = (\succeq_i)_{i \in N}
                            $$
                        - 個人合理性
                            $$
                            \forall i \in N, (x_i = i) \lor (x_i \succeq_i i)
                            $$
                        - pareto支配
                            $$
                            y\ pareto\ x :\\
                            \forall i \in N, (y_i = x_i) \lor (y_i \succ_i x_i) \\
                            \exist i \in N, y_i \succ_i x_i
                            $$
                            - pareto効率性
                                $$
                                \forall y \in \R^n, \lnot(y\ pareto \ x)
                                $$
                        - block/支配
                            $$
                            S\ block\ x : \\
                            \{y_i\}_{i \in S} = S \\
                            \forall i \in S, (y_i = x_i) \lor (y_i \succ_i x_i) \\
                            \exist i \in S, y_i \succ_i x_i
                            $$
                            - コア配分
                                $$
                                \forall S \subset N, \lnot(S\ block\ x)
                                $$
                        - TTC top trading cycle
                            - code
                                ```python
                                N = ["1", "2", "3", "4", "5", "6", "7"]
                                P = {
                                    "1": ["5", "6", "7", "1", "2", "3", "4"],
                                    "2": ["3", "4", "5", "6", "7", "1", "2"],
                                    "3": ["4", "5", "2", "7", "1", "3", "6"],
                                    "4": ["1", "2", "3", "4", "5", "6", "7"],
                                    "5": ["4", "5", "2", "3", "6", "7", "1"],
                                    "6": ["7", "1", "2", "3", "4", "5", "6"],
                                    "7": ["1", "7", "4", "5", "6", "3", "2"]
                                }
                                def search_cycle(P, i, cycle):
                                    if(i in cycle):
                                        return 
                                    cycle.append(i)
                                    search_cycle(P, P[i][0], cycle)
                                while(P):
                                    cycle = []
                                    search_cycle(P, list(P.keys())[0], cycle)
                                    print(cycle)
                                    for elem in cycle:
                                        P.pop(elem)
                                    for key in P:
                                        for elem in cycle:
                                            if elem in P[key]:
                                                P[key].remove(elem)
                                ```
                            - 命題
                                TTC アルゴリズムによって決まる配分は一意なコア配分である.
                            - 競争均衡
                                $$
                                \{d_1(p), ..., d_n(p)\} = \{1, ..., n\}
                                $$
                                この時、この配分を競争均衡配分、価格ベクトルを競争均衡価格という。
                                - 価格ベクトル
                                    $$
                                    p = (p_1, ..., p_n)
                                    $$
                                - 予算制約
                                    $$
                                    p_j \leq p_i
                                    $$
                                - 需要関数
                                    $$
                                    d_i(p) \in \{1, ..., n\}
                                    $$
                    - matching 理論
                        $$
                        u\\
                        (1)\ u(s) \in C \cup {s}, \forall s\in S \\
                        (2)\ u(c) \subset S, |u(c)| \leq q_c, \forall c \in C \\
                        (3)\ u(s) = c \Leftrightarrow s \in u(c), \forall s \in S, \forall c \in C
                        $$
                        - 一対一
                        - 多対一
                        - 個人合理性
                            $$
                            \forall s\in S, \\ 
                            (u(s)=s) \lor (u(s) \succ_s s) \\
                            $$
                            $$
                            \forall c \in C, \forall s \in u(c), s \succ_c c
                            $$
                        - blocking pair
                        - 
                - non-cooperative game 非協力ゲーム
            - static or dynamic
                - static/simultaneous game
                - dynamic/sequential game
            - info
                - game of/with complete info
                - game of/with complete info
        - auction
            - general model
                - player
                    $$
                    N = \{1,2,..., n\}
                    $$
                - value
                    $$
                    V = 
                    $$
                - result
                    - allocation
                    - payment
                - 
            - auction type
                |  | open/oral 公開型 | sealed 封印型 |
                | --- | --- | --- |
                | ascending/first price 競り上げ/第一価格 |  |  |
                | descending/second price 競り下げ/第二価格 |  |  |
                - ascending-bid auction(English auction)
                - descending-bid auction(Dutch auction)
                - first price sealed-bid auction
                - second price sealed-bid auction(Vickrey auction)
            - auction mechanism
                - goods
                    $$
                    \{A_i\}_{i \in \{1, 2, ..., n\}} \\
                    A \subset A_1 \times ... \times A_n
                    $$
                - example
                    - 同質財・複数需要
                        - 財がS単位売られる
                        - $\bar a_i \leq S$ : iが落札可能な上限
                        $$
                        A_i = \{0, 1, ..., \bar a_i\} \\
                        A = \{\bm a | a_i \in A_i, \sum_{i \in N} a_i \leq S\} \\
                        \bm a = (a_i)_{i \in N}
                        $$
                    - 異質財・単一需要
                        $$
                        A_i = \{\phi, x, y, z\} \\
                        A = \{\bm a, a_i \in A_i, a_i \ne a_j, \forall i \ne j\} \\
                        \bm a = (a_i)_{i \in N}
                        $$
                    - 異質財・複数需要
                        $$
                        A_i = 2^{\{x, y, z\}} \\
                        A = \{\bm a, a_i \in A_i, a_i \ne a_j, \forall i \ne j\} \\
                        \bm a = (a_i)_{i \in N}
                        $$
                - VSG mechanism
                    - 定理
                        単一財オークションでのVCG mechanismは第二価格オークションと一致する
                        - 1
                            $$
                            \hat v_i < \max_{j \ne i} \hat v_j
                            $$
                            $$
                            a_i(\hat v) = 0 \\
                            a_j = 1, \exist j \ne i \\
                            W_{-i}(\hat v) = \sum_{j \ne i} \hat v_j(a_j(\hat v)) \\
                            t_i(\hat v) = 0
                            $$
                        - 2
                            $$
                            \hat v_i\geq \max_{j \ne i} \hat v_j \\
                            \hat a(\hat v) = 1 \\
                            \sum_{j \ne i} \hat v_j (a_j(\hat v_i))= 0 \\
                            W_{-i}(\hat v_{-i}) = \max_{j \ne i} \hat v_j \\
                            t_i(\hat v) = \max_{j \ne i} \hat v_j
                            $$
                        - 
            - 複数財オークション
                - 単位財
                - 複数財
                    - 同一財
                    - 異質財
                    - 例
                        - 国債
                        - 周波数
                        - インターネット広告
                - 入札者の需要構造
                    - 単一需要
                    - 複数需要
                        - 代替財
                        - 補完財
                    - mechanism
                        - VCG mechanism
                        - Ausbel auction
            - Ausbel auction
                - time
                $$
                t \in [0, \infin)
                $$
            - the model
                $$
                s\in \{s_1, s_2\} \\
                d \in \{d_1, d_2\} \\
                X = \{s_1, s_2\}
                $$
                - prospect theory
                $$
                U(x) = V(x) - \lambda L(x) 
                $$
                |  | d1 | d2 |
                | --- | --- | --- |
                | s1 | v1 | -\lambda l1 |
                | s2 | -\lambda l2 | v2 |
                - error
                    $$
                    \delta^1 = u_i(s_2d_2) - u_i(s_2d_1)
                    $$
                - bias
                    $$
                    b_i = \frac{\delta_i^2}{\delta^1_i + \delta^2_i}
                    $$
                - expected value
                    $$
                    EV_i = p_i \delta^1_i + (1-p_i)\delta^2_i
                    $$
                - decision rule
                    - common prior belief
                        $$
                        p \in \{0, 1\}
                        $$
                    $$
                    g(b, p) = d_2 if b \leq p\\
                    g(b, p) = d_1
                    $$
                - BAR bias aggregation rule
                    - error proportional rule
                        $$
                        f^\omega(u) = \argmax_f \sum EV_i
                        $$
                    - properties
                        - anonymity
                            $$
                            f(\mu())
                            $$
                        - unaminity
                            $$
                            b_i = b_j \Rightarrow f(u) = b_i
                            $$
                        - monotonicity
                            $$
                            \exist 
                            $$
                        - asymmetry
                        - 
                    - 
                - social welfare function
                - preference
            - government/public auction
        - matching
            - model
            - property
                $$
                $$
        - mechanism design
            $$
            (M, g)
            $$
            $M$ : the message space of i
            $M = \times_{i \in N} M_i$  : message profile space
            $g : M \to A$ : 帰結関数
            - direct mechanism
                $$
                M_i = \mathcal D_i, g = f
                $$
            - weak dominant action
                $$
                \forall m'_i \in M_i, m_{-i} \in M_{-i} \\
                g(m_i, m_{-i}) \\
                $$
            - 社会選択関数
        - game example
            - Baysian game
            - Borda/scoring game
                - voter
                    $$
                    I = \{1, 2, ..., n\}
                    $$
                - alternatives
                    $$
                    X = \{x_1, x_2,..., x_m\}
                    $$
                - score vector
                    $$
                    a = (a_1, a_2,...,a_m) \\
                    $$
                - Borda vector
                    $$
                    b = (1, \frac{m-2}{m-1},..., \frac{m-l}{m-1}..., \frac{1}{m-1}, 0)
                    $$
                - preference profile
                    $$
                    \succeq = (\succeq_1, \succeq_2,..., \succeq_n) \in \mathfrak F^n
                    $$
                - ranking
                    $$
                    r(\succeq_i, x) = |\{y\in X:y \succeq_i x\}|
                    $$
                    $$
                    \sum_{x \in X} r(\succeq_i, x) = \frac{m(m+1)}{2}
                    $$
                - scoring rule
                    on \mathfrak F^n
                    $$
                    f:\mathfrak F^n \to \R^m \\
                    f(\succeq) = (\sum_{i=1}^n a(r(\succeq_i, x_j))_{j \in \{1,...,m\}}
                    $$
                - Borda rule
                    on \mathfrak F^n
                    the score vector is Borda vector
                - f -winner
                    at \succeq \in \mathfrak F^n
                    $$
                    f(\succeq, x) \geq f(\succeq, y), \forall y \in X
                    $$
                - Borda winner
                    f-winner of Borda rule
                - Condorcet criterion
                - pairwise-majority-loser
                    $$
                    \exist y \in X, |\{i \in I : x \succ_i y\}| < |\{i \in I : y \succ_i x\}| 
                    $$
                - strictly majority un-dominated
                    $$
                    \exist y \in X, |\{i \in I : x \succ_i y\}| < |\{i \in I : y \succ_i x\}| 
                    \\ 
                    \Rightarrow 
                    \\
                    \exist z \in X, |\{i \in I : x \succ_i z\}| > |\{i \in I : z \succ_i x\}|
                    $$
                - preposition 1
                    $$
                    \forall m \geq 3, \forall n \geq 2, \forall \succeq \in \mathfrak F^n, \forall x \in BW, \\
                    \exist y \in X, |\{i \in I : x \succ_i y\}| < |\{i \in I : y \succ_i x\}| \\
                    \exist z \in X, |\{i \in I : x \succ_i z\}| > |\{i \in I : z \succ_i x\}|
                    $$
                    - proof
                        - lemma 1
                        - 
                - 
                - pairwise-majority-winner
                    $$
                    \exist z \in X, |\{i \in I : x \succ_i z\}| > |\{i \in I : z \succ_i x\}|
                    $$
                - Borda all winner
                - pair all winner
                - pair winner
                - Baldwin method
                - Condorcet cycles/paradox
                - pdf
                    [OkamotoSakai(2019).pdf](OkamotoSakai(2019).pdf)
            - BCK
                - setting
                    - individuals
                        $$
                        n \in \N
                        $$
                    - utility distribution
                        $$
                        u \in \R
                        $$
                        the level of lifetime well-beibg
                    - all possible distribution
                        $$
                        \Omega = \bigcup_{n \in \N} \R^n
                        $$
                    - r-fold replica of u
                        $$
                        1_r
                        $$
                    - at least as good as
                        $$
                        (u, v) \in R
                        $$
                    - threshold
                        $$
                        \theta \in \R
                        $$
                    - low set
                        $$
                        L^n(u) = \{i \in \{1, ..., n\}| u_i < \theta\}
                        $$
                    - equal set
                        $$
                        E^n(u) = \{i \in \{1, ..., n\}| u_i = \theta\}
                        $$
                    - higher set
                        $$
                        H^n(u) = \{i \in \{1, ..., n\}| u_i > \theta\}
                        $$
                - betterness
                    $$
                    \exist g \in G, \alpha \in \R_{HE}, \sup_{a \in \R} g(a) \leq g(\alpha) \\ 
                    \forall n, m \in \N, \forall u \in \R^n, \forall v \in \R^m, 
                    $$
                - repugnant conclusion
                - sadistic conclusion
                - critical set/band
                    $$
                    Q^k(u) = (\alpham - \frac{}{})
                    $$
                - critical band utititarinanism
                    $$
                    \sum_{i = 1}^n u_i-\alpha \geq \sum_{i = 1}^m u_i-\alpha 
                    $$
                    $$
                    \sum_{i = 1}^n [u_i-\alpha] - \sum_{i = 1}^m [u_i-\alpha] > h(|n-m|) 
                    $$
                - generalized threshold critical
                    - axiom
                        - minimal increasingness
                            $$
                            \forall a, b,  a> b  
                            $$
                            a is better 
                        - incremental equity
                            $$
                            (u_1, ... u_i+d, ..., u_n) \\
                            = (u_1, ... u_j+d, ..., u_n) \\
                            $$
                        - non-empty
                        - exsitence independence
                        - symmetric
                        - 
                - Q
                    $$
                    Q^k(u) = (\alpha- \frac{h(k)}{k}, \alpha +\frac{h(k)}{k}) 
                    $$
        - micro
            - 純粋交換経済
                - player
                    $$
                    \{1, 2\}
                    $$
                - goods
                    $$
                    x, y \in \R
                    $$
                - price
                    $$
                    p_x, p_y \in \R_+
                    $$
                - utility function
                    $$
                    u(x_i, y_i) = x_i^{\frac{1}{2}}y_i^{\frac{1}{2}}
                    $$
            - 社会厚生関数 SWF social welfare function
                - 順序集合 X
                $$
                f: S \to X
                $$
                - condition U 定義域の非制約性
                - condition P パレート原理
                    $$
                    \forall x, y \in X, 
                    $$
                - condition I 無関係な選択肢からの独立性
                - condition D 非独裁性
        - theorem
            - 厚生経済学の第一基本定理
                市場が競争的
                ならば
                均衡における配分はパレート効率的
        - example
            - prisoner’s dilemma 囚人のジレンマ
            - 合理的な豚
            - stag hunt game
                |  | stag | rabbit |
                | --- | --- | --- |
                | stag  | 2, 2 | 0, 1 |
                | rabbit | 1, 0 | 1, 1 |
            - chicken game
            - matching penny
            - strategic voting
            - public goods dilemma
            - battle of the sexes
            - hawk-dove game
            - 予期せぬ絞首刑 Unexpected hanging paradox/surprise test paradox
            - ultimatum game
            - trust game
            - St Petersburg paradox
            - coordination game
            - entry target
            - auction
            - majority game
        - pdf
        - abdul kadlogul and yasuda
        - yasuda yousuke
    - 公共経済学 public economics
        - 外部性 externality
            - 正の外部性
                - 例
                    - 予防接種
                    - 都市開発
                    - 教育
                - 問題点
                    - 供給が過小になる
                    - フリーライダー問題
                - 解決策
                    - 補助金
                ![正の外部性-余剰分析-1.jpg](%25E6%25AD%25A3%25E3%2581%25AE%25E5%25A4%2596%25E9%2583%25A8%25E6%2580%25A7-%25E4%25BD%2599%25E5%2589%25B0%25E5%2588%2586%25E6%259E%2590-1.jpg)
            - 負の外部性
                - モデル
                    - 生産者
                        $$
                        \Pi(x) = px - C_F(x)
                        $$
                    - 消費者
                        $$
                        U(x)=V(x) - px
                        $$
                    - 外部費用
                        $$
                        -C_R(x)
                        $$
                    - 最適化
                        $$
                        \max_x W(x):= \Pi(x)+U(x)-C_R(x)
                        $$
                - 例
                    - 公害
                    - 二酸化炭素排出
                    - 渋滞
                - 問題点
                    - 供給が過大になる
                    - 共有地の悲劇
                - 解決策
                    - ピグー税
                        $$
                        \max_x\ px-C_F(x)-tx
                        $$
                    - 排出権取引
                ![負の外部性-余剰分析.jpg](%25E8%25B2%25A0%25E3%2581%25AE%25E5%25A4%2596%25E9%2583%25A8%25E6%2580%25A7-%25E4%25BD%2599%25E5%2589%25B0%25E5%2588%2586%25E6%259E%2590.jpg)
            - ネットワーク外部性
                利用者が増えるほど、利便性or不便性が増していく現象
            - 水平的財政外部性
                同一政府レベル間での外部性
            - 垂直的財政外部性
                異なる政府レベル間での外部性
            - コースの定理
                1. 取引費用なし
                2. 所有権が明確
                3. 資産効果・所得効果が働かない
                4. 情報が完全
                この時、当事者間で交渉を行うことで最適な資源分配が達成できるという命題（政府の介入は不要）
            - 分権化定理
                公共財の選好が多様な場合、中央政府より地方政府の方が社会厚生の損失を最小限にできる。
            - ピグー税
        - 公共財 public
            - 非競合性
                個人の消費が他の人の消費機会を損なわない
            - 非排除性
                貢献への有無を問わず便益を享受できる
            - サミュエルソン条件 Samuelson condition
                $$
                \sum_{i=1}^N MRS_i = MC
                $$
                MRS_i : 各消費者iの限界代替率 marginal rate of substitution
                MC : 公共財の限界費用 marginal cost
                全ての消費者の限界便益の総和=公共財の限界費用
                - 導出
                    - 経済の構造
                        効用関数 U_i = U_i(x_i, G)
                        x_i : 消費者iの私的財消費量
                        G : 公共財の供給量
                    - 社会厚生の最大化
                        $$
                        \max \sum_{i=1}^N U_i(x_i, G)
                        $$
                    - 制約条件
                        $$
                        \sum_{i=1}^N x_i + C(G) = R
                        $$
                        C(G) : 公共財の供給費用
                        R : 社会の総資源
                    - ラグランジュ関数
                        $$
                        \mathcal{L} = \sum_{i=1}^N U_i(x_i, G) + \lambda \left( R - \sum_{i=1}^N x_i - C(G) \right)
                        $$
                        - 私的財条件
                            $$
                            \frac{\partial \mathcal{L}}{\partial x_i} = \frac{\partial U_i}{\partial x_i} - \lambda = 0
                            $$
                            $$
                            \frac{\partial U_i}{\partial x_i} = \lambda
                            $$
                        - 公共財条件
                            $$
                            \frac{\partial \mathcal{L}}{\partial G} = \sum_{i=1}^N \frac{\partial U_i}{\partial G} - \lambda \frac{dC(G)}{dG} = 0
                            $$
                            $$
                            \sum_{i=1}^N \frac{\partial U_i}{\partial G} = \lambda \cdot MC
                            $$
                        $$
                        \sum_{i=1}^N \frac{\frac{\partial U_i}{\partial G}}{\frac{\partial U_i}{\partial x_i}} = MC
                        $$
                        $$
                        \sum_{i=1}^N MRS_i = MC
                        $$
            - ナッシュ均衡(自発的な公共財の供給)
        - 格差/不平等 inequality
            - 評価に用いる情報
                - 帰結主義　結果により評価
                - 厚生主義　効用のみで評価
            - 社会厚生関数
                $$
                W(U_1, ..., U_2)
                $$
                - パレート基準
                - ベンサム型
                    $$
                    W^B = u_1+u_2
                    $$
                - ロールズ型
                    $$
                    W^B = min\{u_1, u_2\}
                    $$
            - 無知のヴェール
            - 不平等尺度
                - 平均所得
                    $$
                    \mu = \frac{1}{N} \sum y_i
                    $$
                - 均等分配等価所得
                    $$
                    W(y_1, ..., y_N) = W(y^E, ..., y^E)
                    $$
                - セン測度
                    $$
                    s(y_1, ..., y_N) = 1-\frac{y^E}{\mu}
                    $$
                    - 不平等と社会厚生関数
                        $$
                        s(x) \leq s(y) \Leftrightarrow W(x) \geq W(y)
                        $$
                    - ジニ係数
                        $$
                        W(y) = \sum[2(n-i)+1]y_i
                        $$
        - 課税/給付 tax/subsidy
            - 税金 tax
                - 直接税
                    人に対しての税
                    - 所得税
                    - 法人税
                - 間接税
                    商品に対しての税
                    - 消費税
                    - 関税
                - 従量税
                - 従価税
                - 国税
                - 地方税
                - 一括税
                - 個別物品税
                - 一律物品税
            - 物品課税
                - 従量税
                    量に応じて税を付与
                    - 消費者
                        $$
                        \max_x V(x)-(p+t)x
                        $$
                - 従価税
                    価格に応じて税を付与
                    - 消費者
                        $$
                        \max_x V(x)-(1+t)px
                        $$
                - 従量税=従価税(完全競争市場)
                - 一括税
                    定額を徴収
                - 一律物品税
                    全ての物品に従価税
                    $$
                    max
                    $$
                - 一括税=一律物品税(完全競争市場)
            - 所得課税
            - 法人課税
            - 給付
            - アトキンソン・スティグリッツの定理
                $$
                \bar{U}_1 \leq V_1(C_1, Y_1)
                $$
        - sufficientarianism
            focuses on ensuring everyone has "enough" of a relevant good, rather than prioritizing equality or maximizing the well-being of the least well-off
    - 不完全競争市場
        - 独占市場
        - 複占市場
        - 寡占市場
        - 独占的競争
            差別化による独占
            - 例
                - 書籍
                - ブランド品
        - 自然独占(費用低減産業)
            初期費用が膨大なので参入障壁が発生する
            - 例
                - 国家規模の産業
    - Arrow=Debreu 経済
        - market 市場
            - commodity 商品
                $$
                n \in N 
                $$
            - price vector 価格
                $$
                p = (p_n)_{n \in N}
                $$
        - household 家計
            $$
            i \in I
            $$
            - endowment 初期分配
                $$
                r^i \in \R^N_+
                $$
            - ownership 雇用
                $$
                \sum_{i \in I} a^{i, j} = 1, \forall j \in J
                $$
            - income 収入
                $$
                M^i(p) = \langle p, r^i \rangle + \sum_{j \in J} a^{i, j} \Pi^j(p)
                $$
            - CPS consumption possibility set 消費可能集合
                $$
                CPS^i \subset \R_+^N
                $$
            - preference relation 選好関係
                $$
                \succeq^i
                $$
            - utility function 効用関数
                $$
                u^i : CPS^i \rightarrow [0, 1]
                $$
            - consumption plan 消費計画
                $$
                x^i \in CPS^i
                $$
            - budget 予算
                $$
                B^i (p) = \{x^i \in CPS^i : \langle p, x^i \rangle \leq M^i (p)\}
                $$
            - demand 需要
                $$
                D^i (p) \in \R^N_+ \\
                D^i (p) := \arg \max_{x^i \in B^i (p)} u^i (x^i)
                $$
            - consumption plans at least 最低消費額
                $$
                U^i_+(x^i) \subset CPS^i
                $$
        - producer 生産者
            $$
            j \in J
            $$
            - production possibility set 生産可能集合
                $$
                PPS^j \in \R^N \\ 
                investment\ of \ n < 0 \\
                production\ of \ n > 0
                $$
            - production plan 生産計画
                $$
                y^j \in PPS^j
                $$
            - supply 供給
                $$
                S^j (p) := \arg \max_{y^j \in PPS^j} \langle p, y^j \rangle
                $$
            - profit 利益
                $$
                \Pi^j (p) := \langle p, S^j(p) \rangle = \max_{y^j \in PPS^j} \langle p, y^j \rangle
                $$
        - aggregate 統合
        - economy 経済
            $$
            (N, I, J, \succeq^i, CPS^i, PPS^i)
            $$
            - economy with initial distribution 初期経済
                $$
                (r^i, a^{i,j})_{i \in I, j \in J}
                $$
            - state 状態
                $$
                ((p_n)_{n \in N}, (x^i)_{i \in I}, (y^j)_{j \in J})
                $$
            - feasible 実現可能性
                $$
                \sum_{i \in I} x^i \preceq \sum_{j \in J} y^j + r
                $$
            - state price vector 状態一致価格
                $$
                p_{DS} \\ (p_{DS}, (D^i(p))_{i \in I}, (S^j(p))_{j \in J})
                $$
            - equilibrium price vector 均衡価格
                $$
                Z(p)_n = 
                \begin{cases} 
                \leq 0 \ (p_n = 0) \\
                = 0 \ (p_n > 0)
                \end{cases}
                $$
            - equilibrium state均衡状態
                $$
                p_{DS} = Z(p)
                $$
        - story
            | household 家計 | producer 生産者 |
            | --- | --- |
            | 初期分配と雇用を設定 |  |
            | 初期分配を売却 |  |
            |  | 生産者同士で財の交換 |
            |  | 利益最大化で生産 |
            |  | 生産物を全て売却 |
            |  | 利益を従業員に分配 |
            | 利益最大化で消費 |  |
        - diminishing marginal utility
        - shapley-folkman-lemma
        - debureu theorem
    - 用語 words
        - セン測度
        - fuzzy measure
            - Choquet integral
            - website
                [https://www.sciencedirect.com/topics/mathematics/choquet-integral#:~:text=Choquet Integral is an aggregation,is the number of criteria](https://www.sciencedirect.com/topics/mathematics/choquet-integral#:~:text=Choquet%20Integral%20is%20an%20aggregation,is%20the%20number%20of%20criteria).