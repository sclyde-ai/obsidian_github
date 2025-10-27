---
alias:
    ['the limit of binomial model', '極限二項模型']
---
- up & down factor
    $$
    u_n = 1 + \frac{\sigma}{\sqrt n}\\
    d_n = 1 - \frac{\sigma}{\sqrt n}\\
    $$
- risk neutral probability
    $$
    \tilde p = \frac{1+r-d_n}{u_n-d_n}\\
    \tilde q = \frac{1+r-u_n}{d_n-u_n}
    $$
- the number of coin toss
    $$
    nt = H_{nt}+ T_{nt}
    $$
- the random walk
    $$
    M_{nt} = H_{nt}- T_{nt}
    $$
- head & tail
    $$
    H_{nt} = \frac{1}{2}(nt + M_{nt}) \\
    T_{nt} = \frac{1}{2}(nt - M_{nt})
    $$
- stock price
    $$
    S(n,t)= S_0u^{H_{nt}}d^{T_{nt}} \\ 
    = S_0
    \left(1+\frac{\sigma}{\sqrt n}\right)^{\frac{1}{2}(nt+M_{nt})} 
    \left(1-\frac{\sigma}{\sqrt n}\right)^{\frac{1}{2}(nt-M_{nt})} 
    $$
- theorem
    $$
    S(t) = S_0 \exp (\sigma W(t)-\frac{1}{2}\sigma^2 t)
    $$
    - proof
        $$
        = \ln S_0 +  \frac{1}{2}(nt+M_{nt})\ln (1+\frac{\sigma}{\sqrt n}) + \frac{1}{2}(nt-M_{nt})\ln (1-\frac{\sigma}{\sqrt n}) 
        \\ 
        =  \frac{1}{2}(nt+M_{nt})(\frac{\sigma}{\sqrt n} - \frac{\sigma^2}{2n} + O(n^{-\frac{3}{2}})) + \frac{1}{2}(nt-M_{nt})(-\frac{\sigma}{\sqrt n} - \frac{\sigma^2}{2n} + O(n^{-\frac{3}{2}})) \\
        =  nt (\frac{\sigma^2}{2n}+ O(n^{-\frac{3}{2}}))+ M_{nt}(\frac{\sigma}{\sqrt n} + O(n^{-\frac{3}{2}})) \\
        = -\frac{1}{2}\sigma^2 t + O(n^{-\frac{1}{2}})+ \sigma W^{(n)}(t) + O(n^{-\frac{3}{2}})
        $$