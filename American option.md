
any time before the maturity
- call
	$$ 
	v_N = √(S_N - K, 0) \
	v_n = √(S_n - K, B_0^1[ … pv_{n+1}(H)+ (1-… p)v_{n+1}(T)])
	$$ 
- put
	$$ 
	v_N = √(K-S_N, 0) \
	v_n = √(K-S_n, B_0^1[ … pv_{n+1}(H)+ (1-… p)v_{n+1}(T)])
	$$ 
- put call parity
	$$ 
	S_0 - K ≤ CA_T - PA_T ≤ S_0- Ke^{-rT}
	$$ 
	- proof
		- $CA_T - PA_T ≤ S_0 - Ke^{-rT}$
			- time 0
				- long 1 unit underlying asset
					$$ 
					-S_0
					$$ 
					- underlying asset +1
				- long 1 unit put option
					$$ 
					-PA_T
					$$ 
				- short 1 unit call option
					$$ 
					+CA_T
					$$ 
			- time t (if the partner exercise call option)
				$$ 
				+K
				$$ 
				- underlying asset -1
			- time T
				- if the partner exercise call option
					$$ 
					(CA_T - PA_T - S_0)e^{rT} + Ke^{r(T-t)} \
					= (CA_T - PA_T - S_0 + Ke^{-rt})e^{rT} \
					≥ (CA_T - PA_T - S_0 + Ke^{-rT})e^{rT} \
>0
					$$ 
				- else
					$$ 
					(CA_T - PA_T - S_0)e^{rT} + Ke^{r(T-t)} \
					=  (CA_T - PA_T - S_0 + Ke^{-rT})e^{rT} \
>0
					$$ 
		- $S_0 - K ≤ CA_T - PA_T$
			- time 0
				- short 1 unit underlying asset
					$$ 
					+S_0
					$$ 
					- underlying asset -1
				- short 1 unit put option
					$$ 
					+PA_T
					$$ 
				- long 1 unit call option
					$$ 
					-CA_T
					$$ 
			- time t (if the partner exercise call option)
				$$ 
				-K
				$$ 
				- underlying asset +1
			- time T
				- if the partner exercise call option
					$$ 
					(-CA_T + PA_T + S_0)e^{rT} - Ke^{r(T-t)} \
					= (-CA_T + PA_T + S_0 - Ke^{-rt})e^{rT} \
					≥ (-CA_T + PA_T + S_0 - Ke^{-rT})e^{rT} \
>0
					$$ 
				- else
					$$ 
					(-CA_T + PA_T + S_0)e^{rT} - Ke^{r(T-t)} \
					=  (-CA_T + PA_T + S_0 - Ke^{-rT})e^{rT} \
>0
					$$ 
	- carry cost
		$$ 
		S_0 -d_0 - K ≤ CA_T - PA_T ≤ S_0- Ke^{-rT}
		$$ 
	- dividend yield
		$$ 
		S_0e^{-r_{div}T} - K ≤ CA_T - PA_T ≤ S_0- Ke^{-rT}
		$$ 
- sup & inf
	- no carry cost (assumption)
	$$ 
	(S_0 - Ke^{-rT}) ≤ CA_T < S_0 \
	(K-S_0) ≤ PA_T < K
	$$ 