- 直近の上下動の回数に比例して上か下かの確率が変動するmodel
- probability space
    - event space
        $$
        \Omega = \{H, T\}^N=\{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{1,2,...,N\}\}
        $$
    - filtration
        $$
        \mathcal F_0 = \{\phi, \Omega\}\\
        \mathcal F_2= \{\phi, H\{H, T\}^{N-1}, T\{H, T\}^{N-1}, \Omega\} \\
        \mathcal F_1 = \{\phi, 
        HT\{H, T\}^{N-2}, HT\{H, T\}^{N-2}, TH\{H, T\}^{N-2}, TT\{H, T\}^{N-2}, \Omega\}
        \\ \vdots \\
        \mathcal F_n =\{ \phi, 
        \{\omega_1\omega_2...\omega_n\{H, T\}^{N-n}| w_i \in \{H, T\}, \forall i \in \{1,2,...,n\}\}, \Omega\}
        $$
        $$
        \omega_n =\omega_1\omega_2...\omega_n = \omega_1\omega_2...\omega_n\{H, T\}^{N-n} = \{\omega_1\omega_2...\omega_N | w_i \in \{H, T\}, \forall i \in \{n+1,n+2,...,N\}\}
        $$
    - probability measure
        $$
        P_n(\omega_n) =  p^{H_n}q^{T_n} \\
        n = H_n + T_n
        $$
$$
S_n(\omega_1\omega_2...\omega_n\{H, T\}^{N-n}) = S_0 u^{H_n}d^{T_n} \\
n = H_n + T_n
$$
$$
p = f(\omega_1\omega_2...\omega_n) \\
q = f^{-1}(\omega_1\omega_2...\omega_n)\\
p+q=1
$$