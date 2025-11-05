---
alias:
    ['Gamma function']
---
$$ \Gamma(z) = \int_0^\infty x^{z-1}e^{-x} dx $$
- convergence
    - real number
        $$ I = I_1 + I_2 \\ I = \int_0^\infty x^{z-1}e^{-x} dx \\ I_1 = \int_0^c x^{z-1}e^{-x} dx \\ I_2 = \int_c^\infty x^{z-1}e^{-x} dx $$
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