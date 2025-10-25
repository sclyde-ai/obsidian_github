$$
(a+ b)^n = \sum_{i = 0}^n \frac{n!}{k!(n-k)!}a^kb^{n-k}
$$
- proof
    by mathematical induction
    - base case (n = 0)
        $$
        (a+b)^0 = 1
        $$
    - inductive step (n = m)
        $$
        (a+ b)^n = \sum_{k= 0}^n \binom n k a^k b^{n-k} = \sum_{i = 0}^n \frac{n!}{k!(n-k)!}a^kb^{n-k}
        $$
        assume that statement is true for some integer n > 0
        $$
        (a + b) ^{n+1} = (a+b)(a+b)^n \\
        = (a+b) \sum_{k= 0}^n \binom n k a^k b^{n-k}\\
        = a \sum_{k = 0}^n \binom n k a^k b^{n-k}+ b \sum_{k = 0}^n \binom n ka^kb^{n-k} \\
        = \sum_{k = 0}^n \binom n k a^{k+1}b^{n-k} + \sum_{k = 0}^n \binom n k a^kb^{n+1-k} 
        \\
        = \sum_{k = 1}^{n+1} \binom n {k-1} a^kb^{n+1-k} + \sum_{k = 0}^n \binom n k a^kb^{n+1-k} 
        \\ 
        = \binom n n a^{n+1} b^0 + \sum_{k = 1}^{n} \binom n {k-1} a^kb^{n+1-k} + \sum_{k = 1}^n \binom n k a^kb^{n+1-k} + \binom n 0 a^0 b^{n+1} 
        \\
        = a^{n+1} + \sum_{k = 1}^{n} (\binom n {k-1} + \binom n k ) a^kb^{n+1-k} + b^{n+1}
        $$
        - \binom n {k-1} + \binom n k
            $$
            \binom n {k-1} + \binom n k \\
            = \frac{n!}{(n-k+1)!(k-1)!} + \frac{n!}{(n-k)!k!} 
            \\
            = \left(\frac{1}{n-k+1} + \frac{1}{k} \right) \frac{n!}{(n-k)!(k-1)!} 
            \\
            = \frac{n+1}{(n-k+1)k} \frac{n!}{(n-k)!(k-1)!} 
            \\
            = \frac{(n+1)!}{(n+1-k)!k!} 
            \\
            = \binom {n+1} k
            $$
        $$
        a^{n+1}+ b^{n+1} + \sum_{k = 1}^{n} \binom {n+1} k a^kb^{n+1-k} \\
        = \binom {n+1}{n+1} a^{n+1} + \binom {n+1} 0 b^{n+1} + \sum_{k = 1}^{n} \binom {n+1} k a^kb^{n+1-k}
        \\
        = \sum_{k = 0}^{n+1} \binom {n+1} k a^kb^{n+1-k}
        $$