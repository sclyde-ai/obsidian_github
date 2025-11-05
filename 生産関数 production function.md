---
alias:
    ['生産関数', 'production function']
---
    $$
    Y = AK^\alpha L^\beta
    $$
    - Y : 生産量
    - K : 資本
    - L : 労働
    - A : 全要素生産性
    - \alpha : 資本分配率
    - \beta : 労働分配率
    - 規模の収穫
        - 規模に対して収穫一定 $$\alpha + \beta = 1$$
        - 規模に対して収穫逓増 $$\alpha + \beta > 1$$
        - 規模に対して収穫逓減 $$\alpha + \beta < 1$$
    - 限界生産性 marginal product
	    - 資本の限界生産性 MPK marginal product of capital $$ MPK = \frac{\partial Y}{\partial K} = \frac{\partial}{\partial K} AK^\alpha L^\beta = \alpha AK^{\alpha-1} L^\beta = \alpha \frac{Y}{K} $$
	    - 労働の限界生産性 MPL marginal product of labor $$ MPL = \frac{\partial Y}{\partial L} = \frac{\partial}{\partial L} AK^\alpha L^\beta = \beta AK^{\alpha} L^{\beta-1} = \beta \frac{Y}{L} $$
	- 最適化
		- 制約条件$$ rL + wL = I $$
		- Lagrange $$ L=\alpha YK \Delta K+(1−α)YLΔL+λ(ΔI−rΔK−wΔL)\mathcal{L} = \alpha \frac{Y}{K} \Delta K + \beta \frac{Y}{L} \Delta L + \lambda \left( \Delta I - r \Delta K - w \Delta L \right)L=αKY​ΔK+(1−α)LY​ΔL+λ(ΔI−rΔK−wΔL)$$