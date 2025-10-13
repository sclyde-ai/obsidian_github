$$
W^{(n)}(t) = \frac{1}{\sqrt{n}}M_{nt}
$$
- expectation 期待値
    $$
    \mathbb E[W^{(n)}(t) - W^{(n)}(s)] = 0
    $$
- variance 分散
    $$
    V[W^{(n)}(t) - W^{(n)}(s)] = t-s
    $$
- martingale
    $$
    \mathbb E[W^{(n)}(t)| \mathcal F(s)] = \mathbb E[(W^{(n)}(t)-W^{(n)}(s)) + W^{(n)}(s)]
    $$
- quadratic variation
    $$
    [W^{(n)}, W^{(n)}](t) \\
    = \sum_{j=1}^{nt} \left[W^{(n)}\left(\frac{j}{n}\right) - W^{(n)}\left(\frac{j}{n}\right)\right]^2 \\
    = \sum_{j=1}^{nt}\left[\frac{1}{\sqrt n} X_j \right]^2 \\
    = \sum_{j=1}^{nt} \frac{1}{n} \\
    = t
    $$
- central limit
    moment-generating function
    $$
    \phi_n(u) = \mathbb E[e^{uW^{(n)}(t)}] \\
    = \mathbb E [\exp (\frac{u}{\sqrt n}M_{nt})] \\
    = \mathbb E [\exp (\frac{u}{\sqrt n} \sum_{j=1}^{nt} X_j)] \\
    = \mathbb E [\prod_{j=1}^{nt} \exp (\frac{u}{\sqrt n} X_j)] \\
    = \prod_{j=1}^{nt} \mathbb E [\exp (\frac{u}{\sqrt n} X_j)] \\
    = \prod_{j=1}^{nt} \frac{1}{2}e^{\frac{u}{\sqrt n}} + \frac{1}{2}e^{-\frac{u}{\sqrt n}} \\
    = (\frac{1}{2}e^{\frac{u}{\sqrt n}} + \frac{1}{2}e^{-\frac{u}{\sqrt n}})^{nt} \\
    $$
    it sufgice to consider logarithm
    $$
    \log \phi_n(u) = nt \log (\frac{1}{2}e^{\frac{u}{\sqrt n}} + \frac{1}{2}e^{-\frac{u}{\sqrt n}})
    $$
    we make the change of variable $x = \frac{1}{\sqrt n}$ 
    $$
    \lim_{n \to \infin} \log \phi_n(u) = t \lim_{x \downarrow 0} \frac{\log (\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux})}{x^2}
    $$
    we may use L’Hopital’s rule
    $$
    \frac{\partial}{\partial x} \log (\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux}) \\ 
    = \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{\frac{1} {2}e^{ux} + \frac{1}{2}e^{-ux}}
    $$
    $$
    \frac{\partial}{\partial x}x^2 = 2x
    $$
    therefore
    $$
    \lim_{n \to \infin} \log \phi_n(u) 
    \\
    = t\lim_{x \downarrow 0} \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{2x(\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux})} 
    \\
    = \frac{t}{2} 
    \lim_{x \downarrow 0} \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{x} \cdot
     \lim_{x \downarrow 0} \frac{1}{(\frac{1}{2}e^{ux} + \frac{1}{2}e^{-ux})} \\
    = \frac{t}{2} 
    \lim_{x \downarrow 0} \frac{\frac{u}{2}e^{ux} - \frac{u}{2}e^{-ux}}{x}
    $$
    we apply  L’Hopital’s rule again
    $$
    = \frac{t}{2} 
    \lim_{x \downarrow 0} \frac{\frac{u^2}{2}e^{ux} + \frac{u^2}{2}e^{-ux}}{1} \\
    = \frac{1}{2}u^2 t
    $$