---
alias:
  - option
parent: "[[金融派生商品 derivative]]"
---
- component 構成要素
	- strike 権利行使
		- strike price 権利行使価格
		- strike shift
	- maturity 満期
	- intrinsic value
- vanilla option
	- American option
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
	- Bermudan option
	- Boston option
	- the relation between European and American
		- no carry cost (assumption)
		$$ 
		CE_T = CA_T
		$$ 
		- proof
			- $CE_T < CA_T$
				- time 0
					- short 1 unit American call
					- long 1 unit European call
				- time t
				- time T
- exotic option
	- Asian option
		average price
		- arithmetic average
			$$ 
			A_T = ½ ∫_0^T S_t dt
			$$ 
		- geometric average
			$$ 
			A_T = ½ ∫_0^T ∬(S_t) dt
			$$ 
		- average price option
			- call
				$$ 
				V_T = (A_T - K)^+
				$$ 
			- put
				$$ 
				V_T = (K-A_T)^+
				$$ 
		- average strike option
			- call
				$$ 
				V_T = (S_T - k A_T)^+
				$$ 
			- put
				$$ 
				V_T = (k A_T - S_T)^+
				$$ 
	- barrier option
		it’s activate or deactivate 
		if the underlying asset’s price hits the barrier 
		- knock-in
			activate if the price hits the barrier
			- up-and-in
				rise to or above the barrier
			- down-and-in
				fail to or below the barrier
		- knock-out
			deactivate if the price hits the barrier
			- up-and-out
				rise to or above the barrier
			- down-and-out
				fail to or below the barrier
		- in out parity
			$$ 
			C = C_{in} + C_{out}
			$$ 
	- Parisian option
		it’s activate or deactivate 
		if the underlying asset’s price remains above or below the barrier 
		for a continuous period of time(window)
		- up-and-out
		- down-and-out
	- look-back option
		extreme (maximum or minimum)
		- floating strike
			the strike price is floating
			- payoff
				the difference between 
				the extreme price in the maturity
				and
				the market price at the maturity 
			- call
				$$ 
				LC_{float} = √(S_T-S_{min},0)
				$$ 
			- put
				$$ 
				LP_{float} = √(S_{max} - S_T, 0)
				$$ 
		- fixed strike
			the strike price is fixed
			- payoff
				the difference between 
				the extreme price in the maturity
				and
				the strike price
			- call
				$$ 
				LC_{fix} = √(S_{max} - K, 0)
				$$ 
			- put
				$$ 
				LP_{fix} = √(K-S_{min},0)
				$$ 
		- why is it called “look back”?
			"look back" at the price history of the underlying asset over the life of the option and exercise it at the most favorable price
	- binary/digital option
		$$ 
		℀(S_T>K)
		$$ 
		$$ 
		λ C_K(t, T) - λ C_{K+½/λ}} (t, T) \
		→
		-∂ C/∂ K
		… D_K(t, T)
		$$ 
	- cross option/composite option
		- quanto option
	- basket option
		- rainbow option
	- exchange option
- option cases
	|  | long a call | short a call | long a put | short a put |
	| --- | --- | --- | --- | --- |
	| S0 | -c | c | -c | c |
	| K < St | St - K - c | K - St + c | -c | c |
	| St < K | -c  | c | K - St - c | St - K + c |
	- long a call
		|  | 投資家 | 相手 |
		| --- | --- | --- |
		| S0 | -c | c |
		| K < St | St - K - c | K - St + c |
		| St < K | -c | c |
	- short a call
		|  | 投資家 | 相手 |
		| --- | --- | --- |
		| S0 | c | -c |
		| K < St | K - St + c | St - K - c |
		| St < K | c | -c |
	- long a put
		|  | 投資家 | 相手 |
		| --- | --- | --- |
		| S0 | -c | c |
		| K < St | -c | c |
		| St < K | K -St - c | St - K + c |
	- short a put
		|  | 投資家 | 相手 |
		| --- | --- | --- |
		| S0 | -c | c |
		| K < St | -c | c |
		| St < K | St - K + c | K -St - c |
	- call k1 > k2
		投資家はCE1を買い、CE2を売る。
		|  | 投資家 | 相手 |  |
		| --- | --- | --- | --- |
		| S0 | -c1 +c2 | c1 -c2 |  |
		| k2 < k1 < St | St -k1  | St -k2 | -k1 +k2 -c1 +c2 |
		| k2 < St < k1 | 0 | St -k2 | k2 -St  -c1 +c2 |
		| St < k2 < k1 | 0 | 0 |  -c1 +c2 |
	- call k1 < k2
		投資家はCE1を買い、CE2を売る。
		|  | 投資家 | 相手 |  |
		| --- | --- | --- | --- |
		| S0 | - c1 +c2 | c1 -c2 |  |
		| k1 < k2 < St | St -k1  | St -k2 | -k1 +k2 -c1 +c2 |
		| k1 < St < k2 | St -k1  | 0 | St -k1  -c1 +c2 |
		| St < k1 < k2 | 0 | 0 | -c1 +c2 |
	- put k1 > k2
		投資家はPE1を買い、PE2を売る。
		|  | 投資家 | 相手 |  |
		| --- | --- | --- | --- |
		| S0 | - c1 +c2 | c1 -c2 |  |
		| k2 < k1 < St | 0 | 0 | -c1 +c2 |
		| k2 < St < k1 | k1 -St | 0 | k1 -St  -c1 +c2 |
		| St < k2 < k1 | k1 -St | k2 -St | k1 -k2 -c1 +c2 |
	- put k1 < k2
		投資家はPE1を買い、PE2を売る。
		|  | 投資家 | 相手 |  |
		| --- | --- | --- | --- |
		| S0 | - c1 +c2 | c1 -c2 |  |
		| k1 < k2 < St | 0 | 0 | -c1 +c2 |
		| k1 < St < k2 | 0 | k2 -St | St -k2 -c1 +c2 |
		| St < k1 < k2 | k1 - St | k2 -St | k1 -k2 -c1 +c2 |
- option strategy
	- money-ness
		- ITM in the money
			the derivative have a positive intrinsic value
		- ATM at the money
			the derivative have a same intrinsic value
		- OTM out of the money
			the derivative have a negative intrinsic value
	- call
		- long
		- short
	- put
		- long
		- short
	- covered call
		selling call options by an equivalent amount of the underlying security
		- premium
		- stable and bull
		![image.jpeg](image%201.jpeg)
	- protective/married put
		buying put options by an equivalent amount of the underlying security
		- payoff
		- volatile and bull
		- to hedge the potential loss
		![image.jpeg](image%202.jpeg)
	- straddle
		simultaneously 
		either buying or selling 
		both a call and a put option 
		with the same strike price 
		with the same expiration
		![image.jpeg](image%203.jpeg)
		- long straddle
			buying
			- payoff
			- volatile
			![IMG_7406.jpeg](IMG_7406.jpeg)
		- short straddle
			selling
			- premium
			- stable
			- greeks
				- short gamma
					$$ 
					Γ < 0
					$$ 
				- short vega
					$$ 
					ℤ < 0
					$$ 
			![IMG_7406.jpeg](IMG_7406%201.jpeg)
	- strangle
		simultaneously 
		either buying or selling 
		both a call and a put option 
		with the different strike price 
		with the same expiration
		- lower cost than straddle
		![image.jpeg](image%204.jpeg)
		- long strangle
			buying
			- payoff
			- volatile
			![IMG_7407.jpeg](IMG_7407.jpeg)
		- short strangle
			selling
			- premium
			- stable
			![IMG_7407.jpeg](IMG_7407%201.jpeg)
	- vertical spread
		simultaneously 
		both selling and buying 
		either a call or a put option
		with the different strike prices
		with the same expiration
		![image.jpeg](image%205.jpeg)
		- bull call spread
		- bear put spread
	- diagonal spread
		simultaneously entering into 
		a long and short position 
		with the different strike prices 
		with the different expirations
	- butterfly spread
		![image.jpeg](image%206.jpeg)
		- long call
			long one ITM call
			short two ATM calls
			long one OTM call
			- profit from low volatility
		- short call
			short one ITM call
			long two ATM calls
			short one OTM call
			- profit from high volatility
		- long put
			long one ITM call
			short two ATM calls
			long one OTM call
			- profit from low volatility
		- short put
			short one ITM call
			long two ATM calls
			short one OTM call
			- profit from high volatility
	- iron butterfly spread
		sell one ATM call
		sell one ATM put 
		buy one OTM call at higher strike price
	- condor spread
		![](https://www.investopedia.com/thmb/JBLXXJUqPhCfxQma97fXQk8TdxM=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/CondorSpread1-c6ce24585200444cabb8914138fec306.png)
		- long call
			buy a call with the lowest strike price 
			sell a call with the second lowest strike price
			sell a call with the second highest strike
			buy a call with highest strike
		- long put
			buy a put with the lowest strike price 
			sell a put with the second lowest strike price
			sell a put with the second highest strike
			buy a put with highest strike
		- short call
			buy a call with the lowest strike price 
			sell a call with the second lowest strike price
			sell a call with the second highest strike
			buy a call with highest strike
			![](https://www.investopedia.com/thmb/t1ZkG2_inxnTSdgA7vJUtlc_tRY=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/CondorSpread2-6290806efe2c47cb85384ddaa3f9144f.png)
		- short put
			sell a call with the lowest strike price 
			buy a call with the second lowest strike price
			buy a call with the second highest strike
			sell a call with highest strike
	- iron condor spread
	- calendar/horizontal/time spread
		simultaneously enters into
		long and short positions
		with the same strike price
		with the different expirations
		on the same underlying asset 
		- minimizes the effects of time
		![image.jpeg](image%207.jpeg)
		- long call
			buy a longer-term call
			sell a shorter-term call
			- profit from pay
		- short call
			sell a longer-term call 
			buy a shorter-term call
			- profit from premium
		- long put
			buy a longer-term put
			sell a near-term put
			- profit from pay
		- short put
			sell a longer-term put 
			buy a shorter-term put
			- profit from premium