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