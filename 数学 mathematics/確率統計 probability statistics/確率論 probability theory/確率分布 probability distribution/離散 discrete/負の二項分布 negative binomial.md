$$ NB(k, p) = \binom{x+r-1}{k} p^r(1-p)^k $$
- meaning
    k回成功までの失敗回数
- expectation
    $$ \sum_{x = 1}^\infty x \binom{x+k-1}{x} p^k(1-p)^x \\ = p^k \sum_{x = 1}^\infty x \frac{(x+k-1)!}{x!(k-1)!}(1-p)^x $$
- 幾何分布の和
    負の二項分布は幾何分布の和で表すことが可能
    - Xは負の二項分布に従う確率変数
    - Yは幾何分布に従う確率変数
    $$ X = \sum_{k = 1}^n Y_k $$