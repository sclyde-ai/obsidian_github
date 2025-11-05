---
alias:
    ['JS', 'divergence']
---
$$
D_{JS} (P || Q)= \frac{1}{2}D_{KL} (P||M) + \frac{1}{2}D_{KL} (Q||M) 
$$
$$
M = \frac{1}{2}(P+Q)
$$
- 0以上1以下
- 平滑性
- 対称性 
  $$ D_{JS}(P|| Q) = D_{JS} (Q || P)$$
- 有界性