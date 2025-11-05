---
alias:
    ['量子計算', 'quantum computing']
---
- bra & ket
- 量子単位 qubi/quantum bit
    $$ \alpha \ket 0 + \beta \ket 1 \\ \alpha, \beta \in \mathbb C $$
    - 計算基底
        $$ \ket 0, \ket 1 $$
    - 確率振幅 amplitude
        $$ \alpha, \beta \\ \alpha^2 + \beta^2 = 1 $$
    - 同値関係
        $$ \alpha \ket 0 + \beta \ket 1 \sim e^{i\theta}(\alpha \ket 0 + \beta \ket 1) $$
    上記の条件を満たす \alpha, \betaを量子単位という
    - 制約条件が2つなので自由度は4-2=2個
    - Bloch ball
        $$ e^{-i\phi/2} \cos \frac{\theta}{2}\ket 0 + e^{i\phi/2} \cos \frac{\theta}{2}\ket 1 $$
    - 2量子単位 2 qubit
        $$ \alpha \ket {00}+ \beta \ket {01} + \gamma \ket {10} + \delta \ket {11} \\ \alpha, \beta, \gamma, \delta \in \mathbb C $$
        - 量子記録 quantum register
            $$ \ket {00} = \ket 0 \ket 0 \\ \ket {01} = \ket 0 \ket 1 \\ \ket {10} = \ket 1 \ket 0 \\ \ket {11} = \ket 1 \ket 1 $$
        - 確率振幅 amplitude
            $$ \alpha^2 + \beta^2 + \gamma^2 + \delta^2 = 1 \\ $$
        - 同値関係
            $$ \alpha \ket {00}+ \beta \ket {01} + \gamma \ket {10} + \delta \ket {11} \sim \\ e^{i \theta}(\alpha \ket {00}+ \beta \ket {01} + \gamma \ket {10} + \delta \ket {11}) $$
- 量子門 quantum gate
    - 例 example
        - X gate 否定
            $$ X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} $$
        - Z gate 位相反転
            $$ Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} $$
        - Y gate
            $$ Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = i XZ $$
        - Hadamard gate
            $$ H = \frac{1}{\sqrt 2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} $$
        - 回転 gate
            $$ R_n(\theta) = \exp(-i \frac{\theta}{2}(n_x X + n_y Y + n_z Z)) $$
            - $\bm n = (1, 0, 0)$
                $$ R_x (\theta) = \exp (-i \frac{\theta}{2} X) \\ = \cos \frac{\theta}{2} I -i \sin \frac{\theta}{2} X \\ = \begin{pmatrix} \cos \frac{\theta}{2} & 0 \\ 0 & \cos \frac{\theta}{2} \end{pmatrix} + \begin{pmatrix} 0 & -i\sin \frac{\theta}{2}\\ -i\sin \frac{\theta}{2} & 0 \end{pmatrix} \\ = \begin{pmatrix} \cos \frac{\theta}{2} & -i\sin \frac{\theta}{2}\\ -i\sin \frac{\theta}{2} & \cos \frac{\theta}{2} \end{pmatrix} $$
    - 2量子ゲート
        - 制御門 controlled gate
            - 制御 control
            - 標的 target
        - 例 example
            - CNOT controlled not gate
- 量子回路 quantum circuit
- 量子移送 quantum teleportation
- 量子誤り訂正 quantum error detection and correlation
- 量子誤差 quantum error
- 量子もつれ entanglement
- CHSH inequality
- shor’s algorithm
- grover’s algorithm
- CRQC cryptographically relevant quantum computer
- PQC 耐量子計算機暗号 post quantum cryptography
- website
    [Quantum computing for the very curious](https://quantum.country/qcvc)
    [量子コンピューティング・ワークブックへようこそ！ — 量子コンピューティング・ワークブック](https://utokyo-icepp.github.io/qc-workbook/ja/welcome.html)
    [【情報系向け】量子コンピュータを学ぶためのオススメ本・資料](https://zenn.dev/hk_ilohas/articles/quantum-computer-how-learn)