$f : \R^n \to \R$ 
$$
\forall x \in \R^n, \forall \lambda \in[0, 1], f(\lambda x + (1- \lambda)y) \geq \lambda f(x)+ (1-\lambda)f(y)
$$
- 準凹関数
    $$
    \forall x \in \R^n, \forall \lambda \in[0, 1],\\ f(\lambda x + (1- \lambda)y) \geq \min(f(x), f(y))
    $$
- 別解釈
    $$
    \lambda f(x) + (1-\lambda)f(y) \leq f(\lambda x + (1-\lambda)y)
    $$
    1. $\lambda = \xi$
        $$
        \lambda f(x) + (1-\lambda)f(y) \leq f(\lambda x + (1-\lambda)y) = f(y - \xi(y-x))
        $$
    2. $\lambda = 1-\xi$
        $$
        \lambda f(x) + (1-\lambda)f(y) \leq f(\lambda x + (1-\lambda)y) = f(x - \xi(y-x))
        $$
    1と2を足すと
    $$
    f(x) + f(y) = f(x - \xi(y-x)) + f(y - \xi(y-x))
    $$
- 命題(凹ならば準凹)
    $$
    f(\lambda x + (1-\lambda)y) \\
    \geq \lambda f(x) + (1-\lambda)f(y) \\
    \geq \lambda f(y) + (1-\lambda)f(y) \ \ (f(x) 
    \geq f(y))\\
    = f(y) \\
    = \min(f(x), f(y))
    $$