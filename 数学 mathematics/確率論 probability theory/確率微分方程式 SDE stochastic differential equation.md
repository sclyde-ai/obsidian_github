 
    $$ dW_t^2 = \sigma^2dt $$
    - SDE
        $$ dX(t) = f(t, X(t))dt + g(t, X(t)) dW(t) $$
        f : drift
        g : diffusion coefficient
    - solution
        $$ x(0) = x_0 \\ x(T) = x_0 + \int_0^T f(t, X(t))dt + \int_0^T g(t, X(t)) dw $$
    - 一次線形確率微分方程式 linear stochastic differential equation
        $$ dX_t = f(a_t+b_tX_t)dt + g(c_t+d_tX_t) dW_t $$
    - 伊藤積分
        $$ \int f(x(t_i), w(t_i), t_i)dt+g(x(t_i), w(t_i), t_i)dw = \lim_{N}\sum_{i} f(x(t_i), w(t_i), t_i)(t_{i+1}-t_i)+g(x(t_i), w(t_i), t_i)(w(t_{i+1})-w(t_i)) $$
    - 伊藤の公式
        $$ dh(x, t) = \left(\frac{\partial h}{\partial t} + f \frac{\partial h}{\partial x} + \frac{1}{2}g^2 \frac{\partial^2 h}{\partial x^2} \right)dt + g \frac{\partial h}{\partial x}dw $$
        - 導出
            - 普通の全微分
                # $$ dh = \frac{\partial h}{\partial x} dx + \frac{\partial h}{\partial t} dt \\
                $$
    - Malliavin解析
        - malliavin derivative
            $$ DF = \sum_{i=1}^n \frac{\partial f}{\partial x_i} (W(t_1), ..., W(t_n))\cdot 1_{[0, t_i]} $$
            - property
                - linear
                    $$ D(aF+bG) = aDF+bDG $$
                - multiple
                    $$ D(FG) = F\cdot DG + G\cdot DF $$
                - chain
                    - smoothness function \phi
                    $$ D(\phi(F)) = \frac{d \phi(F)}{dF} \cdot DF $$
            - example
                - F = W_1
                    $$ D_t W_1 = 1_{[0, t_i]}(t) $$
                - F = W_1^2
                    $$ D_t (W_1^2) = 2W_1\cdot D_tW_1 = 2W_1 1_{[0, 1]}(t) $$
                - Hilbert space L^2
        - Skorohod calculus 発散作用素
            - probability process
                $$ u_t = \{u_t\}_{t\in[0, 1]} $$
            - Hilbert space L^2
            $$ \delta(u) = \int_0^T u_t dW_t $$
            - characteristics
                $$ \mathbb E[\braket {DF,u}_{L^2([0, 1])} ] = \mathbb E[F\cdot \delta(u)] \\ \braket {DF,u}_{L^2([0, 1])} = \int_0^T (D_tF)u_tdt $$
            - example
                $$ u_t = W_1\cdot 1_{[0,1]}(t) \\ \delta(u) = \int_0^1 W_1dW_1 = W_1(W_1-W_0)=W_1^2 $$
        - malliavin matrix
            - random variable
                $$ F=(F_1,...,F_d) $$
            $$ \sigma_{ij} = \langle DF_i, DF_j\rangle_{L^2([0, T])} $$
            - theorem
                if a malliavin matrix is regular, then probability density of F is absolutely continuous and smoothness
        - Clark-Ocone formula
            $$ F =\mathbb E[F] + \int_0^T \mathbb E[D_t F| \mathcal F_t] dW_t $$
        - Clark-Ocone-Haussmann formula
            $$ F =\mathbb E[F] + \int_0^T \mathbb E[D_t F| \mathcal F_t] dW_t $$
        - malliavin sobolev space
        - Hörmander's condition
    - white noise解析
    - Feynman-Kac formula
        - stochastic process X_s
            $$ d X_s = \mu(X_s, s)ds + \sigma(X_s, s)dW_s $$
        - boundary condition
            $$ u(x, T) = \phi(x) $$
        - PDE
            $$ \frac{\partial u}{\partial t} + \mu(x, t)\frac{\partial u}{\partial t} + \frac{1}{2} \sigma^2 (x, t)\frac{\partial^2 u}{\partial x^2} - k(x, t)u = 0 $$
        - solution
            $$ u(x, t) = \mathbb E_{t, x} \left[\exp\left(-\int_t^T k(X_s, s)ds\right)\phi(X_T)\right] $$
        - application for Black-sholes
            - stock
                $$ x =S $$
            - drift
                $$ \mu (S, t) = rS $$
            - diffusion
                $$ \sigma (S, t) =\sigma S $$
            - rate
                $$ k(S, t) = r $$
            - payoff
                $$ \phi(S_T) = V(S, T) $$
    - Girsanov theorem
    - Numéraire
    - 計算例
        - $dx = a\ dt$
            $$ x = \lim_N \sum_{i=1}^N a(t_{i+1}-t_i) \\ = x_0 + at
            $$
        - $dx = ax\ dt$
            $$ \frac{dx}{x} = a\ dt \\ \ln x = \lim_N \sum_{i=1}^N a(t_{i+1}-t_i) \\ = x_0 + at \\ e^x = e^{x_0+at}
            $$
        - $dx = aw\ dx$
        - $dx = b\ dw$
        - $dx = bx\ dw$
        - $dx = bw\ dw$