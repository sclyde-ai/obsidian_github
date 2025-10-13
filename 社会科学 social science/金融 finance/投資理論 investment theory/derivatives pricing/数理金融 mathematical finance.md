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