- 代数関数 algebraic function
　　$$ g_n(x)\{f(x)\}^n + g_{n-1}(x)\{f( x)\}^{n-1} + \dots + g_1(x)f(x) + g_0(x) = 0 $$
- 有理関数 rational function
        $$ f(x) = \frac{g(x)}{h(x)} $$
        - 多項式関数 polynomial function
            $$ f(x) = a_nx^n + a_{n-1} x^{n-1} + \dots + a_1x + a_0 \\ a_0, ..., a_n \in \R $$
- 超越関数 elementary function
- 偶関数/奇関数 even/odd function
    - 偶関数 even function
        $$ f(-x) = f(x) $$
    - 奇関数 odd function
        $$ f(-x) = -f(x) $$
- 
- 逆三角関数 inverse trigonometric functions
    - arcsin 逆正弦関数 inverse sine curve
        $$ \sin^{-1} $$
        - differential
            $$ \frac{1}{\sqrt{1-x^2}} $$
            - proof
                $$ y = \sin^{-1} x \\ \sin y = x \\ \cos y = \frac{dx}{dy} \\ \frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} \\ \frac{dy}{dx} = \frac{1}{\cos y} \\ \frac{dy}{dx} = \frac{1}{\sqrt {1-x^2}} $$
    - arccos 余弦関数 inverse cosine curve
        $$ \cos^{-1} $$
        - differential
            $$ -\frac{1}{\sqrt{1-x^2}} $$
            - proof
                $$ y = \cos^{-1} x \\ \cos y = x \\ -\sin y = \frac{dx}{dy} \\ \frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} \\ \frac{dy}{dx} = -\frac{1}{\sin y} \\ \frac{dy}{dx} = \frac{1}{\sqrt {1-x^2}} $$
    - arctan 逆正接関数 inverse tangent curve
        $$ \tan^{-1} $$
        - differential
            $$ \frac{1}{1+x^2} $$
            - proof
                $$ y = \tan^{-1}x \\ \tan y = x \\ \sec^2 y = \frac{dx}{dy} \\ \frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} \\ \frac{dy}{dx} = \frac{1}{\sec^2y} \\ \frac{dy}{dx} = \frac{1}{1+\tan^2y} \\ \frac{dy}{dx} = \frac{1}{1+x^2} $$
    - arccot 逆余接関数 inverse cotangent curve
        $$ \cot^{-1} $$
        - differential
            $$ -\frac{1}{1+x^2} $$
- 双曲線関数 hyperbolic function
    - sinh 双曲線正弦関数 hyperbolic sine curve
        $$ \frac{e^x -e^{-x}}{2} $$
    - cosh 双曲線余弦関数 hyperbolic cosine curve
        $$ \frac{e^x + e^{-x}}{2} $$
    - tanh 双曲線正接関数 hyperbolic tangent curve
        $$ \frac{sin}{cos} = \frac{e^x-e^{-x}}{e^x+e^{-x}} $$
- 指数関数 exponential function
    $$ \exp(x) = e^x $$
    - the relation between addiction & multiplication
        $$ \exp(x+y ) = \exp(x) \cdot \exp(y) $$
- 対数関数 logarithm function
    $$ \log_a x $$
    - 微分 differential
        $$ \frac{1}{\ln a}\frac{1}{x} $$
        - proof
            $$ \lim_{h \to 0} \frac{\log_a (x+h) - \log_a x}{h} \\ = \lim_{h \to 0} \frac{\log_a (1+\frac{h}{x}) }{h} \\ = \lim_{h \to 0} \log_a (1+\frac{h}{x})^{\frac{1}{h}} \\ = \lim_{h \to 0} \log_a (((1+\frac{h}{x})^{\frac{x}{h}})^{\frac{1}{x}}) \ = \frac{1}{x} \lim_{h \to 0} \log_a (1+\frac{h}{x})^{\frac{x}{h}}) \\ = \frac{1}{x} \log_a e\\ = \frac{1}{\ln a} \frac{1}{x} $$
    - 基数変換 logarithm change of base rule
        $$ \log_a b = \frac{\log_c b}{\log_c a} $$
        - proof
            $$ a^{\log_a b} = b \\ \log_c (a^{\log_a b}) = \log_c b \\ \log_c (a)^{\log_a b} = \log_c b \\ \log_a b \log_c a = \log_c b \\ \log_a b = \frac{\log_c b}{\log_c a} $$
    - the relation between addiction & multiplication
        $$ \ln (x \cdot y) = \ln x + \ln y $$
- 自然対数関数 natural logarithm function
    $$ \ln x $$
    - 微分 differential
        $$ \frac{1}{x} $$
        - proof
            $$ \lim_{h \to 0} \frac{\ln (x+h) - \ln x}{h} \\ = \lim_{h \to 0} \frac{\ln (1+\frac{h}{x}) }{h} \\ = \lim_{h \to 0} \ln (1+\frac{h}{x})^{\frac{1}{h}} \\ = \lim_{h \to 0} \ln (((1+\frac{h}{x})^{\frac{x}{h}})^{\frac{1}{x}}) \ = \frac{1}{x} \lim_{h \to 0} \ln (1+\frac{h}{x})^{\frac{x}{h}}) \\ = \frac{1}{x} $$
    - 定理 theorem
        $$ \ln (x \cdot y) = \ln x + \ln y $$
- 累乗根 nth root
- gauss function
    $$ \frac{1}{\sigma \sqrt {2\pi}} \exp \left(-\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2\right) $$
- beta function
    $$ B(x, y) = \int_0^1 t^{x-1}(1-t)^{y-1} dt $$
- gamma function
    $$ \Gamma(z) = \int_0^\infin x^{z-1}e^{-x} dx $$
    - convergence
        - real number
            $$ I = I_1 + I_2 \\ I = \int_0^\infin x^{z-1}e^{-x} dx \\ I_1 = \int_0^c x^{z-1}e^{-x} dx \\ I_2 = \int_c^\infin x^{z-1}e^{-x} dx $$
            - I_1
                $$ I_1 = \lim_{r \to 0}\int_r^c e^{-x}x^{s-1}dx $$
            - I_2
    - 階乗の一般化
        $$ \Gamma(z+1) = z \Gamma (z+1) \\ \Gamma(n+1) = n \Gamma(n) $$
        - proof
            mathematical induction
            - z=1
            - z=z
                integration by parts
    - x = 1/2
        gauss function
    - 正則性
- zeta function
    $$ \zeta (s) = \sum_{n = 1}^\infin \frac{1}{n^s} $$
- logistic function
    $$ f(x) = \frac{L}{1+e^{-k(x-x_0)}} $$
- Lorentzian function
- Weierstrass function
- topologist’s sine curve
    $$ \{(x, sin\frac{1}{x}):x \in(0,1]\} \cup\{(0,0)\} $$
- δ(delta) function of Dirac
    $$
    $$
    - def (Fourier transfrom)
        $$ \delta(x) = \frac{1}{2\pi} \int_{-\infin}^{\infin} e^{-ikx}dk $$
        1のFourier変換はdelta関数になる