---
alias:
    ['先物契約', 'future contract']
---
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