$$
dr_t = (a_t- b_t r_t)dt+\sigma_t dW_t 
$$
- solution
    $$
    r_t= \exp\left(-\int_0^t a_v dv\right) [r_0 + \int_0^t \exp\left(\int_0^t a_vdv\right) \theta_u du+\int_0^t \exp\left(\int_0^t a_v dv\right)\sigma_u dW_u]
    $$
    - how to derive
        1. 変数変換
            $$
            x(t) = r(t)\exp\left(\int_0^t a(v)dv\right)
            $$
            とするとSDEは
            $$
            d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)dt+\sigma(t) dW(t)]
            $$
            - how to derive
                $$
                d x(t) = \exp\left(\int_0^t a(v)dv\right) dr(t) + r(t) d\exp\left(\int_0^t a(v)dv\right)
                $$
                - 指数の微分
                    $$
                    r(t) d\exp\left(-\int_0^t a(v)dv\right) = r(t) a(t)\exp\left(-\int_0^t a(v)dv\right)dt
                    $$
                $$
                d x(t) = \exp\left(\int_0^t a(v)dv\right) dr(t) + r(t) a(t)\exp\left(\int_0^t a(v)dv\right)dt
                $$
                $dr_t = (\theta_t- a_t r_t)dt+\sigma_t dW_t$  を代入
                $$
                d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)dt- a(t) r(t)dt+\sigma(t) dW(t)]  + r(t) a(t)\exp\left(\int_0^t a(v)dv\right)dt
                $$
                $\exp\left(\int_0^t a(v)dv\right)$ で分配法則
                $$
                d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)dt- a(t) r(t)dt+\sigma(t) dW(t)  + r(t) a(t)dt]
                $$
                $$
                d x(t) = \exp\left(\int_0^t a(v)dv\right) [\theta(t)+\sigma(t) dW(t)]
                $$
        2. 伊藤積分
            $$
            x(t) = x(0) + \int_0^t \exp\left(\int_0^t a(v)dv\right) \theta(u) du+\int_0^t \exp\left(\int_0^t a(v)dv\right)\sigma(u) dW(u)
            $$
        3. 逆変換
            $$
            r(t) = \exp\left(-\int_0^t a(v)dv\right) [r(0) + \int_0^t \exp\left(\int_0^t a(v)dv\right) \theta(u) du+\int_0^t \exp\left(\int_0^t a(v)dv\right)\sigma(u) dW(u)]
            $$
            - $x(0) = r(0)$
                $$
                x(0) = r(0)\exp\left(\int_0^0 a(v)dv\right) = r(0)\exp(0) = r(0)
                $$