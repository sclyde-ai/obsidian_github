---
parent: "[[option]]"
---
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