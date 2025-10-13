$$
\Delta t = \frac{t}{n}\\
S_t = S_0 u^x d^{n-x}
$$
- up & down factor
    $$
    u = e^{\sigma \sqrt{\Delta t}} \\
    d = e^{-\sigma \sqrt{\Delta t}} \\
    ud = 1
    $$
- S_t
    $$
    S_t = S_0(e^{\sigma \sqrt{\Delta t}})^x (e^{-\sigma \sqrt{\Delta t}})^{n-x} \\ 
    = S_0 e^{\sigma\sqrt{\Delta t}(2x-n)} \\ 
    = S_0 e^{\sigma\frac{\sqrt t(2x-n)}{\sqrt n}} \\
    = S_0 e^{\sigma W_t}
    $$
- option
    - risk neutral probability
        $$
        \\
        p = \frac{e^{r \Delta t} - d}{u - d} \\
        q = \frac{e^{r \Delta t} - u}{d - u} \\
        p + q = 1
        $$
    $$
    m = \min \{i | S_0 u^i d^{n-i} \geq K\}
    $$
    $$
    CE_0 = e^{-r\Delta t}\sum_{i = m}^n \binom n i q^i(1-q)^i (S_0u^i d^{n-i} -K) \\
    = D_t \overline B(m, n, p)(S_0u^i d^{n-i} -K) \\
    = 
    $$
    $$
    \underline B(m, n, p) = \sum_{i=0}^{m-1} p^i (1-p^{n-i})
    $$
    $$
    \overline B(m, n, p) = \sum_{i=m}^n p^i (1-p^{n-i})
    $$
    - call
        $$
        CE_0 = S_0 B(m, N, \bar q) -KRB(m,N, q)
        $$
    - put
        $$
        PE_0 = S_0 B(m, N, \bar q) -KRB(m,N, q)
        $$