- 変数分離形/一階微分方程式
    $$
    \frac{dy}{dx} = f(x)g(y)
    $$
    - 解法
        $$
        \frac{1}{g(y)}\frac{dy}{dx} = f(x) \\
        \int \frac{1}{g(x)}\frac{dy}{dx}dx = \int f(x)dx
        $$
    - 置換積分
        $$
        \int f(x) dx = \int f(g(t))\frac{dx}{dt}dt
        $$
- 同次形
    $$
    \frac{dy}{dx} = f(\frac{y}{x})
    $$
- 一階線形微分方程式
    $$
    \frac{dy}{dx} + p(x)y = g(x)
    $$
- ベルヌーイの微分方程式
    $$
    \frac{dy}{dx} + p(x)y = g(x)y^\alpha
    $$
- 完全微分方程式
    $$
    \frac{\partial F(x,y)}{\partial x}dx + \frac{\partial F(x, y)}{\partial y}dy = 0
    $$
- クレローの微分方程式
    $$
    y = x \frac{dy}{dx} + f(\frac{dy}{dx})
    $$
- 二階線形同次微分方程式
    $$
    \frac{d^2y}{dx^2} + p(x) \frac{dy}{dx} + g(x)y = 0
    $$
- 二階線形非同次微分方程式
    $$
    \frac{d^2y}{dx^2} + p(x) \frac{dy}{dx} + g(x)y = f(x)
    $$
- ルンゲクッタ法
- 境界値問題 boundary value problem
- 固有値問題
- neural OED