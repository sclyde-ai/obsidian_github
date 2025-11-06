 
- 満期日に額面と
- 一定期間ごとにcouponが
支払われる債権

- [[額面 face value]] F
- [[満期 maturity]] T
- r implied rate
- C coupon
- $r_c$ coupon rate


- dirty price
- accrued interest 経過利息
- clean price
	dirty price - accrued interest
- preposition 2.27 (hard)
	$$
	r = r_c \Leftrightarrow F = V_0
	$$
	- proof
		- \Rightarrow
			$$
			\sum_{n = 1}^T \frac{r_c F}{(1+r)^n} + \frac{F}{(1+r)^T} = F
			$$
			- T = 1
				$$
				\frac{r_c F}{1+r} + \frac{F}{1+r} \\= \frac{1+r_c}{1+r} F \\
				= \frac{1+r}{1+r} F \\
				= F
				$$
			- T= k
				T=kで成立すると仮定
				$$
				\sum_{n = 1}^{k+1} \frac{r_c F}{(1+r)^n} + \frac{F}{(1+r)^{k+1}} \\ =
				\sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{r_cF}{(1+r)^{k+1}} + \frac{F}{(1+r)^{k+1}}
				\\ = 
				\sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{(1+r_c)F}{(1+r)^{k+1}}
				\\ = 
				\sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{(1+r)F}{(1+r)^{k+1}}
				\\ = 
				\sum_{n = 1}^{k} \frac{r_c F}{(1+r)^n} + \frac{F}{(1+r)^k}
				\\ = F
				$$
		- \Leftarrow
			$$
			F = \sum_{n=1}^{T-1} \frac{r_c F}{(1+r)^n} + \frac{(1+r_c)F}{(1+r)^T} \\
			(1+r)^T = \sum_{n=1}^{T-1} r_c(1+r)^{T-n} + (1+r_c) \\
			x = 1+r \\
			x^T - \sum_{n=1}^{T-1} r_cx^{T-n} -(1+r_c) = 0 \\
			\sum_{n=1}^{T-1} r_cx^{T-n}
			$$
- par