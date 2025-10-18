- vector space X, Y
$$ \exist A \subset X, T : A \to Y $$
then, T is called linear operator
- difference between linear map and linear operator
    linear operator : the subset of X is the domain
    linear map : whole X is the domain
- example
    - differential operator
- 有界線形作用素 bounded linear operator
    - domain
        $$ D(T) = X
        $$
    - bounded
        $$ \|Tx\| \leq M\|x\| \ (x \in X) $$
    - equivalence
        1. upper bounded
            $$ \exist M > 0, \|Tx\| \leq M \|x\| $$
        2. upper continuous
            $$ \{x_n\}\subset D(T), x \in D(T), x_n \to x \Rightarrow Tx_n \to Tx $$
        3. continuous
            $$ \{x_n\}\subset D(T), x_n \to y \Rightarrow Tx_n \to Ty $$
        - proof
            - 1 → 2
            - 2 → 1
            - 2 → 3
            - 3 → 2