- underlying asset 原資産
	金融派生商品の価格が基づく、元の資産や指数そのもの
	the asset which a derivative's value is based
	- stock 株式
	- commodity 商品
	- currency 通貨
	- interest rate 金利
	- market index 市場指数
- forward contract 先渡契約
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
- future contract 先物契約
	先物市場と
	1. 原資産を取引日に売買 
	2. 期日毎にCFを交換(値洗い m2m mark to market)
	の２つの取引を行う契約
	- 証拠金 margin
		1. 初期投資
			初期証拠金を支払う
			- 初期証拠金 initial margin
				初期証拠金
				=建玉価格
				×持高
				×証拠金率
		2. 値洗い mark to market
			時価を市場価格から算出
			値洗い額=時価の差額×保有量
			or
			清算機関が清算値段/価格を提示
			値洗い額=清算値段の差額×保有量
			- 時価 market value
				- time $t_n$
					$$ 
					f(t_{n+1}, T) - f(t_n, T)
					$$ 
				- time T (maturity)
					$$ 
					f(T, T) = S_T
					$$ 
			- 清算値段/清算価格 settlement price
				当日の基準価格
				- 取引所が決定する
				- 通常、終値や取引時間内の加重平均値
			|  | 価格上昇 | 価格下落 |
			| --- | --- | --- |
			| long | 利益 cash in flow | 損失 cash out flow |
			| short | 損失 cash out flow | 利益 cash in flow |
		3. 追証/証拠金請求 margin call
			証拠金が維持証拠金以下の場合、追加証拠金を預ける
			- 維持証拠金 maintenance margin
			- 追加証拠金 excess margin
		4. 満期 maturity
			- 現物決済
				long : 原資産を受取、契約価格の支払
				short : 原資産を引渡、契約価格の収入
			- 現金決済
				契約開始時と満期時の価格差を収入または支払（原資産の受渡無し）
	- 証拠金制度 margin system
		取引の履行を保証するためにあらかじめ資金を預ける制度
		- 日次清算 mark to market
			1. 証拠金口座へ初期証拠金を預ける
			2. 値洗い額を計算
			値洗い額 = (清算値段(当日) − 清算値段(前日))×保有量
			3. 証拠金残高に値洗い額を加算
			証拠金残高(当日) = 証拠金残高(前日) + 値洗い額
			4. 証拠金残高 < 維持証拠金の時
			追加証拠金 =  維持証拠金 - 証拠金残高(当日)
				   証拠金残高 = 証拠金残高 + 追加証拠金
		- 用語 word
			- 初期証拠金 initial margin
				初期証拠金
				=取引価格
				×取引数量
				×証拠金率
			- 追証/証拠金請求 margin call
			- 維持証拠金 maintenance margin
			- 追加証拠金 excess margin
			- 清算値段/清算価格 settlement price
				当日の基準価格
				- 取引所が決定する
				- 通常、終値（取引終了時の価格）や取引時間内の加重平均値
			- 限月
	- cost 費用
		- 契約時 : costなし
		- position維持 : 証拠金(margin)が必要
	- future price 先物価格
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
	- forward vs future
		forward : 契約時に費用なし、CFも発生しない
		future : 契約時に費用なし、CFは発生する
	- 先物市場の流動性
		1. 標準化
			- 特定の引渡日の先物契約のみが取引
			- 原資産の品質や引渡方法が指定済み
		2. 清算期間(clearing house)
			- 多数の参加者の様々な売買注文を取りまとめて参加者各々のdefault riskを排除
	- 清算金を払えば先物契約解消可能
	- 一般的に先物の費用は現物より低い
	- 慣習で先渡契約締結時に一切のCFは発生しない
- option
	- component 構成要素
		- strike 権利行使
			- strike price 権利行使価格
			- strike shift
		- maturity 満期
		- intrinsic value
	- vanilla option
		- European option
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
				![Screenshot 2025-05-20 151208.png](Screenshot_2025-05-20_151208.png)
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
- swap
	exchange the cashflow between two parties
	- expertise 専門用語
		- leg
			互いに交換するcashflowの片方の部分
		- notional principal amount 想定元本
			金利計算のために仮想的に用いられる元本
		- parallel loan
			AがBに通貨Xでloanを提供
			BがAに通貨Yでloanを提供
	- examples 例
		- IRS interest rate swap
			- plain vanilla swap
				exchange 
				floating interest rate 
				and 
				fixed interest rate 
			- basis swap
				exchange
				two floating interest rates
			- cross-currency/currency swap
				principal amounts 
				and 
				interest payments 
				in different currencies
			- ZCS zero coupon swap
				the stream of floating interest-rate payments
				and 
				one lump-sum payment at the maturity
		- CDS credit default swap
			exchange 
			default risk
		- catastrophe/casualty swap
			insurance company
			and 
			reinsurance company
			to transfer the risk of large-scale & unexpected events like natural disasters
	- 世界最初のswap
		1981年 world bankとIBM
		world bankがUSDで提供
		IBMがSHF(Swiss franc)で提供
	- LIBOR calculation
		|  | 固定金利 | 変動金利 |
		| --- | --- | --- |
		| 企業A | a_A | LIBOR + b_A |
		| 企業B | a_B | LIBOR + b_B |
		Aは固定金利で比較優位、Bは変動金利で比較優位
		$$ 
		a_A + b_B > a_B + b_A　全体の利益で比較
		$$ 
		Aは変動金利を、Bは固定金利を使いたい。
		→ 金利swap発生！
		- 仲介なし
			1. AとBのcashflowを計算
				$$ 
				Acashflow　a_A + LIBOR - c
				$$ 
				$$ 
				Bcashflow　LIBOR +b_B + c - LIBOR = b_B + c
				$$ 
			2. AとBのswapによる利益増加分を計算
				$$ 
				Aの利益増加分　(a_A+LIBOR-c)-(LIBOR+b_A)
				$$ 
				$$ 
				Bの利益増加分　(b_B+c)-a_B
				$$ 
			3. AとBの利益増加分が等しくなる利払いを計算
			$$ 
			(a_A+LIBOR-c)-(LIBOR+b_A)=(b_B+c)-a_B
			$$ 
			$$ 
			c=(
(a_A-b_A)-(a_B-b_B))/2
			$$ 
		- 仲介あり
- swaption
	- Bermudan swaption
	- Bermudan callable swaption
- a.k.a also known as
	- forward commitment
		[先渡 forward](https://www.notion.so/forward-216ec42dd04b81e8b828dfddd3844503?pvs=21) 
		[先物 future](https://www.notion.so/future-216ec42dd04b81578cd5cf62eccbc98c?pvs=21) 
		[swap](https://www.notion.so/swap-216ec42dd04b8157b7e2c3cc3bcd206e?pvs=21) 
	- contingent claim
		[option](https://www.notion.so/option-216ec42dd04b8195b5b9ce9475591bba?pvs=21) 
	- warrant
	- turbo/turbo certificate
		leveraged knock-out barrier
	- callable bull/bear contract
- weather derivative
	financial contracts that pay out based on specific, measurable weather conditions, such as temperature, precipitation, or wind speed, to manage financial risks associated with adverse weather events
- deal contignent hedge
- 地震 derivative
- TRAF target redumption forward