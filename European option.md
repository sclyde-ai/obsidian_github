---
parent: "[[option]]"
---

at the maturity
- call
	$$ 
	V_T = (S_T -K)^+ = √(S_T -K, 0)
	$$ 
	- price
		$$ 
		C_0 = B_0^T … E_… Q[√(S_T-K, 0)]
		$$ 
- put
	$$ 
	V_T = (K - S_T)^+ = √(K - S_T, 0)
	$$ 
	- price
		$$ 
		P_0 = B_0^T … E_… Q [√(K-S_T, 0)]
		$$ 
- put call parity
	$$ 
	CE_T - PE_T = S_0- Ke^{-rT}
	$$
	- proof
		- $CE_T - PE_T > S_0 - Ke^{-rT}$
			- time 0
				- long 1 unit underlying asst
					$$ 
					-S_0
					$$ 
					- underlying asset +1
				- long 1 unit put option
					$$ 
					-PE_T
					$$ 
				- short 1 unit call option
					$$ 
					CE_T
					$$ 
			- time T
				- $S_T ≤ K$
					- I exercise put option
						$$ 
						+K
						$$ 
						- underlying asset -1
				- $S_T > K$
					- the partner exercise call option
						$$ 
						+K
						$$ 
						- underlying asset -1
				$$ 
				(CE_T - PE_T - S_0)e^{rT} + K \
				= (CE_T - PE_T - S_0 + Ke^{-rT})e^{rT} > 0
				$$ 
		- $CE_T - PE_T < S_0 - Ke^{-rT}$
			- time 0
				- short 1 unit underlying asset
					$$ 
					S_0
					$$ 
					- underlying asset -1
				- short 1 unit put option
					$$ 
					PE_T
					$$ 
				- long 1 unit call option
					$$ 
					-CE_T
					$$ 
			- time T
				- $S_T ≤ K$
					- the partner exercise put option
						$$ 
						-K
						$$ 
						- underlying asset +1
				- $S_T > K$
					- I exercise call option
						$$ 
						-K
						$$ 
						- underlying asset +1
				$$ 
				(-CE_T + PE_T + S_0)e^{rT} - K \
				= (-CE_T + PE_T + S_0 - Ke^{-rT})e^{rT} > 0
				$$ 
	- carry cost
		$$ 
		CE_T - PE_T = S_0 - d_0- Ke^{-rT}
		$$ 
	- dividend yield
		$$ 
		CE_T - PE_T = S_0e^{-r_{div}T}- Ke^{-rT}
		$$ 
- sup & inf
	$$ 
	(S_0 - Ke^{-rT}) ≤ CE_T < S_0 \
	(Ke^{-rT}-S_0) ≤ PE_T < Ke^{-rT}
	$$ 
	- proof
		- $CE_T < S_0$
			let me assume $CE_T ≥ S_0$
			- time 0
				- short 1 unit call
					$$ 
					+ CE_T
					$$ 
				- long 1 unit underlying asset
					$$ 
					-S_0
					$$ 
					- underlying asset +1
			- time T
				- $S_T ≥ K$
					- the partner exercises the call
						$$ 
						+K
						$$ 
						- underlying asset -1
				- $S_T < K$
					- I sell the underlying asset
						$$ 
						+S_T
						$$ 
						- underlying asset -1
			$$ 
			(CE_T - S_0)e^{rT} + √(S_T, K) > 0
			$$ 
		- $PE_T ≥ K e^{-rT} - S_0$
			put call parity
			$$ 
			CE_T - PE_T = S_0- Ke^{-rT} \
			-CE_T + PE_T = -S_0 + Ke^{-rT} \
			 PE_T ≥ Ke^{-rT} - S_0
			$$ 
		- $CE_T ≥ S_0 - K e^{-rT}$
			put call parity
			$$ 
			CE_T - PE_T = S_0- Ke^{-rT} \
			CE_T ≥ S_0- Ke^{-rT}
			$$ 
		- $PE_T < Ke^{-rT}$
			put call parity
			$$ 
			CE_T - PE_T = S_0- Ke^{-rT} \
			-CE_T + PE_T = -S_0 +Ke^{-rT} \
			PE_T + S_0 = CE_T +Ke^{-rT} \
			PE_T + S_0 < S_0 +Ke^{-rT} \
			PE_T < Ke^{-rT}
			$$ 
	- carry cost
		$$ 
		(S_0 - d_0 - Ke^{-rT}) ≤ CE_T < S_0 - d_0\
		(Ke^{-rT}-S_0 + d_0) ≤ PE_T < Ke^{-rT}
		$$ 