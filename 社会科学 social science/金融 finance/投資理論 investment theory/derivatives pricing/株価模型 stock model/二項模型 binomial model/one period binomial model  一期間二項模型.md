- def
    - probability space
        $$
        \Omega = \{H, T\} \\
        \mathcal F = \{\phi, \{H\}, \{T\}, \Omega\} \\
        P = 
        \left\{ 
          \begin{alignedat}{}   
           & 0 & & \phi,\Omega\\   
           & p & & \{H\} \\ 
           & 1-p & & \{T\}
          \end{alignedat} 
         \right.
        $$
    - stock(random variable)
        $$
        S_1(\omega)= 
        \left\{ 
          \begin{alignedat}{}   
           & S_0 & & \phi, \Omega \\   
           & uS_0 & & \{H\} \\ 
           & dS_0 & & \{T\}
          \end{alignedat} 
         \right.
        \\ u\geq d
        $$
        $u$ : up factor
        $d$ : down factor
- martingale
    - safety asset
        $$
        A_1 = (1+r)A_0 = RA_0
        $$
        $r$  : interest rate
    - discount factor
        $$
        D = \frac{1}{(1+r)}
        $$
    - martingale
        $$
        S_0 = D(\tilde pS_1(H)+ (1-\tilde p)S_1(T))
        $$
- arbitrage
    - arbitrage
        $$
        u > 1+r\land d \geq 1+r \\
        \lor \\
        u \geq 1+r \land d > 1+r \\
        \lor \\
        u < 1+r\land d \leq 1+r \\
        \lor \\
        u \leq 1+r \land d < 1+r
        $$
        - how to derive
            - buy side
                $$
                (1)\ \ P(DS_1 \geq S_0) = 1 \\
                (2)\ \ P(DS_1 > S_0) > 0
                $$
                $$
                (1)\ \ \forall \omega \in \Omega, DS_1(\omega) \geq S_0 \\
                (2)\ \ \exist \omega \in \Omega, DS_1(\omega) > S_0
                $$
                - (1)
                    $$
                    \forall \omega \in \Omega, \frac{1}{1+r}S_1(\omega) \geq S_0\\
                    uS_0 \geq (1+r) S_0 \\
                    dS_0 \geq (1+r) S_0 \\
                    u \geq 1+r \\
                    d \geq 1+r \\
                    u \geq 1+r \land d \geq 1+r
                    $$
                - (2)
                    $$
                    \exist \omega \in \Omega, \frac{1}{1+r}S_1(\omega) > S_0\\
                    uS_0 > (1+r) S_0 \\
                    dS_0 > (1+r) S_0 \\
                    u > 1+r \\
                    d > 1+r \\
                    u > 1+r \lor d > 1+r
                    $$
                1と2より
                $$
                u \geq 1+r\land d \geq 1+r \\
                \land \\
                u > 1+r \lor d > 1+r
                $$
                分配法則より
                $$
                u > 1+r\land d \geq 1+r \\
                \lor \\
                u \geq 1+r \land d > 1+r
                $$
            - sell side
                $$
                (1)\ \ P(DS_1 \leq S_0) = 1 \\
                (2)\ \ P(DS_1 < S_0) > 0 
                $$
                $$
                (1)\ \ \forall \omega \in \Omega, DS_1(\omega) \leq S_0 \\
                (2)\ \ \exist \omega \in \Omega, DS_1(\omega) < S_0
                $$
                - (1)
                    $$
                    \forall \omega \in \Omega, \frac{1}{1+r}S_1(\omega) \leq S_0\\
                    uS_0 \leq (1+r) S_0 \\
                    dS_0 \leq (1+r) S_0 \\
                    u \leq 1+r \\
                    d \leq 1+r \\
                    u \leq 1+r \land d \leq 1+r
                    $$
                - (2)
                    $$
                    \exist \omega \in \Omega, \frac{1}{1+r}S_1(\omega) < S_0\\
                    uS_0 < (1+r) S_0 \\
                    dS_0 < (1+r) S_0 \\
                    u < 1+r \\
                    d < 1+r \\
                    u < 1+r \lor d > 1+r
                    $$
                1と2より
                $$
                u \leq 1+r\land d \leq 1+r \\
                \land \\
                u < 1+r \lor d < 1+r
                $$
                分配法則より
                $$
                u < 1+r\land d \leq 1+r \\
                \lor \\
                u \leq 1+r \land d < 1+r
                $$
    - risk neutral probability
        $$
        \tilde {\mathbb P} = 
        \left\{ 
          \begin{alignedat}{}   
           & 0 & & \phi, \Omega\\   
           & \frac{(1+r)-d}{u-d} & & \{H\} \\ 
           & \frac{u - (1+r)}{u-d } & & \{T\}
          \end{alignedat} 
         \right.
        $$
        - how to derive
            $$
            \tilde {\mathbb P} = 
            \left\{ 
              \begin{alignedat}{}   
               & 0 & & \phi , \Omega\\   
               & \tilde p & & \{H\} \\ 
               & \tilde q& & \{T\}
              \end{alignedat} 
             \right.
            \\
            \tilde p + \tilde q = 1
            $$
            - equivalent
                $$
                P(\phi) = 0, P(\Omega) = 0 \\
                \tilde P(\phi) = 0, \tilde P (\Omega) = 0
                $$
            - martingale
                $$
                \mathbb E_Q[DS_1] = S_0 \\
                \frac{1}{1+r}(uS_0 \tilde p+ dS_0(1-\tilde p)) = S_0
                \\
                \frac{(u-d) \tilde p+ d}{1+r} S_0 = S_0\\
                (u-d)\tilde p + d = 1+r \\
                \tilde p = \frac{1+r-d}{u-d}
                $$
    - FTAP fundamental theorem of asset pricing
        - FTAP 1
            - non-arbitrage
                $$
                \lnot [u > 1+r\land d \geq 1+r \\
                \lor \\
                u \geq 1+r \land d > 1+r \\
                \lor \\
                u < 1+r\land d \leq 1+r \\
                \lor \\
                u \leq 1+r \land d < 1+r]
                $$
                De Morgan’s lawより
                $$
                u \leq 1+r \lor d < 1+r \\
                \land \\
                u < 1+r \lor d \leq 1+r \\
                \land \\
                u \geq 1+r \lor d > 1+r \\
                \land \\
                u > 1+r \lor d \geq 1+r
                $$
                分配律より
                $$
                (u < 1+r \lor d \leq u < 1+r \\
                \lor \\
                d \leq u \leq 1+r \lor d < 1+r)
                \\ \land \\
                (u > 1+r \lor d \geq u > 1+r \\
                \lor \\
                d \geq u \geq 1+r \lor d > 1+r)
                $$
                論理和と含意の関係より
                $$
                (u < 1+r 
                \lor 
                d \leq u \leq 1+r
                \lor 
                d < 1+r)
                \\ \land \\
                (u > 1+r 
                \lor 
                d \geq u \geq 1+r 
                \lor 
                d > 1+r)
                $$
                分配律より
                $$
                d < 1+r < u \\
                \lor \\
                u < 1+r < d
                $$
                初期条件より
                $$
                d < 1+r < u
                $$
            - risk neutral probability exists
                $$
                0 \leq \frac{(1+r)-d}{u-d} \leq 1 \\ \land \\
                0 \leq \frac{u-(1+r)}{u-d} \leq 1
                $$
                $$
                1+r \leq u \land d \leq 1+r \\
                d \leq 1+r \leq u
                $$
        - FTAP 2
            - assets
                - stock
                    price $S_0$
                    future value $uS_0\ or\ dS_0$
                - risk-free asset
                    price $S_0$
                    future value $(1+r)S_0$
            - states
                $$
                \omega = H\ or \ T
                $$
- option
    $$
    V_1(\omega)= 
    \left\{ 
      \begin{alignedat}{}   
       & V_0 & & \phi, \Omega \\   
       & (S_1(H) - K)^+ & & \{H\} \\ 
       & (S_1(T) - K)^+  & & \{T\}
      \end{alignedat} 
     \right.
    \\ u\geq d
    $$
    - wealth equation
        $$
        X_1 - \Delta_0 S_1 = (1+r)(X_0 - \Delta_0 S_0)
        $$
    - delta hedge formula
        $$
        \Delta_0 = \frac{V_1(H)- V_1(T)}{S_1(H) - S_1(T)} = \frac{V_1(H)- V_1(T)}{(u-d)S_0} 
        $$
    - option price
        $$
        V_0 = X_0 = \frac{1}{1+r}(\tilde p V_1(H) + \tilde qV_1(T))
        $$
    - stock price
        $$
        S_0 = \frac{1}{1+r}(\tilde p S_1(H) + \tilde qS_1(T))
        $$