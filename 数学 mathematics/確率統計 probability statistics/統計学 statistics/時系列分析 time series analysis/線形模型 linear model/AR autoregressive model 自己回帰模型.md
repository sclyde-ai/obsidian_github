---
alias:
    ['AR', 'autoregressive model', '自己回帰模型']
---
過去の値が現在の値に影響
- white noise $\epsilon_t$
$$
y_t = c + \sum_{k=1}^p \phi_k y_{t-k} + \epsilon_t
$$
- 期待値
    $$
    \mathbb E[\hat y_t] = \frac{c}{1 - \sum_{i = 1}^p \phi_i}
    $$
- 分散
    $$
    var (\hat y_t) = \frac{\sigma^2}{1 - \sum_{i = 1}^p \phi_i \rho_i}
    $$
- 定常性条件
    $$
    1 -\sum^p_{i=1} \phi_i z^i = 0
    $$