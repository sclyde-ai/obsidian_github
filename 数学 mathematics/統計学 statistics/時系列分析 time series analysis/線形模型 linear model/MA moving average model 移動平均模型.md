
        過去の誤差が現在の値に影響
        - white noise $\epsilon_t$
        $$
        y_t= \mu + \epsilon_t + \sum_{k=1}^q \theta_k\epsilon_{t-k}
        $$
        - 期待値
            $$
            \mathbb E [\hat y_t] = \mu
            $$
        - 分散
            $$
            (1+ \theta_1^2 + ...+ \theta_q^2)\sigma^2
            $$