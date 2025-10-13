
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