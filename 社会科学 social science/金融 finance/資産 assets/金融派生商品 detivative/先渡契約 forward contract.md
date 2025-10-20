	- 特定の資産を (原資産 underlying asset)
	- 特定の将来時点で (満期日 maturity)
	- 現時点で決めた価格で (先渡価格 forward price)
	取引する売買契約
	- component 構成要素
		- S_t underlying asset 原資産
		- T maturity 満期
		- forward price 先渡価格
			- forward price (no carry cost)
				$$ 
				For_S(t, T) = S(t)/B(t, T)
				$$ 
				- cashflow
					- T
						$$ 
						S_T - K
						$$ 
				- proof
					- $F(t, T) > S_t/B(t, T)$
						- short $B(t, T)$ unit forward
							- underlying asset -1
							- cash
								$$ 
								+B(t, T)F(t, T)
								$$ 
						- long 1 unit underlying asset
							- underlying asset +1
							- cash
								$$ 
								-S_T
								$$ 
						- underlying asset -1 +1 = 0
						- cash
							$$ 
							B(t, T)F(t, T) - S_t \
							> B(t, T)S_t/B(t, T) -S_t \
							= 0
							$$ 
					- $F(t, T) < S_t/B(t, T)$
						- long $B(t, T)$ unit forward
							- underlying asset +1
							- cash
								$$ 
								-B(t, T)F(t, T)
								$$ 
						- short 1 unit underlying asset
							- underlying asset -1
							- cash
								$$ 
								+S_T
								$$ 
						- underlying asset +1 -1 = 0
						- cash
							$$ 
							-B(t, T)F(t, T) +S_t \
							> -B(t, T)S_t/B(t, T) +S_t \
							= 0
							$$ 
			- forward price (carry cost)
				- carry cost 維持費用
					the cost to keep a position
					- stock : dividend(+)
					- FX : interest rate(+, -)
					- commodity : storage cost(-)
				$$ 
				F(0, T) = (S_0 - d_0)/B(0, T)
				d_0 := B(0, t)d
				$$ 
				$$ 
				F(0, T) = (S_0 - d_0)/B(0, T)
				d_0 := ∑_{n=1}^NB(0, t_n)d_n
				$$ 
				- proof
					- $F(0, T) > (S_0 -d_0)/B(t, T)$
						- time 0
							- short $B(t, T)$ unit forward
							- long 1 unit underlying asset
							- sell safety asset
								- safety asset -1
								- cash
									$$ 
									+d_0
									$$ 
							$$ 
							B(0, T)F(0, T) - S_0 +d_0\
							> B(0, T) (S_0 -d_0)/B(0, T) - S_0 +d_0\
							= 0
							$$ 
						- time t
					- $F(0, T) < (S_0 - d_0)/B(0, T)$
						先物契約を $B(0, T)$でlong position
						原資産を1単位売る
						- time 0
							$$ 
							S_0 - B(0, T)F(0, T) \
							> S_0 - B(0, T)(S_0 -d_0)/B(0, T)\
							= d_0
							$$ 
						- time t
			- forward price (dividend yield)
				- dividend yield
					連続的に発生するcarry cost
					- 時刻tまでの配当は全て再投資
					- 時刻tで $e^{r_{div}t}$ 単位の資産を配当として受取
				$$ 
				F(0, T) = S_0 e^{-r_{div}T}/B(0, T)
				$$ 
	- basis
		現物と先物の価格差
		$$ 
		F(t, T) - S_t
		$$ 
		- theorem
			$$ 
			F(t, T) - S_t 	o 0 \
			(t 	o T)
			$$ 
	- market value 時価
		時刻tの契約書(先渡契約)の価値
		$$ 
		V(t) = (F(t, T) - F(0, T))B(t, T)
		$$ 
		- 含み損 unrealized loss
		- 含み益 unrealized gain
	- cashflow
		| position  | price up 価格上昇 | price down 価格下落 |
		| --- | --- | --- |
		| long | 利益 cash in flow | 損失 cash out flow |
		| short | 損失 cash out flow | 利益 cash in flow |
	- delivery
		原資産を届けること
		- delivery date
	- 先渡価格 vs 時価
		先渡価格 : 原資産の取引価格
		時価 : 契約書の取引価格
	- 例 example
		- TARF