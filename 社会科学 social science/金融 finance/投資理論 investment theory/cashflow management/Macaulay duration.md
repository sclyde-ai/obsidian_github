    $$
    D = \frac{\sum_{k=1}^n \frac{k}{m} \frac{C_k}{(1+\frac{y}{m})^{k}}}{\sum_{k=1}^n \frac{C_k}{(1+\frac{y}{m})^k}}
    $$
    - parameters
        $C_k$ : coupon of k
        m : the number of payment per year
        n : maturity
        y : yield
- Macaulay duration (cross form solution)
    $$
    D = \frac{1+y}{my}-\frac{1+y+n(c-y)}{mc[(1+y)^n-1]+my}
    $$
    - parameters
        c : coupon rate
        y : yield
        m : the number of payment per year
        n : maturity