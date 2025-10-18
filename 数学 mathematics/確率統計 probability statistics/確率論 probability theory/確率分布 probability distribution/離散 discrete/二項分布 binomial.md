$$ Bin(n, p) = \binom{n}{k} \ p^k(1-p)^{n-k} $$
- meaning
    n回Bernoulli試行の成功回数
- moment
    - expectation
        $$ \mathbb E[X] = \int x \binom{n}{x} \ p^x(1-p)^{n-x}dx \\ = \sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = \sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = np\sum_{k = 0}^n \frac{(n-1)!}{(k-1)!(n-k)!} \ p^{k-1}(1-p)^{n-k} \\ = np $$
    - variance
        $$ \mathbb E[X^2] = \int x \binom{n}{x} \ p^x(1-p)^{n-x}dx \\ = \sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = \sum_{k = 0}^n (k(k-1)+k)\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = \sum_{k = 0}^n k(k-1)\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} +\sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = n(n-1)p^2\sum_{k = 0}^n \frac{(n-2)!}{(k-2)!(n-k)!} \ p^{k-2}(1-p)^{n-k} +\sum_{k = 0}^n \frac{(n-1)!}{(k-1)!(n-k)!} \ p^{k-1}(1-p)^{n-k} \\ = n(n-1)p^2 + np $$
        $$ Var(X) = n(n-1)p^2 + np -(np)^2 \\ = np - np^2 \\ = np(1-p) $$
- 正規近似
- 再生性