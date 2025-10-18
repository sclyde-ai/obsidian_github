$$ Po(\lambda) = \frac{\lambda^k}{k!} e^{-\lambda} $$
- parameter
    $\lambda$ : the average rate of occurrence of events
    k : the number of events
- moment
    - expectation
        $$ \mathbb E[X] = \sum_{k=1}^\infin k \mathbb P(X = k) \\ = \sum_{k=1}^\infin ke^{-\lambda}\frac{\lambda^k}{k!} \\ = e^{-\lambda} \sum_{k=1}^\infin \frac{\lambda^k}{(k-1)!} \\ = e^{-\lambda} \lambda \sum_{k=1}^\infin\frac{\lambda^{k-1}}{(k-1)!} \\ = \lambda e^{-\lambda} \sum_{k=0}^\infin \frac{\lambda^k}{k!} \\ = \lambda e^{-\lambda} e^{\lambda} \\= \lambda $$
    - variance
        $$ \mathbb E[X^2] = \mathbb E[X(X-1)] + \mathbb E[X] \\ = \sum_{k=2}^\infin k(k-1) e^{-\lambda}\frac{\lambda^k}{k!} + \lambda \\ = e^{-\lambda} \sum_{k=2}^\infin \frac{\lambda^k}{(k-2)!} + \lambda \\ = \lambda^2 e^{-\lambda} \sum_{k=2}^\infin \frac{\lambda^{k-2}}{(k-2)!} + \lambda \\ = \lambda^2 e^{-\lambda} e^\lambda + \lambda \\ = \lambda^2 + \lambda $$
        $$ Var(X) = \mathbb E[X^2] - (\mathbb E[X])^2 \\ = \lambda^2 + \lambda - \lambda^2 \\ = \lambda $$
- Poisson is the limit of Binomial
    $$ np = \lambda \\ p = \frac{\lambda}{n} $$
    $$ \binom{n}{x} \ p^x(1-p)^{n-x} \\ = \frac{n!}{x! (n-x)!} \left(\frac{\lambda}{n}\right)^x \left(1-\frac{\lambda}{n}\right)^{n-x} \\ = \frac{n(n-1)...(n-(x-1))}{x!} \frac{\lambda^x}{n^x} \left(1-\frac{\lambda}{n}\right)^n \left(1-\frac{\lambda}{n}\right)^{-x} \\ = \frac{1(1-\frac{1}{n})...(1-(\frac{x-1}{n}))}{x!} \lambda^x \left(1-\frac{\lambda}{n}\right)^n \left(\left(1-\frac{\lambda}{n}\right)^n\right)^{-\frac{x}{n}} \\ \xrightarrow{n\to\infty} \frac{1(1-0)...(1-0)}{x!} \lambda^x e^{-\lambda} e^{-\lambda\cdot 0} \\ = \frac{\lambda^x}{x!}e^{-\lambda} $$
- example
    - earthquake