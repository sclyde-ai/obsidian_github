
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