
        
        
        - Brownian motion 連続酔歩運動
            
            
            
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