---
alias:
    ['FFT', 'Fast Fourier Transform']
---
- 特性関数
    $$
    \phi_{\ln S_t}(u)=\mathbb E[\exp(i u \ln S_t)] 
    $$
- option price
    $$
    C(K) = \exp(-rT) \int_{-\infin}^\infin \exp(iu \ln K) \psi(u)du \\
    \psi(u) = \frac{\phi(u-i)}{iu\phi(-i)}
    $$