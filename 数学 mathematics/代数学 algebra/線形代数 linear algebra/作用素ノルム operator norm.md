$$ \|A\|_p = \max_{\vec x \ne 0} \frac{\|A\vec x\|_p}{\|\vec x\|_p} = \max_{\|\vec x\|_p = 1} \|A\vec x\|_p $$
vector x に行列 Aをかけると、norm が何倍になるか
- p = 1
    列ごとの成分の合計の最大値
- p = 2 (spectral norm)
- p = $\infin$
    行ごとの成分の合計の最大値
- theorem
    $$ A = A^\top \\ \max | v^\top A v ｜= \|A\| $$
    $$ |v^\top A v | \leq \|v\| \|Av\| \leq \|v\| \|A\| \|v\| = \|A\| \|v\|^2 = \|A\| $$