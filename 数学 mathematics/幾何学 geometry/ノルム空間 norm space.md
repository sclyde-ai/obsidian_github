---
alias:
    ['ノルム空間', 'norm space']
---
- vector space V on K
- norm $V \rightarrow \R$
    - 正値
        $$
        \| x \| > 0
        $$
    - 零
        $$
        \| x \| = 0 \Leftrightarrow x = 0
        $$
    - 斉次性
        $$
        \|kx\| = |k| \|x\|
        $$
    - 三角不等式
        $$
        \| x+y \| \leq \|x\| + \|y\|
        $$
- theorem
- example
    - $L^p$ norm
        $$
        \|x \|_p = \sqrt[p]{\sum x_i^p}
        $$
    - $L^1$ norm
        $$
        \|x \|_1 = \sum |x_i|
        $$
    - $L^2$  norm
        $$
        \|x \|_2 = \sqrt[2]{\sum x_i^2}
        $$
    - $L^\infty$ norm
        $$
        \|x \|_\infty = \sqrt[\infty]{\sum x_i^\infty} = \max(|x_1|, ...)
        $$