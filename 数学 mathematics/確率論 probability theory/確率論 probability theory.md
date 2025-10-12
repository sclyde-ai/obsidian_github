    - 測度 measure
        - 可測空間 measurable space
            - 集合X
            - 完全加法族F
                [完全加法族/可算加法族/σ-加法族 σ-field/σ-algebra](https://www.notion.so/field-algebra-216ec42dd04b818888e3ff7e92bd559c?pvs=21)
            $$ (X, \mathcal F) $$
            を可測空間という
        - 測度空間 measure space
            - 集合X
            - 完全加法族F
                [完全加法族/可算加法族/σ-加法族 σ-field/σ-algebra](https://www.notion.so/field-algebra-216ec42dd04b818888e3ff7e92bd559c?pvs=21)
            - 測度u
                [測度 measure](https://www.notion.so/measure-216ec42dd04b81cf9d21f1df3e1fc229?pvs=21)
            $$ (X, \mathcal F, \mu) $$
            を測度空間という
            - 完備測度空間 complete
                - 測度空間(X, F, u)
                $$ \forall N \in \mathcal F, \forall A \subset N \\ \mu(N) = 0 \Rightarrow A \in \mathcal F \land \mu(A) = 0 $$
            - Borel measure space
                F is Borel field
        - 完全加法族/可算加法族/σ-加法族 σ-field/σ-algebra
            - 空集合
            $$ \phi \in \mathcal{F} $$
            - 補集合
                $$ \forall A \in \mathcal{F}, A^c \in \mathcal{F} $$
            - 完全加法性/可算加法性
                $$
                \forall n \in \N, A_n \in \mathcal{F} \Rightarrow \bigcup_{n=1}^\infin A_n \in \mathcal{F} $$
            この時、Fを完全加法族/可算加法族/σ-加法族という。
            - theorem
                - 積集合を含む
                    $$ \bigcap_{n= 1}^\infin A_n = (\bigcup_{n= 1}^\infin A_n^c)^c \\ A \cap B = (A^c \cup B^c)^c
                    $$
                - 差集合を含む
                    $$ A/B = A \cap B^c $$
            - 有限加法族
                - 空集合
                    $$ \phi \in \mathcal{F} $$
                - 補集合
                    $$ \forall A \in \mathcal{F}, A^c \in \mathcal{F} $$
                - 有限加法性
                    $$ \forall A,B \in \mathcal F\Rightarrow A \cup B \in \mathcal F $$
                - theorem 定理
                    有限加法族の直和は有限加法族
            - 生成される完全加法族 generated
                - 集合X
                - Xの部分集合族F_0
                - σ‐加法族全体の集合 $\mathscr F$
                $$ \sigma[\mathcal{F}_0] = \bigcap \{\mathcal{F} \in \mathfrak{F}| \mathcal{F}_0 \subset \mathcal{F}\} $$
                - 「生成される」の意味
                    「高々可算個の集合の共通部分・和集合・補集合・差集合を取る操作」を可算回行うこと
                - process to generate
                    1. F_0の要素を追加
                    2. 空集合Φを追加
                    3. 全ての要素の補集合を追加
                    4. 生成可能な全ての可算和を追加
                    5. 上記を繰り返す
                - example
                    - 有限集合
                        $$ X = \{1, 2, 3\}, F_0 = \{\{1\}\} $$
                        $$ 1.\ \sigma(F_0) = \{\{1\}\} \\ 2.\ \sigma(F_0) = \{\phi, \{1\}\} \\ 3.\ \sigma(F_0) = \{\phi, \{1\}, \{2, 3\}, X\} $$
                        $$ X = \{1, 2, 3\}, F_0 = \{\{1\}, \{2\}\} $$
                        $$ 1.\ \sigma(F_0) = \{\{1\}, \{2\}\} \\ 2.\ \sigma(F_0) = \{\phi, \{1\}, \{2\}\} \\ 3.\ \sigma(F_0) = \{\phi, \{1\},\{2\}, \{2, 3\}, \{3, 1\}, X\} \\ 4.\ \sigma(F_0) = \{\phi, \{1\},\{2\}, \{1, 2\}, \{2, 3\}, \{3, 1\}, X\} \\ 5.\ \sigma(F_0) = \{\phi, \{1\},\{2\}, \{3\}, \{1, 2\}, \{2, 3\}, \{3, 1\}, X\}
                        $$
                    - 実数上の開区間
                        $$ X = \mathbb R, F_0 = \{(a, b) | a < b, \forall a, b \in \R\} $$
                        1. 開集合を全て追加
                            $$ \{(a, b) | a < b, \forall a, b \in \R\} $$
                        2. 2つの片側無限閉区間を全て追加（開区間の補集合）
                            $$ \{(-\infin, a], [b, \infin) | a < b, \forall a, b \in \R\} $$
                        3. 片側無限開区間を全て追加（開区間と片側無限閉区間の和集合）
                            $$ \{(-\infin, b) | \forall b \in \R\} \\ \{(a, \infin) | \forall a \in \R\} $$
                        4. 片側閉区間を全て追加（片側無限開区間の補集合）
                            $$ \{(-\infin, a] | \forall a \in \R\} \\ \{[b, \infin) | \forall b \in \R\} $$
                        5. 閉区間を全て追加（片側無限閉区間の和集合）
                            $$ \{[a, b] | a < b, \forall, b \in \R\} $$
                        6. 半区間を全て追加（開区間と閉区間の和集合）
                            $$ \{(a, b] | a < b, \forall, b \in \R\} \\ \{[a, b) | a < b, \forall, b \in \R\} $$
            - Borel加法族 Borel field
                - 位相空間(X, O)
                $$ \mathcal B(X) = \sigma(\mathcal O(X)) $$
                この時、BをBorel fieldという
                Oは開集合系でも閉集合系でもよい
                - Borel set
                    - closed interval
                    - open interval
                    - open set
                    - closed set
                - 実数上のボレル集合
                    $$ (a,b) \\ [a, b] \\ [a, b) \\ {a} \\ \mathbb Q \\ \R / \mathbb Q $$
            - example
                - 自明なσ加法族 trivial
                    $$ \{\phi, X\} $$
                - 冪集合 power set
                    $$ 2^X $$
                - コイン投げ
                    $$ X = \{H, T\} $$
                    - 表か裏か
                        $$ \mathcal F = \{\phi, \{H\}, \{T\}, X\} $$
                    - 投げたか否か
                        $$ \mathcal F = \{\phi, X\} $$
                - 有限集合
                    $$ X = \{1, 2, 3\} $$
                    - どの要素か
                        $$ \mathcal F = \{\phi, \{1\}, \{2\}, \{3\}, \{2, 3\}, \{3, 1\}, \{1, 2\}, X\} $$
                    - 1か否か
                        $$ \mathcal F = \{\phi, \{1\}, \{2, 3\}, X\} $$
                    - 2か否か
                        $$ \mathcal F = \{\phi, \{2\} ,\{3, 1\}, X\} $$
                    - 3か否か
                        $$ \mathcal F = \{\phi, \{3\}, \{1, 2\}, X\} $$
                    - 集合内の要素か否か
                        $$ \mathcal F = \{\phi, X\} $$
                - さいころ
                    $$ \Omega = \{\omega_1, \omega_2,\omega_3,\omega_4,\omega_5, \omega_6\} $$
                    - 偶数かどうか
                        $$ A = \{ \omega_2,\omega_4, \omega_6\} $$
                        - 台集合
                            $$ \Omega $$
                        - 完全加法族
                            $$ \{\phi, A, A^c, \Omega\} $$
                        - 確率測度
                            $$ P(S) = \begin{matrix} A \end{matrix} $$
        - 測度 measure
            - 非負性 non-negative
                $$ 0 \leq \mu(A) \leq \infin, \forall A \in \mathcal{F},\\ \mu(\phi) = 0 $$
            - 完全加法性/可算加法性 countable additivity
                - A is disjoint
                    $$ \forall i, j \in \N, A_i \cap A_j \neq \phi $$
                $$ \mu(\bigcup_{n=1}^\infin A_n) = \sum_{n=1}^\infin \mu(A_n) $$
            - property
                - 単調性
                    $$ A \subset B \Rightarrow \mu(A) \leq \mu(B) \\ \forall A, B \in \mathcal{F} $$
                    - 証明
                        $$ A \subset B \Rightarrow B = A \cup (B/A) \\ \mu(B) = \mu(A) + \mu(B/A) \\ \mu(B/A) \geq0 \Rightarrow \mu(B) \geq \mu(A) $$
                - 劣加法性
                    $$ \mu(\bigcup_{n=1}^\infin A_n) \leq \sum_{n=1}^\infin \mu(A_n) \\ \{A_n\} \in \mathcal F $$
                    - 証明
                        $$ B_1=A_1, B_n = A_n/\bigcup_{i=1}^{n-1} A_i \\ \Rightarrow \forall i, j \in \N, B_i \cap B_j \neq \phi \\ B_n \subset A_n \\ \bigcup_{n=1}^\infin A_n = \bigcup_{n=1}^\infin B_n \\ \Rightarrow \mu(\bigcup_{n=1}^\infin A_n) = \mu(\bigcup_{n=1}^\infin B_n) = \sum_{n=1}^\infin B_n \leq \sum_{n=1}^\infin A_n
                        $$
                - 有限加法性
                - 上方連続性
                - 下方連続性
                - 極限（単調増加）
                    - 単調増加列A_n
                    $$ \mu(\lim_{n\to\infin}A_n) = \lim_{n\to\infin}\mu(A_n) $$
                    - proof
                        $$ A_n = \sum_{k=1}^n (A_k - A_{k-1})\\ \lim_{n\to\infin}A_n = \sum_{k=1}^\infin (A_k - A_{k-1}) $$
                        完全加法性より
                        $$ \mu(\lim_{n\to\infin}A_n) = \sum_{k=1}^\infin \mu(A_k - A_{k-1}) \\ = \lim_{n\to\infin}\sum_{k=1}^n (A_k - A_{k-1}) = \lim_{n\to \infin} \mu(A_n) $$
                - 極限（単調減少）
                    - 単調減少列A_n
                    - $\mu(A_1) < \infin$
                    $$ \mu(\lim_{n\to\infin}A_n) = \lim_{n\to\infin}\mu(A_n) $$
                    - proof
                        $$ \{A_1 - A_n | \forall n \in \N\} $$
                        は単調増加なので
                        [proof](https://www.notion.so/proof-216ec42dd04b81459d1aced407ccb78d?pvs=21)
                - 下極限
                - 上極限
                - 極限
            - example
                - 零測度 null measure
                    $$ \forall A \in \mathcal F, \mu_0(A) = 0 $$
                - counting measure 計数測度
                    $$ \mu_1 : \mathcal F \to [0, \infin] \\ \mu_1(F) = |F| $$
                - Delta/Dirac measure
                - Lebesgue measure
                    - closed interval [a, b]
                    $$ \mathbb P [a, b] = b-a $$
                    - open interval (a, b)
                        $$ (a,b) = \bigcup_{n=1}^\infin [a+\frac{1}{n}, b-\frac{1}{n}] \\ \mathbb P (a, b) = b-a $$
                        - preposition
                            sigma-algebra of Lebesgue integral contains all open interval
            - 有限加法測度 finite addictive measure
                - non-negative
                    $$ \forall A \in \mathcal{A}, 0 \leq \nu(A) \leq \infin, \nu(\phi) = 0 $$
                - finite additivity
                    - A and B are disjoint
                        $$ \forall A, B \in \mathcal{A}, A \cap B = \phi $$
                    $$ \nu(A \cup B) = \nu(A) + \nu(B) $$
            - 有限測度 finite measure
                $$ \forall X \in \mathcal{F}, \mu(X) < \infin $$
            - σ-有限測度 σ-finite
                - mesurable space (X, F)
                - measure u
                $$ \exist \{A_n\} \subset \mathcal F, A_n \uparrow X \land \mu(A_n) < \infin $$
                - another description
                    $$ \exist \{A_n\} \subset \mathcal F, X= \bigcup^\infin_{n=1} A_n \land \mu(A_n) < \infin $$
            - 絶対連続 absolutely continuous
                - mesurable space (X, F)
                    [可測空間 measurable space](https://www.notion.so/measurable-space-216ec42dd04b81eb81a5c19fc5636ae0?pvs=21)
                - measure u, v
                    [測度 measure](https://www.notion.so/measure-216ec42dd04b81cf9d21f1df3e1fc229?pvs=21)
                $$ \mu(A) = 0, A \in \mathcal F \Rightarrow \nu(A) = 0 $$
                この時、vがuに関して絶対連続であるという
                表記 $\nu \ll \mu$
                - 同値 equivalent
                    $$ \nu \ll \mu \land \nu \gg \mu $$
                    - interpretation
                        測度を持つ集合が等しい（値が等しいとは限らない）
                - 特異 singular
                    $$ \exist A \in \mathcal F, \mu(A) = \nu(A^c) = 0 $$
                    表記 $\mu \perp \nu$
                    - interpretation
                        測度を持つ集合が完全に異なる
                - 零測度
                - Lebesgue decomposition theorem
                    - 可測空間(X, F)
                        [可測空間 measurable space](https://www.notion.so/measurable-space-216ec42dd04b81eb81a5c19fc5636ae0?pvs=21)
                    - σ-有限測度u, v
                        [σ-有限測度 σ-finite](https://www.notion.so/finite-216ec42dd04b81e49550cc63c25fd1fe?pvs=21)
                    $$ \nu = \nu_c + \nu_s \\ \nu_c \ll \mu, \nu_s \perp \mu $$
                    - proof
                        - 有限測度の場合
                            $$ \alpha = \sup_{N \in \mathcal F, \mu(N) = 0} \nu(N) \\ = \sup\{\nu(N) \in \R | \forall N \in \mathcal F, \mu(N)=0\} $$
        - 可測関数 measurable function
            - measurable space (X, F) (Y, E)
            $$ f : X \to Y \\ f^{-1} (E) := \{x \in X | f(x) \in E\} \in \mathcal F $$
            - Borel measurable
                F and E are borel set
            - 測度保存変換 measure-preserving transformation
                - measure space (X, F, u)
                - mesurable function T
                $$ T: X \to X \\ \mu(T^{-1}(A)) = \mu(A) $$
        - 零集合 null set
            - 測度空間(X, F, μ)
                [測度空間 measure space](https://www.notion.so/measure-space-216ec42dd04b8113aee3d7c2ec0123c1?pvs=21)
            $$ N \in \mathcal{F}, \mu(N) = 0 $$
            Nを零集合という
            - ほとんどいたるところ almost everywhere/essentially
                $$ \forall x \in X/N, \mu(N) = 0, N \in \mathcal F $$
    - Riemann integral
        $$ \int_a^b f(x)dx = \lim_{||\Pi|| \to 0} RS_{\Pi}^+(f) = \lim_{||\Pi|| \to 0} RS_{\Pi}^-(f) $$
        - partition
            $$ \Pi = \{x_0, x_1, ..., \}\\ [x_0, x_1], [x_1, x_2], ..., [x_{n-1}, x_n] \\ a = x_0 < x_1 < ...< x_n = b $$
            $$ || \Pi|| = \max_{1 \leq k \leq n} (x_k -x_{k-1}) $$
        - the upper Riemann sum
            $$ RS_{\Pi}^+(f) = \sum_{k=1}^n M_k(x_k -x_{k-1}) \\ M_k = \max_{x_{k-1}\leq x \leq x_k}(x_k -x_{k-1}) $$
        - the lower Riemann sum
            $$ RS_{\Pi}^-(f) = \sum_{k=1}^n m_k(x_k -x_{k-1}) \\ m_k = \min_{x_{k-1}\leq x \leq x_k}(x_k -x_{k-1}) $$
        - average value
    - Lebesgue integral
        $$ \int_\Omega Xd\mathbb P = \int_\Omega X(\omega)d\mathbb P(\omega) = \lim_{||\Pi|| \to 0} LS_{\Pi}^-(f) $$
        - assumption
            $$ 0 \leq X(\omega) < \infin $$
        - partition
            $$ \Pi = \{y_0, y_1, ..., \}\\ 0 = y_0 < y_1 < ... \\ [y_k, y_{k+1}] $$
            $$ || \Pi|| = \max_{1 \leq k \leq n} (y_k -y_{k-1}) $$
        - the lower Lebesgue sum
            $$ LS_{\Pi}^-(X) = \sum_{k=1}^\infin y_k \mathbb P(A_k) $$
            - A_k
                $$ A_k = \{\omega \in \Omega : y_k \leq X(\omega) < y_{k+1}\} $$
        - positive and negative
            $$ \int_\Omega X(\omega) d\mathbb P(\omega) = \int_\Omega X^+ (\omega) d\mathbb P(\omega)
            - \int_\Omega X^-(\omega) d\mathbb P(\omega) $$
            $$ X^+ = \max(X(\omega), 0)\\ X^- = \max(-X(\omega), 0) $$
            - finite or infinite
        - theorem
            - finite
            - integrability
            - comparison
            - linearity
        - indicator function
            $$ \mathbb I_A(\omega) = \left( \begin{matrix} 1 & if & \omega \in A\\ 0 & if & \omega \notin A \end{matrix} \right. $$
        - subset integral
            $$ \int_A X(\omega)d\mathbb P(\omega)= \int_\Omega \mathbb I_A(\omega) X(\omega)d\mathbb P(\omega) $$
            - disjoint
    - comparison of Riemann and Lebesgue
        f is a bounded function
        - 1
            Riemann integral is defined
            if and only if
            the set of points x in [a, b] where f(x) is not continuous has Lebesgue measure zero
        - 2
            Riemann integral is defined
            then
            f is Borel mesurable
            and
            Riemann and Lebesgue integral agree
        - restate
            the Riemann integral exists
            if and only if
            f(x) is almost everywhere continuous
    - Lebesgue measure
        - the σ-algebra of Borel subsets
        $$ \mathcal L[a, b] = b-a $$
        - countable additivity property
            $$ \mathcal L(\bigcup_{n=1}^\infin B_n) = \sum_{n=1}^\infin \mathcal L(B_n) $$
    - convergence of integrals
        - random variable convergence
            - random variable sequence
            - probability space
            - null set N
            $$ \lim_{n \to \infin} X_n(\omega)= X(\omega), \forall \omega\in \Omega/N $$
        - strong law of large number
        - monotone convergence
            $$ 0 \leq X_1 \leq X_2 \leq ... \\ \lim_{n \to \infin} \mathbb E[X_n] = X\\ almost\ surely $$
            $$ 0 \leq f_1 \leq f_2 \leq ... \\ \lim_{n \to \infin} \int_{-\infin}^\infin f_n(x) dx= \int_{-\infin}^\infin f(x) dx\\ almost\ surely $$
            - corollary
                - countably many random variable
                    $$ X = \{x_0, x_1, ...\} $$
                $$ \mathbb E[X] = \sum_{k=0}^\infin x_k \mathbb P(X=x_k) $$
                - proof
                    $$ X_n = \sum_{k=0}^n x_k \mathbb I_{\{X=k\}} \\ \lim_{n \to \infin} X_n = X $$
                    $$ \mathbb E[X] = \lim_{n \to \infin} \mathbb E[X_n] = \lim_{n \to \infin} \sum_{k=0}^n x_k \mathbb P_{\{X=k\}} = \sum_{k=0}^n x_k \mathbb P_{\{X=k\}} $$
            - example (Petersburg paradox)
                E[X] is infinite, even though X is finite almost surely
        - dominated convergence
            - X_n
                $$ \lim_{n \to \infin} X_n = X $$
            - Y_n
                $$ \mathbb E[Y] < \infin \\ |X_n | < Y $$
            $$ \lim_{n \to \infin} \mathbb E[X_n] = \mathbb E[X] $$
            - f
            - g
                $$ \int_{-\infin}^\infin g(x) dx < \infin\\ |f_n| \leq g $$
            $$ \lim_{n \to \infin}\int_{-\infin}^\infin f_n(x) dx = \int_{-\infin}^\infin f(x) dx $$
    - Radon-Nikodym derivative
        - $\mathbb E[Z] = 1$
        - equivalent
            $$ \{\omega \in \Omega: \mathbb P(\omega) =0\} = \{\omega \in \Omega: \tilde{\mathbb P}(\omega) =0\} $$
        $$ Z = \frac{d\tilde {\mathbb P}}{d\mathbb P}\\ \tilde {\mathbb P}(A) = \int_A Z(\omega) d \mathbb P(\omega) $$
        - proof p33~34
            - $\tilde{\mathbb P}(\Omega) = 1$
                $$ \tilde {\mathbb P}(A) = \int_A Z(\omega) d \mathbb P(\omega) = \mathbb E[Z] = 1 $$
            - countably addictive
                - A is disjoint
                $$ B_n = \bigcup_{k=1}^n A_k ,B_{\infin} = \bigcup_{k=1}^\infin A_k \\
                $$
        - theorem
            $$ \tilde{\mathbb E} [X]= \mathbb E[XZ] \\ \tilde{\mathbb E} [Y]= \mathbb E[\frac{Y}{Z}] \\
            $$
        - Girsanov theorem
            $$ dW_t^Q = dW_t^P + \theta_t dt $$
        - example (normal random variable)
    - first-order variation
        $$ FV_T(f) = \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1}|f(t_{j+1}) -f(t_j)| $$
        - theorem
            $$ FV_T(f) = \int_0^T|f'(t)| dt $$
            - proof
                - the mean value theorem
                    $$ f'(t_j^_) = \frac{f(t_{j+1})-f(t_j)}{t_{j+1}-t_j}, \exist t_j^_ \in [t_j, t_{j+1}] $$
                $$ \lim_{|\Pi| \to 0} \sum_{j=0}^{n-1} |f(t_{j+1}) -f(t_j)| \\ = \lim_{|\Pi| \to 0} \sum_{j=0}^{n-1} |f'(t_j^*)|(t_{j+1} - t_j) \\ = \int_0^T|f'(t)| dt $$
    - quadratic variation
        $$ [f, f](T) = \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1}(f(t_{j+1})-f(t_j))^2 $$
        - theorem
            f is integrable (the integral of f is finite)
            then,
            $$ [f, f](T) = 0 $$
            - proof
                $$ \sum_{j=0}^{n-1}(f(t_{j+1})-f(t_j))^2 \\ = \sum_{j=0}^{n-1}|f(t_j^_)|^2(t_{j+1}-t_j)^2 \\ = \|\Pi\|\sum_{j=0}^{n-1}|f(t_j^_)|^2(t_{j+1}-t_j)\\ $$
                $$ [f, f](T) \leq \lim_{\|\Pi\| \to 0}\|\Pi\|\sum_{j=0}^{n-1}|f(t_j^_)|^2(t_{j+1}-t_j)\\ = \lim_{\|\Pi\| \to 0} \|\Pi\| \cdot \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1}|f(t_j^_)|^2(t_{j+1}-t_j)\\ = \lim_{\|\Pi\| \to 0} \|\Pi\| \cdot \int_0^T|f'(t)|^2 dt = 0 $$
    - Poisson random measure
        - 測度空間
            $$ (E, \mathcal A, \mu) $$
- 確率論 probability theory
    - 確率 probability
        - 確率空間 probability space
            - 可測空間 mesurable space $(\Omega, \mathcal F)$
                $$ (\Omega, \mathcal{F}) $$
                - 集合 set
                    $$ \Omega $$
                - σ-集合族、完全加法族 sigma-algebra
                    $$ \mathcal{F} \subset 2^\Omega \\ \Omega \in \mathcal{F} \\ A \in \mathcal{F}, A^c \in \mathcal{F} \\ (A_n)_{n \in \N} \subset \mathcal{F}, \bigcup_{n \in \N} A_n \in \mathcal{F} $$
                    「事象の分類方法」
            [確率測度 probability measure](https://www.notion.so/probability-measure-216ec42dd04b8167afd2ccd5210fd24b?pvs=21) P
            $$ (\Omega, \mathcal{F}, P) $$
            $\Omega$ 標本空間 sample space
            $\omega \in \Omega$ 標本点 sample point
            $F \in \mathcal F$ 事象 event
            - limit
                - limit supremum
                    $$ \limsup_{n \to \infin} A_n = \bigcap_{n=1}^{\infin} \bigcup_{k=n}^{\infin} A_k $$
                    $$ \forall n \in \N, \exist k \geq n, \omega \in A_k $$
                    「無限回A_nが起こる」
                    「事象が無限に頻繁に発生する」
                - limit infimum
                    $$ \liminf_{n \to \infin} A_n = \bigcup_{n=1}^{\infin} \bigcap_{k=n}^{\infin} A_k $$
                    $$ \exist n \in \N, \forall k \geq n, \omega \in A_k $$
                    「ある時点以降ずっとA_nが起こり続ける」
                    「事象がある時点以降恒常的に発生する」
                - inequity
                    $$ \liminf_{n \to \infin} A_n \subset \limsup_{n \to \infin} A_n $$
                - convergence
                    $$ \liminf_{n \to \infin} A_n = \limsup_{n \to \infin} A_n $$
                    この時、事象列は収束するという
            - example
                - heads or tails
                - real number
                    $$ (\R, \mathcal B(\R), \mu_X) $$
        - 確率測度 probability measure
            - 可測空間 measurable space $(\Omega, \mathcal F)$
                [可測空間 mesurable space $(\Omega, \mathcal F)$](https://www.notion.so/mesurable-space-Omega-mathcal-F-216ec42dd04b8114af34e95b07ec8c08?pvs=21)
            $$ \mathbb P : \mathcal{F} \rightarrow [0, 1] $$
            $$ \mathbb P(\Omega) = 1 $$
            - 加算加法性 countable additivity
                - A is disjoint
                    $$ \forall i, j \in \N, A_i \cap A_j = \phi $$
                $$ \mathbb P(\bigcup_{n = 1}^\infin A_n) = \sum_{n = 1}^\infin \mathbb P(A_n) $$
            - 離散 discrete
                $$ P(X=x) = p_i \\ \sum_i p_i = 1 \\ x \in \R $$
            - 連続 continuous
                $$ P(X \in A) = \int_A f(x)dx \in[0, 1] $$
                $$ P(a \leq X \leq b) = \int_a^b f(x) dx $$
            - property
                - $P(\phi) = 0$
                    $$ \Omega \in \mathcal F \Rightarrow \phi = A^c \in \mathcal F \\ \forall k \geq 1, A_k = \phi \ \Rightarrow \\ P(\phi) = P(\bigcup_{k=1}^\infin A_k) = \sum_{k=1}^\infin P(A_k) = \sum_{k=1}^\infin P(\phi) $$
                - finite additivity
                    - A is disjoint
                        $$ \forall i, j \in \N, A_i \cap A_j = \phi $$
                    $$ \Omega \in \mathcal F \Rightarrow \phi = A^c \in \mathcal F \\ \forall k \geq N+1, A_k = \phi \ \Rightarrow \\ P(\bigcup_{k=1}^\infin A_k) = \sum_{k=1}^\infin P(A_k) \\ P(\bigcup_{k=1}^N A_k) + P(\bigcup_{k=N+1}^\infin A_k) = \sum_{k=1}^N P(A_k) + \sum_{k=N+1}^\infin P(A_k) \\
                    P(\bigcup_{k=1}^N A_k) + P(\phi) = \sum_{k=1}^N P(A_k) + \sum_{k=N+1}^\infin P(\phi) \\ P(\bigcup_{k=1}^N A_k) = \sum_{k=1}^N P(A_k) $$
                - 補集合の確率
                    $$ A \cup A^c = \Omega \\ 1 =P(\Omega) = P(A\cup A^c) = P(A)+ P(A^c) \\ P(A^c) = 1 - P(A) $$
                - 差集合の確率
                    $$ A, B \in \mathcal F, A \subset B \\ \Rightarrow P(B/A) = P(B)-P(A) $$
                    $$
                    B/A = B\cap A^c \in \mathcal F\\ B = (B/A) \cup A, (B/A) \cap A = \phi \\ P(B) = P(B/A) + P(A) $$
                - 和集合の確率
                - 単調性
                    $$ A, B \in \mathcal F,A \subset B \Rightarrow P(A) \leq P(B) $$
                    $$ P(B/A) \geq 0 $$
                - 加法定理
                    $$ P(A\cup B) = P(A) + P(B) - P(A \cap B) $$
                    - proof
                        $$ A \cup B = A \cup (B/A) = A \cup (B / (A \cap B) $$
                        $$ P(A\cup B) = P(A) + P(B/(A \cap B)) = P(A) + P(B) - P(A \cap B) $$
                - 劣加法性
                    $$ A_k \in \mathcal F, P(\bigcup_{k=1}^\infin A_k) \leq \sum_{k=1}^\infin P(A_k) $$
                    - proof
                        $$ B_1 = A_1 \\ B_k = A_k/A_{k-1} $$
                        と定義すると
                        $$ A_k = \bigcup_{k=1}^n B_k \\ \bigcup_{k=1}^\infin A_k = \bigcup_{k=1}^\infin B_k $$
                        が成立する
                        $$ P(\bigcup_{k=1}^\infin A_k) = P(\bigcup_{k=1}^\infin B_k) $$
                        加算加法性より
                        $$ = \sum_{k=1}^\infin P(B_k) \\ = \lim_{n \to \infin }\sum_{k=1}^n P(B_k) $$
                        有限加法性より
                        $$ = \lim_{n \to \infin} P(\bigcup_{k=1}^n B_k) \\ = \lim_{n \to \infin } P(A_n) $$
                - 単調連続性（増加列）
                    $$ A_n \uparrow A \Rightarrow \mathbb P(A_n) \uparrow \mathbb P(A) $$
                    - description
                        $$ A_1 \subset A_2 \subset ... \\ \lim_{k\to \infin} P(A_k) = P(\lim_{k \to \infin} A_k) $$
                    - proof
                        $$ B_1 = A_1 \\ B_k = A_k/A_{k-1} $$
                        と定義すると
                        $$ A_k = \bigcup_{k=1}^n B_k \\ \bigcup_{k=1}^\infin A_k = \bigcup_{k=1}^\infin B_k $$
                        が成立
                        加算加法性より
                        $$ = \sum_{k=1}^\infin P(B_k) $$
                        劣加法性より
                        $$ \leq \sum_{k=1}^\infin P(A_k) $$
                - 単調連続性（減少列）
                    $$ A_n \downarrow A \Rightarrow \mathbb P(A_n) \downarrow \mathbb P(A) $$
                    - description
                        $$ A_1 \supset A_2 \supset ... \\ \lim_{k\to \infin} P(A_k) = P(\lim_{k \to \infin} A_k) $$
                - Fatouの補題
                    $$ P(\liminf A_k) \leq \liminf P(A_k) \\ \leq \\ \limsup P(A_k) \leq P(\limsup A_k) $$
                    - proof
                        $$ B_n = \bigcap_{k=n}^\infin A_k $$
                        $$ P(\liminf A_k) = P(\bigcup_{n=1}^\infin \bigcap_{k=1}^\infin A_k) = P(\bigcup_{k=1}^\infin B_n) = \lim P(B_n) \leq \liminf P(A_k) $$
                        B_nの定義より
                        $$ \forall k \geq n, B_n \subset A_k, P(B_n) \leq P(A_k) \Rightarrow P(B_n) \leq \inf_{k\geq n} P(A_k) $$
                - Borel-Cantelli lemma 1
                    - 事象列
                    $$ \sum_{n=1}^\infin P(A_n) < \infin \Rightarrow P(\limsup_{n \to \infin} A_n) = 0 $$
                    - proof
                        $$ E_k = \bigcup_{n=k}^\infin A_n \\ \limsup_{n \to \infin} A_n \subset E_k \\ P(\limsup_{n \to \infin} A_n) \leq P(E_k) \leq \sum_{n=k}^\infin P(A_n) $$
                - Borel-Cantelli lemma 2
                    - 互いに独立な事象列
                    $$ \sum_{n=1}^\infin P(A_n) = \infin \Rightarrow P(\limsup_{n \to \infin} A_n) = 1 $$
                    - proof
                        $$ \forall k \in \N, P(\bigcup_{n=k}^\infin A_n) = 1 $$
                        let me prove it
                        $$
                        \forall N \in \N \\ 1-P(\bigcup_{n=k}^\infin A_n) \leq 1-P(\bigcup_{n=k}^N A_n) \\ = P((\bigcup_{n=k}^N A_n)^c) \\ = P(\bigcap_{n=k}^N A_n^c) \\ = \prod_{n=k}^N P(A_n^c) \\ = \prod_{n=k}^N (1-P(A_n)) \\ \leq \prod_{n=k}^N \exp(-P(A_n))\\ = \exp(-\sum_{n=k}^N P(A_n)) \\ \xrightarrow{n\to\infty} 0 \\ P(\bigcup_{n=k}^\infin A_n) = 1 $$
        - 確率変数 random variable
            事象を数値で表現
            - Borel field B
            $$ X : \Omega \rightarrow \R \\ \{\omega \in \Omega| X(\omega) \in B\} \in \mathcal F, \forall B \in \mathcal B(\R) $$
            then, X is called the random variable
            - 確率要素 random element
                確率変数の一般化
                - 確率空間 probability space
                    $$ (\Omega, \mathcal F, \mathbb P) $$
                - 可測空間 measurable space
                    $$ (E, \mathcal E) $$
                $$ X : \Omega \rightarrow E \\ \{\omega \in \Omega| X(\omega) \in B\} \in \mathcal F, \forall B \in \mathcal E $$
                then, X is called the random element
        - 分布測度 distribution measure
            - 確率空間 probability space $(\Omega, \mathcal F, P)$
            - 確率変数 random variable X
            - Borel field B
            $$ \mu_X: \mathcal B (\R) \to \R \\ \mu_X(B) = \mathbb P (X\in B) $$
            then, \mu is the distribution measure
            - 分布が等しい identically distributed
                $$ \mathbb P(X \in A) = \mathbb P(Y \in A) $$
                then, X and Y are identically distributed
            - example
                $$ X(\omega) = \omega \\ Y(\omega) = 1-\omega $$
                - measure 1
                    $$ \mathbb P[a, b] = b-a $$
                - measure 2
                    $$ \mathbb P [a, b] = b^2 -a^2 $$
        - 累積分布関数/分布関数 cumulative distribution function/distribution function
            $$ F_X(x) = \mathbb P(X\leq x) = \mu_X(-\infin, x] \\ x \in \R $$
            then, F is the cumulative distribution function
            - theorem
                - order
                    $$ x \leq y, F_X(x) \leq F_X(y) $$
                    - proof
                        $$ (-\infin, x_1] \subset (-\infin, x_2] \\ A_1 = X^{-1}(-\infin, x_1] \\ A_2 = X^{-1}(-\infin, x_2] \\ A_1 \subset A_2 $$
                - limit
                    $$ \lim_{x \to +\infin} F_X(x) = 1 \\ \lim_{x \to -\infin} F_X(x) = 0 $$
                    - proof
                        $$ \lim_{x \to -\infin} P(X \leq x) = \lim_{x \to -\infin} \mu(-\infin, x] \\ = \mu(\phi) = 0 $$
                        $$ \lim_{x \to \infin} P(X \leq x) = \lim_{x \to \infin} \mu(-\infin, x] \\ = \mu(\R) = 1
                        $$
                - right-hand continuous
                    - proof
                        $$ x_n = x + \epsilon_n, \epsilon_n \downarrow 0\\ x_n \downarrow x \\ A_n = (-\infin, x_n] \\ \lim_{n\to \infin} A_n = \bigcap_{n=1}^\infin (-\infin, x_n] = (-\infin, x] \\ \lim_{n \to \infin} F(x_n) = \mu_X(\bigcap_{n=1}^\infin [-\infin, x_n]) = \mu_X(-\infin, x_n] = F(x) $$
                    - the case of the left-hand…
                        $$ x_n = x - \epsilon_n, \epsilon_n \uparrow 0\\ x_n \uparrow x, \forall x_n < x \\ A_n = (-\infin, x_n] \\ \lim_{n\to \infin} A_n = \bigcup_{n=1}^\infin (-\infin, x_n] = (-\infin, x) \\
                        $$
                - compute distribution measure 1
                    $$ \mu_X(x, y] = F(y) -F(x) $$
                - compute distribution measure 2
                    $$ \mu_X[a, b] = \lim_{n \to \infin }\mu_X(a-\frac{1}{n}, b] = F(b) - \lim_{n \to \infin}F(a-\frac{1}{n}) $$
        - 確率密度関数 probability density function
            縦軸は確率密度
            $$ \mu_X(B) = \mathbb P(X \in B) = \int_B f_X(x) dx \\ B \in \mathcal B(\R) $$
            then, f is the density function
            - continuous
                $$ F(x) = \int_{-\infin}^x f(x)dx \\ \int_{-\infin}^{\infin} f(x)dx = 1 \\f(x) \geq 0, x \in \R $$
        - 確率質量関数 probability mass function
            縦軸は確率
            $$ \mu_X(B) = \sum_{\{i;x_i \in B\}} p_i \\ B \in \mathcal B(\R) $$
            - another uniform distribution
                - random variable
                    $$ Y_n(\omega) = \left\{ \begin{matrix} 1 & if & \omega_n = H \\ 0 & if & \omega_n = T \end{matrix} \right. \\ X = \sum_{n=1}^\infin \frac{Y_n}{2^n} $$
                - distribution measure
                    $$ \mu_X[\frac{k}{2^n}, \frac{k+1}{2^n}] = \frac{1}{2^n} $$
                - Lebesgue integral
                    $$ \mu_X[\frac{k}{2^n}, \frac{m}{2^n}] = \frac{m}{2^n} - \frac{k}{2^n} \\ \mu_X[a, b] = b-a\\ b = \frac{m}{2^n}, a = \frac{k}{2^n} $$
            - standard normal
                $$ \phi(x) = \frac{1}{\sqrt{2\pi}}\exp(-\frac{x^2}{2}) $$
                $$ N(x) = \int_{-\infin}^x \phi(\xi)d\xi $$
        - 基準化定数 normalization constant
            $$ c = \frac{1}{\int_{-\infin}^{\infin}f(x)dx} $$
        - 変数変換 random variable transformation
            - 1-dimensioan (monotonic)
                - random variable
                    $$ Y = g(X) $$
                    g is monotonic
                $$ p_Y(y) = p_X (g^{-1}(y)) \left|\frac{d}{dy} g^{-1}(y)\right| $$
                - proof
                    $$ F_Y(y) = \mathbb P(Y \leq y) \\ = \mathbb P(g(X) \leq y) \\ = \mathbb P(X \leq g^{-1}(y)) \\ = F_X(g^{-1 }(y)) $$
                    differentiate F with respect to y
                    $$ f_Y(y) = \frac{d}{dy} F_Y(y) \\ = \frac{d}{dy} F_X(g^{-1}(y)) \\ = f_X(g^{-1}(y)) \left|\frac{d}{dy}g^{-1}(y)\right| $$
        - 確率変数が分布に従う a random variable is distributed according to a distribution
            - random variable X
            there are two cases when it is called that a random variable is distributed according to a distribution
            - cumulative distribution function F
                $$ X \sim F \\ \mathbb P(X \leq x) = F(x) $$
            - probability density/mass function f
                $$ X \sim f \\ \mathbb P(X = x) = f(x) $$
    - 関数 function
        - 期待値/母平均 expected value/population mean
            $$ \mathbb E[X] = \int_{\Omega} X(\omega) d\mathbb P(\omega) = \mu $$
            - property
                - discrete
                    $$ X =\{x_0, x_1, ..., x_n \}\\ \Rightarrow \\ \mathbb E[X] = \sum_{k=0}^n x_k\mathbb P(X = x_k) $$
                - integrability
                    X is integrable
                    if and only if
                    $$ \mathbb E[|X|] < \infin $$
                - comparison
                    $$ \mathbb P(X \leq Y) = 1 \\ \Rightarrow \\ \mathbb E[X] \leq \mathbb E[Y] $$
                - linearity
                    $$ \mathbb E[aX+bY] = a \mathbb E[X] + b \mathbb E[Y] $$
                - scalar
                    $$ X = c \Rightarrow \mathbb E[X] = c $$
                - zero
                    $$ X \geq 0 \land \mathbb E[X] = 0 \Rightarrow X = 0 $$
                - absolute value
                    $$ |\mathbb E[X]| \leq \mathbb E[|X|] $$
                - Jensen’s inequality
                    - \phi is a convex
                    $$ \phi(\mathbb E[X]) \leq \mathbb E[\phi (X)] $$
            - 条件付き期待値 conditional expectation
                - probability space
                - sigma-algebra G
                - measurability
                    $$
                    $$
                    E is g-measurable
                - partial average
                    $$
                    $$
        - 母分散 population variance
            $$ V[X] = \mathbb E[(X-\mu)^2] =\sigma^2 $$
            - theorem
                - $V[X] = \mathbb E[X^2] - \mathbb (E[X])^2$
                    $$ Var[X] = \mathbb E[(X-\mu)^2] \\ = \mathbb E[X^2 - 2X\mu + \mu^2] \\ = \mathbb E[X^2] -2\mu \mathbb E[X] + \mu^2 \\ = \mathbb E[X^2] -2\mu^2 + \mu^2 \\ = \mathbb E[X^2] - \mu^2 \\ = \mathbb E[X^2] - \mathbb (E[X])^2 $$
                - constant
                    $$ X = c \Rightarrow V[c] = 0 $$
                - scalar
                    $$ V[kX] = k^2 V[X] $$
                - linearity
                    $$ V[X+Y] = V[X] + V[Y] $$
        - 積率 moment
            $$ \mathbb E[(X-\mu)^k] = \mu_k $$
        - 定義関数/指示関数 indicator function
        - 分位点関数 quantile function
            確率p
            $$ x_p = F^{-1}(p) $$
        - 確率母関数 probability generating function
            $$ G_X(s)=\mathbb E[s^X] = \sum_{x=0}^\infin s^x p(x) $$
            - 収束条件
                - 非負の整数値をとる離散確率変数
                - $|s| \leq 1$
                - $p(x) \geq 0$
                - $\sum p(x) = 1$
            - 期待値
                $$ \left. \frac{dG(s)}{ds} \right|_{s=1} =\left. \sum_{x=0}^\infin xs^{x-1}p(x) \right|_{s=1} = \sum_{x=0}^\infin xp(x) = \mathbb E[X] $$
            - 階乗積率 factorial moment
                $$ G^{(k)}(1)=\mathbb E[X(X-1)...(X-k+1)] $$
        - 積率母関数 moment generating function
            $$ M_X(t) = G_X(e^t) = \mathbb E[e^{t X}] = \sum_{k=0}^\infin \frac{\theta^t}{k!}\mu'_k $$
            - 積率 moment
                $$ \mathbb E[X^n] = M_X^{(n)}(0) $$
            - central moment
                $$ \phi(\theta)e^{-\mu \theta} = \mathbb E[e^{\theta (X-\mu)}] $$
            - 独立
                XとYが独立ならば
                $$ M_{X+Y}(t) = M_X(t)M_Y(t) $$
        - 特性関数 characteristic function
            $$ \phi_X(t) = \mathbb E[e^{itX}] = \sum_{x=-\infin}^\infin e^{itx}p(x) $$
            - 積率 moment
                $$ \mathbb E[X^n] = i^n \phi^{(n)}_X (0) $$
            - 逆転公式 inversion formula
                differential
            - FFT Fast Fourier Transform
                $$ \phi_X(t) = \int_{-\infin}^\infin\exp(itx)f_X(x)dx $$
                特性関数は確率密度関数のフーリエ変換に一致する
        - Laplace–Stieltjes transform
            $$ F_X^*(s) = \int_0^\infin e^{-sx}f_X(x)dx $$
    - 多変量確率変数 multivariate random variable
        - 確率方向量 probability vector
            - n個の連続型確率変数
                $$ X_1 : \Omega \to \R \\ \vdots \\ X_n : \Omega \to \R $$
            $$ (X_1, ..., X_n):\Omega \to \R^n $$
        - 同時確率分布 joint probability distribution
            $$ p(x, y) = P(X = x, Y=y)\\ F(x, y) = P(X \leq x, Y \leq y) $$
        - 周辺分布 marginal distribution
            同時確率分布から一部の確率変数を消去した確率分布
            $$ p_X(x) = \mathbb P(X=x) = \sum_y \mathbb P(X=x, Y=y) = \sum_y p(x, y) $$
            - 周辺化 marginalization
                同時確率分布から周辺分布を作ること
        - 条件付き分布 conditional distribution
            $$ p_{Y|X}(y|x) = P(Y=y | X=x) = \frac{P(X=x, Y=y)}{P(X=x)} =\frac{p(x, y)}{p_X(x)} $$
            $$ p(x, y) = p_X(x)p_{Y|X}(y) $$
        - 互いに独立 mutually independent
            $$ p(x, y) = p_X(x)p_Y(y) $$
        - 畳み込み convolution
            - 2 variables
                $$ Z = X+ Y $$
                # $$ \left( \begin{matrix} W \\ Z \end{matrix} \right)
                # \left( \begin{matrix} 1 & 0 \\ 1 & 1 \end{matrix} \right)
                \left( \begin{matrix} X \\ Y \end{matrix} \right) $$
                - PDF
                    $$ f_X*f_Y = \int_{-\infin}^\infin f_X(w)f_Y(z-w)dw $$
                - CDF
                    $$ F_{X+Y}(z) = P(X+Y \leq z) \\ = \int_{-\infin}^\infin \int_{\infin}^{y=z-x}f_{X, Y}(x, y)dydx \\ = \int_{-\infin}^\infin F_Y(z-x)f_X(x)dx \\ = F_X *F_Y(z) $$
            - multi-variables
                $$ S_n = \sum_{i=1}^n X_i $$
                $$ P(S_1 \leq t) = P(X_1 \leq t) = F(t) \\ P(S_2 \leq t) = \int_0^t F(t-x)f(x)dx \\ = \int_0^t F(t-x)dF(x) \\ = F*F(t) = F^{(2)}(t) $$
            - dependent
                $$ Z = Y_1 + Y_2\\ F_Z(z) =\int_{-\infin}^\infin \int_{-\infin}^{z-x_1} f_{Y_1, Y_2} (y_1, y_2) dy_2 dy_1 $$
                - 変数変換
                    # $$ \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix}
                    \left( \begin{matrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2\\ \end{matrix} \right) \begin{pmatrix} X_1 - \mu_1 \\ X_2 - \mu_2 \end{pmatrix} $$
                    $$ Y_1 = \sigma_1^2(X_1 - \mu_1) + \rho \sigma_1 \sigma_2(X_2 - \mu_2) \\ Y_2 = \rho \sigma_1 \sigma_2(X_1 - \mu_1) + \sigma_2^2(X_2 - \mu_2) $$
                $$ = \int_{-\infin}^\infin \int_{-\infin}^{z-x_1} f_{X_1}(y_1) f_{X_2}(y_2) | \Sigma |dy_2 dy_1 $$
            - 正規分布 → 正規分布
                $$
                $$
            - Bernoulli → 二項分布
                - Bernoulli X
                    $$ M_X(t) = \sum_{x = 0}^1 e^{tx} p^x (1-p)^{1-x} = pe^t + q $$
                - 二項分布 $S_n$
                    $$ M_{S_n}(t) = \sum_{x = 0}^n e^{tx} \binom n x p^x (1-p)^{1-x} = (pe^t + q)^n $$
            - 幾何分布 → 負の二項分布
                - 幾何分布 X
                    $$ \phi_X(t) = \sum_{x = 0}^\infin pq^x e^{itx} = \frac{p}{1-qe^{ix}} \\ |qe^{ix}| = q < 1 \\ t < \log \frac{1}{q} $$
                - 負の二項分布
                    $$ \phi_{S_n}(t) = \sum_{x = 0}^\infin \binom {-n}{x} p^nq^xe^{itx} \\ = p^n \sum_{x = 0}^\infin (-1)^x\binom {-n}{x} q^xe^{itx} \\ = p^n \sum_{x = 0}^\infin \binom {-n}{x} (-q)^xe^{itx}
                    $$
                    we apply $(1+u)^{-n} = \sum_{x=0}^\infin \binom{-n}{x} u^x$
                    $$ = p^n(1+(-qe^{it}))^{-n} \\ = (\frac{p}{1-qe^{ix}})^n $$
            - 指数分布 → gamma 分布
            - website
                [【徹底解説】確率変数の和の分布と畳み込み | Academaid](https://academ-aid.com/statistics/sum-rv-conv)
                [確率変数の和の分布を計算する【確率論，畳み込み】 | k-san.link](https://k-san.link/sum-random-variables/)
        - 独立 independent
            $$ \mathbb P(XY) = \mathbb P(X) \mathbb P(Y) $$
        - 共分散 covariance
            $$ Cov(X, Y) = \mathbb E[(X-\mathbb E(X))(Y-\mathbb E[Y])] $$
        - 相関係数 correlation coefficient
            $$ \mathbb E[X $$
            - spearman
            - kendoll’s tau
        - 分散共分散行列 covariance matrix
            - random variable vector
                $$ X = (X_1, X_2, ..., X_n)^\top $$
            $$ \Sigma_{i, j} = Cov(X_i, X_j) $$
            - 精度行列 precision matrix/情報行列 information matrix
                $$ \Sigma^{-1} $$
            - 2-dimensional
                $$ \Sigma = \left( \begin{matrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2\\ \end{matrix} \right) $$
                - 精度行列 precision matrix
                    $$ \frac{1}{(1-\rho^2)\sigma_1\sigma_2}\left( \begin{matrix} \sigma_2^2 & -\rho \sigma_1 \sigma_2 \\ -\rho \sigma_1 \sigma_2 & \sigma_1^2 \end{matrix} \right) $$
                    - proof
                        $$
                        \left( \begin{array}{cc|cc} \sigma_1^2 & \rho \sigma_1 \sigma_2 & 1 & 0\\ \rho \sigma_1 \sigma_2 & \sigma_2^2 & 0 & 1 \end{array} \right) \\ \left( \begin{array}{cc|cc} \sigma_1 & \rho \sigma_2 & \frac{1}{\sigma_1} & 0 \\ \rho \sigma_1 & \sigma_2 & 0 & \frac{1}{\sigma_2} \end{array} \right) \\ \left( \begin{array}{cc|cc} \sigma_1 & \rho \sigma_2 & \frac{1}{\sigma_1} & 0\\ 0 & (1-\rho^2)\sigma_2 & -\frac{\rho}{\sigma_1} & \frac{1}{\sigma_2}\\ \end{array} \right) \\ \left( \begin{array}{cc|cc} \sigma_1 & \rho \sigma_2 & \frac{1}{\sigma_1} & 0 \\ -\frac{\rho}{(1-\rho^2)\sigma_1}& \frac{1}{(1-\rho^2)\sigma_2} & 0 & \sigma_2 \end{array} \right) \\ \left( \begin{array}{cc|cc} \sigma_1 & 0&\frac{1}{\sigma_1} + \frac{\rho^2}{(1-\rho^2)\sigma_1} & -\frac{\rho}{(1-\rho^2)\sigma_2} \\ 0 & \sigma_2 & -\frac{\rho}{(1-\rho^2)\sigma_1}& \frac{1}{(1-\rho^2)\sigma_2} \end{array} \right) \\ \left( \begin{array}{cc|cc} \sigma_1 & 0 & \frac{1}{(1-\rho^2)\sigma_1} & -\frac{\rho}{(1-\rho^2)\sigma_2} \\ 0 & \sigma_2 & -\frac{\rho}{(1-\rho^2)\sigma_1}& \frac{1}{(1-\rho^2)\sigma_2} \end{array} \right) \\ \left( \begin{array}{cc|cc} 1 & 0 & \frac{1}{(1-\rho^2)\sigma_1^2} & -\frac{\rho}{(1-\rho^2)\sigma_2 \sigma_1} \\ 0 & 1 & -\frac{\rho}{(1-\rho^2)\sigma_1\sigma_2}& \frac{1}{(1-\rho^2)\sigma_2^2} \end{array} \right)
                        $$
    - 分布が等しい vs 確率変数が等しい
        - example
            $$ X \sim U(0, 1) \\ Y = -X \sim U(0, 1) $$
            $$ F_X = F_Y \\ X \ne Y $$
    - 確率変数列 random variable sequence
        $$ \{X_n\} \\ X_n : \Omega \rightarrow \R
        $$
        - 各点収束 pointwise convergent
            $$ \lim_{n \to \infin} X_n(\omega) \in \R $$
            この時、確率変数X_nはwで各点収束する
            $$ \forall \omega \in \Omega :\lim_{n \to \infin} X_n(\omega)\in \R $$
            この時、確率変数X_nは各点収束する
            $$ \forall \omega \in \Omega :\lim_{n \to \infin} X_n(\omega)= X(\omega) $$
            Xを各点極限という
        - 確率収束 converges in probability 確率極限 probability limit
            - 同一確率空間上の確率変数列 $\{X_n\}$
            - probability 0 version
                $$ \forall \epsilon > 0, \lim_{n \rightarrow \infin} P(|X_n-X| \geq \epsilon\}) = 0 $$
                - strict def
                    $$ \forall \epsilon > 0, \forall \delta > 0, \exist N \in \N, \forall n > N, \\ |\mathbb P(\{\omega \in \Omega: |X_n(\omega)-X(\omega)| \geq \epsilon\})| < \delta $$
            - probability 1 version
                $$ \forall \epsilon > 0, \lim_{n \rightarrow \infin} P(|X_n-X| < \epsilon) = 1 $$
                - strict def
                    $$ \forall \epsilon > 0, \forall \delta > 0, \exist N \in \N, \forall n > N, \\ |\mathbb P(\{\omega \in \Omega: |X_n(\omega)-X(\omega)| < \epsilon\})-1| < \delta $$
            この時、確率変数列 $\{X_n\}$は確率変数Xへ確率収束する
            - 表記
                $$ X_n \to X\ c.p. \\ X_n \stackrel{p}{\to} X $$
            確率変数Xを確率変数列 $\{X_n\}$の確率極限という
        - 概収束 almost sure/everywhere convergent 概極限 almost sure/everywhere limit
            - 同一確率空間上の確率変数列 $\{X_n\}$
            $$ P(\{\forall \omega \in \Omega :\lim_{n \to \infin} X_n(\omega)\in \R \}) = 1 $$
            この時、確率変数列 $\{X_n\}$は概収束する
            - 表記
                $$ X_n \to X\ a.s./a.e. \\ X_n \stackrel{a.s./a.e.}{\to} X $$
            $$ X : \Omega \to \R \\ \forall \omega \in A: X(\omega) = \lim_{n \to \infin} X_n(\omega) $$
            確率変数Xを確率変数列 $\{X_n\}$の概極限という
        - 分布収束/法則収束 converges in distribution/law 分布極限/法則極限 limit in distribution/law
            $$ \lim_{n \rightarrow \infin} F_{X_n}(x) = F_X(x) $$
            確率変数列 $\{X_n\}$は確率変数Xに分布収束するという
            - 表記
                $$ X_n \to X\ c.d. \\ X_n \stackrel{d}{\to} X $$
            確率変数Xを確率変数列 $\{X_n\}$の分布/法則極限という
            $F_X$を漸近/極限分布 asymptotic/limiting distributionという
        - 平均収束 convergence in mean
            $$ \lim_{n \to \infin} \mathbb E(|X_n - X|^r) = 0 $$
            この時、確率変数列 $\{X_n\}$は確率変数Xへr次平均収束する
            - 表記
                $$ X_n \to X\ c.p. \\ X_n \stackrel{p}{\to} X $$
            確率変数Xを確率変数列 $\{X_n\}$のr次平均極限という
    - 極限定理 limit theorem
        - Markov’s inequality
            X is non-negative
            $$ \mathbb P(X \geq c) \leq \frac{\mathbb E[X]}{c} $$
            - proof
                $$ Y= \begin{cases} 0 & if & X < c \\ c & if & X \geq c \end{cases} \\ X \geq Y \ (X\geq 0 \land Y \geq 0) \\ \mathbb E[X] \geq \mathbb E[Y] = c\mathbb P(X \geq c) \\ c \mathbb P(X \geq c) \leq \mathbb E[X] \\ \mathbb P(X \geq c) \leq \frac{\mathbb E[X]}{c}
                $$
        - Chebyshev’s inequality
            $$ \mathbb P(|X-\mu| \geq c) \leq \frac{\sigma^2}{c^2} $$
            - proof
                $$ X = (X-\mu)^2 \\ c = c^2 \\ \mathbb E[(X-\mu)^2] = \sigma^2 \\ \mathbb P((X-\mu)^2 \geq c^2) \leq \frac{\sigma^2}{c^2} \\ \mathbb P(|X-\mu| \geq c) \leq \frac{\sigma^2}{c^2} $$
        - 大数の弱法則 weak law of large numbers
            - covariance = 0
                $$ \forall i, j \in \N, Cov(X_i, X_j) = 0 $$
            - 平均 average
                $$ \bar X_n = \frac{1}{n} \sum_{i = 1}^n X_i $$
            $$ \lim_{n \rightarrow \infin} \mathbb P(|\bar X_n - \mu| \geq \epsilon) = 0, \forall \epsilon > 0 $$
            $$ \lim_{n \rightarrow \infin} \mathbb P(|\bar X_n - \mu| < \epsilon) = 1, \forall \epsilon > 0 $$
            - 証明 proof
                $$ \bar X_n = \frac{1}{n}(\sum_{i = 1}^n X_i) \\ \mathbb E[\bar X_n] = \mu \\ \mathbb E[(\bar X_n-\mu)^2]= \frac{\sigma^2}{n} \\ \mathbb P((\bar X_n - \mu)^2 \geq \epsilon^2) = \frac{\sigma^2}{n \epsilon^2} \\ \lim_{n \rightarrow \infin} \mathbb P(|\bar X_n - \mu| \geq \epsilon) = 0, \forall \epsilon > 0 $$
            - 誤差が基準より大きくなる確率は0に収束させることができる定理（例外あり）
            - 裏を考えると有限のnでは基準を超える可能性がある
        - 大数の強法則 strong law of large number
            $$ \mathbb P(\lim_{n \rightarrow \infin} \bar X_n = \mu) = 1 $$
            - 証明 proof
                - assumption
                    - 独立同分布な確率変数列 $X_1, X_2, ...$
                    - 期待値有限
                        $$ \mathbb E[|X_i|] < \infin $$
                        - 裾の確率が0に収束
                            $$ \mathbb P(|X_i| > n) \xrightarrow{n\to\infty} 0 $$
                            - proof
                                [Markov’s inequality](https://www.notion.so/Markov-s-inequality-216ec42dd04b81588729e355952b6934?pvs=21)
                                $$ \mathbb P(|X_i|>n) \leq \frac{\mathbb E[|X_i|}{n} \\ \xrightarrow{n\to\infty} \\ \mathbb P(|X_i|>n) \to 0 $$
                        - 和の有限性
                            $$ \sum_{n=1}^\infin \mathbb P(|X_i| > n) = \mathbb E[|X_i|] < \infin $$
                - sign
                    - 標本平均
                        $$ \bar X_n $$
                    - 部分和
                        $$ S_n $$
                一般性を失わず\mu = 0 を仮定
                1. truncation
                    $$ X_i^{(n)} = X_i \cdot 1_{|X_i| \leq n} \\ Y_i^{(n)} = X_i - X_i^{(n)} $$
                2. $\bar Y_n^{(n)} \to 0$
                3. $\bar X_n^{(n)} \to 0$
            - 誤差が基準より大きくなる確率は0に収束させることができる定理（例外なし）
        - 中心極限定理 central limit theorem
            - S_n
                $$ S_n = \sum_{k=1}^n X_k \\ E[S_n] = n\mu, V[S_n]= n\sigma^2 $$
            $$ \lim_{n \to \infin }P\left(\frac{S_n- n\mu}{\sqrt n\sigma} \leq \alpha \right) \rightarrow \frac{1}{\sqrt{2\pi}} \int_{-\infin}^\alpha e^{-\frac{x^2}{2}}dx $$
            - link
                [https://youtu.be/XXsTu66VB-E?si=TIqafd8YA9_zA7Zz](https://youtu.be/XXsTu66VB-E?si=TIqafd8YA9_zA7Zz)
        - 4次moment評価
            - 独立な確率変数 $X_1, ..., X_n$
            - 4次momentが有限
            1. 中心化
                $$ Y_i = X_i -\mu \\ \mathbb E[Y_i] = 0, \mathbb E[Y_i^2] = \sigma^2, \mathbb E[Y_i^4] = \kappa $$
            2. 展開
                $$ \left(\sum_{i=1}^n Y_i\right)^4 = \sum_{i=1}^n Y_i^4 + 4\sum_{i\ne j} Y_i^3Y_j + 6\sum_{i < j}Y_i^2Y_j^2 + 12\sum_{i < j < k} Y_i^2Y_jY_k + 24\sum_{i < j < k < l} Y_iY_jY_kY_l \\ = n\kappa + 3n(n-1)\sigma^4 $$
                - $4$
                    $$ \sum_{i=1}^n Y_i^4 = n\kappa $$
                - $3 \times 1$
                    $$ 4\sum_{i\ne j} Y_i^3Y_j = 4(n-1) \mathbb E[Y_i^3Y_j] = 4(n-1)\mathbb E[Y_i^3]\mathbb E[Y_j] = 0 $$
                - $2\times 2$
                    $$ 6\sum_{i < j}Y_i^2Y_j^2 = 6\cdot\binom{n}{2}\mathbb E[Y_i^2Y_j^2] = 6\cdot\frac{n!}{2!(n-2)!} \mathbb E[Y_i^2]\mathbb E[Y_j^2] = 3n(n-1)\sigma^4 $$
                - $2\times 1\times 1$
                    $$ 12\sum_{i < j < k} Y_i^2Y_jY_k = 12\cdot \binom{n}{3} \mathbb E[Y_i^2Y_jY_k] = 12\cdot \frac{n!}{3!(n-3)!}\mathbb E[Y_i^2]\mathbb E[Y_j] \mathbb E[Y_k] = 0 $$
                - $1\times 1 \times 1 \times 1$
                    $$ 24\sum_{i < j < k < l} Y_iY_jY_kY_l = 24 \cdot \binom{n}{4} \mathbb E[Y_iY_jY_kY_l] = 24\cdot \frac{n!}{4!(n-4)!}\mathbb E[Y_i]\mathbb E[Y_j] \mathbb E[Y_k] \mathbb E[Y_l] = 0
                    $$
            3. 期待値
                $$ \mathbb E[(\bar X_n - \mu)^4] = \frac{\mathbb E[(\sum Y_i)^4]}{n^4} \approx \frac{3\sigma^4}{n^2} $$
                $$ \mathbb E[(\bar X_n - \mu)^4] =O(\frac{1}{n^2}) $$
        - Etemadi’s trick
            $$ \mathbb E[|X|] < \infin $$
            - Truncation
                - 確率変数 X_i
                - 閾値 c_n
                $$ X_{i,n} = X_i \cdot 1_{|X_i| <c_n} $$
            - symmetrization
        - Kolmogorov’s maximum inequality
        - Kolmogorov’s two series theorem
        - Kolmogorov’s three series theorem
    - langevin方程式
        $$ \langle (\Delta x)^2 \rangle \propto t
        \\
        # m\frac{d^2 x}{d t^2}
        - \gamma \frac{d f}{d x}
        - R(t)
        \\
        # mx\frac{d^2 x}{d t^2}
        - \gamma x \frac{d f}{d x}
        - x R(t)
        \\
        \frac{m}{2} \frac{d^2 x^2}{d t^2}
        - m(\frac{d x}{d t})^2 = -\frac{x}{2} \frac{d x^2}{d t}
        - xR(t) \ ...\ (1)
        \\
        \frac{m}{2}\frac{d^2 \langle x^2 \rangle}{d t^2}
        - m \langle (\frac{d x}{d t})^2 \rangle = -\frac{x}{2} \frac{d \langle x^2 \rangle}{d t}
        - \langle xR(t) \rangle
        \\
        \frac{m}{2}\frac{d^2 \langle x^2 \rangle}{d t^2}
        - k_b T = -\frac{x}{2} \frac{d \langle x^2 \rangle}{d t} \ ...\ (2)
        \\
        # \frac{m}{2}\frac{d z}{d t} +\frac{x}{2} z
        k_b T \ ...\ (3)
        \\
        z(t) = C e^{- \frac{\gamma}{m} t} + \frac{2 k_b T}{\gamma}
        \\
        \beta t >> 1 \ ... (4)\\
        z(t) = \frac{d \langle x^2 \rangle}{dt} \simeq \frac{2 k_b T}{\gamma}
        \\
        \langle x^2(t) \rangle \simeq \frac{2 k_b T}{\gamma}t $$
        $$ (1)\ \frac{d x^2}{d t} = 2x \frac{d x}{d t}
        \\
        \frac{d^2 x^2}{d t^2} = 2\{\frac{d x}{d t}
        - x\frac{d^2 x}{d t^2}\}
        \\
        (2)\ \langle R(t) \rangle = 0, \langle x(t)R(t) \rangle = \langle x(t) \rangle \langle R(t) \rangle = 0
        \\
        \frac{m}{2} \langle (\frac{d x}{d t})^2 \rangle = \frac{1}{2} k_bT
        \\
        (3)\ z(t) := \frac{d \langle x^2 \rangle}{dt} $$
        - $R(t)$の重要性
            # $$ m\frac{\partial v}{\partial t}
            - \gamma v \\ z(t) = v_0 e^{- \frac{\gamma}{m} t} $$
            すぐに静止する
            $$ \hat R(t) \rightarrow \hat v(t) \rightarrow \frac{m}{2} \langle \hat v^2 \rangle = \frac{1}{2} k_bT $$
    - 拡散方程式
        粒子の空間当たり密度P(x, t)、粒子数N
        [https://www.sk.tsukuba.ac.jp/~kiyoshi/pdf/stochasticProcessShort.pdf](https://www.sk.tsukuba.ac.jp/~kiyoshi/pdf/stochasticProcessShort.pdf)
- 確率分布 probability distribution
    - 分布の特徴量 feature of distribution
        - 母数 parameter
        - 台 support
        - 確率密度関数 PDF
        - 累積分布関数 CDF
        - 平均値/期待値 mean/average
        - 分散 variance
        - 歪度 skewness
        - 尖度 kurtosis
        - entropy
        - 確率母関数 probability generating function
        - 積率母関数 moment generating function
        - 特性関数 characteristic function
    - 変換 transform
        ![image.png](attachment:8f0d6e28-8a9e-43e3-ab1f-9424fcad0af2:image.png)
    - 指数型分布族 exponential family
    - 離散分布 discrete
        - 指数型分布族 exponential family
            - Bernoulli
                $$ Bin(1, p) = p^k(1-p)^{1-k} $$
                - meaning
                    成功or失敗（結果が2種類）
            - Poisson
                $$ Po(\lambda) = \frac{\lambda^k}{k!} e^{-\lambda} $$
                - parameter
                    $\lambda$ : the average rate of occurrence of events
                    k : the number of events
                - moment
                    - expectation
                        $$ \mathbb E[X] = \sum_{k=1}^\infin k \mathbb P(X = k) \\ = \sum_{k=1}^\infin ke^{-\lambda}\frac{\lambda^k}{k!} \\ = e^{-\lambda} \sum_{k=1}^\infin \frac{\lambda^k}{(k-1)!} \\ = e^{-\lambda} \lambda \sum_{k=1}^\infin\frac{\lambda^{k-1}}{(k-1)!} \\ = \lambda e^{-\lambda} \sum_{k=0}^\infin \frac{\lambda^k}{k!} \\ = \lambda e^{-\lambda} e^{\lambda} \\= \lambda $$
                    - variance
                        $$ \mathbb E[X^2] = \mathbb E[X(X-1)] + \mathbb E[X] \\ = \sum_{k=2}^\infin k(k-1) e^{-\lambda}\frac{\lambda^k}{k!} + \lambda \\ = e^{-\lambda} \sum_{k=2}^\infin \frac{\lambda^k}{(k-2)!} + \lambda \\ = \lambda^2 e^{-\lambda} \sum_{k=2}^\infin \frac{\lambda^{k-2}}{(k-2)!} + \lambda \\ = \lambda^2 e^{-\lambda} e^\lambda + \lambda \\ = \lambda^2 + \lambda $$
                        $$ Var(X) = \mathbb E[X^2] - (\mathbb E[X])^2 \\ = \lambda^2 + \lambda - \lambda^2 \\ = \lambda $$
                - Poisson is the limit of Binomial
                    $$ np = \lambda \\ p = \frac{\lambda}{n} $$
                    $$ \binom{n}{x} \ p^x(1-p)^{n-x} \\ = \frac{n!}{x! (n-x)!} \left(\frac{\lambda}{n}\right)^x \left(1-\frac{\lambda}{n}\right)^{n-x} \\ = \frac{n(n-1)...(n-(x-1))}{x!} \frac{\lambda^x}{n^x} \left(1-\frac{\lambda}{n}\right)^n \left(1-\frac{\lambda}{n}\right)^{-x} \\ = \frac{1(1-\frac{1}{n})...(1-(\frac{x-1}{n}))}{x!} \lambda^x \left(1-\frac{\lambda}{n}\right)^n \left(\left(1-\frac{\lambda}{n}\right)^n\right)^{-\frac{x}{n}} \\ \xrightarrow{n\to\infty} \frac{1(1-0)...(1-0)}{x!} \lambda^x e^{-\lambda} e^{-\lambda\cdot 0} \\ = \frac{\lambda^x}{x!}e^{-\lambda} $$
                - example
                    - earthquake
            - 二項分布 binomial
                $$ Bin(n, p) = \binom{n}{k} \ p^k(1-p)^{n-k} $$
                - meaning
                    n回Bernoulli試行の成功回数
                - moment
                    - expectation
                        $$ \mathbb E[X] = \int x \binom{n}{x} \ p^x(1-p)^{n-x}dx \\ = \sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = \sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = np\sum_{k = 0}^n \frac{(n-1)!}{(k-1)!(n-k)!} \ p^{k-1}(1-p)^{n-k} \\ = np $$
                    - variance
                        $$ \mathbb E[X^2] = \int x \binom{n}{x} \ p^x(1-p)^{n-x}dx \\ = \sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = \sum_{k = 0}^n (k(k-1)+k)\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = \sum_{k = 0}^n k(k-1)\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} +\sum_{k = 0}^n k\frac{n!}{k!(n-k)!} \ p^k(1-p)^{n-k} \\ = n(n-1)p^2\sum_{k = 0}^n \frac{(n-2)!}{(k-2)!(n-k)!} \ p^{k-2}(1-p)^{n-k} +\sum_{k = 0}^n \frac{(n-1)!}{(k-1)!(n-k)!} \ p^{k-1}(1-p)^{n-k} \\ = n(n-1)p^2 + np $$
                        $$ Var(X) = n(n-1)p^2 + np -(np)^2 \\ = np - np^2 \\ = np(1-p) $$
                - 正規近似
                - 再生性
            - 負の二項分布 negative binomial
                $$ NB(k, p) = \binom{x+r-1}{k} p^r(1-p)^k $$
                - meaning
                    k回成功までの失敗回数
                - expectation
                    $$ \sum_{x = 1}^\infin x \binom{x+k-1}{x} p^k(1-p)^x \\ = p^k \sum_{x = 1}^\infin x \frac{(x+k-1)!}{x!(k-1)!}(1-p)^x $$
                - 幾何分布の和
                    負の二項分布は幾何分布の和で表すことが可能
                    - Xは負の二項分布に従う確率変数
                    - Yは幾何分布に従う確率変数
                    $$ X = \sum_{k = 1}^n Y_k $$
            - 幾何分布 geometric
                - 成功までの試行回数 $X = 1, 2, ...$
                    $$ Geo(p) = p(1-p)^k $$
                - 成功までの失敗回数 $X = 0, 1, ...$
                    $$ Geo(p) = p(1-p)^{k-1} $$
                - theorem
                    - 無記憶性 memoryless
            - 多項分布 multinomial
                $$ \frac{n!}{k_1!\ ...\ k_m!}p_1^{k_1}\ ...\ p_m^{k_m} $$
                - meaning
                    結果がK種類（二項分布の一般化）
        - 離散一様分布 discrete uniform
            $$ \forall n \in \{1, ..., N\}, P(X=n) = \frac{1}{N} $$
        - 超幾何分布 hypergeometric
            $$ HG(N, M, n) = \frac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}} \\ \max\{0, n-(N-M)\} \leq k \leq \min\{n, M\} $$
            - meaning
                赤玉M個、白玉N-M個から
                n個を非復元無作為抽出
                した時の赤玉の個数
            - 有限母集団補正 finite population correction
    - 連続分布 continuous
        - 指数型分布族 exponential family
            - 正規分布 normal/gauss
                - 母数 parameter
                    - average
                    - variance
                - 確率密度関数 probability density function
                    $$ N(\mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(−\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} $$
                - 統計量 statistics
                    - 期待値 expectation
                        $$ \left. \frac{d}{dt}\mathbb E[e^{tX}]\right|_{t=0} \\ = \left. \frac{d}{dt} \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) \right|_{t=0} \\ = \left. (\mu +\sigma t)\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\right|_{t=0} \\ = \mu $$
                    - 分散 variance
                        $$ \left. \frac{d^2}{dt^2}\mathbb E[e^{tX}]\right|_{t=0} \\ = \left. \frac{d^2}{dt^2} \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) \right|_{t=0} \\ = \frac{d}{dt} \left. (\mu +\sigma t)\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\right|_{t=0} \\ = \left. \sigma\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\right|_{t=0} \\ = \sigma $$
                - 積率母関数 moment-generating function
                    $$ \mathbb E[e^{tX}] = \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) $$
                    - proof
                        $$ \mathbb E[e^{tX}] \\ = \int e^{tx}\frac{1}{\sigma \sqrt{2\pi}}\exp{\left(−\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(tx−\frac{(x−\mu)^2}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(\frac{2x\sigma^2 t}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{ x^2 -2x(\mu+\sigma^2 t) +\mu^2}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{ x^2 -2x(\mu+\sigma^2 t)
                        - (\mu+\sigma^2 t) ^2 -2\mu\sigma^2t -\sigma^4 t^2}{2\sigma^2}\right)}dx \\ = \int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{(x -(\mu+\sigma^2 t))^2}{2\sigma^2} + \mu t + \frac{1}{2}\sigma^2 t^2\right)}dx \\ = \exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\int \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(-\frac{(x -(\mu+\sigma^2 t))^2}{2\sigma^2}\right)}dx \\ =\exp \left(\mu t + \frac{1}{2}\sigma^2 t^2\right) $$
                - 特性関数 characteristic function
                    $$ \mathbb E[e^{itX}] = \exp \left(i\mu t - \frac{1}{2}\sigma^2 t^2\right) $$
                    - proof
                        # $$ \mathbb E[e^{itX}] = \int_{-\infin}^\infin e^{itx} \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(−\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} dx \\
                        # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{\left(itx −\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} dx \\ = \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{\left(itx −\frac{1}2\left(\frac{x−\mu}{\sigma}\right)^2\right)} dx \\
                        # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\frac{x^2 −2\mu x - 2it\sigma^2x + \mu^2 }{\sigma^2}\right) \right) } dx \\
                        # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\frac{(x−(\mu +it\sigma^2))^2 - (\mu +it\sigma^2)^2 + \mu^2 }{\sigma^2}\right) \right) } dx \\
                        # \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\left(\frac{x−(\mu +it\sigma^2)}{\sigma}\right)^2 - 2it\mu +t^2\sigma^2 \right) \right)}dx \\
                        \exp{ \left(it\mu -\frac{1}{2}t^2\sigma^2\right) } \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infin}^\infin\exp{ \left( −\frac{1}{2}\left(\left(\frac{x−(\mu +it\sigma^2)}{\sigma}\right)^2 \right) \right)}dx \\ = \exp{ \left(i\mu t-\frac{1}{2}\sigma^2 t^2 \right) } $$
            - 多変量正規分布 multivariate normal distribution
                $$ \frac{1}{\sqrt{(2 \pi)^k\det \Sigma}} \exp \left(-\frac{1}{2}(\bm x -\bm \mu)^\top \Sigma^{-1}(\bm x - \bm \mu)\right) $$
            - 指数分布 exponential
                - probability density function
                    $$ \exp(\lambda) = \left\{ \begin{matrix} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{matrix} \right. $$
                - moment
                    - expectation
                        $$ \mathbb E[X] \\ = \int_0^\infin x \lambda e^{-\lambda x} dx \\ = \lambda \int_0^\infin x e^{-\lambda x} dx \\ = \lambda (\left[-\frac{x}{\lambda}e^{-\lambda x}\right]_0^\infin -\int_0^\infin -\frac{1}{\lambda}e^{-\lambda x}dx)\\ = \int_0^\infin e^{-\lambda x}dx \\ = \left[-\frac{1}{\lambda}e^{-\lambda x}\right]_0^\infin \\ = \frac{1}{\lambda} $$
                    - variance
                        $$ \mathbb E[X^2] \\ = \int_0^\infin x^2 \lambda e^{-\lambda x} dx \\ = \lambda \int_0^\infin x^2 e^{-\lambda x} dx \\ = \lambda (\left[-\frac{x^2}{\lambda}e^{-\lambda x}\right]_0^\infin -\int_0^\infin -\frac{2x}{\lambda}e^{-\lambda x}dx)\\ = \frac{2}{\lambda}\int_0^\infin xe^{-\lambda x}dx \\ = \frac{2}{\lambda^2}
                        $$
                        $$ Var(X) = \frac{2}{\lambda^2} - \left(\frac{1}{\lambda}\right)^2 = \frac{1}{\lambda^2} $$
            - gamma
                - parameter
                    $\lambda> 0$ : rate parameter
                    $\alpha > 0$ : shape parameter
                $$ Gam(\alpha, \lambda) = \left\{ \begin{matrix} \frac{1}{\Gamma(\alpha)} \lambda^\alpha x^{\alpha-1}e^{-\lambda x} &(x>0) \\ 0 & (x \leq0) \end{matrix} \right.
                $$
                $$ \Gamma(\alpha) = \int_{0}^\infin x^{\alpha-1} e^{-x}dx $$
                - theorem
                    - $\Gamma(1) = 1$
                    - $\Gamma(\frac{1}{2}) = \sqrt{\pi}$
                    - $\Gamma(\alpha+1) = \alpha\Gamma(\alpha)$
                    - $\Gamma(n+1) = n!$
                    - $Gam(\frac{1}{2}, \frac{1}{2}) = N(0, 1)$
                    - $Gam(\frac{n}{2}, \frac{1}{2}) = \chi^2()$
                - expectation
                    $$ \mathbb E[X] = \int_{0}^\infin \frac{1}{\Gamma(\alpha)} \lambda^\alpha x^{\alpha}e^{-\lambda x} \\ = \frac{\alpha}{\lambda}\int_{0}^\infin \frac{1}{\Gamma(\alpha+1)} \lambda^{\alpha+1} x^{\alpha}e^{-\lambda x} \\ =\frac{\alpha}{\lambda} $$
                - variance
            - beta
            - xi
                - Z_1, …, Z_k 標準正規分布
                $$ \chi^2 = \sum_{k=1}^nZ_k^2 $$
                - 再生性
            - Dirichlet
            - Weibull
                故障する確率など
                - parameter
                    - scale $\lambda$
                    - shape $k$
                - PDF
                - CDF
                    $$ 1-\exp(-(\frac{t}{\tau})^m) $$
                    ![Weibull_CDF.svg.png](attachment:f97313c8-cf5c-4b0c-997c-813baddf0d75:Weibull_CDF.svg.png)
        - 連続一様分布 continuous uniform
        - 対数正規分布 logarithm
            - 母数 parameter
            - PDF
                $$ N(\mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}}\exp{\left(−\frac{1}2\left(\frac{\ln x−\mu}{\sigma}\right)^2\right)} $$
            - 積率 moment
                - 期待値 expectation
                    $$ \exp({\mu + \frac{\sigma^2}{2}}) $$
                - 中央値 median
                    $$ \exp (\mu) $$
                - 最頻値 mode
                    $$ \exp (\mu -\sigma^2) $$
        - 複素正規分布 complex normal
        - t
            - 標準正規分布 Z
            - カイ二乗分布 W
            $$ t = \frac{Z}{\sqrt{\frac{W}{n}}} $$
        - F
            - カイ二乗分布 X, Y
            - 標本の大きさ n, m
            $$ F = \frac{\frac{X}{n}}{\frac{Y}{m}} $$
        - Cauchy
            $$ \frac{1}{\pi} \frac{\sigma}{\pi x^2 + \sigma^2} $$
        - logistic/sigmoid
            $$ \frac{1}{1+\exp(-x)} $$
        - levy
            - PDF
                $$ \sqrt \frac{c}{2\pi} \frac{\exp(-\frac{c}{2x})}{x^{\frac{3}{2}}} $$
                ![image.png](attachment:5b92e06d-0331-4bdb-bf72-069cd582325f:image.png)
            - CDF
        - Gomperts
        - Frechet
            - parameter
                - location
                - scale
                - shape
            - PDF
            - CDF
                $$ \exp(-(\frac{x-m}{s})^{-\alpha}) $$
                ![Frechet_cdf.svg.png](attachment:5e9e15f3-5e14-426b-9442-72e975062081:Frechet_cdf.svg.png)
        - Gumbel
            - parameter
                - location $\mu$
                - scale $\beta$
            - PDF
            - CDF
                $$ \exp(-\exp(-\frac{x-\mu}{\beta})) $$
                ![Gumbel-Cumulative.svg.png](attachment:73734e5e-ae08-46e8-b8cc-c3469410af3b:Gumbel-Cumulative.svg.png)
        - maxwell
            熱力学的平衡状態において気体分子の速度が従う分布関数
            - PDF
                $$ \sqrt{\frac{2}{\pi}} \frac{x^2}{a^3} \exp(-\frac{x^2}{2a^2}) $$
                ![image.png](attachment:29431730-b02a-42ac-a218-43879f7ac32d:image.png)
            - CDF
            [マクスウェル分布](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%AF%E3%82%B9%E3%82%A6%E3%82%A7%E3%83%AB%E5%88%86%E5%B8%83)
        - Rayleigh
            - 正規分布 X, Y
            - PDF
                $$ \frac{x}{\sigma^2}\exp(-\frac{x^2}{2\sigma^2}) $$
            - CDF
                $$ 1-\exp(-\frac{x^2}{2\sigma^2}) $$
- 確率過程 stochastic process
    - 確率空間 $(\Omega, \mathcal F, P)$
    - 確率変数 X
        $$ X :T\times \Omega \to \R \\ \forall t \in T, A \in \mathcal B(\R), \{\omega \in \Omega|X(t, \omega) \in A\} \in \mathcal F $$
        for all t in T, X(t,•) is F-measurable
    - 時間(全順序集合) T
        - 離散確率過程 : $\N$
        - 連続確率過程 : $\R_+$
    $$ \{X_t\}_{t \in T} $$
    これを確率過程という
    $X(t)$ は任意の時間tで確率変数となる
    - 軌跡 path
        $$ X(t, \omega): \Omega^T \to \R^T, \forall t \in T $$
    - 情報系/情報増大系 filtration
        - probability space $(\Omega, \mathcal F, P)$
        $$ \{\mathcal F_t\}_{t\in T} \\ \forall s, t \in T, s < t \Rightarrow \mathcal{F}_s \subset \mathcal{F}_t \subset \mathcal{F} $$
        意味「時間の経過により情報が増加」
        all available information in t is contained
        - 適合過程 adapted process
            $$ \forall t \in T, A \in \mathcal B(\R), \{\omega \in \Omega|X_t(\omega) \in A\} \in \mathcal F_t $$
            for all t in T, X(t, •) is F-measurable
            意味「未来が予測不可能」
        - 可予測性 predictable
        - 情報付き確率空間 filtered probability space 確率基底 stochastic basis
            $$ \{\Omega, \mathcal F, \{\mathcal F_t \}_{t \in T}, P\} $$
        - 条件付き期待値 conditional expectation with filtration
            $$ \mathbb E[X_t|\mathcal F_s] $$
            the expectation of X_t based on the info in t
    - 定常性 stationary
        - 弱定常性 weak stationary
            - 時間差k
            $$ \mathbb E[y_t] = \mu \\ var(y_t) = \sigma^2 \\ cov(y_t, y_{t-k}) = \gamma_k $$
            共分散は時間差に依存
        - 強定常性 strict stationary
            $$ f(y_t, ..., y_{t+l}) = f(y_{t+k}, ..., y_{t+k+l}) $$
    - 連続性 continuous
        - 零集合 N
        $$ \forall \omega \in \Omega/N, \forall t \in T, \forall \epsilon > 0, \lim_{h \to 0} P(|X(t+h, \omega)-X(t, \omega)| < \epsilon)=0 $$
        for almost every path on the X, X is continuous
        - 平均二乗連続性 mean square continuous
            $$ \lim_{h\to 0} \mathbb E[|X(t+h) -X(t)|^2] = 0 $$
    - 増分 increments
        - 独立増分性 independent increment
            $$ \forall t_1,s_1,t_2,s_2 \in T, \\ s_1 \leq t_1 \leq s_2 \leq t_2 \Rightarrow \\ \mathbb P[X_{t_1}-X_{s_1} \cap X_{t_2}-X_{s_2}] = \mathbb P[X_{t_1}-X_{s_1}] \mathbb P[X_{t_2}-X_{s_2}] $$
            all increments are independent on each other
        - 定常増分性 stationary increment
            $$ \forall t,s\in T, \\ s \leq t\Rightarrow \\ X_{s+h} - X_{s} \sim X_{t+h} - X_{t} $$
            時間差が等しい増分は分布が等しい
    - martingale
        - probability space $(\Omega, \mathcal F, P)$
        - filtration F
        - adapted stochastic process M_t
        $$ \forall s, t \in T, \mathbb E[X_t | \mathcal F_s] = X_s $$
        - sub-martingale
            $$ \forall s, t \in T, \mathbb E[X_t | \mathcal F_s] \geq X_s $$
        - super-martingale
            $$ \forall s, t \in T, \mathbb E[X_t | \mathcal F_s] \leq X_s $$
    - Markov property
        - Markov chain (discrete)
            $$ \mathbb P(X_{n+1}= x_{n+1}|X_n = x_n, X_{n-1} = x_{n-1} ..., X_0= x_0) = \mathbb P(X_{n+1}= x_{n+1}|X_n = x_n) $$
            過去 past : $X_{n-1} ..., X_0$
            現在 present : $X_n$
            未来 future : $X_{n+1}$
            - time homogeneous Markov chain/process
                $$ P\{X_{n+1} = y | X_n = x\} = P\{X_{m+1} = y | X_m = x\}, \forall n, m \in \N $$
            - 確率遷移行列 probability transition matrix
                $$ [P_{ij}]\\ P_{ij} = \{X_{n+1} = j | X_n = i\},\ i, j \in \{1, 2, ..., m\} $$
                - 到達可能性
                - 通信類/同値類 communicating class
                - 閉じた集合
            - Chapman-Kolmogorov equation
                $$ P(x_3, t_3|x_1, t_1)=\int dx_2 P(x_3, t_3|x_2,t_2) P(x_2, t_2|x_1,t_1) $$
            - 状態の分類
                - 到着可能
                    $$ i \to j : \exist n \geq 0, P_{ij} > 0 $$
                    - $i \to i$
                        $$ P_{ii}^{(0)} = 1 $$
                - 相互到着可能
                    $$ i \leftrightarrow j : i \to j \land j \to i $$
                    この二項関係において同値類が構成可能
                    - 同値
                        - 反射律
                        - 対称率
                        - 推移律
                    - 既約
                        $A \subset S$の要素が互いに相互到着可能
                    - 既約なマルコフ連鎖
                        Sが一つの同値類から構成される
                    - 集合Aが閉じている
                        $$ \forall i \in A, \sum_{j \in A}P_{ij} = 1 $$
                        $$ \Rightarrow k \in A, P_{ik} = 0 $$
                    既約かつ閉じていれば同値類
                    - 再帰性
                        - def
                            $$ n \geq 1, f_{ij}^{(n)} = P(X_n = j, X_r \ne j, \forall r, 1 \leq r \leq n-1 | X_0 = i) $$
                        - 初期通過確率
                            便宜上
                            $$ f_{ij}^{(0)} = 0, (f_{ii}^{(0)} = 0) $$
                            $P_{ij}^{(n)}$ は初めてである必要はない
                            $$ f_{ij}^{(1)} = P_{ij}^{(1)} = P_{ij} $$
                        - 最終推移確率
                            - def
                                $$ f_{ij} = \sum_{n = 1}^\infin f_{ij}^{(n)} \leq 1 $$
                            単調収束定理より収束
                            - $i = j$
                                - 再帰的
                                    $$ g_i = f_{ii} = 1 $$
                                - 非再帰的
                                    $$ g_i = f_{ii} = -1 $$
                                    非再帰的とは戻ってこれないのではなく戻ってこれない確率がある
                        - 初期通過時刻
                            - def
                                $$ T_i = \inf \{n \geq 1 | X_n = i\} $$
                            $$ f_{ii}^{(n)}= P(T_i = n| X_0 = i) $$
                            $$ 1 - g_i = P(T_i = \infin | X_0 = i) $$
                            $$ g_i = P(T_i < \infin | X_0 = i) = \sum_{n = 1}^\infin f_{ii}^{(n)} $$
                            $g_i^m$ : m回戻ってくる(m乗している)
                            - $m \to \infin$
                                - 非再帰的
                                    $$ g_i < 1 \Rightarrow \lim_{m \to \infin} g_i^m = 0 $$
                                    無限回戻ってくることは不可能
                                - 再帰的
                                    $$ g_i^m = 1 $$
                        - 再帰性の判定
                            - lemma
                                $$ P_{ij}^{(n)} = \sum_{k = 1}^\infin f_{ij}^{(n)} P_{jj}^{(n-k)} $$
                            - theorem
                                再帰的
                                if and only if
                                $$ \sum_{n =1}^\infin P_{ij}^{(n)} = \infin $$
                            - cor
                                $$ \sum_{n =1}^\infin P_{ij}^{(n)} = \frac{f_{ij}}{1 - g_i} $$
            - 周期性
                $$ \exist n \geq 1, P_{ii}^{(n)} > 0 $$
                $$ I_i = \{n \in \N| P_{ii}^{(n)} > 0\} $$
                $I_i$ の最大公約数を周期 $d_i$
                - 非周期的
                    $$ d_i = 1 $$
                - theorem 1
                    $I_i$ は加法的な集合
                    $$ n, m \in I_i \Rightarrow n + m \in I_i $$
                    - proof
                        $$ \exist n, m \in \N , P_{ii}^{(n)} > 0, P_{ii}^{(m)} > 0 $$
                        Chapman-Kolmogorov equationより
                        $$ P_{ii}^{(n+m)} \geq P_{ii}^{(n)}P_{ii}^{(m)} > 0 $$
                - remark
                    $$ 2, 3 \in I_i $$
                    ならば非周期的
                - gcd
                    $$ \gcd(A_1, ..., A_m) = d \\ \Rightarrow \exist c_i \in \Z, c_1 A_1 + \cdots + c_M A_M = d $$
                - theorem 2
                    $I_i$ は差が $d_i$ の2つの $I_i$ の要素を含む
                    $$ \exist n_1, ..., n_M \in I_i, \gcd(A_1, ..., A_m) = d \\ \Rightarrow \exist c_i \in \Z, c_1 A_1 + \cdots + c_M A_M = d $$
                    $$ c_i > 0, (1 \leq i \leq S) \\ c_i > 0, (S \leq i \leq M) $$
                    としても一般性を失わない
                    $$ n_1 c_1 + \cdots + n_Sc_S = (-c_{S+1})n_{S+1} + \cdots + (-c_M) n_M + d_i $$
                    $$ l = n_1 c_1 + \cdots + n_Sc_S \in I_i \\ m = (-c_{S+1})n_{S+1} + \cdots + (-c_M) n_M \in I_i $$
                    $$ l - m = d_i $$
                - theorem 3
                    $$ I_i \ne \phi \\ \exist n_1 \in I_i, n_1 + n d_i \in I_i, \forall n \geq 0 $$
                    $$ n_1, n_1 + d_i, n_1 + 2d_i , ... \in I_i $$
                    - proof
                        $$ \exist n_0 \in \N, n_0, n_0 + d_i \in I_i $$
                        $I_i$ の加法性より
                        $$ K_2 = \{2n_0, 2n_0+d_i, 2n_0+2d_i, \} \subset I_i \\ K_j = \{jn_0, jn_0+d_i, \cdots ,jn_0+jd_i, \} \subset I_i $$
                        $$ K_{j + d_i} = \{(j + d_i)n_0, \cdots ,(j + d_i)(n_0+d_i)\} \subset I_i $$
                        $$ (j + d_i)n_0 + k d_i \in K_{j + d_i}, (0 \leq k \leq j + d_i) $$
                        $$ (j + d_i)n_0 + (j - n_0)d_i \\ = j n_0 + jd_i = P \\ K_j \cap K_{j + d_i} $$
                - theorem 4
                    $$ i \leftrightarrow j \Rightarrow d_i = d_j $$
        - Markov process (continuous)
            - filtration $\{F_t\}_{t \in T}$
            - X_t is adapted F_t
            - Borel measurable f, g
            $$ \forall s, t \in T, \mathbb E[f(X_t)| \mathcal F_s] = g(X_s) $$
    - Poisson process
        ||時間|回数|
        |---|---|---|
        |二項過程|幾何分布|二項分布|
        |Poisson 過程|指数分布|Poisson 分布|
        - 計数過程 counting process
            $$ \{N_t\}_{t \in \N} $$
            - 定義 def
                - 初期値 initial condition
                    $$ N_0 = 0 $$
                - 非負整数 non-negative integer
                    $$ N_t \in \Z_+ $$
                - 広義単調性 non-decreasing
                    $$ s < t \Rightarrow N_s \leq N_t \\ \forall s, t \in \N $$
            - 定義 def
                微小区間 h
                - 定常独立増分
                - N = 0
                    $$ N(0) = 0 \Leftarrow P(N(0) = 0) = 1 $$
                - N = 1
                    $$ P(N(h) = 1) = \lambda h + o(h) $$
                - N > 1
                    $$ P(N(h) \geq 2) = o(h) $$
            - 区間 (0, t], k 回
                $$ P_k(t) = P(N(t) = k | N(0) = 0) \\ = P(N(t) = k) \\
                $$
            - 区間 (0, h], k 回
                $$ P_k(h) = P(N(h) = k)\\ = \left\{ \begin{matrix} o(h) & k \geq 2 \\ \lambda h + o(h) & k = 1 \\ 1 - \lambda h + o(h) & k = 0 \end{matrix} \right. $$
                $$ P_k(h) = P(N(h) = k) \\ = P(N(h) - N(0) = k) \\ stationary \\ = P(N(t+h) - N(t) = k) \\ independent\ increments \\ = P(N(t+h) - N(t) = k|N(t)-N(0 = i)) $$
                区間 (0, t] でi回事象が発生 区間 (t, t+h] でk回事象が発生
                することは独立
                上記を考慮し、帰納的に求める
                - k = 0
                    $$ P_0 (t+h) = P(N(t+h) - N(t) = 0|N(t)-N(0) = 0) \\ = P(N(t+h) - N(t) = 0)P(N(t)-N(0) = 0) \\ = P(N(h) - N(0) = 0)P(N(t)-N(0) = 0) \\ = P_0(h)P_0(t) \\ = P_0(t)(1 -\lambda h + o(h)) $$
                    $$ \frac{P_0(t+h) - P_0(t)}{h} = -\lambda P_0(t) + o(1) \\ h \to 0 \\ \frac{d P_0(t)}{dt} = -\lambda P_0(t) \\ P_0(t) = Ce^{-\lambda t} $$
                    - initial condition
                        $$ P_0(0) = P(N(0) = 0) = 1 $$
                    $$ P(t) = e^{-\lambda t} $$
                - k > 0
                    $$ P_k(t+h) = P_k(t) P_0(h) + P_{k-1}P_1(h) + \sum_{i = 2}^k P_{k-i}(t) P_i(h) \\ = P_k(t)(1 - \lambda h + o(h)) + P_{k -1} (t) (\lambda h + o(h)) + o(h) $$
                    $$ \frac{P_k(t+h) - P_k(t)}{h} = -\lambda P_k(t) + \lambda P_{k-1}(t) + o(1) \\ \frac{d P_k(t)}{d t} =\lambda (P_{k-1}(t) - P_k(t)) \\ e^{\lambda t} (P_k'(t) + \lambda P_k(t)) \\ = \lambda e^{\lambda t} P_{k-1} (t) $$
                    $$ \frac{d}{dt} (e^{\lambda t} P_k(t)) = \lambda e^{\lambda t} P_{k-1}(t) $$
                    $$ P_0(0) = P(N(0) = 0) = 1 \\ P_k (0) = P(N(0) = k) = 0 $$
                    - k = 1
                        $$ \frac{d}{dt} (e^{\lambda t} P_1(t)) = \lambda \\ e^{\lambda t} P_1(t) = \lambda t + C \\ t = 0, 0 = C \\ P_1(t) = (\lambda t)e^{-\lambda t} $$
                    - k = k
                        $$ P_{k-1}(t) = e^{-\lambda t}\frac{(\lambda t)^{k-1}}{(k-1)!} $$
                        $$ P_k(t) = e^{-\lambda t}\frac{(\lambda t)^k}{k!} $$
            - 到着時間分布
                - 確率変数
                    $$ t_1, t_2, ... $$
                    $$ T_1, T_2, ... $$
                    $$ T_i = t_1 + ...+ t_i $$
                - $t_1$ の分布
                    $$ P(t_1 \leq S) = 1 -P(t_1 > S) = 1-P(N(S) = 0) = 1 - e^{-\lambda S} $$
                    S以降に1回目が起こる = 時刻Sで事象は発生していない
                    $$ f_{t_1}(S) = \lambda e^{-\lambda S} \\ f_{t_2 | t_1}(t | S) = \frac{f_{t_1, t_2}(S, t)}{f_{t_1}(S)} \\ F_{t_2 | t_1}(t | S) = \int_{-\infin}^t f_{t_2 | t_1}(u | S)du \\ = P(t_2 \leq t | t_1 = S) \\ = P(t_1 + t_2 \leq S +t | t_1 = S) \\ = 1 - P(t_1 + t_2 > S +t | t_1 = S) $$
                    $$ N(S + t) = 1, N(S) = 1 \\ N (S + t) - N(S) = 1, N(S) - N(0) = 1 $$
                    $$ = 1 - P(N(S+t)-N(S) = 0 | N(S) - N(0) = 1) \\ independent \ increments \\ = 1 - P(N(S+t)-N(S) = 0) \\ stationary \\ = 1 - P(N(t)-N(0) = 0) \\ = 1 - e^{-\lambda t} $$
            - meaning
                $N_T$ : the count of events
        - 二項過程 binomial process
            $$ \mathbb P(N_t = n) = \binom t n p^n (1-p)^{t-n} $$
            成功確率p のBernoulli分布
            $N_n$は成功の回数
            - 独立増分
            - 定常増分
            二項過程は定常独立増分の計数過程
            - 時間の分布が幾何分布
            - 回数の分布が二項分布
        - Poisson process
            - the stochastic process of independent and stationary increments $(N_t)_{t \in T}$
            $$ P(N_t = k) = e^{-\lambda t} \frac{(\lambda t)^k}{k!} $$
            - the limit of the binomial process
                $$ (1-p)^{m-1}p = (1 - \lambda \Delta t)^{m-1} \lambda \Delta t \\ = (1 - \frac{\lambda t}{m} )^{m-1} \frac{\lambda}{m} $$
                $t = m \Delta t$ : time
                $p = \lambda \Delta t$ : probability
                - proof
                    $$
                    $$
            - counting process
    - gaussian process
    - 平均 average
        - 時間平均 time average
        - 確率集団平均 ensemble average
- 確率積分 stochastic calculus
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
- 確率微分方程式 SDE stochastic differential equation
    $$ dW_t^2 = \sigma^2dt $$
    - SDE
        $$ dX(t) = f(t, X(t))dt + g(t, X(t)) dW(t) $$
        f : drift
        g : diffusion coefficient
    - solution
        $$ x(0) = x_0 \\ x(T) = x_0 + \int_0^T f(t, X(t))dt + \int_0^T g(t, X(t)) dw $$
    - 一次線形確率微分方程式 linear stochastic differential equation
        $$ dX_t = f(a_t+b_tX_t)dt + g(c_t+d_tX_t) dW_t $$
    - 伊藤積分
        $$ \int f(x(t_i), w(t_i), t_i)dt+g(x(t_i), w(t_i), t_i)dw = \lim_{N}\sum_{i} f(x(t_i), w(t_i), t_i)(t_{i+1}-t_i)+g(x(t_i), w(t_i), t_i)(w(t_{i+1})-w(t_i)) $$
    - 伊藤の公式
        $$ dh(x, t) = \left(\frac{\partial h}{\partial t} + f \frac{\partial h}{\partial x} + \frac{1}{2}g^2 \frac{\partial^2 h}{\partial x^2} \right)dt + g \frac{\partial h}{\partial x}dw $$
        - 導出
            - 普通の全微分
                # $$ dh = \frac{\partial h}{\partial x} dx + \frac{\partial h}{\partial t} dt \\
                $$
    - Malliavin解析
        - malliavin derivative
            $$ DF = \sum_{i=1}^n \frac{\partial f}{\partial x_i} (W(t_1), ..., W(t_n))\cdot 1_{[0, t_i]} $$
            - property
                - linear
                    $$ D(aF+bG) = aDF+bDG $$
                - multiple
                    $$ D(FG) = F\cdot DG + G\cdot DF $$
                - chain
                    - smoothness function \phi
                    $$ D(\phi(F)) = \frac{d \phi(F)}{dF} \cdot DF $$
            - example
                - F = W_1
                    $$ D_t W_1 = 1_{[0, t_i]}(t) $$
                - F = W_1^2
                    $$ D_t (W_1^2) = 2W_1\cdot D_tW_1 = 2W_1 1_{[0, 1]}(t) $$
                - Hilbert space L^2
        - Skorohod calculus 発散作用素
            - probability process
                $$ u_t = \{u_t\}_{t\in[0, 1]} $$
            - Hilbert space L^2
            $$ \delta(u) = \int_0^T u_t dW_t $$
            - characteristics
                $$ \mathbb E[\braket {DF,u}_{L^2([0, 1])} ] = \mathbb E[F\cdot \delta(u)] \\ \braket {DF,u}_{L^2([0, 1])} = \int_0^T (D_tF)u_tdt $$
            - example
                $$ u_t = W_1\cdot 1_{[0,1]}(t) \\ \delta(u) = \int_0^1 W_1dW_1 = W_1(W_1-W_0)=W_1^2 $$
        - malliavin matrix
            - random variable
                $$ F=(F_1,...,F_d) $$
            $$ \sigma_{ij} = \langle DF_i, DF_j\rangle_{L^2([0, T])} $$
            - theorem
                if a malliavin matrix is regular, then probability density of F is absolutely continuous and smoothness
        - Clark-Ocone formula
            $$ F =\mathbb E[F] + \int_0^T \mathbb E[D_t F| \mathcal F_t] dW_t $$
        - Clark-Ocone-Haussmann formula
            $$ F =\mathbb E[F] + \int_0^T \mathbb E[D_t F| \mathcal F_t] dW_t $$
        - malliavin sobolev space
        - Hörmander's condition
    - white noise解析
    - Feynman-Kac formula
        - stochastic process X_s
            $$ d X_s = \mu(X_s, s)ds + \sigma(X_s, s)dW_s $$
        - boundary condition
            $$ u(x, T) = \phi(x) $$
        - PDE
            $$ \frac{\partial u}{\partial t} + \mu(x, t)\frac{\partial u}{\partial t} + \frac{1}{2} \sigma^2 (x, t)\frac{\partial^2 u}{\partial x^2} - k(x, t)u = 0 $$
        - solution
            $$ u(x, t) = \mathbb E_{t, x} \left[\exp\left(-\int_t^T k(X_s, s)ds\right)\phi(X_T)\right] $$
        - application for Black-sholes
            - stock
                $$ x =S $$
            - drift
                $$ \mu (S, t) = rS $$
            - diffusion
                $$ \sigma (S, t) =\sigma S $$
            - rate
                $$ k(S, t) = r $$
            - payoff
                $$ \phi(S_T) = V(S, T) $$
    - Girsanov theorem
    - Numéraire
    - 計算例
        - $dx = a\ dt$
            $$ x = \lim_N \sum_{i=1}^N a(t_{i+1}-t_i) \\ = x_0 + at
            $$
        - $dx = ax\ dt$
            $$ \frac{dx}{x} = a\ dt \\ \ln x = \lim_N \sum_{i=1}^N a(t_{i+1}-t_i) \\ = x_0 + at \\ e^x = e^{x_0+at}
            $$
        - $dx = aw\ dx$
        - $dx = b\ dw$
        - $dx = bx\ dw$
        - $dx = bw\ dw$
- pdf
    - probability essentials
        [978-3-642-55682-1.pdf](attachment:10bb1e2b-7f1e-454e-8f87-4138c396b1b1:978-3-642-55682-1.pdf)
    - probability_v5
        [probability_v5.pdf](attachment:4312cf9b-8762-41cd-93f5-1c2b96c82264:probability_v5.pdf)
    - investment theory class
- 応用確率論
    - 単調収束定理
        - 単調増大
            - 測度空間
            - 単調増加
                $$ A_1 \subset A_2 \subset ... \subset \mathcal F $$
            $$ \mu (\bigcup^\infin_{n=1} A_n) = \lim_{n \to \infin} \mu(A_n) $$
        - 単調減少
            - 測度空間
            - 単調減少
                $$ A_1 \supset A_2 \supset ... \supset \mathcal F $$
            $$ \mu (\bigcap^\infin_{n=1} A_n) = \lim_{n \to \infin} \mu(A_n) $$