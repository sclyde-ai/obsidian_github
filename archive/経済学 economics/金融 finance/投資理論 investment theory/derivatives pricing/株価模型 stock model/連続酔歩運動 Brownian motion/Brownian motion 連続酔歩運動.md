---
alias:
    ['Brownian motion', '連続酔歩運動']
---
- probability space
- def 定義
    - initial condition 初期値
        $$
        W_0= 0
        $$
    - independent increment 独立増分
        $$
        \forall s_1,t_1,s_2,t_2 \in T, \\ 
        s_1 \leq t_1 \leq s_2 \leq t_2 \Rightarrow \\ \mathbb P[X_{t_1}-X_{s_1} \cap X_{t_2}-X_{s_2}] = \mathbb P[X_{t_1}-X_{s_1}] \mathbb P[X_{t_2}-X_{s_2}]
        $$
        the increments are independent on each other 
    - normal/gaussian increment 正規増分
        $$
        \forall s,t \in T, X_t - X_s \sim N(0, t-s)
        $$
        Each of these increments is normally distributed 
    - alternative characterization of Brownian motion
- increment 増分
    $$
    W_{t_1}-W_{t_0}\\
    W_{t_2}-W_{t_1}\\ 
    ..., W_{t_m}-W_{t_{m-1}} \\
    t_0 < t_1 < ... < t_m
    $$
    is independent and normally distributed
    - expectation
        $$
        \mathbb E[W_{t_{i+1}}-W_{t_i}] = 0 
        $$
    - variance
        $$
        Var[W_{t_{i+1}}-W_{t_i}] = t_{i+1}-t_i
        $$
- filtration
    - information accumulates
        $$
        \forall s, t \in T, s < t \Rightarrow \mathcal F_s \subset \mathcal F_t
        $$
    - adaptivity
        Brownian motion W_t at the time t is F_t-measurable
        $$
        \{\omega \in \Omega: W_t(\omega) \in B, \forall B \in \mathcal B(\R)\} \in \mathcal F(t)
        $$
    - independence future increments
        the increment W_t - W_s is independent of F_t
        $$
        \forall F \in \mathcal F_t
        $$
        F and W_t - W_s are independent 
- property 性質
    - martingale
        $$
        \mathbb E[W_t|\mathcal F_s] = W_s, \forall s, t \in T
        $$
        almost surely
        - proof
            $$
            \mathbb E[W_t|\mathcal F_s] \\ 
            = \mathbb E[W_s + (W_t-W_s)|\mathcal F_s] \\ 
            = \mathbb E[W_s| \mathcal F_s] + \mathbb E[(W_t-W_s)|\mathcal F_s] \\
             =W_s + 0
            $$
    - Markov property
        - Borel measurable func f, g
        $$
        \mathbb E[f(W_t)|\mathcal F_s] = g(W_t)
        $$
        - proof
            $$
            \mathbb E[f(W_t)|\mathcal F_s] =
            \mathbb E[f(W_t - W_s) + W_s|\mathcal F_s] =
            $$
    - not differential
        $$
        W(t+h) - W(t) \sim N(0, h)
        $$
        $$
        \frac{W(t+h)-W(t)}{h} = \frac{\sqrt h Z}{h} = \frac{Z}{\sqrt h}
        $$
    - fractal
        - self-similarity
            $$
            W(ct) \stackrel{\mathrm{d}}{=} \sqrt c W(t)
            $$
        - holder continuity
            $$
            |W_t-W_s| \leq C|t-s|^\alpha
            $$
- moment 積率
    - the moment-generating function
    - expectation 期待値
        $$
        \mathbb E[X_t] = 0
        $$
        - proof
            $$
            X_t = X_t -X_0 \sim N(0, t-0) = N(0, t) \\ \Rightarrow \mathbb E[X_t] = 0
            $$
    - variance 分散
        $$
        \mathbb E[(X_t-\mu)^2] = t
        $$
        - proof
            $$
            X_t = X_t -X_0 \sim N(0, t-0) = N(0, t) \\ \Rightarrow \mathbb E[X_t^2] = t
            $$
    - covariance 共分散
        $$
        Cov(W_s, W_t) = \mathbb E[W_sW_t] = \min(s, t)
        $$
        - proof
            $$
            \mathbb E[W_sW_t] \\
            = \mathbb E[W_s(W_s+W_t-W_s)] \\
            = \mathbb E[W_s^2] + \mathbb [W_s(W_t-W_s)] \\ 
            = s
            $$
        - covariance matrix
            $$
            \bm{\Sigma} = \mathbb{E}\left[\begin{pmatrix}(X_1 - \mathbb{E}[X_1])^2 & (X_1 - \mathbb{E}[X_1])(X_2 - \mathbb{E}[X_2]) & \cdots & (X_1 - \mathbb{E}[X_1])(X_n - \mathbb{E}[X_n]) \\(X_2 - \mathbb{E}[X_2])(X_1 - \mathbb{E}[X_1]) & (X_2 - \mathbb{E}[X_2])^2 & \cdots & (X_2 - \mathbb{E}[X_2])(X_n - \mathbb{E}[X_n]) \\\vdots & \vdots & \ddots & \vdots \\(X_n - \mathbb{E}[X_n])(X_1 - \mathbb{E}[X_1]) & (X_n - \mathbb{E}[X_n])(X_2 - \mathbb{E}[X_2]) & \cdots & (X_n - \mathbb{E}[X_n])^2\end{pmatrix}\right]
            $$
- quadratic variation
    $$
    [W, W](T) = T
    $$
    - proof
        $$
        Q_\Pi = \sum_{j=0}^{n-1}(W(t_{j+1}) - W(t_j))^2
        $$
        $$
        \mathbb E[(W(t_{j+1})-W(t_j))^2] = Var [W(t_{j+1})-W(t_j)] = t_{j+1} - t_j
        $$
        $$
        \mathbb E[Q_\Pi] = \sum_{j=0}^{n-1}\mathbb E[(W(t_{j+1})-W(t_j))^2] = \sum_{j=0}^{n-1} t_{j+1} - t_j = T
        $$
        $$
        Var[]
        $$