- 導関数 derivative function
    $$ f'(x) = \frac{df}{dx} (x) = \frac{d}{dx} f(x) \\ \forall a \in U, \exist f'(a) $$
    f(x) is differentiable on U
- 演算 operation
    - 線形性
        $$ \{kf(x)+lg(x)\}' = kf'(x)+lg'(x) $$
    - 掛け算
        $$ \{f(x)g(x)\}'=f'(x)g(x)+f(x)g'(x) $$
    - 割り算
        $$ \left\{\frac{f(x)}{g(x)}\right\}' = \frac{f'(x)g(x)-f(x)g'(x)}{\{g(x)\}^2} $$
- 合成関数の微分
    $$ \frac{df(g(x))}{dx}= \frac{df(g )}{dg}\cdot \frac{dg(x)}{dx} $$
    - proof
        $$ \lim_{a \to b} \frac{f(g(x+h))-f(g(x))}{h} = \lim_{h \to 0} \frac{f(g(x+h))-f(g(x))}{g(x+h)-g(x)} \frac{g(x+h)-g(x)}{h} \\ = \lim_{h \to 0} \frac{f(g(x+h))-f(g(x))}{g(x+h)-g(x)} \lim_{h \to 0} \frac{g(x+h)-g(x)}{h} \\ = \frac{df(g)}{dg} \cdot \frac{dg(x)}{dx} $$
- 逆関数の微分
    $$ \frac{d y}{dx} = \frac{1}{\frac{d x}{d y}} $$
    - proof
        $$ y =f^{-1}(x) \\ x = f(y) \\ 1 = \frac{\partial f(y)}{\partial y} \frac{\partial y}{\partial x} \\ 1 = \frac{\partial x}{\partial y} \frac{\partial y}{\partial x} \\ \frac{\partial y}{\partial x} = \frac{1}{\frac{\partial x}{\partial y}} $$
- 商の微分
    $$ \frac{\frac{df(x)}{dx}g(x) - f(x)\frac{dg(x)}{dx}}{\{g(x)\}^2} $$
    - proof
        $$ \lim_{h \to 0} \frac{\frac{f(x+h)}{g(x+h)} - \frac{f(x)}{g(x)}}{h} \\ \lim_{h \to 0} \frac{\frac{f(x+h)g(x)-f(x)g(x+h)}{g(x+h)g(x)}}{h} \\ \lim_{h \to 0} \frac{\frac{f(x+h)g(x) - f(x)g(x) + f(x)g(x )-f(x)g(x+h)}{g(x+h)g(x)}}{h}\\ \lim_{h \to 0} \frac{\frac{(f(x+h)-f(x))g(x) - f(x)(g(x+h)-g(x))}{g(x+h)g(x)}}{h} \\ \xrightarrow{h \to 0 } \frac{f'(x)g(x) - f(x)g'(x)}{\{g(x)\}^2} $$
- 高階微分
- 微分公式集
    - log 対数
        $$ \frac{1}{\ln a}\frac{1}{x} $$
        - proof
            $$ \lim_{h \to 0} \frac{\log_a (x+h) - \log_a x}{h} \\ = \lim_{h \to 0} \frac{\log_a (1+\frac{h}{x}) }{h} \\ = \lim_{h \to 0} \log_a (1+\frac{h}{x})^{\frac{1}{h}} \\ = \lim_{h \to 0} \log_a (((1+\frac{h}{x})^{\frac{x}{h}})^{\frac{1}{x}}) \ = \frac{1}{x} \lim_{h \to 0} \log_a (1+\frac{h}{x})^{\frac{x}{h}}) \\ = \frac{1}{x} \log_a e\\ = \frac{1}{\ln a} \frac{1}{x} $$
    - ln 自然対数
        $$ \frac{1}{x} $$
        - proof
            $$ \lim_{h \to 0} \frac{\log (x+h) - \log x}{h} \\ = \lim_{h \to 0} \frac{\log (1+\frac{h}{x}) }{h} \\ = \lim_{h \to 0} \log (1+\frac{h}{x})^{\frac{1}{h}} \\ = \lim_{h \to 0} \log (((1+\frac{h}{x})^{\frac{x}{h}})^{\frac{1}{x}}) \ = \frac{1}{x} \lim_{h \to 0} \log (1+\frac{h}{x})^{\frac{x}{h}}) \\ = \frac{1}{x} $$
    - 分数の対数