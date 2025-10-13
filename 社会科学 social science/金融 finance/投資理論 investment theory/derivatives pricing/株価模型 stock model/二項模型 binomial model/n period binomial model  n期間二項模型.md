
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