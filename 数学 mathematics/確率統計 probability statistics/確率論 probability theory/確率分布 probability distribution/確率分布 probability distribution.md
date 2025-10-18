- 分布の特徴量 feature of distribution
    - 母数 parameter
    - 台 support
    - 確率密度関数 PDF
    - 累積分布関数 CDF
    - 平均値/期待値 mean/average
    - 分散 variance
    - 歪度 skewness
    - 尖度 kurtosis
    - entropy
    - 確率母関数 probability generating function
    - 積率母関数 moment generating function
    - 特性関数 characteristic function
- 変換 transform
    ![image.png](attachment:8f0d6e28-8a9e-43e3-ab1f-9424fcad0af2:image.png)
- 指数型分布族 exponential family
- 離散分布 discrete
    - 指数型分布族 exponential family
- 連続分布 continuous
    - 指数型分布族 exponential family
        - 正規分布 normal/gauss
            - 母数 parameter
                - average
                - variance
            - 確率密度関数 probability density function
                $$ N(\mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(−\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} $$
            - 統計量 statistics
                - 期待値 expectation
                    $$ \left. \frac{d}{dt}\mathbb E[e^{tX}]\right|_{t=0} \\ = \left. \frac{d}{dt} \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) \right|_{t=0} \\ = \left. (\mu +\sigma t)\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\right|_{t=0} \\ = \mu $$
                - 分散 variance
                    $$ \left. \frac{d^2}{dt^2}\mathbb E[e^{tX}]\right|_{t=0} \\ = \left. \frac{d^2}{dt^2} \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) \right|_{t=0} \\ = \frac{d}{dt} \left. (\mu +\sigma t)\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\right|_{t=0} \\ = \left. \sigma\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\right|_{t=0} \\ = \sigma $$
            - 積率母関数 moment-generating function
                $$ \mathbb E[e^{tX}] = \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) $$
                - proof
                    $$ \mathbb E[e^{tX}] \\ = \int e^{tx}\frac{1}{\sigma \sqrt{2\pi}}\exp{\left(−\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(tx−\frac{(x−\mu)^2}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(\frac{2x\sigma^2 t}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{ x^2 -2x(\mu+\sigma^2 t) +\mu^2}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{ x^2 -2x(\mu+\sigma^2 t)
                    - (\mu+\sigma^2 t) ^2 -2\mu\sigma^2t -\sigma^4 t^2}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{(x -(\mu+\sigma^2 t))^2}{2\sigma^2} + \mu t + \frac{1}{2}\sigma^2 t^2\right)}dx \\ = \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{(x -(\mu+\sigma^2 t))^2}{2\sigma^2}\right)}dx \\ =\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) $$
            - 特性関数 characteristic function
                $$ \mathbb E[e^{itX}] = \exp \left(i\mu t - \frac{1}{2}\sigma^2 t^2\right) $$
                - proof
                    # $$ \mathbb E[e^{itX}] = \int_{-\infin}^\infin e^{itx} \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(−\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} dx \\
                    # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{\left(itx −\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} dx \\ = \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{\left(itx −\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} dx \\
                    # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\frac{x^2 −2\mu x - 2it\sigma^2x + \mu^2 }{\sigma^2}\right) \right) } dx \\
                    # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\frac{(x−(\mu +it\sigma^2))^2 - (\mu +it\sigma^2)^2 + \mu^2 }{\sigma^2}\right) \right) } dx \\
                    # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\left(\frac{x−(\mu +it\sigma^2)}{\sigma}\right)^2 - 2it\mu +t^2\sigma^2 \right) \right)}dx \\
                    \exp{ \left(it\mu -\frac{1}{2}t^2\sigma^2\right) } \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\left(\frac{x−(\mu +it\sigma^2)}{\sigma}\right)^2 \right) \right)}dx \\ = \exp{ \left(i\mu t-\frac{1}{2}\sigma^2 t^2 \right) } $$
        - 多変量正規分布 multivariate normal distribution
            $$ \frac{1}{\sqrt{(2 \pi)^k\det \Sigma}} \exp \left(-\frac{1}{2}(\bm x -\bm \mu)^\top \Sigma^{-1}(\bm x - \bm \mu)\right) $$
        - 指数分布 exponential
            - probability density function
                $$ \exp(\lambda) = \left\{ \begin{matrix} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{matrix} \right. $$
            - moment
                - expectation
                    $$ \mathbb E[X] \\ = \int_0^\infin x \lambda e^{-\lambda x} dx \\ = \lambda \int_0^\infin x e^{-\lambda x} dx \\ = \lambda (\left[-\frac{x}{\lambda}e^{-\lambda x}\right]_0^\infin -\int_0^\infin -\frac{1}{\lambda}e^{-\lambda x}dx)\\ = \int_0^\infin e^{-\lambda x}dx \\ = \left[-\frac{1}{\lambda}e^{-\lambda x}\right]_0^\infin \\ = \frac{1}{\lambda} $$
                - variance
                    $$ \mathbb E[X^2] \\ = \int_0^\infin x^2 \lambda e^{-\lambda x} dx \\ = \lambda \int_0^\infin x^2 e^{-\lambda x} dx \\ = \lambda (\left[-\frac{x^2}{\lambda}e^{-\lambda x}\right]_0^\infin -\int_0^\infin -\frac{2x}{\lambda}e^{-\lambda x}dx)\\ = \frac{2}{\lambda}\int_0^\infin xe^{-\lambda x}dx \\ = \frac{2}{\lambda^2}
                    $$
                    $$ Var(X) = \frac{2}{\lambda^2} - \left(\frac{1}{\lambda}\right)^2 = \frac{1}{\lambda^2} $$
        - gamma
            - parameter
                $\lambda> 0$ : rate parameter
                $\alpha > 0$ : shape parameter
            $$ Gam(\alpha, \lambda) = \left\{ \begin{matrix} \frac{1}{\Gamma(\alpha)} \lambda^\alpha x^{\alpha-1}e^{-\lambda x} &(x>0) \\ 0 & (x \leq0) \end{matrix} \right.
            $$
            $$ \Gamma(\alpha) = \int_{0}^\infin x^{\alpha-1} e^{-x}dx $$
            - theorem
                - $\Gamma(1) = 1$
                - $\Gamma(\frac{1}{2}) = \sqrt{\pi}$
                - $\Gamma(\alpha+1) = \alpha\Gamma(\alpha)$
                - $\Gamma(n+1) = n!$
                - $Gam(\frac{1}{2}, \frac{1}{2}) = N(0, 1)$
                - $Gam(\frac{n}{2}, \frac{1}{2}) = \chi^2()$
            - expectation
                $$ \mathbb E[X] = \int_{0}^\infin \frac{1}{\Gamma(\alpha)} \lambda^\alpha x^{\alpha}e^{-\lambda x} \\ = \frac{\alpha}{\lambda}\int_{0}^\infin \frac{1}{\Gamma(\alpha+1)} \lambda^{\alpha+1} x^{\alpha}e^{-\lambda x} \\ =\frac{\alpha}{\lambda} $$
            - variance
        - beta
        - xi
            - Z_1, …, Z_k 標準正規分布
            $$ \chi^2 = \sum_{k=1}^nZ_k^2 $$
            - 再生性
        - Dirichlet
        - Weibull
            故障する確率など
            - parameter
                - scale $\lambda$
                - shape $k$
            - PDF
            - CDF
                $$ 1-\exp(-(\frac{t}{\tau})^m) $$
                ![Weibull_CDF.svg.png](attachment:f97313c8-cf5c-4b0c-997c-813baddf0d75:Weibull_CDF.svg.png)
    - 連続一様分布 continuous uniform
    - 複素正規分布 complex normal
    - 
    - 
    - 
    - 
    - 
    - Gomperts
    - Frechet
        - parameter
            - location
            - scale
            - shape
        - PDF
        - CDF
            $$ \exp(-(\frac{x-m}{s})^{-\alpha}) $$
            ![Frechet_cdf.svg.png](attachment:5e9e15f3-5e14-426b-9442-72e975062081:Frechet_cdf.svg.png)
    !d et- Gumbel
        - parameter
            - location $\mu$
            - scale $\beta$
        - PDF
        - CDF
            $$ \exp(-\exp(-\frac{x-\mu}{\beta})) $$
            ![Gumbel-Cumulative.svg.png](attachment:73734e5e-ae08-46e8-b8cc-c3469410af3b:Gumbel-Cumulative.svg.png)
  k  - maxweby