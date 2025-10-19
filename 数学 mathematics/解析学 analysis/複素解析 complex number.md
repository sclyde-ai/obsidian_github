$$
a + b
i = \sqrt{-1}
$$
- exp & tri
    $$
    \exp iz = \cos z + i\sin z
    $$
    - exp
        $$
        \exp z= \sum_{n=0}^\infty \frac{z^n}{n!}
        $$
    - sin
        $$
        \sin z = \sum_{n=0}^\infty \frac{z^{2n+1}}{(2n+1)!}
        $$
    - cos
        $$
        \sin z = \sum_{n=0}^\infty \frac{z^{2n}}{(2n)!}
        $$
    - Eular formula
        $$
        \exp \theta = \cos \theta + i\sin i\theta
        $$
    - Eular equation
        $$
        e^{\pi i} = -1
        $$
- log
    $$
    w = \ln z
    $$
    $$
    w = u+iv \\
    z = e^w \\
    re^{i\theta} = e^u\cdot e^{iv} \\
    r = e^u \mathbb Rightarrow u = \ln r\\
    e^{i\theta} = e^{iv} \mathbb Rightarrow v = \theta + 2n\pi
    $$
    $$
    w = \ln z = \ln r +i(\theta + 2n\pi) \\
    w = \ln |z| + i \arg z + 2n\pi i
    $$
- differential
    $$
    \frac{df(z)}{dz} = \lim_{\Delta z \to 0} \frac{f(z+\Delta z)-f(z)}{\Delta z}
    $$
    - Cauchy Lieman
        - setting
            $$
            z = x+iy \\
            f(z) = u(x,y) +iv(x,y)
            $$
        - CR equation
            $$
            \frac{\partial u}{\partial x}(x, y) = \frac{\partial v}{\partial y}(x, y) \\
            \frac{\partial u}{\partial y}(x, y) = -\frac{\partial v}{\partial x}(x, y)
            $$
        - f(z) が微分可能
        - u(x, y)とv(x, y)が全微分可能かつCRの公式が成立
        上記二つが同値関係
        - 必要条件(上→下)
            $$
            \frac{f(z+\Delta z)-f(z)}{\Delta z} \\ = \frac{(u(x+\Delta x, y + \Delta y) + i v(x+\Delta x, y + \Delta y)) - (u(x, y) + i v(x, y))}{\Delta x + i \Delta y}
            \\ = \frac{(u(x+\Delta x, y + \Delta y) - u(x, y)) + i (v(x+\Delta x, y + \Delta y)+ v(x, y))}{\Delta x + i \Delta y}
            $$
            - 実軸平行
                $$
                \frac{df(z)}{dz} = \frac{\partial u}{\partial x}(x,y) + i \frac{\partial v}{\partial x}(x,y)
                $$
            - 虚軸平行
                $$
                \frac{df(z)}{dz} = -i \frac{\partial u}{\partial y}(x,y) + \frac{\partial v}{\partial y}(x,y)
                $$
        - 十分条件(下→上)
- calculus
- pdf
    [kansuron.pdf](kansuron.pdf)