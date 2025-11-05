---
alias:
    ['risk premium']
---
rはPを用いて次のように変形できる
$$
r_i = (r_m - r_f)\beta + r_f, \beta = \frac{\sigma_{im}}{\sigma_m^2}$$ 
 $$
r_i = \frac{P_{t+1}}{P_t} -1 $$ 
 $$
P_t = \frac{P_{t+1}}{r_i + 1} = \frac{P_{t+1}}{(r_m - r_f)\beta + r_f+1} 
$$
ここで\betaは
$$
\beta=\frac{Cov(\frac{P_{t+1}}{P_t}-1, r_m)}{\sigma_m^2} = \frac{Cov(P_{t+1}, r_m)}{P_t\sigma_m^2}
$$
よって
$$
P_t = \frac{P_{t+1}}{(r_m - r_f) \frac{Cov(P_{t+1}, r_m)}{P_t\sigma_m^2} + r_f+1}$$ 
 $$
(r_m - r_f) \frac{Cov(P_{t+1}, r_m)}{\sigma_m^2} + P_t(r_f+1)= P_{t+1} $$ 
 $$
P_t(r_f +1) - P_{t+1} = -\frac{Cov(P_{t+1}, r_m)}{\sigma_m^2}
$$