---
parent: "[[先物契約 future contract]]"
---

$$ 
f(0, T) = F(0, T)
$$ 
- proof
	- $f(0, T) > F(0, T)$
		- time 0
			- long 1 unit forward
			- short $e^{-r(T-t)}$ unit future
		- time t
			- pay future margin
				- cash
					$$ 
					-e^{-r(T-t)}(f(t, T) - f(0, T))
					$$ 
			- sell safety asset
				- safety asset -1
				- cash
					$$ 
					e^{-r(T-t)}(f(t, T) - f(0, T))
					$$ 
		- time T
			- settle future
				- underlying asset +1
				- cash
					$$ 
					-S_T +f(t, T)
					$$ 
			- settle forward
				- underlying asset -1
				- cash
					$$ 
					S_T - F(0, T)
					$$ 
			- buy safety asset
				- safety asset +1
				- cash
					$$ 
					-f(t,T) +f(0,T)
					$$ 
			- underlying asset +1 -1 =0
			- safety asset -1 +1 =0
			- cash
				$$ 
				-S_T +f(t, T) +S_T -F(0, T) -f(t,T) +f(0,T) \
				= f(0, T) -F(0, T) >0
				$$ 
	- $f(0, T) < F(0, T)$
		- time 0
			- short 1 unit forward
			- long $e^{-r(T-t)}$ unit future
		- time t
			- take future margin
				- cash
					$$ 
					e^{-r(T-t)}(f(t, T) - f(0, T))
					$$ 
			- buy safety asset
				- safety asset +1
				- cash
					$$ 
					-e^{-r(T-t)}(f(t, T) - f(0, T))
					$$ 
		- time T
			- settle future
				- underlying asset -1
				- cash
					$$ 
					S_T -f(t, T)
					$$ 
			- settle forward
				- underlying asset +1
				- cash
					$$ 
					-S_T +F(0, T)
					$$ 
			- buy safety asset
				- safety asset -1
				- cash
					$$ 
					+f(t,T) -f(0,T)
					$$ 
			- underlying asset +1 +1 =0
			- safety asset +1 -1 =0
			- cash
				$$ 
				S_T -f(t, T) -S_T +F(0, T) +f(t,T) -f(0,T) \
				= -f(0, T) +F(0, T) >0
				$$ 