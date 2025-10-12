- binomial theorem
            $$
            (a+ b)^n = \sum_{i = 0}^n \frac{n!}{k!(n-k)!}a^kb^{n-k}
            $$
            - proof
                by mathematical induction
                - base case (n = 0)
                    $$
                    (a+b)^0 = 1
                    $$
                - inductive step (n = m)
                    $$
                    (a+ b)^n = \sum_{k= 0}^n \binom n k a^k b^{n-k} = \sum_{i = 0}^n \frac{n!}{k!(n-k)!}a^kb^{n-k}
                    $$
                    assume that statement is true for some integer n > 0
                    $$
                    (a + b) ^{n+1} = (a+b)(a+b)^n \\
                    = (a+b) \sum_{k= 0}^n \binom n k a^k b^{n-k}\\
                    = a \sum_{k = 0}^n \binom n k a^k b^{n-k}+ b \sum_{k = 0}^n \binom n ka^kb^{n-k} \\
                    = \sum_{k = 0}^n \binom n k a^{k+1}b^{n-k} + \sum_{k = 0}^n \binom n k a^kb^{n+1-k} 
                    \\
                    = \sum_{k = 1}^{n+1} \binom n {k-1} a^kb^{n+1-k} + \sum_{k = 0}^n \binom n k a^kb^{n+1-k} 
                    \\ 
                    = \binom n n a^{n+1} b^0 + \sum_{k = 1}^{n} \binom n {k-1} a^kb^{n+1-k} + \sum_{k = 1}^n \binom n k a^kb^{n+1-k} + \binom n 0 a^0 b^{n+1} 
                    \\
                    = a^{n+1} + \sum_{k = 1}^{n} (\binom n {k-1} + \binom n k ) a^kb^{n+1-k} + b^{n+1}
                    $$
                    - \binom n {k-1} + \binom n k
                        $$
                        \binom n {k-1} + \binom n k \\
                        = \frac{n!}{(n-k+1)!(k-1)!} + \frac{n!}{(n-k)!k!} 
                        \\
                        = \left(\frac{1}{n-k+1} + \frac{1}{k} \right) \frac{n!}{(n-k)!(k-1)!} 
                        \\
                        = \frac{n+1}{(n-k+1)k} \frac{n!}{(n-k)!(k-1)!} 
                        \\
                        = \frac{(n+1)!}{(n+1-k)!k!} 
                        \\
                        = \binom {n+1} k
                        $$
                    $$
                    a^{n+1}+ b^{n+1} + \sum_{k = 1}^{n} \binom {n+1} k a^kb^{n+1-k} \\
                    = \binom {n+1}{n+1} a^{n+1} + \binom {n+1} 0 b^{n+1} + \sum_{k = 1}^{n} \binom {n+1} k a^kb^{n+1-k}
                    \\
                    = \sum_{k = 0}^{n+1} \binom {n+1} k a^kb^{n+1-k}
                    $$
- inequality
            - Cauchy-schwarz inequality
                - metric vector space X
                $$
                |\langle x, y\rangle| \leq \|x\| \|y\| \\
                |\langle x, y\rangle|^2 \leq \langle x, x\rangle \langle y, y\rangle
                $$
            - Chebyshev inequality
                - monotone increasing
                    $$
                    x_1 < x_2 < ... < x_n \\
                    y_1 < y_2 < ... < y_n
                    $$
                $$
                \frac{1}{n}\sum_{i=1}^n x_iy_i \geq (\frac{1}{n}\sum_{i=1}^n x_i)(\frac{1}{n}\sum_{i=1}^n y_i) \geq \frac{1}{n}\sum_{i=1}^n x_iy_{n+1-i}
                $$
                - proof
                    $$
                    \sum_{i=1}^n \sum_{j=1}^n (x_i - x_j)(y_i-y_j) \geq 0
                    $$
                    $$
                    \sum_{i=1}^n \sum_{j=1}^n 
                    x_iy_i+x_jy_j-x_iy_j-x_jy_i \geq 0
                    \\
                    \sum_{i=1}^n \sum_{j=1}^n (x_iy_i+x_jy_j) \geq \sum_{i=1}^n \sum_{j=1}^n (x_iy_j+x_jy_i) 
                    \\
                    \sum_{i=1}^n \sum_{j=1}^n x_iy_i+ \sum_{i=1}^n \sum_{j=1}^n x_jy_j \geq \sum_{i=1}^n \sum_{j=1}^n x_iy_j+ \sum_{i=1}^n \sum_{j=1}^n x_jy_i
                    \\
                    2\sum_{i=1}^n \sum_{i=1}^n  x_iy_i \geq 2\sum_{i=1}^n \sum_{j=1}^n x_iy_j
                    \\ 
                    n\sum_{i=1}^n x_iy_i \geq \sum_{i=1}^n \sum_{j=1}^n x_iy_j
                    \\
                    n\sum_{i=1}^n x_iy_i \geq \sum_{i=1}^n x_i \sum_{j=1}^n y_j
                    \\
                    $$
            - young inequality
                $$
                ab \leq \frac{a^p}{p} + \frac{b^q}{q} \\
                a, b \geq 1, p, q > 1 \\
                \frac{1}{p} + \frac{1}{q} = 1
                $$
                - proof
                    $$
                    \log ab = \log a + \log b = \frac{1}{p} \log a^p + \frac{1}{q} \log b^q
                    $$
                    これは(a^, \log a^p) と(b, \log b^q)の内分点である。
                    またlogは凹関数なので
                    $$
                    \frac{1}{p} \log a^p + \frac{1}{q} \log b^q \leq \log (\frac{a^p}{p} + \frac{b^q}{q})
                    $$
                    が成立する。よって
                    $$
                    \log ab = \log (\frac{a^p}{p} + \frac{b^q}{q}) \\
                    ab = \frac{a^p}{p} + \frac{b^q}{q}
                    $$
            - Young inequality(integral)
                $$
                ab \leq \int_0^a f(x) dx + \int_0^b f^{-1}(x) dx
                $$
                ![image.png](image%2010.png)
            - Jensen inequality
            - Holder inequality
                $$
                \|fg\|_1 \leq \|f\|_p \|g\|_q \\
                \frac{1}{p} + \frac{1}{q} = 1
                $$
                - description
                    $$
                    \int_X |f(x)g(x)|d\mu \leq \left(\int_X |f(x)g(x)|^p d\mu\right)^{\frac{1}{p}} + \left(\int_X |f(x)g(x)|^q d\mu\right)^{\frac{1}{q}} \\
                    \frac{1}{p} + \frac{1}{q} = 1
                    $$
                - proof
                    正規化
                    $$
                    \tilde f = \frac{f}{\|f\|_p}, \tilde g = \frac{g}{\|g\|_q} 
                    $$
                    とおくと
                    $$
                    \|fg\|_1 \ = \int_X |fg| d\mu = \|f\|_p \|g\|_q \int_X |\tilde f \tilde g| d\mu 
                    $$
                    が成立する、よって
                    $$
                    \int_X |\tilde f \tilde g| d\mu  \leq 1
                    $$
                    を示す
                    - Young inequality
                    $$
                    |\tilde f \tilde g| \leq \frac{|\tilde f|^p}{p} + \frac{|\tilde g|^q}{q} 
                    $$
                    両辺積分すると
                    $$
                    \int_X |\tilde f \tilde g| d\mu \leq \int_X \frac{|\tilde f|^p}{p} + \frac{|\tilde g|^q}{q} d\mu \\
                    = \frac{1}{p}\int_X |\tilde f|^p + \frac{1}{q}\int_X |\tilde g|^q d\mu \\
                    = \frac{1}{p} + \frac{1}{q} \\
                    = 1
                    $$
- 解の公式
            $$
            a x^2 + b x + c = 0 \\
             x^2 + \frac{b}{a} x + \frac{c}{a} = 0 \\
            (x - \frac{b}{2a})^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0 \\
            (x - \frac{b}{2a})^2 = \frac{b^2}{4a^2} - \frac{c}{a}  \\
            (x - \frac{b}{2a})^2 = \frac{b^2 -4ac}{4a^2} \\
            x = \frac{b}{2a} \pm \sqrt{\frac{b^2 -4ac}{4a^2}} \\
            x = \frac{b\pm \sqrt{b^2 -4ac}}{2a} 
            $$