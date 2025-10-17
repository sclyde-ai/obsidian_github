- Ito integral
    - simple process
        - partition
            $$ \Pi = \{t_0, t_1, ..., t_n\}\\ 0 = t_0 \leq t_1 \leq ... \leq t_n =T $$
            - subinterval
                $$ [t_j, t_{j+1}) $$
        $$ \Delta_t = c, \forall t \in [t_j, t_{j+1}) $$
    $$ I_t = \int_0^t \Delta_udW_u \\ = \sum_{j=0}^{k-1}\Delta_{t_j}[W_{t_{j+1}} - W_{t_j}] + \Delta_{t_k}[W_t - W_{t_k}] \\ t_k\leq t \leq t_{k+1} $$
    - property
        - martingale
            $$ \mathbb E[I_t | \mathcal F_s] = I_s $$
            - proof
                - variables
                    - $0 \leq s \leq t \leq T$
                    - $t_l \leq t_k$
                    - $s \in [t_l, t_{l+1})$
                    - $t \in [t_k, t_{k+1})$
                $$ I_t = \sum_{j=0}^{l-1}\Delta_{j}(W_{t_{j+1}} - W_{t_j}) + \Delta_{t_l}(W_{t_{l+1}} - W_{t_l}) + \sum_{j=l+1}^{k-1}\Delta_{j}(W_{t_{j+1}} - W_{t_j}) + \Delta_{t_k}(W_t - W_{t_k}) $$
                - first summand
                    $$ \sum_{j=0}^{l-1}\Delta_{j}(W_{t_{j+1}} - W_{t_j}) $$
                    - expectation
                        - $0 \leq t_l \leq s$
                        $$ \mathbb E[\sum_{j=0}^{l-1}\Delta_{j}(W_{t_{j+1}} - W_{t_j}) | \mathcal F_s] = \sum_{j=0}^{l-1}\Delta_{j}(W_{t_{j+1}} - W_{t_j}) $$
                - second summand
                    $$ \Delta_{t_l}(W_{t_{l+1}} - W_{t_l}) $$
                    - expectation
                        $$ \mathbb E[\Delta_{t_l}(W_{t_{l+1}} - W_{t_l})| \mathcal F_s] \\ = \Delta_{t_l}\mathbb E[(W_{t_{l+1}} - W_{t_l})| \mathcal F_s] \\ = \Delta_{t_l}(\mathbb E[W_{t_{l+1}} | \mathcal F_s]- \mathbb E[W_{t_l}| \mathcal F_s]) \\ = \Delta_{t_l}(W_s - W_{t_l}) $$
                - third summand
                    $$ \sum_{j=l+1}^{k-1}\Delta_{j}(W_{t_{j+1}} - W_{t_j}) $$
                    - expectation
                        - $s \leq t_{l+1} \leq t_j$
                        $$ \mathbb E[\Delta_{j}(W_{t_{j+1}} - W_{t_j}) | \mathcal F_s] \\ = \mathbb E[\mathbb E[\Delta_{j}(W_{t_{j+1}} - W_{t_j}) | \mathcal F_{t_j}]| \mathcal F_s] \\ = \mathbb E[\Delta_{j}\mathbb E[W_{t_{j+1}} - W_{t_j}] | \mathcal F_{t_j}]| \mathcal F_s] \\ = \mathbb E[\Delta_{j}(\mathbb E[W_{t_{j+1}}| \mathcal F_{t_j}] - \mathbb E[W_{t_j} | \mathcal F_{t_j}])| \mathcal F_s] \\ = \mathbb E[\Delta_{j}(W_{t_j} - W_{t_j})| \mathcal F_s] \\ = 0 $$
                - fourth summand
                    $$ \Delta_{t_k}(W_t - W_{t_k}) $$
                    - expectation
                        $$ \mathbb E[\Delta_k (W_t - W_{t_k}) | \mathcal F_s] \\ = \mathbb E[\mathbb E[\Delta_k(W_t - W_{t_k}) | \mathcal F_{t_k}]| \mathcal F_s] \\ = \mathbb E[\Delta_k \mathbb E[W_t - W_{t_k}] | \mathcal F_{t_k}]| \mathcal F_s] \\ = \mathbb E[\Delta_k(\mathbb E[W_t | \mathcal F_{t_k}] - \mathbb E[W_{t_k} | \mathcal F_{t_k}])| \mathcal F_s] \\ = \mathbb E[\Delta_k(W_{t_k} - W_{t_k})| \mathcal F_s] \\ = 0 $$
        - isometry
            $$ \mathbb E[I_t^2] = \mathbb E [\int_0^t \Delta^2_u du] $$
            - proof
                $$ D_j = W_{j+1} - W_j $$
                $$ \mathbb E[I_t^2] = \mathbb E[ \sum_{i = 0}^k\sum_{j = 0}^k \Delta_{t_i} \Delta_{t_j}D_i D_j] \\ = \mathbb E[\sum_{j=0}^k\Delta^2_{t_j} D_j^2 + 2 \sum_{0 \leq i \leq j \leq k} \Delta_{t_i} \Delta_{t_j}D_i D_j] \\ = \sum_{j=0}^k \mathbb E[\Delta^2_{t_j} D_j^2] + 2 \sum_{0 \leq i \leq j \leq k} \mathbb E [\Delta_{t_i} \Delta_{t_j}D_i D_j] $$
                - i \ne j
                    $$ \mathbb E[\Delta_{t_i} \Delta_{t_j}D_i D_j ] = $$
        - quadratic variation
            $$ [I, I](t) = \int_0^t \Delta^2_u du $$
    - differential form
        $$ d I_t = \Delta_t d W_t $$
    - integral form
        $$ I_t = I_0 + \int_0^t\Delta_u dW_u $$
    - square differential
        $$ d I_t dI_t = \Delta^2_t d W_t dW_t = \Delta^2_t dt $$
- Ito integral (limit)
    $$ \int_0^t \Delta_u d W_u = \lim_{n \to \infin} \int_0^t \Delta_{u, n} d W_u $$
    - theorem
        - an adapted stochastic process
        - integrability
        - continuity
        - adaptivity
        - linearity
        - martingale
        - ito isometry
        - quadratic variation
- Ito-Doeblin formula
    - differential form
        $$ df(W_t) = f'(W_t) dW_t + \frac{1}{2} f''(W_t) dt $$
        - ordinary calculus
            $$ \frac{d}{dt} f(W_t) = f'(W_t) W_t' \\ df(W_t) = f'(W_t) dW_t $$
    - integral form
        $$ f(W_t) - f(W_0) = \int_0^t f'(W_u) dW_u + \frac{1}{2} \int_0^t f''(W_u) du $$
    - brownian motion
    - Ito process