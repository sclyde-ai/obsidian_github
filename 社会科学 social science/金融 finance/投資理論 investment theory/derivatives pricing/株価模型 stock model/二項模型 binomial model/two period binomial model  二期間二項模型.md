---
alias:
    ['two period binomial model', '二期間二項模型']
---
$$
S_1(\omega_1\omega_2)= 
\left\{ 
  \begin{alignedat}{}   
   & S_0 & & \phi, \Omega \\   
   & uS_0 & & \{HH, HT\} \\ 
   & dS_0 & & \{TH, TT\}
  \end{alignedat} 
 \right. \\
S_2(\omega_1\omega_2)=
\left\{ 
  \begin{alignedat}{}   
   & S_0 & & \phi, \Omega \\   
   & u^2 S_0& & \{HH\} \\ 
   & ud S_0& & \{HT\}, \{TH\} \\ 
   & d^2 S_0& & \{TT\}
  \end{alignedat} 
 \right. 
\\ where \ u\geq d
$$
- probability space
    $$
    \Omega = \{HH,HT, TH, TT\} \\
    $$
    $$
    \mathcal F_0 = \{\phi, \Omega\}\\
    \mathcal F_1 = \{\phi, \{HH, HT\}, \{TH, TT\}, \Omega\} \\
    \mathcal F_2 = \{\phi, \{HH\},\{ HT\}, \{TH\}, \{TT\}, \Omega\} 
    $$
    $$
    P_1 = 
    \left\{ 
      \begin{alignedat}{}   
       & 0 & & \phi, \Omega \\   
       & p & & \{HH, HT\} \\ 
       & q & & \{TH, TT\}
      \end{alignedat} 
     \right. \\
    P_2 = 
    \left\{ 
      \begin{alignedat}{}   
       & 0 & & \phi, \Omega \\   
       & p^2 & & \{HH\} \\ 
       & pq & & \{HT\}, \{TH\} \\ 
       & q^2 & & \{TT\}
      \end{alignedat} 
     \right. \\
    where\ p+q=1
    $$
- discount price
    $$
    D_1 = \frac{1}{(1+r)} \\
    D_2 = \frac{1}{(1+r)^2}
    $$
- risk neutral probability
    $$
    \tilde P_1 = 
    \left\{ 
      \begin{alignedat}{}   
       & 0 & & \phi, \Omega \\   
       & \tilde p & & \{HH, HT\} \\ 
       & \tilde q & & \{TH, TT\}
      \end{alignedat} 
     \right. \\
    \tilde P_2 = 
    \left\{ 
      \begin{alignedat}{}   
       & 0 & & \phi, \Omega \\   
       & \tilde p^2 & & \{HH\} \\ 
       & \tilde p \tilde q & & \{HT\}, \{TH\} \\ 
       & \tilde q^2 & & \{TT\}
      \end{alignedat} 
     \right. \\
    \tilde p = \frac{(1+r)-d}{u-d} \\
    \tilde q = \frac{u - (1+r)}{u-d}
    $$
    - how to derive
        $$
        \tilde P = 
        \left\{ 
          \begin{alignedat}{}   
           & 0 & & \phi , \Omega\\   
           & \tilde p & & \{H\} \\ 
           & 1-\tilde p& & \{T\}
          \end{alignedat} 
         \right.
        \\
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