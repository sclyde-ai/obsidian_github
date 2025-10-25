$$
\mathbb E[R_i] = r_f + \beta_i (\mathbb E[R_M] - r_f)
$$
$$
\beta_i = \frac{\sigma_{im}}{\sigma_m^2}
$$
- proof
    - expectation
        $$
        \mathbb E[R_P] = w \mathbb E[R_i] + (1-w) \mathbb E[R_M]
        $$
    - variance
        $$
        \sigma_P^2 = w^2 \sigma_i^2 + (1-w)^2 \sigma_M^2 + 2w(1-w) \sigma_{iM}
        $$
    - the derivative of r with respect to w
        $$
        \frac{d \mathbb E[R_P]}{d w} = \mathbb E[R_i] - \mathbb E[R_M]
        $$
    - the derivative of sigma^2 with respect to w
        $$
        \frac{d \sigma_P^2}{d w} = 2w \sigma_i^2 -2(1-w)\sigma_M^2 +2\sigma_{iM}-4w\sigma_{iM}
        = 2\sigma_P\frac{d \sigma_P}{d w}
        $$
    - the derivative of sigma with respect to w
        $$
        \frac{d \sigma_P}{d w} =\frac{w \sigma_i^2 -(1-w)\sigma_M^2 +(1-2w)\sigma_{iM}}{\sigma_P}
        $$
    $$
    \frac{\partial \mathbb E[R_P]}{\partial \sigma_P} = \frac{\frac{d \mathbb E[R_P]}{d w}}{\frac{d \sigma_P}{d w}} =\frac{(\mathbb E[R_i] - \mathbb E[R_M])\sigma_P}{w \sigma_i^2 -(1-w)\sigma_M^2 +(1-2w)\sigma_{iM}}
    $$
    plug in $w = 0$ 
    $$
    \left.\frac{\partial \mathbb E[R_P]}{\partial \sigma_P}\right|_{w=0} = \frac{(\mathbb E[R_P] - \mathbb E[R_M])\sigma_M}{-\sigma_M^2 +\sigma_{iM}}
    $$
    it corresponds to capital allocation line 
    $$
    \frac{(r_i - r_m)\sigma_m}{-\sigma_m^2 +\sigma_{im}} = \frac{r_m - r_f}{\sigma_m} $$
     $$
    r_i - r_m = (r_m - r_f)(-1 +\frac{\sigma_{im}}{\sigma_m^2})$$ 
    $$
    r_i - r_m + r_m - r_f = (r_m - r_f)\frac{\sigma_{im}}{\sigma_m^2} $$
     $$
    r_i - r_f = (r_m - r_f)\frac{\sigma_{im}}{\sigma_m^2} 
    $$