自然現象や社会現象を数式を用いて表すこと
- logistic model
    - discrete
        $$
        x_{n+1} = \mu x_n(1-x_n)
        $$
    - continuous
        - equation
            - setting
                - 全体の個体数 L
                - 感染者数 y
            $$
            \dot y = ky(1-\frac{y}{L})
            $$
        - solution
            $$
            y = \frac{y_0 L}{y_0 + (L-y_0)e^{-kt}}
            $$
            - how to derive
                $$
                \dot y = \frac{k}{L}y(L-y)\\
                \frac{\dot y}{y(L-y)}= \frac{k}{L} \\
                \frac{1}{L}(\frac{\dot y}{y} + \frac{\dot y}{L-y}) = \frac{k}{L} \\
                \frac{\dot y}{y} + \frac{\dot y}{L-y} = k \\
                \int \frac{\dot y}{y} + \frac{\dot y}{L-y} dy = kt + A\\
                log \ y - log \ |y-L| = kt + A\\
                log \ y - log \ (L-y) = kt + A\\
                \frac{L}{y} -1 = Be^{-kt} \\
                y = \frac{L}{1+Be^{-kt}} \\
                y_0 = y(0) = \frac{L}{1+B} \\
                B = \frac{L}{y_0} -1 \\
                y = \frac{y_0 L}{y_0 + (L-y_0)e^{-kt}}
                $$
    - meaning
        感染症の患者数
- Matlthusian model
    - model
        $$
        \dot y = ky
        $$
    - 解 solution
        $$
        y = y_0 e^{ky}
        $$
    - 意味 meaning
- Lotka-Volterra equations
    $$
    \frac{dx}{dt}=ax-bxy \\
    \frac{dy}{dt}=cxy-dy
    $$
    xは被食者、yは捕食者
    - 意味 meaning
        個体数の増減
- Equations of Motions 運動方程式
    $$
    m \frac{dv}{dt} = -mg 
    $$
    - how to derive
        $$
        v(t)-v(0) = \int_0^t gdt = -gt 
        $$
- Navier-Stokes Equations
    - 非圧縮性
    - 等質
    $$
    \rho(\frac{\partial \vec v}{\partial t} + (\vec v \cdot \nabla)\vec v) = -\nabla p + \mu \nabla^2 \vec v + \rho\vec f
    $$
    $$
    \frac{\partial \vec v}{\partial t} + (\vec v \cdot \nabla)\vec v = -\frac{1}{\rho}\nabla p + \nu \nabla^2 \vec v + \vec f
    $$
    - variable
        - $\rho$  流体密度
        - v  流体速度
        - p  流体にかかる圧力
        - $\mu$  粘性係数
        - $\nu = \frac{\mu}{\rho}$  動粘性係数
    - term
        - $\frac{\partial \vec v}{\partial t}$  時間微分項
            流れが急に加速したり減速したりする場合
        - $(\vec v \cdot \nabla)\vec v$  移流項、対流項
            速い部分と遅い部分が相互作用する効果
        - $\nabla p$  圧力項
            圧力が高い領域から低い領域へ流体が移動する
        - $\mu \nabla^2 \vec v$  粘性項
        - $\rho\vec f$  外力項
- Eular method
    $$
    w(t+1) = w(t) - \nabla L(w)
    $$
    $$
    \frac{dw}{dt} = - \nabla L(W(t))
    $$
- 渦の数理モデル
[R1-yamada.pdf](R1-yamada.pdf)