
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