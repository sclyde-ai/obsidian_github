---
parent: "[[金融派生商品 derivative]]"
---

- strike 権利行使
	- strike price 権利行使価格
	- strike shift
- maturity 満期
- intrinsic value
- vanilla option
	[[European option]]
	[[American option]]
	[[Bermudan option]]
	[[Boston option]]
- exotic option
	[[Asian option]]
	[[barrier option]]
	[[Parisian option]]
	[[look-back option]]
	[[binary•digital option]]
	cross option/composite option
	quanto option
	basket option
	rainbow option
	exchange option
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
- strategy
	[[covered call]]
	[[protective•married put]]
	[[straddle]]
	[[strangle]]
	[[diagonal spread]]
	[[butterfly spread]]
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