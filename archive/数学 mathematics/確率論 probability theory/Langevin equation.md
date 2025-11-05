---
alias:
    ['Langevin equation']
---
$$ \langle (\Delta x)^2 \rangle \propto t
\\
# m\frac{d^2 x}{d t^2}
- \gamma \frac{d f}{d x}
- R(t)
\\
# mx\frac{d^2 x}{d t^2}
- \gamma x \frac{d f}{d x}
- x R(t)
\\
\frac{m}{2} \frac{d^2 x^2}{d t^2}
- m(\frac{d x}{d t})^2 = -\frac{x}{2} \frac{d x^2}{d t}
- xR(t) \ ...\ (1)
\\
\frac{m}{2}\frac{d^2 \langle x^2 \rangle}{d t^2}
- m \langle (\frac{d x}{d t})^2 \rangle = -\frac{x}{2} \frac{d \langle x^2 \rangle}{d t}
- \langle xR(t) \rangle
\\
\frac{m}{2}\frac{d^2 \langle x^2 \rangle}{d t^2}
- k_b T = -\frac{x}{2} \frac{d \langle x^2 \rangle}{d t} \ ...\ (2)
\\
# \frac{m}{2}\frac{d z}{d t} +\frac{x}{2} z
k_b T \ ...\ (3)
\\
z(t) = C e^{- \frac{\gamma}{m} t} + \frac{2 k_b T}{\gamma}
\\
\beta t >> 1 \ ... (4)\\
z(t) = \frac{d \langle x^2 \rangle}{dt} \simeq \frac{2 k_b T}{\gamma}
\\
\langle x^2(t) \rangle \simeq \frac{2 k_b T}{\gamma}t $$
$$ (1)\ \frac{d x^2}{d t} = 2x \frac{d x}{d t}
\\
\frac{d^2 x^2}{d t^2} = 2\{\frac{d x}{d t}
- x\frac{d^2 x}{d t^2}\}
\\
(2)\ \langle R(t) \rangle = 0, \langle x(t)R(t) \rangle = \langle x(t) \rangle \langle R(t) \rangle = 0
\\
\frac{m}{2} \langle (\frac{d x}{d t})^2 \rangle = \frac{1}{2} k_bT
\\
(3)\ z(t) := \frac{d \langle x^2 \rangle}{dt} $$
- $R(t)$の重要性
    # $$ m\frac{\partial v}{\partial t}
    - \gamma v \\ z(t) = v_0 e^{- \frac{\gamma}{m} t} $$
    すぐに静止する
    $$ \hat R(t) \rightarrow \hat v(t) \rightarrow \frac{m}{2} \langle \hat v^2 \rangle = \frac{1}{2} k_bT $$