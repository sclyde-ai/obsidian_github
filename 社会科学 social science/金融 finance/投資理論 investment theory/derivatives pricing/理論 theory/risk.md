- VaR value at risk
    $$
    VaR_\alpha(X) = -\inf\{x\in \R | F_X(x)>\alpha\} \\ = F_Y^{-1}(1-\alpha)
    $$
    $\alpha$ : risk
    ![image.png](image.png)
    - 欠点
        1. riskの過小評価
        2. riskの方向性なし
        3. 絶対値でない
        4. 
- expected shortfall
    $$
    ES_\alpha(X)=\frac{1}{\alpha}\int_0^\alpha VaR_\gamma (X)d\gamma \\
    = -\frac{1}{\alpha}(\mathbb E[X 1_{X \leq x_\alpha}]+x_\alpha(\alpha-P[X \leq x_\alpha]))
    $$
    $$
    x_\alpha = -VaR_\alpha(X) \\ = \inf\{x \in \R:P(X \leq x) \geq \alpha\}
    $$
    ![image.png](image%201.png)
- risk/reward ratio