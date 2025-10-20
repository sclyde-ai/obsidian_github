
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