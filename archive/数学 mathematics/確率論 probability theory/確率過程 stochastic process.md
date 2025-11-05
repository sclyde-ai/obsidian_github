---
alias:
    ['確率過程', 'stochastic process']
---
- 確率空間 $(\Omega, \mathcal F, P)$
- 確率変数 X
    $$ X :T\times \Omega \to \mathbb R\\ \forall t \in T, A \in \mathcal B(\R), \{\omega \in \Omega|X(t, \omega) \in A\} \in \mathcal F $$
    for all t in T, X(t,•) is F-measurable
- 時間(全順序集合) T
    - 離散確率過程 : $\mathbb N$
    - 連続確率過程 : $\R_+$
$$ \{X_t\}_{t \in T} $$
これを確率過程という
$X(t)$ は任意の時間tで確率変数となる
- 軌跡 path
    $$ X(t, \omega): \Omega^T \to \R^T, \forall t \in T $$
- 情報系/情報増大系 filtration
    - probability space $(\Omega, \mathcal F, P)$
    $$ \{\mathcal F_t\}_{t\in T} \\ \forall s, t \in T, s < t \Rightarrow \mathcal{F}_s \subset \mathcal{F}_t \subset \mathcal{F} $$
    意味「時間の経過により情報が増加」
    all available information in t is contained
    - 適合過程 adapted process
        $$ \forall t \in T, A \in \mathcal B(\R), \{\omega \in \Omega|X_t(\omega) \in A\} \in \mathcal F_t $$
        for all t in T, X(t, •) is F-measurable
        意味「未来が予測不可能」
    - 可予測性 predictable
    - 情報付き確率空間 filtered probability space 確率基底 stochastic basis
        $$ \{\Omega, \mathcal F, \{\mathcal F_t \}_{t \in T}, P\} $$
    - 条件付き期待値 conditional expectation with filtration
        $$ \mathbb E[X_t|\mathcal F_s] $$
        the expectation of X_t based on the info in t
- 定常性 stationary
    - 弱定常性 weak stationary
        - 時間差k
        $$ \mathbb E[y_t] = \mu \\ var(y_t) = \sigma^2 \\ cov(y_t, y_{t-k}) = \gamma_k $$
        共分散は時間差に依存
    - 強定常性 strict stationary
        $$ f(y_t, ..., y_{t+l}) = f(y_{t+k}, ..., y_{t+k+l}) $$
- 連続性 continuous
    - 零集合 N
    $$ \forall \omega \in \Omega/N, \forall t \in T, \forall \epsilon > 0, \lim_{h \to 0} P(|X(t+h, \omega)-X(t, \omega)| < \epsilon)=0 $$
    for almost every path on the X, X is continuous
    - 平均二乗連続性 mean square continuous
        $$ \lim_{h\to 0} \mathbb E[|X(t+h) -X(t)|^2] = 0 $$
- 増分 increments
    - 独立増分性 independent increment
        $$ \forall t_1,s_1,t_2,s_2 \in T, \\ s_1 \leq t_1 \leq s_2 \leq t_2 \Rightarrow \\ \mathbb P[X_{t_1}-X_{s_1} \cap X_{t_2}-X_{s_2}] = \mathbb P[X_{t_1}-X_{s_1}] \mathbb P[X_{t_2}-X_{s_2}] $$
        all increments are independent on each other
    - 定常増分性 stationary increment
        $$ \forall t,s\in T, \\ s \leq t\Rightarrow \\ X_{s+h} - X_{s} \sim X_{t+h} - X_{t} $$
        時間差が等しい増分は分布が等しい
- martingale
    - probability space $(\Omega, \mathcal F, P)$
    - filtration F
    - adapted stochastic process M_t
    $$ \forall s, t \in T, \mathbb E[X_t | \mathcal F_s] = X_s $$
    - sub-martingale
        $$ \forall s, t \in T, \mathbb E[X_t | \mathcal F_s] \geq X_s $$
    - super-martingale
        $$ \forall s, t \in T, \mathbb E[X_t | \mathcal F_s] \leq X_s $$
- Markov property
    - Markov chain (discrete)
        $$ \mathbb P(X_{n+1}= x_{n+1}|X_n = x_n, X_{n-1} = x_{n-1} ..., X_0= x_0) = \mathbb P(X_{n+1}= x_{n+1}|X_n = x_n) $$
        過去 past : $X_{n-1} ..., X_0$
        現在 present : $X_n$
        未来 future : $X_{n+1}$
        - time homogeneous Markov chain/process
            $$ P\{X_{n+1} = y | X_n = x\} = P\{X_{m+1} = y | X_m = x\}, \forall n, m \in \mathbb N $$
        - 確率遷移行列 probability transition matrix
            $$ [P_{ij}]\\ P_{ij} = \{X_{n+1} = j | X_n = i\},\ i, j \in \{1, 2, ..., m\} $$
            - 到達可能性
            - 通信類/同値類 communicating class
            - 閉じた集合
        - Chapman-Kolmogorov equation
            $$ P(x_3, t_3|x_1, t_1)=\int dx_2 P(x_3, t_3|x_2,t_2) P(x_2, t_2|x_1,t_1) $$
        - 状態の分類
            - 到着可能
                $$ i \to j : \exists n \geq 0, P_{ij} > 0 $$
                - $i \to i$
                    $$ P_{ii}^{(0)} = 1 $$
            - 相互到着可能
                $$ i \leftrightarrow j : i \to j \land j \to i $$
                この二項関係において同値類が構成可能
                - 同値
                    - 反射律
                    - 対称率
                    - 推移律
                - 既約
                    $A \subset S$の要素が互いに相互到着可能
                - 既約なマルコフ連鎖
                    Sが一つの同値類から構成される
                - 集合Aが閉じている
                    $$ \forall i \in A, \sum_{j \in A}P_{ij} = 1 $$
                    $$ \Rightarrow k \in A, P_{ik} = 0 $$
                既約かつ閉じていれば同値類
                - 再帰性
                    - def
                        $$ n \geq 1, f_{ij}^{(n)} = P(X_n = j, X_r \ne j, \forall r, 1 \leq r \leq n-1 | X_0 = i) $$
                    - 初期通過確率
                        便宜上
                        $$ f_{ij}^{(0)} = 0, (f_{ii}^{(0)} = 0) $$
                        $P_{ij}^{(n)}$ は初めてである必要はない
                        $$ f_{ij}^{(1)} = P_{ij}^{(1)} = P_{ij} $$
                    - 最終推移確率
                        - def
                            $$ f_{ij} = \sum_{n = 1}^\infty f_{ij}^{(n)} \leq 1 $$
                        単調収束定理より収束
                        - $i = j$
                            - 再帰的
                                $$ g_i = f_{ii} = 1 $$
                            - 非再帰的
                                $$ g_i = f_{ii} = -1 $$
                                非再帰的とは戻ってこれないのではなく戻ってこれない確率がある
                    - 初期通過時刻
                        - def
                            $$ T_i = \inf \{n \geq 1 | X_n = i\} $$
                        $$ f_{ii}^{(n)}= P(T_i = n| X_0 = i) $$
                        $$ 1 - g_i = P(T_i = \infty | X_0 = i) $$
                        $$ g_i = P(T_i < \infty | X_0 = i) = \sum_{n = 1}^\infty f_{ii}^{(n)} $$
                        $g_i^m$ : m回戻ってくる(m乗している)
                        - $m \to \infty$
                            - 非再帰的
                                $$ g_i < 1 \Rightarrow \lim_{m \to \infty} g_i^m = 0 $$
                                無限回戻ってくることは不可能
                            - 再帰的
                                $$ g_i^m = 1 $$
                    - 再帰性の判定
                        - lemma
                            $$ P_{ij}^{(n)} = \sum_{k = 1}^\infty f_{ij}^{(n)} P_{jj}^{(n-k)} $$
                        - theorem
                            再帰的
                            if and only if
                            $$ \sum_{n =1}^\infty P_{ij}^{(n)} = \infty $$
                        - cor
                            $$ \sum_{n =1}^\infty P_{ij}^{(n)} = \frac{f_{ij}}{1 - g_i} $$
        - 周期性
            $$ \exists n \geq 1, P_{ii}^{(n)} > 0 $$
            $$ I_i = \{n \in \mathbb N| P_{ii}^{(n)} > 0\} $$
            $I_i$ の最大公約数を周期 $d_i$
            - 非周期的
                $$ d_i = 1 $$
            - theorem 1
                $I_i$ は加法的な集合
                $$ n, m \in I_i \Rightarrow n + m \in I_i $$
                - proof
                    $$ \exists n, m \in \mathbb N , P_{ii}^{(n)} > 0, P_{ii}^{(m)} > 0 $$
                    Chapman-Kolmogorov equationより
                    $$ P_{ii}^{(n+m)} \geq P_{ii}^{(n)}P_{ii}^{(m)} > 0 $$
            - remark
                $$ 2, 3 \in I_i $$
                ならば非周期的
            - gcd
                $$ \gcd(A_1, ..., A_m) = d \\ \Rightarrow \exists c_i \in \Z, c_1 A_1 + \cdots + c_M A_M = d $$
            - theorem 2
                $I_i$ は差が $d_i$ の2つの $I_i$ の要素を含む
                $$ \exists n_1, ..., n_M \in I_i, \gcd(A_1, ..., A_m) = d \\ \Rightarrow \exists c_i \in \Z, c_1 A_1 + \cdots + c_M A_M = d $$
                $$ c_i > 0, (1 \leq i \leq S) \\ c_i > 0, (S \leq i \leq M) $$
                としても一般性を失わない
                $$ n_1 c_1 + \cdots + n_Sc_S = (-c_{S+1})n_{S+1} + \cdots + (-c_M) n_M + d_i $$
                $$ l = n_1 c_1 + \cdots + n_Sc_S \in I_i \\ m = (-c_{S+1})n_{S+1} + \cdots + (-c_M) n_M \in I_i $$
                $$ l - m = d_i $$
            - theorem 3
                $$ I_i \ne \phi \\ \exists n_1 \in I_i, n_1 + n d_i \in I_i, \forall n \geq 0 $$
                $$ n_1, n_1 + d_i, n_1 + 2d_i , ... \in I_i $$
                - proof
                    $$ \exists n_0 \in \mathbb N, n_0, n_0 + d_i \in I_i $$
                    $I_i$ の加法性より
                    $$ K_2 = \{2n_0, 2n_0+d_i, 2n_0+2d_i, \} \subset I_i \\ K_j = \{jn_0, jn_0+d_i, \cdots ,jn_0+jd_i, \} \subset I_i $$
                    $$ K_{j + d_i} = \{(j + d_i)n_0, \cdots ,(j + d_i)(n_0+d_i)\} \subset I_i $$
                    $$ (j + d_i)n_0 + k d_i \in K_{j + d_i}, (0 \leq k \leq j + d_i) $$
                    $$ (j + d_i)n_0 + (j - n_0)d_i \\ = j n_0 + jd_i = P \\ K_j \cap K_{j + d_i} $$
            - theorem 4
                $$ i \leftrightarrow j \Rightarrow d_i = d_j $$
    - Markov process (continuous)
        - filtration $\{F_t\}_{t \in T}$
        - X_t is adapted F_t
        - Borel measurable f, g
        $$ \forall s, t \in T, \mathbb E[f(X_t)| \mathcal F_s] = g(X_s) $$
- Poisson process
    ||時間|回数|
    |---|---|---|
    |二項過程|幾何分布|二項分布|
    |Poisson 過程|指数分布|Poisson 分布|
    - 計数過程 counting process
        $$ \{N_t\}_{t \in \mathbb N} $$
        - 定義 def
            - 初期値 initial condition
                $$ N_0 = 0 $$
            - 非負整数 non-negative integer
                $$ N_t \in \Z_+ $$
            - 広義単調性 non-decreasing
                $$ s < t \Rightarrow N_s \leq N_t \\ \forall s, t \in \mathbb N $$
        - 定義 def
            微小区間 h
            - 定常独立増分
            - N = 0
                $$ N(0) = 0 \Leftarrow P(N(0) = 0) = 1 $$
            - N = 1
                $$ P(N(h) = 1) = \lambda h + o(h) $$
            - N > 1
                $$ P(N(h) \geq 2) = o(h) $$
        - 区間 (0, t], k 回
            $$ P_k(t) = P(N(t) = k | N(0) = 0) \\ = P(N(t) = k) \\
            $$
        - 区間 (0, h], k 回
            $$ P_k(h) = P(N(h) = k)\\ = \left\{ \begin{matrix} o(h) & k \geq 2 \\ \lambda h + o(h) & k = 1 \\ 1 - \lambda h + o(h) & k = 0 \end{matrix} \right. $$
            $$ P_k(h) = P(N(h) = k) \\ = P(N(h) - N(0) = k) \\ stationary \\ = P(N(t+h) - N(t) = k) \\ independent\ increments \\ = P(N(t+h) - N(t) = k|N(t)-N(0 = i)) $$
            区間 (0, t] でi回事象が発生 区間 (t, t+h] でk回事象が発生
            することは独立
            上記を考慮し、帰納的に求める
            - k = 0
                $$ P_0 (t+h) = P(N(t+h) - N(t) = 0|N(t)-N(0) = 0) \\ = P(N(t+h) - N(t) = 0)P(N(t)-N(0) = 0) \\ = P(N(h) - N(0) = 0)P(N(t)-N(0) = 0) \\ = P_0(h)P_0(t) \\ = P_0(t)(1 -\lambda h + o(h)) $$
                $$ \frac{P_0(t+h) - P_0(t)}{h} = -\lambda P_0(t) + o(1) \\ h \to 0 \\ \frac{d P_0(t)}{dt} = -\lambda P_0(t) \\ P_0(t) = Ce^{-\lambda t} $$
                - initial condition
                    $$ P_0(0) = P(N(0) = 0) = 1 $$
                $$ P(t) = e^{-\lambda t} $$
            - k > 0
                $$ P_k(t+h) = P_k(t) P_0(h) + P_{k-1}P_1(h) + \sum_{i = 2}^k P_{k-i}(t) P_i(h) \\ = P_k(t)(1 - \lambda h + o(h)) + P_{k -1} (t) (\lambda h + o(h)) + o(h) $$
                $$ \frac{P_k(t+h) - P_k(t)}{h} = -\lambda P_k(t) + \lambda P_{k-1}(t) + o(1) \\ \frac{d P_k(t)}{d t} =\lambda (P_{k-1}(t) - P_k(t)) \\ e^{\lambda t} (P_k'(t) + \lambda P_k(t)) \\ = \lambda e^{\lambda t} P_{k-1} (t) $$
                $$ \frac{d}{dt} (e^{\lambda t} P_k(t)) = \lambda e^{\lambda t} P_{k-1}(t) $$
                $$ P_0(0) = P(N(0) = 0) = 1 \\ P_k (0) = P(N(0) = k) = 0 $$
                - k = 1
                    $$ \frac{d}{dt} (e^{\lambda t} P_1(t)) = \lambda \\ e^{\lambda t} P_1(t) = \lambda t + C \\ t = 0, 0 = C \\ P_1(t) = (\lambda t)e^{-\lambda t} $$
                - k = k
                    $$ P_{k-1}(t) = e^{-\lambda t}\frac{(\lambda t)^{k-1}}{(k-1)!} $$
                    $$ P_k(t) = e^{-\lambda t}\frac{(\lambda t)^k}{k!} $$
        - 到着時間分布
            - 確率変数
                $$ t_1, t_2, ... $$
                $$ T_1, T_2, ... $$
                $$ T_i = t_1 + ...+ t_i $$
            - $t_1$ の分布
                $$ P(t_1 \leq S) = 1 -P(t_1 > S) = 1-P(N(S) = 0) = 1 - e^{-\lambda S} $$
                S以降に1回目が起こる = 時刻Sで事象は発生していない
                $$ f_{t_1}(S) = \lambda e^{-\lambda S} \\ f_{t_2 | t_1}(t | S) = \frac{f_{t_1, t_2}(S, t)}{f_{t_1}(S)} \\ F_{t_2 | t_1}(t | S) = \int_{-\infty}^t f_{t_2 | t_1}(u | S)du \\ = P(t_2 \leq t | t_1 = S) \\ = P(t_1 + t_2 \leq S +t | t_1 = S) \\ = 1 - P(t_1 + t_2 > S +t | t_1 = S) $$
                $$ N(S + t) = 1, N(S) = 1 \\ N (S + t) - N(S) = 1, N(S) - N(0) = 1 $$
                $$ = 1 - P(N(S+t)-N(S) = 0 | N(S) - N(0) = 1) \\ independent \ increments \\ = 1 - P(N(S+t)-N(S) = 0) \\ stationary \\ = 1 - P(N(t)-N(0) = 0) \\ = 1 - e^{-\lambda t} $$
        - meaning
            $N_T$ : the count of events
    - 二項過程 binomial process
        $$ \mathbb P(N_t = n) = \binom t n p^n (1-p)^{t-n} $$
        成功確率p のBernoulli分布
        $N_n$は成功の回数
        - 独立増分
        - 定常増分
        二項過程は定常独立増分の計数過程
        - 時間の分布が幾何分布
        - 回数の分布が二項分布
    - Poisson process
        - the stochastic process of independent and stationary increments $(N_t)_{t \in T}$
        $$ P(N_t = k) = e^{-\lambda t} \frac{(\lambda t)^k}{k!} $$
        - the limit of the binomial process
            $$ (1-p)^{m-1}p = (1 - \lambda \Delta t)^{m-1} \lambda \Delta t \\ = (1 - \frac{\lambda t}{m} )^{m-1} \frac{\lambda}{m} $$
            $t = m \Delta t$ : time
            $p = \lambda \Delta t$ : probability
            - proof
                $$
                $$
        - counting process
- gaussian process
- 平均 average
    - 時間平均 time average
    - 確率集団平均 ensemble average