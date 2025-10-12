- 全順序体 T
- 位相空間 (X, O)
$$
f : T\times X \to X \\
f(0, x) = x, \forall x \in X\\
f(s, f(t,x))=f(s+t, x), \forall x \in X, \forall s, t \in T
$$
- 離散力学系
    $$
    f: X \to X \\
    x_{n+1} = f(x_n)
    $$
    - 固定点
        $$
        x^* = f(x^*)
        $$
    - 周期点
        $$
        x^* = f^k(x^*)
        $$
    - mandelbrot set
    - julia set
- 連続力学系
- ergodicity
- chaos theory
- Langton’s Ant
    - definition of the grid
    - 
        $$
        C(x, y, t) \in \{0, 1\}
        $$
    - The ant’s state
        $$
        d(t) \in \{0, 1, 2, 3\}
        $$
    - Update rules
        - check the current cell’s color
            $$
            c = C(x(t), y(t), t)
            $$
        - flip the cell’s color
            $$
            C(x(t), y(t), t+1) = 1-c
            $$
        - turn based on the cell’s color
            - if c=0 (white), turn 90 right
                $$
                d(t+1) =d(t)+1 \mod 4
                $$
            - if c=1 (black), turn 90 left
                $$
                d(t+1) =d(t)-1 \mod 4
                $$
            - move forward one cell
                $$
                (x(t+1), y(t+1)) = 
                \left\{
                \begin{matrix}
                (x(t), y(t)+1) & if & d(t+1)=0 \\
                (x(t)+1, y(t)) & if & d(t+1)=1 \\
                (x(t), y(t)-1) & if & d(t+1)=2 \\
                (x(t)-1, y(t)) & if & d(t+1)=3 
                \end{matrix}
                \right.
                $$
        - move forward one cell
    - initial conditions
    - 