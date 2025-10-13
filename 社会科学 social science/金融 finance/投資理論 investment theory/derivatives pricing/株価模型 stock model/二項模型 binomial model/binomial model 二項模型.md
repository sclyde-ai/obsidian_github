
           
            
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