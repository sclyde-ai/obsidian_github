- 金融市場 financial market
        - 株価 stock
            $$
            S_t 
            $$
            - 無作為性 randomness
                Sは確率変数
            - 正値性 positive
                $$
                S_t > 0
                $$
        - 安全資産 safety asset
            $$
            A_t
            $$
            - 正値性 positive
                $$
                A_t > 0
                $$
        - 金融派生商品 derivative
            $$
            H_t
            $$
            - 支払能力 solvency
                $$
                V_t \geq 0
                $$
        - portfolio
            $$
            V_t = x_t S_t + y_t A_t
            $$
            - 分割性 divisibility
                完備性
                $$
                x, y \in \R
                $$
            - 流動性 liquidity
                無限を含む
                $$
                x, y \in \R \cap \{\infin\}
                $$
            - 空売り可能 short selling
                負値をとる
                $$
                x, y < 0
                $$
            - 許容可能 admissible
                - 自己資金調達 self-financing
                    $$
                    dV_t = x_t dS_t + y_t A_t
                    $$
                - 非負性 non-negative
                    $$
                    V_t \geq 0
                    $$
- 数理金融 mathematical finance
    - how to
        - hedge
        - 複製 duplication
            - option
                $$
                O_1 = 
                \left\{
                \begin{matrix}
                a - K \\
                0
                \end{matrix}
                \right.
                $$
            - portfolio
                $$
                P_1 = 
                \left\{
                \begin{matrix}
                ay - x(1+r) \\
                by - x(1+r)
                \end{matrix}
                \right.
                $$
            - 一物一価の法則 law of one price
                $$
                a - K = ay - x(1+r) \\
                0 = by - x(1+r)
                $$
            $$
            a-K - 0 = ay - by \\
            a - K = (a-b)y \\
            y = \frac{a - K}{a-b} \\
            x = \frac{b}{1+r} y
            $$
            $$
            x = \frac{b}{1+r} \frac{a - K}{a- b} \\
            y = \frac{a - K}{a-b}
            $$
        - risk neutral factor
    - stock price model 株価模型
        - binomial model 二項模型
            - one period binomial model  一期間二項模型
                - def
                    - probability space
                        $$
                        \Omega = \{H, T\} \\
                        \mathcal F = \{\phi, \{H\}, \{T\}, \Omega\} \\
                        P = 
                        \left\{ 
                          \begin{alignedat}{}   
                           & 0 & & \phi,\Omega\\   
                           & p & & \{H\} \\ 
                           & 1-p & & \{T\}
                          \end{alignedat} 
                         \right.
                        $$
                    - stock(random variable)
                        $$
                        S_1(\omega)= 
                        \left\{ 
                          \begin{alignedat}{}   
                           & S_0 & & \phi, \Omega \\   
                           & uS_0 & & \{H\} \\ 
                           & dS_0 & & \{T\}
                          \end{alignedat} 
                         \right.
                        \\ u\geq d
                        $$
                        $u$ : up factor
                        $d$ : down factor
                - martingale
                    - safety asset
                        $$
                        A_1 = (1+r)A_0 = RA_0
                        $$
                        $r$  : interest rate
                    - discount factor
                        $$
                        D = \frac{1}{(1+r)}
                        $$
                    - martingale
                        $$
                        S_0 = D(\tilde pS_1(H)+ (1-\tilde p)S_1(T))
                        $$
                - arbitrage
                    - arbitrage
                        $$
                        u > 1+r\land d \geq 1+r \\
                        \lor \\
                        u \geq 1+r \land d > 1+r \\
                        \lor \\
                        u < 1+r\land d \leq 1+r \\
                        \lor \\
                        u \leq 1+r \land d < 1+r
                        $$
                        - how to derive
                            - buy side
                                $$
                                (1)\ \ P(DS_1 \geq S_0) = 1 \\
                                (2)\ \ P(DS_1 > S_0) > 0
                                $$
                                $$
                                (1)\ \ \forall \omega \in \Omega, DS_1(\omega) \geq S_0 \\
                                (2)\ \ \exist \omega \in \Omega, DS_1(\omega) > S_0
                                $$
                                - (1)
                                    $$
                                    \forall \omega \in \Omega, \frac{1}{1+r}S_1(\omega) \geq S_0\\
                                    uS_0 \geq (1+r) S_0 \\
                                    dS_0 \geq (1+r) S_0 \\
                                    u \geq 1+r \\
                                    d \geq 1+r \\
                                    u \geq 1+r \land d \geq 1+r
                                    $$
                                - (2)
                                    $$
                                    \exist \omega \in \Omega, \frac{1}{1+r}S_1(\omega) > S_0\\
                                    uS_0 > (1+r) S_0 \\
                                    dS_0 > (1+r) S_0 \\
                                    u > 1+r \\
                                    d > 1+r \\
                                    u > 1+r \lor d > 1+r
                                    $$
                                1と2より
                                $$
                                u \geq 1+r\land d \geq 1+r \\
                                \land \\
                                u > 1+r \lor d > 1+r
                                $$
                                分配法則より
                                $$
                                u > 1+r\land d \geq 1+r \\
                                \lor \\
                                u \geq 1+r \land d > 1+r
                                $$
                            - sell side
                                $$
                                (1)\ \ P(DS_1 \leq S_0) = 1 \\
                                (2)\ \ P(DS_1 < S_0) > 0 
                                $$
                                $$
                                (1)\ \ \forall \omega \in \Omega, DS_1(\omega) \leq S_0 \\
                                (2)\ \ \exist \omega \in \Omega, DS_1(\omega) < S_0
                                $$
                                - (1)
                                    $$
                                    \forall \omega \in \Omega, \frac{1}{1+r}S_1(\omega) \leq S_0\\
                                    uS_0 \leq (1+r) S_0 \\
                                    dS_0 \leq (1+r) S_0 \\
                                    u \leq 1+r \\
                                    d \leq 1+r \\
                                    u \leq 1+r \land d \leq 1+r
                                    $$
                                - (2)
                                    $$
                                    \exist \omega \in \Omega, \frac{1}{1+r}S_1(\omega) < S_0\\
                                    uS_0 < (1+r) S_0 \\
                                    dS_0 < (1+r) S_0 \\
                                    u < 1+r \\
                                    d < 1+r \\
                                    u < 1+r \lor d > 1+r
                                    $$
                                1と2より
                                $$
                                u \leq 1+r\land d \leq 1+r \\
                                \land \\
                                u < 1+r \lor d < 1+r
                                $$
                                分配法則より
                                $$
                                u < 1+r\land d \leq 1+r \\
                                \lor \\
                                u \leq 1+r \land d < 1+r
                                $$
                    - risk neutral probability
                        $$
                        \tilde {\mathbb P} = 
                        \left\{ 
                          \begin{alignedat}{}   
                           & 0 & & \phi, \Omega\\   
                           & \frac{(1+r)-d}{u-d} & & \{H\} \\ 
                           & \frac{u - (1+r)}{u-d } & & \{T\}
                          \end{alignedat} 
                         \right.
                        $$
                        - how to derive
                            $$
                            \tilde {\mathbb P} = 
                            \left\{ 
                              \begin{alignedat}{}   
                               & 0 & & \phi , \Omega\\   
                               & \tilde p & & \{H\} \\ 
                               & \tilde q& & \{T\}
                              \end{alignedat} 
                             \right.
                            \\
                            \tilde p + \tilde q = 1
                            $$
                            - equivalent
                                $$
                                P(\phi) = 0, P(\Omega) = 0 \\
                                \tilde P(\phi) = 0, \tilde P (\Omega) = 0
                                $$
                            - martingale
                                $$
                                \mathbb E_Q[DS_1] = S_0 \\
                                \frac{1}{1+r}(uS_0 \tilde p+ dS_0(1-\tilde p)) = S_0
                                \\
                                \frac{(u-d) \tilde p+ d}{1+r} S_0 = S_0\\
                                (u-d)\tilde p + d = 1+r \\
                                \tilde p = \frac{1+r-d}{u-d}
                                $$
                    - FTAP fundamental theorem of asset pricing
                        - FTAP 1
                            - non-arbitrage
                                $$
                                \lnot [u > 1+r\land d \geq 1+r \\
                                \lor \\
                                u \geq 1+r \land d > 1+r \\
                                \lor \\
                                u < 1+r\land d \leq 1+r \\
                                \lor \\
                                u \leq 1+r \land d < 1+r]
                                $$
                                De Morgan’s lawより
                                $$
                                u \leq 1+r \lor d < 1+r \\
                                \land \\
                                u < 1+r \lor d \leq 1+r \\
                                \land \\
                                u \geq 1+r \lor d > 1+r \\
                                \land \\
                                u > 1+r \lor d \geq 1+r
                                $$
                                分配律より
                                $$
                                (u < 1+r \lor d \leq u < 1+r \\
                                \lor \\
                                d \leq u \leq 1+r \lor d < 1+r)
                                \\ \land \\
                                (u > 1+r \lor d \geq u > 1+r \\
                                \lor \\
                                d \geq u \geq 1+r \lor d > 1+r)
                                $$
                                論理和と含意の関係より
                                $$
                                (u < 1+r 
                                \lor 
                                d \leq u \leq 1+r
                                \lor 
                                d < 1+r)
                                \\ \land \\
                                (u > 1+r 
                                \lor 
                                d \geq u \geq 1+r 
                                \lor 
                                d > 1+r)
                                $$
                                分配律より
                                $$
                                d < 1+r < u \\
                                \lor \\
                                u < 1+r < d
                                $$
                                初期条件より
                                $$
                                d < 1+r < u
                                $$
                            - risk neutral probability exists
                                $$
                                0 \leq \frac{(1+r)-d}{u-d} \leq 1 \\ \land \\
                                0 \leq \frac{u-(1+r)}{u-d} \leq 1
                                $$
                                $$
                                1+r \leq u \land d \leq 1+r \\
                                d \leq 1+r \leq u
                                $$
                        - FTAP 2
                            - assets
                                - stock
                                    price $S_0$
                                    future value $uS_0\ or\ dS_0$
                                - risk-free asset
                                    price $S_0$
                                    future value $(1+r)S_0$
                            - states
                                $$
                                \omega = H\ or \ T
                                $$
                - option
                    $$
                    V_1(\omega)= 
                    \left\{ 
                      \begin{alignedat}{}   
                       & V_0 & & \phi, \Omega \\   
                       & (S_1(H) - K)^+ & & \{H\} \\ 
                       & (S_1(T) - K)^+  & & \{T\}
                      \end{alignedat} 
                     \right.
                    \\ u\geq d
                    $$
                    - wealth equation
                        $$
                        X_1 - \Delta_0 S_1 = (1+r)(X_0 - \Delta_0 S_0)
                        $$
                    - delta hedge formula
                        $$
                        \Delta_0 = \frac{V_1(H)- V_1(T)}{S_1(H) - S_1(T)} = \frac{V_1(H)- V_1(T)}{(u-d)S_0} 
                        $$
                    - option price
                        $$
                        V_0 = X_0 = \frac{1}{1+r}(\tilde p V_1(H) + \tilde qV_1(T))
                        $$
                    - stock price
                        $$
                        S_0 = \frac{1}{1+r}(\tilde p S_1(H) + \tilde qS_1(T))
                        $$
            - two period binomial model  二期間二項模型
                $$
                S_1(\omega_1\omega_2)= 
                \left\{ 
                  \begin{alignedat}{}   
                   & S_0 & & \phi, \Omega \\   
                   & uS_0 & & \{HH, HT\} \\ 
                   & dS_0 & & \{TH, TT\}
                  \end{alignedat} 
                 \right. \\
                S_2(\omega_1\omega_2)=
                \left\{ 
                  \begin{alignedat}{}   
                   & S_0 & & \phi, \Omega \\   
                   & u^2 S_0& & \{HH\} \\ 
                   & ud S_0& & \{HT\}, \{TH\} \\ 
                   & d^2 S_0& & \{TT\}
                  \end{alignedat} 
                 \right. 
                \\ where \ u\geq d
                $$
                - probability space
                    $$
                    \Omega = \{HH,HT, TH, TT\} \\
                    $$
                    $$
                    \mathcal F_0 = \{\phi, \Omega\}\\
                    \mathcal F_1 = \{\phi, \{HH, HT\}, \{TH, TT\}, \Omega\} \\
                    \mathcal F_2 = \{\phi, \{HH\},\{ HT\}, \{TH\}, \{TT\}, \Omega\} 
                    $$
                    $$
                    P_1 = 
                    \left\{ 
                      \begin{alignedat}{}   
                       & 0 & & \phi, \Omega \\   
                       & p & & \{HH, HT\} \\ 
                       & q & & \{TH, TT\}
                      \end{alignedat} 
                     \right. \\
                    P_2 = 
                    \left\{ 
                      \begin{alignedat}{}   
                       & 0 & & \phi, \Omega \\   
                       & p^2 & & \{HH\} \\ 
                       & pq & & \{HT\}, \{TH\} \\ 
                       & q^2 & & \{TT\}
                      \end{alignedat} 
                     \right. \\
                    where\ p+q=1
                    $$
                - discount price
                    $$
                    D_1 = \frac{1}{(1+r)} \\
                    D_2 = \frac{1}{(1+r)^2}
                    $$
                - risk neutral probability
                    $$
                    \tilde P_1 = 
                    \left\{ 
                      \begin{alignedat}{}   
                       & 0 & & \phi, \Omega \\   
                       & \tilde p & & \{HH, HT\} \\ 
                       & \tilde q & & \{TH, TT\}
                      \end{alignedat} 
                     \right. \\
                    \tilde P_2 = 
                    \left\{ 
                      \begin{alignedat}{}   
                       & 0 & & \phi, \Omega \\   
                       & \tilde p^2 & & \{HH\} \\ 
                       & \tilde p \tilde q & & \{HT\}, \{TH\} \\ 
                       & \tilde q^2 & & \{TT\}
                      \end{alignedat} 
                     \right. \\
                    \tilde p = \frac{(1+r)-d}{u-d} \\
                    \tilde q = \frac{u - (1+r)}{u-d}
                    $$
                    - how to derive
                        $$
                        \tilde P = 
                        \left\{ 
                          \begin{alignedat}{}   
                           & 0 & & \phi , \Omega\\   
                           & \tilde p & & \{H\} \\ 
                           & 1-\tilde p& & \{T\}
                          \end{alignedat} 
                         \right.
                        \\
                        $$
                        - equivalent
                            $$
                            P(\phi) = 0, P(\Omega) = 0 \\
                            \tilde P(\phi) = 0, \tilde P (\Omega) = 0
                            $$
                        - martingale
                            $$
                            \mathbb E_Q[DS_1] = S_0 \\
                            \frac{1}{1+r}(uS_0 \tilde p+ dS_0(1-\tilde p)) = S_0
                            \\
                            \frac{(u-d) \tilde p+ d}{1+r} S_0 = S_0\\
                            (u-d)\tilde p + d = 1+r \\
                            \tilde p = \frac{1+r-d}{u-d}
                            $$
            - n period binomial model  n期間二項模型
                $$
                S_n(\omega_1\omega_2...\omega_n\{H, T\}^{N-n}) = S_0 u^{H_n}d^{T_n} \\
                n = H_n + T_n
                $$
                - probability space
                    - event space
                        $$
                        \Omega = \{H, T\}^N=\{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{1,2,...,N\}\}
                        $$
                    - filtration
                        $$
                        \mathcal F_0 = \{\phi, \Omega\}\\
                        \mathcal F_2= \{\phi, H\{H, T\}^{N-1}, T\{H, T\}^{N-1}, \Omega\} \\
                        \mathcal F_1 = \{\phi, 
                        HT\{H, T\}^{N-2}, HT\{H, T\}^{N-2}, TH\{H, T\}^{N-2}, TT\{H, T\}^{N-2}, \Omega\}
                        \\ \vdots \\
                        \mathcal F_n =\{ \phi, 
                        \{\omega_1\omega_2...\omega_n\{H, T\}^{N-n}| w_i \in \{H, T\}, \forall i \in \{1,2,...,n\}\}, \Omega\}
                        $$
                        $$
                        \omega_n =\omega_1\omega_2...\omega_n = \omega_1\omega_2...\omega_n\{H, T\}^{N-n} = \{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{n+1,n+2,...,N\}\}
                        $$
                    - probability measure
                        $$
                        P_n(\omega_n) =  p^{H_n}q^{T_n} \\
                        n = H_n + T_n
                        $$
                - discount price
                    $$
                    D_n = \frac{1}{(1+r)^n}
                    $$
                - risk neutral probability
                - portfolio
                    - position size
                        random variable 
                    $$
                    x_n S_n + y_n A_n = V_n
                    $$
                    - self-financing
                        $$
                        x_nS_n(\omega_n) + y_n A_n = x_{n+1}S_n(\omega_n) + y_{n+1} A_n
                        $$
                    - predictable
                        $$
                        x_n (\omega) = x_n(\omega_{n-1}) \\
                        y_n (\omega) = y_n(\omega_{n-1})
                        $$
                    - admissible
                        $$
                        V_n \geq 0
                        $$
                - option
                    $$
                    x_n S_{n+1}(\Omega_n H) + y_n A_n = V
                    $$
                    - European
                        $$
                        x_n (\omega) = \frac{V_n(H) - V_n(T)}{(u-d)S_n}
                        $$
                        $$
                        y_1 = \frac{V_0 - x_1 S_0}{A_0}
                        \\
                        y_n(\omega) = y_{n-1} - \frac{S_{n-1}(\omega)}{A_{n-1}}(x_n(\omega) - x_{n-1}(\omega))
                        $$
                    - American
            - one period trinomial model 一期間三項模型
                - probability space
                    $$
                    \Omega = \{H, N, T\} \\
                    \mathcal F = \{\phi, \{H\}, \{N\}, \{T\}, \Omega\} \\
                    P = 
                    \left\{ 
                      \begin{alignedat}{}   
                       & 0 & & \phi,\Omega\\   
                       & p & & \{H\} \\ 
                       & 1-p-q & & \{N\} \\
                       & q & & \{T\}
                      \end{alignedat} 
                     \right.
                    $$
                - random variable
                    $$
                    S_1(\omega)= 
                    \left\{ 
                      \begin{alignedat}{}   
                       & S_0 & & \phi, \Omega \\   
                       & uS_0 & & \{H\} \\ 
                       & nS_0 & & \{N\} \\ 
                       & dS_0 & & \{T\}
                      \end{alignedat} 
                     \right.
                    \\ where \ u \geq n \geq d
                    $$
                - discount price
                    $$
                    D = \frac{1}{(1+r)}
                    $$
                - risk neutral probability
                    $$
                    \tilde P = 
                    \left\{ 
                      \begin{alignedat}{}   
                       & 0 & & \phi, \Omega\\   
                       & \frac{(1+r)-d}{u-d} & & \{H\} \\ 
                       & \frac{u - (1+r)}{u-d } & & \{T\}
                      \end{alignedat} 
                     \right.
                    $$
                    - how to derive
                        $$
                        \tilde P = 
                        \left\{ 
                          \begin{alignedat}{}   
                           & 0 & & \phi , \Omega\\   
                           & \tilde p & & \{H\} \\ 
                           & 1-\tilde p& & \{T\}
                          \end{alignedat} 
                         \right.
                        \\
                        $$
                        - equivalent
                            $$
                            P(\phi) = 0, P(\Omega) = 0 \\
                            \tilde P(\phi) = 0, \tilde P (\Omega) = 0
                            $$
                        - martingale
                            $$
                            \mathbb E_Q[DS_1] = S_0 \\
                            \frac{1}{1+r}(uS_0 \tilde p+ dS_0(1-\tilde p)) = S_0
                            \\
                            \frac{(u-d) \tilde p+ d}{1+r} S_0 = S_0\\
                            (u-d)\tilde p + d = 1+r \\
                            \tilde p = \frac{1+r-d}{u-d}
                            $$
                - arbitrage
                    $$
                    u > 1+r\land d \geq 1+r \\
                    \lor \\
                    u \geq 1+r \land d > 1+r \\
                    \lor \\
                    u < 1+r\land d \leq 1+r \\
                    \lor \\
                    u \leq 1+r \land d < 1+r
                    $$
                    - how to derive
                        - buy side
                            $$
                            (1)\ \ P(DS_1 \geq S_0) = 1 \\
                            (2)\ \ P(DS_1 > S_0) > 0
                            $$
                            $$
                            (1)\ \ \forall \omega \in \Omega, DS_1(\omega) \geq S_0 \\
                            (2)\ \ \exist \omega \in \Omega, DS_1(\omega) > S_0
                            $$
                            - (1)
                                $$
                                \forall \omega \in \Omega, \frac{1}{1+r}S_1(\omega) \geq S_0\\
                                uS_0 \geq (1+r) S_0 \\
                                dS_0 \geq (1+r) S_0 \\
                                u \geq 1+r \\
                                d \geq 1+r \\
                                u \geq 1+r \land d \geq 1+r
                                $$
                            - (2)
                                $$
                                \exist \omega \in \Omega, \frac{1}{1+r}S_1(\omega) > S_0\\
                                uS_0 > (1+r) S_0 \\
                                dS_0 > (1+r) S_0 \\
                                u > 1+r \\
                                d > 1+r \\
                                u > 1+r \lor d > 1+r
                                $$
                            1と2より
                            $$
                            u \geq 1+r\land d \geq 1+r \\
                            \land \\
                            u > 1+r \lor d > 1+r
                            $$
                            分配法則より
                            $$
                            u > 1+r\land d \geq 1+r \\
                            \lor \\
                            u \geq 1+r \land d > 1+r
                            $$
                        - sell side
                            $$
                            (1)\ \ P(DS_1 \leq S_0) = 1 \\
                            (2)\ \ P(DS_1 < S_0) > 0 
                            $$
                            $$
                            (1)\ \ \forall \omega \in \Omega, DS_1(\omega) \leq S_0 \\
                            (2)\ \ \exist \omega \in \Omega, DS_1(\omega) < S_0
                            $$
                            - (1)
                                $$
                                \forall \omega \in \Omega, \frac{1}{1+r}S_1(\omega) \leq S_0\\
                                uS_0 \leq (1+r) S_0 \\
                                dS_0 \leq (1+r) S_0 \\
                                u \leq 1+r \\
                                d \leq 1+r \\
                                u \leq 1+r \land d \leq 1+r
                                $$
                            - (2)
                                $$
                                \exist \omega \in \Omega, \frac{1}{1+r}S_1(\omega) < S_0\\
                                uS_0 < (1+r) S_0 \\
                                dS_0 < (1+r) S_0 \\
                                u < 1+r \\
                                d < 1+r \\
                                u < 1+r \lor d > 1+r
                                $$
                            1と2より
                            $$
                            u \leq 1+r\land d \leq 1+r \\
                            \land \\
                            u < 1+r \lor d < 1+r
                            $$
                            分配法則より
                            $$
                            u < 1+r\land d \leq 1+r \\
                            \lor \\
                            u \leq 1+r \land d < 1+r
                            $$
            - the limit of binomial model 極限二項模型
                - up & down factor
                    $$
                    u_n = 1 + \frac{\sigma}{\sqrt n}\\
                    d_n = 1 - \frac{\sigma}{\sqrt n}\\
                    $$
                - risk neutral probability
                    $$
                    \tilde p = \frac{1+r-d_n}{u_n-d_n}\\
                    \tilde q = \frac{1+r-u_n}{d_n-u_n}
                    $$
                - the number of coin toss
                    $$
                    nt = H_{nt}+ T_{nt}
                    $$
                - the random walk
                    $$
                    M_{nt} = H_{nt}- T_{nt}
                    $$
                - head & tail
                    $$
                    H_{nt} = \frac{1}{2}(nt + M_{nt}) \\
                    T_{nt} = \frac{1}{2}(nt - M_{nt})
                    $$
                - stock price
                    $$
                    S(n,t)= S_0u^{H_{nt}}d^{T_{nt}} \\ 
                    = S_0
                    \left(1+\frac{\sigma}{\sqrt n}\right)^{\frac{1}{2}(nt+M_{nt})} 
                    \left(1-\frac{\sigma}{\sqrt n}\right)^{\frac{1}{2}(nt-M_{nt})} 
                    $$
                - theorem
                    $$
                    S(t) = S_0 \exp (\sigma W(t)-\frac{1}{2}\sigma^2 t)
                    $$
                    - proof
                        $$
                        = \ln S_0 +  \frac{1}{2}(nt+M_{nt})\ln (1+\frac{\sigma}{\sqrt n}) + \frac{1}{2}(nt-M_{nt})\ln (1-\frac{\sigma}{\sqrt n}) 
                        \\ 
                        =  \frac{1}{2}(nt+M_{nt})(\frac{\sigma}{\sqrt n} - \frac{\sigma^2}{2n} + O(n^{-\frac{3}{2}})) + \frac{1}{2}(nt-M_{nt})(-\frac{\sigma}{\sqrt n} - \frac{\sigma^2}{2n} + O(n^{-\frac{3}{2}})) \\
                        =  nt (\frac{\sigma^2}{2n}+ O(n^{-\frac{3}{2}}))+ M_{nt}(\frac{\sigma}{\sqrt n} + O(n^{-\frac{3}{2}})) \\
                        = -\frac{1}{2}\sigma^2 t + O(n^{-\frac{1}{2}})+ \sigma W^{(n)}(t) + O(n^{-\frac{3}{2}})
                        $$
            - CRR/Cox-Ross-Rubinstein method
                $$
                \Delta t = \frac{t}{n}\\
                S_t = S_0 u^x d^{n-x}
                $$
                - up & down factor
                    $$
                    u = e^{\sigma \sqrt{\Delta t}} \\
                    d = e^{-\sigma \sqrt{\Delta t}} \\
                    ud = 1
                    $$
                - S_t
                    $$
                    S_t = S_0(e^{\sigma \sqrt{\Delta t}})^x (e^{-\sigma \sqrt{\Delta t}})^{n-x} \\ 
                    = S_0 e^{\sigma\sqrt{\Delta t}(2x-n)} \\ 
                    = S_0 e^{\sigma\frac{\sqrt t(2x-n)}{\sqrt n}} \\
                    = S_0 e^{\sigma W_t}
                    $$
                - option
                    - risk neutral probability
                        $$
                        \\
                        p = \frac{e^{r \Delta t} - d}{u - d} \\
                        q = \frac{e^{r \Delta t} - u}{d - u} \\
                        p + q = 1
                        $$
                    $$
                    m = \min \{i | S_0 u^i d^{n-i} \geq K\}
                    $$
                    $$
                    CE_0 = e^{-r\Delta t}\sum_{i = m}^n \binom n i q^i(1-q)^i (S_0u^i d^{n-i} -K) \\
                    = D_t \overline B(m, n, p)(S_0u^i d^{n-i} -K) \\
                    = 
                    $$
                    $$
                    \underline B(m, n, p) = \sum_{i=0}^{m-1} p^i (1-p^{n-i})
                    $$
                    $$
                    \overline B(m, n, p) = \sum_{i=m}^n p^i (1-p^{n-i})
                    $$
                    - call
                        $$
                        CE_0 = S_0 B(m, N, \bar q) -KRB(m,N, q)
                        $$
                    - put
                        $$
                        PE_0 = S_0 B(m, N, \bar q) -KRB(m,N, q)
                        $$
        - random walk 酔歩運動
            - symmetric random walk 対処酔歩運動
                the outcome of the nth toss $X_j$
                $$
                X_j =
                  \left\{ 
                  \begin{matrix}
                1 \ (\omega_j = H) \\
                -1 \ (\omega_j= T)
                  \end{matrix} 
                  \right. 
                $$
                the process $M_k$
                $$
                M_k = \sum_{j=1}^k X_j, \forall k \in \N \\ M_0 = 0
                $$
                is a symmetric random walk
                - increment 増分
                    $$
                    M_{k_{i+1}} - M_{k_i} = \sum_{j=k_i+1}^{k_{i+1}} X_j
                    $$
                    Each of these random variable is called an increment of random walk
                    - independent increment
                    - expectation
                        $$
                        \mathbb E[M_{k_{i+1}} - M_{k_i}] = \mathbb E[\sum_{j=k_i+1}^{k_{i+1}} X_j] = \sum_{j=k_i+1}^{k_{i+1}} \mathbb E[X_j] = 0 
                        $$
                    - variance
                        $$
                        Var(M_{k_{i+1}} - M_{k_i}) = Var(\sum_{j=k_i+1}^{k_{i+1}} X_j) =  \sum_{j=k_i+1}^{k_{i+1}} Var(X_j) =  \sum_{j=k_i+1}^{k_{i+1}} 1 = k_{i+1} - k_i
                        $$
                    - martingale
                        $$
                        \mathbb E[M_l|\mathcal F_k] = \mathbb E[(M_l - M_k) + M_k|\mathcal F_k] \\ = \mathbb E[(M_l - M_k)|\mathcal F_k] + \mathbb E[M_k|\mathcal F_k] \\
                        = 0 + M_k = M_k
                        $$
                        the conditional expectation based on the information at time k
                    - quadratic variation
                        $$
                        [M, M]_k = \sum_{j=1}^k (M_j - M_{j-1})^2 = k
                        $$
            - scaled random walk
                $$
                W^{(n)}(t) = \frac{1}{\sqrt{n}}M_{nt}
                $$
                - expectation 期待値
                    $$
                    \mathbb E[W^{(n)}(t) - W^{(n)}(s)] = 0
                    $$
                - variance 分散
                    $$
                    V[W^{(n)}(t) - W^{(n)}(s)] = t-s
                    $$
                - martingale
                    $$
                    \mathbb E[W^{(n)}(t)| \mathcal F(s)] = \mathbb E[(W^{(n)}(t)-W^{(n)}(s)) + W^{(n)}(s)]
                    $$
                - quadratic variation
                    $$
                    [W^{(n)}, W^{(n)}](t) \\
                    = \sum_{j=1}^{nt} \left[W^{(n)}\left(\frac{j}{n}\right) - W^{(n)}\left(\frac{j}{n}\right)\right]^2 \\
                    = \sum_{j=1}^{nt}\left[\frac{1}{\sqrt n} X_j \right]^2 \\
                    = \sum_{j=1}^{nt} \frac{1}{n} \\
                    = t
                    $$
                - central limit
                    moment-generating function
                    $$
                    \phi_n(u) = \mathbb E[e^{uW^{(n)}(t)}] \\
                    = \mathbb E [\exp (\frac{u}{\sqrt n}M_{nt})] \\
                    = \mathbb E [\exp (\frac{u}{\sqrt n} \sum_{j=1}^{nt} X_j)] \\
                    = \mathbb E [\prod_{j=1}^{nt} \exp (\frac{u}{\sqrt n} X_j)] \\
                    = \prod_{j=1}^{nt} \mathbb E [\exp (\frac{u}{\sqrt n} X_j)] \\
                    = \prod_{j=1}^{nt} \frac{1}{2}e^{\frac{u}{\sqrt n}} + \frac{1}{2}e^{-\frac{u}{\sqrt n}} \\
                    = (\frac{1}{2}e^{\frac{u}{\sqrt n}} + \frac{1}{2}e^{-\frac{u}{\sqrt n}})^{nt} \\
                    $$
                    it sufgice to consider logarithm
                    $$
                    \log \phi_n(u) = nt \log (\frac{1}{2}e^{\frac{u}{\sqrt n}} + \frac{1}{2}e^{-\frac{u}{\sqrt n}})
                    $$
                    we make the change of variable $x = \frac{1}{\sqrt n}$ 
                    $$
                    \lim_{n \to \infin} \log \phi_n(u) = t \lim_{x \downarrow 0} \frac{\log (\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux})}{x^2}
                    $$
                    we may use L’Hopital’s rule
                    $$
                    \frac{\partial}{\partial x} \log (\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux}) \\ 
                    = \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{\frac{1} {2}e^{ux} + \frac{1}{2}e^{-ux}}
                    $$
                    $$
                    \frac{\partial}{\partial x}x^2 = 2x
                    $$
                    therefore
                    $$
                    \lim_{n \to \infin} \log \phi_n(u) 
                    \\
                    = t\lim_{x \downarrow 0} \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{2x(\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux})} 
                    \\
                    = \frac{t}{2} 
                    \lim_{x \downarrow 0} \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{x} \cdot
                     \lim_{x \downarrow 0} \frac{1}{(\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux})} \\
                    = \frac{t}{2} 
                    \lim_{x \downarrow 0} \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{x}
                    $$
                    we apply  L’Hopital’s rule again
                    $$
                    = \frac{t}{2} 
                    \lim_{x \downarrow 0} \frac{\frac{u^2}{2}e^{ux} + \frac{u^2}{2}e^{-ux}}{1} \\
                    = \frac{1}{2}u^2 t
                    $$
        - Brownian motion 連続酔歩運動
            - Brownian motion 連続酔歩運動
                - probability space
                - def 定義
                    - initial condition 初期値
                        $$
                        W_0= 0
                        $$
                    - independent increment 独立増分
                        $$
                        \forall s_1,t_1,s_2,t_2 \in T, \\ 
                        s_1 \leq t_1 \leq s_2 \leq t_2 \Rightarrow \\ \mathbb P[X_{t_1}-X_{s_1} \cap X_{t_2}-X_{s_2}] = \mathbb P[X_{t_1}-X_{s_1}] \mathbb P[X_{t_2}-X_{s_2}]
                        $$
                        the increments are independent on each other 
                    - normal/gaussian increment 正規増分
                        $$
                        \forall s,t \in T, X_t - X_s \sim N(0, t-s)
                        $$
                        Each of these increments is normally distributed 
                    - alternative characterization of Brownian motion
                - increment 増分
                    $$
                    W_{t_1}-W_{t_0}\\
                    W_{t_2}-W_{t_1}\\ 
                    ..., W_{t_m}-W_{t_{m-1}} \\
                    t_0 < t_1 < ... < t_m
                    $$
                    is independent and normally distributed
                    - expectation
                        $$
                        \mathbb E[W_{t_{i+1}}-W_{t_i}] = 0 
                        $$
                    - variance
                        $$
                        Var[W_{t_{i+1}}-W_{t_i}] = t_{i+1}-t_i
                        $$
                - filtration
                    - information accumulates
                        $$
                        \forall s, t \in T, s < t \Rightarrow \mathcal F_s \subset \mathcal F_t
                        $$
                    - adaptivity
                        Brownian motion W_t at the time t is F_t-measurable
                        $$
                        \{\omega \in \Omega: W_t(\omega) \in B, \forall B \in \mathcal B(\R)\} \in \mathcal F(t)
                        $$
                    - independence future increments
                        the increment W_t - W_s is independent of F_t
                        $$
                        \forall F \in \mathcal F_t
                        $$
                        F and W_t - W_s are independent 
                - property 性質
                    - martingale
                        $$
                        \mathbb E[W_t|\mathcal F_s] = W_s, \forall s, t \in T
                        $$
                        almost surely
                        - proof
                            $$
                            \mathbb E[W_t|\mathcal F_s] \\ 
                            = \mathbb E[W_s + (W_t-W_s)|\mathcal F_s] \\ 
                            = \mathbb E[W_s| \mathcal F_s] + \mathbb E[(W_t-W_s)|\mathcal F_s] \\
                             =W_s + 0
                            $$
                    - Markov property
                        - Borel measurable func f, g
                        $$
                        \mathbb E[f(W_t)|\mathcal F_s] = g(W_t)
                        $$
                        - proof
                            $$
                            \mathbb E[f(W_t)|\mathcal F_s] =
                            \mathbb E[f(W_t - W_s) + W_s|\mathcal F_s] =
                            $$
                    - not differential
                        $$
                        W(t+h) - W(t) \sim N(0, h)
                        $$
                        $$
                        \frac{W(t+h)-W(t)}{h} = \frac{\sqrt h Z}{h} = \frac{Z}{\sqrt h}
                        $$
                    - fractal
                        - self-similarity
                            $$
                            W(ct) \stackrel{\mathrm{d}}{=} \sqrt c W(t)
                            $$
                        - holder continuity
                            $$
                            |W_t-W_s| \leq C|t-s|^\alpha
                            $$
                - moment 積率
                    - the moment-generating function
                    - expectation 期待値
                        $$
                        \mathbb E[X_t] = 0
                        $$
                        - proof
                            $$
                            X_t = X_t -X_0 \sim N(0, t-0) = N(0, t) \\ \Rightarrow \mathbb E[X_t] = 0
                            $$
                    - variance 分散
                        $$
                        \mathbb E[(X_t-\mu)^2] = t
                        $$
                        - proof
                            $$
                            X_t = X_t -X_0 \sim N(0, t-0) = N(0, t) \\ \Rightarrow \mathbb E[X_t^2] = t
                            $$
                    - covariance 共分散
                        $$
                        Cov(W_s, W_t) = \mathbb E[W_sW_t] = \min(s, t)
                        $$
                        - proof
                            $$
                            \mathbb E[W_sW_t] \\
                            = \mathbb E[W_s(W_s+W_t-W_s)] \\
                            = \mathbb E[W_s^2] + \mathbb [W_s(W_t-W_s)] \\ 
                            = s
                            $$
                        - covariance matrix
                            $$
                            \bm{\Sigma} = \mathbb{E}\left[\begin{pmatrix}(X_1 - \mathbb{E}[X_1])^2 & (X_1 - \mathbb{E}[X_1])(X_2 - \mathbb{E}[X_2]) & \cdots & (X_1 - \mathbb{E}[X_1])(X_n - \mathbb{E}[X_n]) \\(X_2 - \mathbb{E}[X_2])(X_1 - \mathbb{E}[X_1]) & (X_2 - \mathbb{E}[X_2])^2 & \cdots & (X_2 - \mathbb{E}[X_2])(X_n - \mathbb{E}[X_n]) \\\vdots & \vdots & \ddots & \vdots \\(X_n - \mathbb{E}[X_n])(X_1 - \mathbb{E}[X_1]) & (X_n - \mathbb{E}[X_n])(X_2 - \mathbb{E}[X_2]) & \cdots & (X_n - \mathbb{E}[X_n])^2\end{pmatrix}\right]
                            $$
                - quadratic variation
                    $$
                    [W, W](T) = T
                    $$
                    - proof
                        $$
                        Q_\Pi = \sum_{j=0}^{n-1}(W(t_{j+1}) - W(t_j))^2
                        $$
                        $$
                        \mathbb E[(W(t_{j+1})-W(t_j))^2] = Var [W(t_{j+1})-W(t_j)] = t_{j+1} - t_j
                        $$
                        $$
                        \mathbb E[Q_\Pi] = \sum_{j=0}^{n-1}\mathbb E[(W(t_{j+1})-W(t_j))^2] = \sum_{j=0}^{n-1} t_{j+1} - t_j = T
                        $$
                        $$
                        Var[]
                        $$
            - athematic Brownian motion 算術連続酔歩運動
                - SDE stochastic differential equations
                    $$
                    dS_t = \mu dt + \sigma dW_t
                    $$
            - geometric Brownian motion 幾何連続酔歩運動
                - SDE stochastic differential equations
                    $$
                    d S_t = \mu S_t dt + \sigma S_t d W_t
                    $$
                - solution
                    $$
                    S_t = S_0 \exp \left(\sigma W_t +\left(\mu-\frac{1}{2}\sigma^2\right)t\right)
                    $$
                    - how to derive
                        $$
                        dS_t = \mu S_t dt + \sigma S_t dW_t
                        $$
                        $$
                        \frac{d S_t}{S_t} = d\ln S_t = \mu dt + \sigma dW_t
                        $$
                        伊藤の公式‣
                        $$
                        dh(x, t) = \left(\frac{\partial h}{\partial t} + f \frac{\partial h}{\partial x} + \frac{1}{2}g^2 \frac{\partial^2 h}{\partial x^2} \right)dt + g \frac{\partial h}{\partial x}d\omega
                        $$
                        $$
                        x = S_t, h(S_t, t) = \ln S_t \\
                        \frac{\partial \ln S_t}{\partial S_t} = \frac{1}{S_t} \\
                        \frac{\partial^2 \ln S_t}{\partial S_t^2} = -\frac{1}{S_t^2} \\
                        \frac{\partial \ln S_t}{\partial t} = 0
                        $$
                        $$
                        d \ln S_t= \left(0 + \mu S_t\frac{1}{S_t} + \frac{1}{2}(\sigma S_t)^2 (-\frac{1}{S_t^2})\right)dt + \sigma S_t\frac{1}{S_t}d\omega \\
                        = \left(\mu - \frac{1}{2}\sigma^2\right)dt+\sigma d\omega
                        $$
                        $$
                        S_t = S_0 \exp \left(\left( \mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)
                        $$
                - assumption 仮定
                    - frictionless market
                        - no transaction cost and tax
                        - lend and borrow with risk-free interest rate
                    - perfect and complete market
                        - price taker
                        - infinite divisibility
                        - not limit short selling
                        - any payoff is replicable
                    - risk-free asset
                        risk-free asset exists 
                        interest rate is known and constant
                    - efficient market
                        no-arbitrage
                - option
                    - call
                        - SDE
                            $$
                            \frac{\partial C_t}{\partial t}+ rS_t \frac{\partial C_t}{\partial S_t}+\frac{1}{2}\sigma^2S_t^2 \frac{\partial^2 C_t}{\partial S_t^2} -rC_t=0
                            $$
                            - how to derive
                                - portfolio
                                    - 一物一価の法則
                                        $$
                                        C(t) = p(t)S(t) + q(t)B(t)
                                        $$
                                    - 自己資本充足
                                        $$
                                        dpS + dqB = 0
                                        $$
                                    一物一価の法則より
                                    $$
                                    C(t) = p(t)S(t) + q(t)B(t)
                                    $$
                                    全微分をすると
                                    $$
                                    dC = dpS + pdS + dpB + qdB 
                                    $$
                                    自己資本充足より
                                    $$
                                    dC = pdS + qdB \\
                                    = (paS + qrB)dt + p\sigma S d\omega
                                    $$
                                - 伊藤の公式
                                    $$
                                    dC = \left(\frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} \right)dt + \sigma S \frac{\partial C}{\partial S}d\omega
                                    $$
                                dtとdwの係数比較すると
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  = paS + qrB
                                $$
                                $$
                                \sigma S \frac{\partial C}{\partial S}
                                = p\sigma S
                                $$
                                第二式を変形すると
                                $$
                                \frac{\partial C}{\partial S} = p
                                $$
                                一物一価の法則より
                                $$
                                rC = rpS+rqB \\
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - paS = qrB = rC - rpS
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - \frac{\partial C}{\partial S}aS =rC - r\frac{\partial C}{\partial S}S
                                $$
                                $$
                                \frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  =rC
                                $$
                        - solution
                            $$
                            C_0 = \Phi (d_1)S_0 - \Phi (d_2)Ke^{-rt} \\
                            d_1 = \frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\
                            d_2 = \frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\ 
                            \Phi(d) = \frac{1}{2\pi} \int^d_{- \infin} e^{- \frac{x^2}{2}} dx
                            $$
                            - how to derive
                                $$
                                C_0 = e^{-rt}\mathbb E_\mathbb Q[\max(S_t-K, 0)] 
                                \\
                                = e^{-rt} \mathbb E_\mathbb Q[(S_t-K)\cdot1_{K\leq S_t}] 
                                \\
                                = 
                                e^{-rt} (\mathbb E_\mathbb Q[S_t\cdot 1_{K\leq S_t}] - \mathbb E_\mathbb Q[K\cdot 1_{K\leq S_t}])
                                $$
                                - $\mathbb E_\mathbb Q[S_t\cdot1_{K\leq S_t}]$
                                    - 測度変換をすると
                                        $$
                                        \frac{d\mathbb Q^S}{d\mathbb Q} = \frac{S_t}{S_0e^{rt}}
                                        $$
                                    $$
                                    = \mathbb E_\mathbb Q[S_0 e^{rt} \frac{d\mathbb Q^S}{d\mathbb Q}\cdot 1_{K \leq S_t}] \\
                                    = S_0 e^{rt}\mathbb E_\mathbb Q[\frac{d\mathbb Q^S}{d\mathbb Q}\cdot 1_{K \leq S_t}] 
                                    $$
                                    - 期待値の計算より
                                    $$
                                    = S_0 e^{rt}\mathbb E_{\mathbb Q^S}[1_{K \leq S_t}] \\
                                    = S_0 e^{rt} \mathbb Q^S(K \leq S_t) 
                                    $$
                                    - Girsanovの定理より
                                        $$
                                        W_t^{\mathbb Q^S} = W_t^\mathbb Q - \sigma t
                                        $$
                                    $$
                                    \ln S_t = \ln S_0 + \left(r- \frac{\sigma^2}{2}\right)t + \sigma W_t^\mathbb Q \\
                                    = \ln S_0 + \left(r + \frac{\sigma^2}{2}\right)t + \sigma W_t^{\mathbb Q^S}
                                    $$
                                    株価S_tは対数正規分布に従うので
                                    $$
                                    \ln S_t \sim N(\mu, \sigma^2t) \\
                                    \mu = \ln S_0 + \left(r+\frac{\sigma^2}{2}\right)t
                                    $$
                                    標準化すると
                                    $$
                                    \frac{\mu - \ln K}{\sigma\sqrt t} =  \frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}
                                    $$
                                    $$
                                    \mathbb Q^S(K \leq S_t) = \mathbb Q^S(\ln K \leq \ln S_t) = \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                    上記より
                                    $$
                                    \mathbb E_\mathbb Q[S_t\cdot1_{K\leq S_t}]
                                    = S_0 e^{rt} \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                - $\mathbb E_\mathbb Q[K\cdot 1_{K\leq S_t}]$
                                    $$
                                    = K \cdot \mathbb E_\mathbb Q[1_{K\leq S_t}]
                                    \\ = K\cdot \mathbb Q(K\leq S_t)
                                    $$
                                    株価S_tは対数正規分布に従うので
                                    $$
                                    \ln S_t \sim N(\mu, \sigma^2t) \\
                                    \mu = \ln S_0 + \left(r-\frac{\sigma^2}{2}\right)t
                                    $$
                                    標準化すると
                                    $$
                                    \frac{\mu - \ln K}{\sigma\sqrt t} =  \frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}
                                    $$
                                    $$
                                    \mathbb Q(K \leq S_t)
                                    \\ 
                                    = \mathbb Q(\ln K \leq \ln S_t) 
                                    \\ 
                                    = \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                    上記より
                                    $$
                                    \mathbb E_\mathbb Q[K\cdot 1_{K\leq S_t}] 
                                    = K \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)
                                    $$
                                $$
                                C_0 = e^{-rt}(S_0 e^{rt} \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)- K \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right))
                                \\
                                =S_0 \Phi\left(\frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right)- K e^{-rt} \Phi \left(\frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t}\right))
                                $$
                    - put
                        - SDE
                            $$
                            \frac{\partial P_t}{\partial t}+ rS_t \frac{\partial P_t}{\partial S_t}+\frac{1}{2}\sigma^2S_t^2 \frac{\partial^2 P_t}{\partial S_t^2} -rP_t=0
                            $$
                            - how to derive
                                - portfolio
                                    - 一物一価の法則
                                        $$
                                        C(t) = p(t)S(t) + q(t)B(t)
                                        $$
                                    - 自己資本充足
                                        $$
                                        dpS + dqB = 0
                                        $$
                                    一物一価の法則より
                                    $$
                                    C(t) = p(t)S(t) + q(t)B(t)
                                    $$
                                    全微分をすると
                                    $$
                                    dC = dpS + pdS + dpB + qdB 
                                    $$
                                    自己資本充足より
                                    $$
                                    dC = pdS + qdB \\
                                    = (paS + qrB)dt + p\sigma S d\omega
                                    $$
                                - 伊藤の公式
                                    $$
                                    dC = \left(\frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} \right)dt + \sigma S \frac{\partial C}{\partial S}d\omega
                                    $$
                                dtとdwの係数比較すると
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  = paS + qrB
                                $$
                                $$
                                \sigma S \frac{\partial C}{\partial S}
                                = p\sigma S
                                $$
                                第二式を変形すると
                                $$
                                \frac{\partial C}{\partial S} = p
                                $$
                                一物一価の法則より
                                $$
                                rC = rpS+rqB \\
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - paS = qrB = rC - rpS
                                $$
                                $$
                                \frac{\partial C}{\partial t}+aS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  - \frac{\partial C}{\partial S}aS =rC - r\frac{\partial C}{\partial S}S
                                $$
                                $$
                                \frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}  =rC
                                $$
                        - solution
                            $$
                            P_t = \Phi (-d_2)Ke^{-rt}- \Phi (-d_1)S_0 \\
                            d_1 = \frac{\ln \frac{S_0}{K} + (r+\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\
                            d_2 = \frac{\ln \frac{S_0}{K} + (r-\frac{\sigma^2}{2})t}{\sigma\sqrt t} \\ 
                            \Phi(d) = \frac{1}{2\pi} \int^d_{- \infin} e^{- \frac{x^2}{2}} dx
                            $$
                            - how to derive
                                $$
                                P_0 = D_t \mathbb E_\mathbb Q[\max(K-S_t, 0)] \\
                                = D_t \mathbb E_\mathbb Q[(K -S_t)\cdot1_{S_t\leq K}] \\
                                = D_t (\mathbb E_\mathbb Q[K\cdot 1_{S_t\leq K}] -\mathbb E_\mathbb Q[S_t\cdot1_{S_t\leq K}])
                                $$
                                - $\mathbb E_\mathbb Q[K\cdot 1_{S_t\leq K}]$
                                - $\mathbb E_\mathbb Q [S_t\cdot1_{S_t\leq K}]$
                    - 熱伝導方程式 heat equation
                        $$
                        \frac{\partial u}{\partial \tau} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2} \\
                        \tau = T-t \\
                        u = Ce^{r\tau} \\
                        x = \frac{y+(r-\frac{1}{2}\sigma^2)\tau}{\sigma}
                        $$
                        - how to derive
                - log return
                    $$
                    \log \frac{S_{t_{j+1}}}{S_{t_j}} = \sigma(W_{t_{j+1}}-W_{t_j}) +\left(a-\frac{1}{2}\sigma^2\right)(t_{j+1}-t_j)
                    $$
                - realized volatility
                    $$
                    \log \frac{S_{t_{j+1}}}{S_{t_j}} = \sigma(W_{t_{j+1}}-W_{t_j}) +\left(a-\frac{1}{2}\sigma^2\right)(t_{j+1}-t_j)
                    $$
                    $$
                    \sum_{j=0}^{m-1}\left(\log \frac{S_{t_{j+1}}}{S_{t_j}} \right)^2 
                    = \sigma^2 \sum_{j=0}^{m-1} (W_{t_{j+1}}-W_{t_j})^2 
                    + \sigma \left(a-\frac{1}{2}\sigma^2\right) \sum_{j=0}^{m-1} (W_{t_{j+1}}-W_{t_j}) (t_{j+1}-t_j)
                     + \left(a-\frac{1}{2}\sigma^2\right)^2 \sum_{j=0}^{m-1} (t_{j+1}-t_j)^2
                    \\ \xrightarrow{\| \Pi \| \to 0}
                    \sigma^2(T_2 - T_1)
                    $$
                - Jensen’s inequality
                    $$
                    \mathbb E[\ln S_t] \leq \ln \mathbb E[S_t]
                    $$
                    $$
                    \mathbb E[\ln S_t] = \ln S_0 +  \left( \mu - \frac{\sigma^2}{2}\right)t \\
                    \ln \mathbb E[S_t] = \ln S_0 + \mu t
                    $$
            - fractional Brownian motion 非整数連続酔歩運動
                - 定義 def
                    - 初期値0
                        $$
                        B(0) = 0 
                        $$
                    - 期待値0
                        $$
                        \mathbb E[B(t)] = 0
                        $$
                    - 自己相関
                        $$
                        Cov(B(t), B(t +\tau)) = \frac{1}{2}(t^{2H} + (t+\tau)^{2H}-\tau^{2H})
                        $$
                    - Hurst parameter
                        $$
                        0< H<1
                        $$
                - 定常増分性
                    $$
                    B(t+\tau) -B(t) \sim B(\tau)
                    $$
                - 自己相似性
                    $$
                    B(at) = a^H B(t)
                    $$
                - 長期依存性
                    $$
                    \sum_{k=1}^\infin Cov(X_1, X_{1+k}) = \infin \\
                    X_i = B(i) - B(i-1)
                    $$
            - CEV constant elasticity of variance model
                $$
                dS_t = \sigma S_t^\beta dW_t
                $$
            - jump diffusion model 跳躍拡散模型
                - merton
                    $$
                    dS_t = (\mu -\lambda \cdot k)S_t dt + \sigma S_t dW_t + S_t dJ_t
                    $$
                    - diffusion part 拡散項
                        $$
                        \sigma S_t dW_t
                        $$
                        - standard Wiener process
                    - jump part 跳躍項
                        $$
                        S_t d J_t
                        $$
                        - compound Poisson process
        - my model
            - 直近の上下動の回数に比例して上か下かの確率が変動するmodel
            - probability space
                - event space
                    $$
                    \Omega = \{H, T\}^N=\{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{1,2,...,N\}\}
                    $$
                - filtration
                    $$
                    \mathcal F_0 = \{\phi, \Omega\}\\
                    \mathcal F_2= \{\phi, H\{H, T\}^{N-1}, T\{H, T\}^{N-1}, \Omega\} \\
                    \mathcal F_1 = \{\phi, 
                    HT\{H, T\}^{N-2}, HT\{H, T\}^{N-2}, TH\{H, T\}^{N-2}, TT\{H, T\}^{N-2}, \Omega\}
                    \\ \vdots \\
                    \mathcal F_n =\{ \phi, 
                    \{\omega_1\omega_2...\omega_n\{H, T\}^{N-n}| w_i \in \{H, T\}, \forall i \in \{1,2,...,n\}\}, \Omega\}
                    $$
                    $$
                    \omega_n =\omega_1\omega_2...\omega_n = \omega_1\omega_2...\omega_n\{H, T\}^{N-n} = \{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{n+1,n+2,...,N\}\}
                    $$
                - probability measure
                    $$
                    P_n(\omega_n) =  p^{H_n}q^{T_n} \\
                    n = H_n + T_n
                    $$
            $$
            S_n(\omega_1\omega_2...\omega_n\{H, T\}^{N-n}) = S_0 u^{H_n}d^{T_n} \\
            n = H_n + T_n
            $$
            $$
            p = f(\omega_1\omega_2...\omega_n) \\
            q = f^{-1}(\omega_1\omega_2...\omega_n)\\
            p+q=1
            $$
    - interest rate model 金利模型
        - short rate
            - Ho-Lee
                $$
                dr_t = a_t dt+\sigma dW_t
                $$
                - solution
                    $$
                    r(t) = r(0)+ \int_0^t \theta_u du + \sigma W_t
                    $$
            - Hull-White
                $$
                dr_t = (a_t- b_t r_t)dt+\sigma_t dW_t 
                $$
                - solution
                    $$
                    r_t= \exp\left(-\int_0^t a_v dv\right) [r_0 + \int_0^t \exp\left(\int_0^t a_vdv\right) \theta_u du+\int_0^t \exp\left(\int_0^t a_v dv\right)\sigma_u dW_u]
                    $$
                    - how to derive
                        1. 変数変換
                            $$
                            x(t) = r(t)\exp\left(\int_0^t a(v)dv\right)
                            $$
                            とするとSDEは
                            $$
                            d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)dt+\sigma(t) dW(t)]
                            $$
                            - how to derive
                                $$
                                d x(t) = \exp\left(\int_0^t a(v)dv\right) dr(t) + r(t) d\exp\left(\int_0^t a(v)dv\right)
                                $$
                                - 指数の微分
                                    $$
                                    r(t) d\exp\left(-\int_0^t a(v)dv\right) = r(t) a(t)\exp\left(-\int_0^t a(v)dv\right)dt
                                    $$
                                $$
                                d x(t) = \exp\left(\int_0^t a(v)dv\right) dr(t) + r(t) a(t)\exp\left(\int_0^t a(v)dv\right)dt
                                $$
                                $dr_t = (\theta_t- a_t r_t)dt+\sigma_t dW_t$  を代入
                                $$
                                d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)dt- a(t) r(t)dt+\sigma(t) dW(t)]  + r(t) a(t)\exp\left(\int_0^t a(v)dv\right)dt
                                $$
                                $\exp\left(\int_0^t a(v)dv\right)$ で分配法則
                                $$
                                d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)dt- a(t) r(t)dt+\sigma(t) dW(t)  + r(t) a(t)dt]
                                $$
                                $$
                                d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)+\sigma(t) dW(t)]
                                $$
                        2. 伊藤積分
                            $$
                            x(t) = x(0) + \int_0^t \exp\left(\int_0^t a(v)dv\right) \theta(u) du+\int_0^t \exp\left(\int_0^t a(v)dv\right)\sigma(u) dW(u)
                            $$
                        3. 逆変換
                            $$
                            r(t) = \exp\left(-\int_0^t a(v)dv\right) [r(0) + \int_0^t \exp\left(\int_0^t a(v)dv\right) \theta(u) du+\int_0^t \exp\left(\int_0^t a(v)dv\right)\sigma(u) dW(u)]
                            $$
                            - $x(0) = r(0)$
                                $$
                                x(0) = r(0)\exp\left(\int_0^0 a(v)dv\right) = r(0)\exp(0) = r(0)
                                $$
            - CIR Cox-Ingasoll-Ross
                $$
                dr_t = (a -b r_t)dt+\sigma \sqrt r_t dW_t
                $$
            - Vasicek
                $$
                dr_t = \beta(\theta-r_t)dt+\sigma dW_t
                $$
                - solution
                    $$
                    r_t = r_0 e^{-at}+b(1-e^{-at})+\sigma e^{-at} \int_0^t e^{as} d W_s
                    $$
            - Omstein-Uhlenbeck
                $$
                dr_t = -\theta(r_t-\mu)dt+\sigma dW_t
                $$
            - Black-Karasinski
                $$
                d \ln r_t = \frac{dr_t}{r_t} =  (\theta_t-a_t\ln r_t)dt + \sigma d W_t
                $$
            - Black-Derman-Toy
                $$
                \ln r_{t+1} = \ln r_t + \theta_t + \sigma_tZ
                $$
            - G++
        - momentary forward rate
            - Health-Jarrow-Morton frame work
        - forward rate
            - LIBOR market model
            - swap market model
        - shifted lognormal/displaced diffusion model
        - Brace-Gatarek-Musiela
        - Health-Jarrow-Morton
    - models
        - Barone-Adesi and Whaley
            considering early exercise of American option
            $$
            V_{BAW} = V_{BS} + V_{Early\ Exercise}
            $$
            - Whaley approximation
                $$
                V_{Early\ Exercise} = A\left(\frac{S}{S^*}\right)^\lambda
                $$
                $$
                A = \frac{S}{\lambda}(1-e^{(c-r)t}\Phi(d_1^*)) \\
                \lambda = \frac{1}{2}\left(-(\beta-1) + \sqrt{(\beta-1)^2 + \frac{4\alpha}{h}}\right)
                $$
                $$
                \alpha = \frac{2r}{\sigma^2} \\
                \beta = \frac{2(r-\delta)}{\sigma^2}
                $$
                $$
                \tau = T-t \\
                h(\tau) = 1-e^{-r\tau}
                $$
            - Ju-Zhong
        - Bjerksund and Stensland
        - McKean and van Moerbeke
            - Stefan problem
        - Car-Madan
        - Longstaff-Schwartz
        - Dupire
        - Clark-Ocone
        - Karatzas-Pikovsky
        - LIBOR market model
        - Markov functional
    - calculation method
        - FFT Fast Fourier Transform
            - 特性関数
                $$
                \phi_{\ln S_t}(u)=\mathbb E[\exp(i u \ln S_t)] 
                $$
            - option price
                $$
                C(K) = \exp(-rT) \int_{-\infin}^\infin \exp(iu \ln K) \psi(u)du \\
                \psi(u) = \frac{\phi(u-i)}{iu\phi(-i)}
                $$
        - Monte Carlo simulation
        - 有限差分法 finite difference method
            時間と空間を一定区間で区切り離散化
            - 差分
                - 前進差分
                    $$
                    \frac{\partial V}{\partial t} \approx \frac{V_{i, j+1} - V_{i, j}}{\Delta t}
                    $$
                - 後退差分
                    $$
                    \frac{\partial V}{\partial t} \approx \frac{V_{i, j} - V_{i, j-1}}{\Delta t}
                    $$
                - 中心差分
                    $$
                    \frac{\partial V}{\partial t} \approx \frac{V_{i, j+1} - V_{i, j-1}}{2\Delta t}
                    $$
            - 方法
                - 陽的差分法 explicit
                    $$
                    V_{i,j+1} = V_{i,j} + \Delta t \left( r S_i \frac{V_{i+1,j} - V_{i-1,j}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{\Delta S^2} - r V_{i,j} \right)
                    $$
                - 陰的差分法 implicit
                    $$
                    \frac{V_{i,j+1} - V_{i,j}}{\Delta t} + r S_i \frac{V_{i+1,j+1} - V_{i-1,j+1}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j+1} - 2V_{i,j+1} + V_{i-1,j+1}}{\Delta S^2} - r V_{i,j+1} = 0
                    $$
                - 半陽的差分法 Crank-Nicolson
                    $$
                    \frac{V_{i,j+1} - V_{i,j}}{\Delta t} = \frac{1}{2} \left[ r S_i \frac{V_{i+1,j+1} - V_{i-1,j+1}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j+1} - 2V_{i,j+1} + V_{i-1,j+1}}{\Delta S^2} - r V_{i,j+1} \right] + \frac{1}{2} \left[ r S_i \frac{V_{i+1,j} - V_{i-1,j}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{\Delta S^2} - r V_{i,j} \right]
                    $$
        - Euler-Maruyama
            $$
            X_{t+\Delta t} = X_t + a(X_t)\Delta t + b(X_t) \Delta W_t
            $$
        - Milstein method
            $$
            X_{t+\Delta t} = X_t + a(X_t)\Delta t + b(X_t) \Delta W_t + \frac{1}{2}b(X_t)\frac{\partial b(X_t)}{\partial X_t}((\Delta W_t)^2 - \Delta t)
            $$
        - Levenberg-Marquardt
        - Feller condition
        - Turnbull-Wakeman
        - moment matching