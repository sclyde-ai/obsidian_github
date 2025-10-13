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
    - 
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