
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