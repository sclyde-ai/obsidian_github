---
alias:
    ['確率論', 'probability theory']
---
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
            \forall n \in \mathbb N, A_n \in \mathcal{F} \Rightarrow \bigcup_{n=1}^\infty A_n \in \mathcal{F} $$
        この時、Fを完全加法族/可算加法族/σ-加法族という。
        - theorem
            - 積集合を含む
                $$ \bigcap_{n= 1}^\infty A_n = (\bigcup_{n= 1}^\infty A_n^c)^c \\ A \cap B = (A^c \cup B^c)^c
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
                    $$ X = \mathbb R F_0 = \{(a, b) | a < b, \forall a, b \in \R\} $$
                    1. 開集合を全て追加
                        $$ \{(a, b) | a < b, \forall a, b \in \R\} $$
                    2. 2つの片側無限閉区間を全て追加（開区間の補集合）
                        $$ \{(-\infty, a], [b, \infty) | a < b, \forall a, b \in \R\} $$
                    3. 片側無限開区間を全て追加（開区間と片側無限閉区間の和集合）
                        $$ \{(-\infty, b) | \forall b \in \R\} \\ \{(a, \infty) | \forall a \in \R\} $$
                    4. 片側閉区間を全て追加（片側無限開区間の補集合）
                        $$ \{(-\infty, a] | \forall a \in \R\} \\ \{[b, \infty) | \forall b \in \R\} $$
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
                $$ (a,b) \\ [a, b] \\ [a, b) \\ {a} \\ \mathbb Q \\ \mathbb R/ \mathbb Q $$
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
                $$ 0 \leq \mu(A) \leq \infty, \forall A \in \mathcal{F},\\ \mu(\phi) = 0 $$
            - 完全加法性/可算加法性 countable additivity
                - A is disjoint
                    $$ \forall i, j \in \mathbb N, A_i \cap A_j \neq \phi $$
                $$ \mu(\bigcup_{n=1}^\infty A_n) = \sum_{n=1}^\infty \mu(A_n) $$
            - property
                - 単調性
                    $$ A \subset B \Rightarrow \mu(A) \leq \mu(B) \\ \forall A, B \in \mathcal{F} $$
                    - 証明
                        $$ A \subset B \Rightarrow B = A \cup (B/A) \\ \mu(B) = \mu(A) + \mu(B/A) \\ \mu(B/A) \geq0 \Rightarrow \mu(B) \geq \mu(A) $$
                - 劣加法性
                    $$ \mu(\bigcup_{n=1}^\infty A_n) \leq \sum_{n=1}^\infty \mu(A_n) \\ \{A_n\} \in \mathcal F $$
                    - 証明
                        $$ B_1=A_1, B_n = A_n/\bigcup_{i=1}^{n-1} A_i \\ \Rightarrow \forall i, j \in \mathbb N, B_i \cap B_j \neq \phi \\ B_n \subset A_n \\ \bigcup_{n=1}^\infty A_n = \bigcup_{n=1}^\infty B_n \\ \Rightarrow \mu(\bigcup_{n=1}^\infty A_n) = \mu(\bigcup_{n=1}^\infty B_n) = \sum_{n=1}^\infty B_n \leq \sum_{n=1}^\infty A_n
                        $$
                - 有限加法性
                - 上方連続性
                - 下方連続性
                - 極限（単調増加）
                    - 単調増加列A_n
                    $$ \mu(\lim_{n\to\infty}A_n) = \lim_{n\to\infty}\mu(A_n) $$
                    - proof
                        $$ A_n = \sum_{k=1}^n (A_k - A_{k-1})\\ \lim_{n\to\infty}A_n = \sum_{k=1}^\infty (A_k - A_{k-1}) $$
                        完全加法性より
                        $$ \mu(\lim_{n\to\infty}A_n) = \sum_{k=1}^\infty \mu(A_k - A_{k-1}) \\ = \lim_{n\to\infty}\sum_{k=1}^n (A_k - A_{k-1}) = \lim_{n\to \infty} \mu(A_n) $$
                - 極限（単調減少）
                    - 単調減少列A_n
                    - $\mu(A_1) < \infty$
                    $$ \mu(\lim_{n\to\infty}A_n) = \lim_{n\to\infty}\mu(A_n) $$
                    - proof
                        $$ \{A_1 - A_n | \forall n \in \mathbb N\} $$
                        は単調増加なので
                        [proof](https://www.notion.so/proof-216ec42dd04b81459d1aced407ccb78d?pvs=21)
                - 下極限
                - 上極限
                - 極限
            - example
                - 零測度 null measure
                    $$ \forall A \in \mathcal F, \mu_0(A) = 0 $$
                - counting measure 計数測度
                    $$ \mu_1 : \mathcal F \to [0, \infty] \\ \mu_1(F) = |F| $$
                - Delta/Dirac measure
                - Lebesgue measure
                    - closed interval [a, b]
                    $$ \mathbb P [a, b] = b-a $$
                    - open interval (a, b)
                        $$ (a,b) = \bigcup_{n=1}^\infty [a+\frac{1}{n}, b-\frac{1}{n}] \\ \mathbb P (a, b) = b-a $$
                        - preposition
                            sigma-algebra of Lebesgue integral contains all open interval
            - 有限加法測度 finite addictive measure
                - non-negative
                    $$ \forall A \in \mathcal{A}, 0 \leq \nu(A) \leq \infty, \nu(\phi) = 0 $$
                - finite additivity
                    - A and B are disjoint
                        $$ \forall A, B \in \mathcal{A}, A \cap B = \phi $$
                    $$ \nu(A \cup B) = \nu(A) + \nu(B) $$
            - 有限測度 finite measure
                $$ \forall X \in \mathcal{F}, \mu(X) < \infty $$
            - σ-有限測度 σ-finite
                - mesurable space (X, F)
                - measure u
                $$ \exists \{A_n\} \subset \mathcal F, A_n \uparrow X \land \mu(A_n) < \infty $$
                - another description
                    $$ \exists \{A_n\} \subset \mathcal F, X= \bigcup^\infty_{n=1} A_n \land \mu(A_n) < \infty $$
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
                    $$ \exists A \in \mathcal F, \mu(A) = \nu(A^c) = 0 $$
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
                            $$ \alpha = \sup_{N \in \mathcal F, \mu(N) = 0} \nu(N) \\ = \sup\{\nu(N) \in \mathbb R| \forall N \in \mathcal F, \mu(N)=0\} $$
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
            $$ 0 \leq X(\omega) < \infty $$
        - partition
            $$ \Pi = \{y_0, y_1, ..., \}\\ 0 = y_0 < y_1 < ... \\ [y_k, y_{k+1}] $$
            $$ || \Pi|| = \max_{1 \leq k \leq n} (y_k -y_{k-1}) $$
        - the lower Lebesgue sum
            $$ LS_{\Pi}^-(X) = \sum_{k=1}^\infty y_k \mathbb P(A_k) $$
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
            $$ \mathcal L(\bigcup_{n=1}^\infty B_n) = \sum_{n=1}^\infty \mathcal L(B_n) $$
    - convergence of integrals
        - random variable convergence
            - random variable sequence
            - probability space
            - null set N
            $$ \lim_{n \to \infty} X_n(\omega)= X(\omega), \forall \omega\in \Omega/N $$
        - strong law of large number
        - monotone convergence
            $$ 0 \leq X_1 \leq X_2 \leq ... \\ \lim_{n \to \infty} \mathbb E[X_n] = X\\ almost\ surely $$
            $$ 0 \leq f_1 \leq f_2 \leq ... \\ \lim_{n \to \infty} \int_{-\infty}^\infty f_n(x) dx= \int_{-\infty}^\infty f(x) dx\\ almost\ surely $$
            - corollary
                - countably many random variable
                    $$ X = \{x_0, x_1, ...\} $$
                $$ \mathbb E[X] = \sum_{k=0}^\infty x_k \mathbb P(X=x_k) $$
                - proof
                    $$ X_n = \sum_{k=0}^n x_k \mathbb I_{\{X=k\}} \\ \lim_{n \to \infty} X_n = X $$
                    $$ \mathbb E[X] = \lim_{n \to \infty} \mathbb E[X_n] = \lim_{n \to \infty} \sum_{k=0}^n x_k \mathbb P_{\{X=k\}} = \sum_{k=0}^n x_k \mathbb P_{\{X=k\}} $$
            - example (Petersburg paradox)
                E[X] is infinite, even though X is finite almost surely
        - dominated convergence
            - X_n
                $$ \lim_{n \to \infty} X_n = X $$
            - Y_n
                $$ \mathbb E[Y] < \infty \\ |X_n | < Y $$
            $$ \lim_{n \to \infty} \mathbb E[X_n] = \mathbb E[X] $$
            - f
            - g
                $$ \int_{-\infty}^\infty g(x) dx < \infty\\ |f_n| \leq g $$
            $$ \lim_{n \to \infty}\int_{-\infty}^\infty f_n(x) dx = \int_{-\infty}^\infty f(x) dx $$
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
                $$ B_n = \bigcup_{k=1}^n A_k ,B_{\infty} = \bigcup_{k=1}^\infty A_k \\
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
                    $$ f'(t_j^_) = \frac{f(t_{j+1})-f(t_j)}{t_{j+1}-t_j}, \exists t_j^_ \in [t_j, t_{j+1}] $$
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
                    $$ \mathcal{F} \subset 2^\Omega \\ \Omega \in \mathcal{F} \\ A \in \mathcal{F}, A^c \in \mathcal{F} \\ (A_n)_{n \in \mathbb N} \subset \mathcal{F}, \bigcup_{n \in \mathbb N} A_n \in \mathcal{F} $$
                    「事象の分類方法」
            確率測度 probability measure$$ (\Omega, \mathcal{F}, P) $$
            $\Omega$ 標本空間 sample space
            $\omega \in \Omega$ 標本点 sample point
            $F \in \mathcal F$ 事象 event
            - limit
                - limit supremum
                    $$ \limsup_{n \to \infty} A_n = \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k $$
                    $$ \forall n \in \mathbb N, \exists k \geq n, \omega \in A_k $$
                    「無限回A_nが起こる」
                    「事象が無限に頻繁に発生する」
                - limit infimum
                    $$ \liminf_{n \to \infty} A_n = \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} A_k $$
                    $$ \exists n \in \mathbb N, \forall k \geq n, \omega \in A_k $$
                    「ある時点以降ずっとA_nが起こり続ける」
                    「事象がある時点以降恒常的に発生する」
                - inequity
                    $$ \liminf_{n \to \infty} A_n \subset \limsup_{n \to \infty} A_n $$
                - convergence
                    $$ \liminf_{n \to \infty} A_n = \limsup_{n \to \infty} A_n $$
                    この時、事象列は収束するという
            - example
                - heads or tails
                - real number
                    $$ (\mathbb R \mathcal B(\R), \mu_X) $$
        - 確率測度 probability measure
            - 可測空間 measurable space $(\Omega, \mathcal F)$
                [可測空間 mesurable space $(\Omega, \mathcal F)$](https://www.notion.so/mesurable-space-Omega-mathcal-F-216ec42dd04b8114af34e95b07ec8c08?pvs=21)
            $$ \mathbb P : \mathcal{F} \rightarrow [0, 1] $$
            $$ \mathbb P(\Omega) = 1 $$
            - 加算加法性 countable additivity
                - A is disjoint
                    $$ \forall i, j \in \mathbb N, A_i \cap A_j = \phi $$
                $$ \mathbb P(\bigcup_{n = 1}^\infty A_n) = \sum_{n = 1}^\infty \mathbb P(A_n) $$
            - 離散 discrete
                $$ P(X=x) = p_i \\ \sum_i p_i = 1 \\ x \in \mathbb R$$
            - 連続 continuous
                $$ P(X \in A) = \int_A f(x)dx \in[0, 1] $$
                $$ P(a \leq X \leq b) = \int_a^b f(x) dx $$
            - property
                - $P(\phi) = 0$
                    $$ \Omega \in \mathcal F \Rightarrow \phi = A^c \in \mathcal F \\ \forall k \geq 1, A_k = \phi \ \Rightarrow \\ P(\phi) = P(\bigcup_{k=1}^\infty A_k) = \sum_{k=1}^\infty P(A_k) = \sum_{k=1}^\infty P(\phi) $$
                - finite additivity
                    - A is disjoint
                        $$ \forall i, j \in \mathbb N, A_i \cap A_j = \phi $$
                    $$ \Omega \in \mathcal F \Rightarrow \phi = A^c \in \mathcal F \\ \forall k \geq N+1, A_k = \phi \ \Rightarrow \\ P(\bigcup_{k=1}^\infty A_k) = \sum_{k=1}^\infty P(A_k) \\ P(\bigcup_{k=1}^N A_k) + P(\bigcup_{k=N+1}^\infty A_k) = \sum_{k=1}^N P(A_k) + \sum_{k=N+1}^\infty P(A_k) \\
                    P(\bigcup_{k=1}^N A_k) + P(\phi) = \sum_{k=1}^N P(A_k) + \sum_{k=N+1}^\infty P(\phi) \\ P(\bigcup_{k=1}^N A_k) = \sum_{k=1}^N P(A_k) $$
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
                    $$ A_k \in \mathcal F, P(\bigcup_{k=1}^\infty A_k) \leq \sum_{k=1}^\infty P(A_k) $$
                    - proof
                        $$ B_1 = A_1 \\ B_k = A_k/A_{k-1} $$
                        と定義すると
                        $$ A_k = \bigcup_{k=1}^n B_k \\ \bigcup_{k=1}^\infty A_k = \bigcup_{k=1}^\infty B_k $$
                        が成立する
                        $$ P(\bigcup_{k=1}^\infty A_k) = P(\bigcup_{k=1}^\infty B_k) $$
                        加算加法性より
                        $$ = \sum_{k=1}^\infty P(B_k) \\ = \lim_{n \to \infty }\sum_{k=1}^n P(B_k) $$
                        有限加法性より
                        $$ = \lim_{n \to \infty} P(\bigcup_{k=1}^n B_k) \\ = \lim_{n \to \infty } P(A_n) $$
                - 単調連続性（増加列）
                    $$ A_n \uparrow A \Rightarrow \mathbb P(A_n) \uparrow \mathbb P(A) $$
                    - description
                        $$ A_1 \subset A_2 \subset ... \\ \lim_{k\to \infty} P(A_k) = P(\lim_{k \to \infty} A_k) $$
                    - proof
                        $$ B_1 = A_1 \\ B_k = A_k/A_{k-1} $$
                        と定義すると
                        $$ A_k = \bigcup_{k=1}^n B_k \\ \bigcup_{k=1}^\infty A_k = \bigcup_{k=1}^\infty B_k $$
                        が成立
                        加算加法性より
                        $$ = \sum_{k=1}^\infty P(B_k) $$
                        劣加法性より
                        $$ \leq \sum_{k=1}^\infty P(A_k) $$
                - 単調連続性（減少列）
                    $$ A_n \downarrow A \Rightarrow \mathbb P(A_n) \downarrow \mathbb P(A) $$
                    - description
                        $$ A_1 \supset A_2 \supset ... \\ \lim_{k\to \infty} P(A_k) = P(\lim_{k \to \infty} A_k) $$
                - Fatouの補題
                    $$ P(\liminf A_k) \leq \liminf P(A_k) \\ \leq \\ \limsup P(A_k) \leq P(\limsup A_k) $$
                    - proof
                        $$ B_n = \bigcap_{k=n}^\infty A_k $$
                        $$ P(\liminf A_k) = P(\bigcup_{n=1}^\infty \bigcap_{k=1}^\infty A_k) = P(\bigcup_{k=1}^\infty B_n) = \lim P(B_n) \leq \liminf P(A_k) $$
                        B_nの定義より
                        $$ \forall k \geq n, B_n \subset A_k, P(B_n) \leq P(A_k) \Rightarrow P(B_n) \leq \inf_{k\geq n} P(A_k) $$
                - Borel-Cantelli lemma 1
                    - 事象列
                    $$ \sum_{n=1}^\infty P(A_n) < \infty \Rightarrow P(\limsup_{n \to \infty} A_n) = 0 $$
                    - proof
                        $$ E_k = \bigcup_{n=k}^\infty A_n \\ \limsup_{n \to \infty} A_n \subset E_k \\ P(\limsup_{n \to \infty} A_n) \leq P(E_k) \leq \sum_{n=k}^\infty P(A_n) $$
                - Borel-Cantelli lemma 2
                    - 互いに独立な事象列
                    $$ \sum_{n=1}^\infty P(A_n) = \infty \Rightarrow P(\limsup_{n \to \infty} A_n) = 1 $$
                    - proof
                        $$ \forall k \in \mathbb N, P(\bigcup_{n=k}^\infty A_n) = 1 $$
                        let me prove it
                        $$
                        \forall N \in \mathbb N \\ 1-P(\bigcup_{n=k}^\infty A_n) \leq 1-P(\bigcup_{n=k}^N A_n) \\ = P((\bigcup_{n=k}^N A_n)^c) \\ = P(\bigcap_{n=k}^N A_n^c) \\ = \prod_{n=k}^N P(A_n^c) \\ = \prod_{n=k}^N (1-P(A_n)) \\ \leq \prod_{n=k}^N \exp(-P(A_n))\\ = \exp(-\sum_{n=k}^N P(A_n)) \\ \xrightarrow{n\to\infty} 0 \\ P(\bigcup_{n=k}^\infty A_n) = 1 $$
        - 確率変数 random variable
            事象を数値で表現
            - Borel field B
            $$ X : \Omega \rightarrow \mathbb R\\ \{\omega \in \Omega| X(\omega) \in B\} \in \mathcal F, \forall B \in \mathcal B(\R) $$
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
            $$ \mu_X: \mathcal B (\R) \to \mathbb R\\ \mu_X(B) = \mathbb P (X\in B) $$
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
            $$ F_X(x) = \mathbb P(X\leq x) = \mu_X(-\infty, x] \\ x \in \mathbb R$$
            then, F is the cumulative distribution function
            - theorem
                - order
                    $$ x \leq y, F_X(x) \leq F_X(y) $$
                    - proof
                        $$ (-\infty, x_1] \subset (-\infty, x_2] \\ A_1 = X^{-1}(-\infty, x_1] \\ A_2 = X^{-1}(-\infty, x_2] \\ A_1 \subset A_2 $$
                - limit
                    $$ \lim_{x \to +\infty} F_X(x) = 1 \\ \lim_{x \to -\infty} F_X(x) = 0 $$
                    - proof
                        $$ \lim_{x \to -\infty} P(X \leq x) = \lim_{x \to -\infty} \mu(-\infty, x] \\ = \mu(\phi) = 0 $$
                        $$ \lim_{x \to \infty} P(X \leq x) = \lim_{x \to \infty} \mu(-\infty, x] \\ = \mu(\R) = 1
                        $$
                - right-hand continuous
                    - proof
                        $$ x_n = x + \epsilon_n, \epsilon_n \downarrow 0\\ x_n \downarrow x \\ A_n = (-\infty, x_n] \\ \lim_{n\to \infty} A_n = \bigcap_{n=1}^\infty (-\infty, x_n] = (-\infty, x] \\ \lim_{n \to \infty} F(x_n) = \mu_X(\bigcap_{n=1}^\infty [-\infty, x_n]) = \mu_X(-\infty, x_n] = F(x) $$
                    - the case of the left-hand…
                        $$ x_n = x - \epsilon_n, \epsilon_n \uparrow 0\\ x_n \uparrow x, \forall x_n < x \\ A_n = (-\infty, x_n] \\ \lim_{n\to \infty} A_n = \bigcup_{n=1}^\infty (-\infty, x_n] = (-\infty, x) \\
                        $$
                - compute distribution measure 1
                    $$ \mu_X(x, y] = F(y) -F(x) $$
                - compute distribution measure 2
                    $$ \mu_X[a, b] = \lim_{n \to \infty }\mu_X(a-\frac{1}{n}, b] = F(b) - \lim_{n \to \infty}F(a-\frac{1}{n}) $$
        - 確率密度関数 probability density function
            縦軸は確率密度
            $$ \mu_X(B) = \mathbb P(X \in B) = \int_B f_X(x) dx \\ B \in \mathcal B(\R) $$
            then, f is the density function
            - continuous
                $$ F(x) = \int_{-\infty}^x f(x)dx \\ \int_{-\infty}^{\infty} f(x)dx = 1 \\f(x) \geq 0, x \in \mathbb R$$
        - 確率質量関数 probability mass function
            縦軸は確率
            $$ \mu_X(B) = \sum_{\{i;x_i \in B\}} p_i \\ B \in \mathcal B(\R) $$
            - another uniform distribution
                - random variable
                    $$ Y_n(\omega) = \left\{ \begin{matrix} 1 & if & \omega_n = H \\ 0 & if & \omega_n = T \end{matrix} \right. \\ X = \sum_{n=1}^\infty \frac{Y_n}{2^n} $$
                - distribution measure
                    $$ \mu_X[\frac{k}{2^n}, \frac{k+1}{2^n}] = \frac{1}{2^n} $$
                - Lebesgue integral
                    $$ \mu_X[\frac{k}{2^n}, \frac{m}{2^n}] = \frac{m}{2^n} - \frac{k}{2^n} \\ \mu_X[a, b] = b-a\\ b = \frac{m}{2^n}, a = \frac{k}{2^n} $$
            - standard normal
                $$ \phi(x) = \frac{1}{\sqrt{2\pi}}\exp(-\frac{x^2}{2}) $$
                $$ N(x) = \int_{-\infty}^x \phi(\xi)d\xi $$
        - 基準化定数 normalization constant
            $$ c = \frac{1}{\int_{-\infty}^{\infty}f(x)dx} $$
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
                    $$ \mathbb E[|X|] < \infty $$
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
            $$ G_X(s)=\mathbb E[s^X] = \sum_{x=0}^\infty s^x p(x) $$
            - 収束条件
                - 非負の整数値をとる離散確率変数
                - $|s| \leq 1$
                - $p(x) \geq 0$
                - $\sum p(x) = 1$
            - 期待値
                $$ \left. \frac{dG(s)}{ds} \right|_{s=1} =\left. \sum_{x=0}^\infty xs^{x-1}p(x) \right|_{s=1} = \sum_{x=0}^\infty xp(x) = \mathbb E[X] $$
            - 階乗積率 factorial moment
                $$ G^{(k)}(1)=\mathbb E[X(X-1)...(X-k+1)] $$
        - 積率母関数 moment generating function
            $$ M_X(t) = G_X(e^t) = \mathbb E[e^{t X}] = \sum_{k=0}^\infty \frac{\theta^t}{k!}\mu'_k $$
            - 積率 moment
                $$ \mathbb E[X^n] = M_X^{(n)}(0) $$
            - central moment
                $$ \phi(\theta)e^{-\mu \theta} = \mathbb E[e^{\theta (X-\mu)}] $$
            - 独立
                XとYが独立ならば
                $$ M_{X+Y}(t) = M_X(t)M_Y(t) $$
        - 特性関数 characteristic function
            $$ \phi_X(t) = \mathbb E[e^{itX}] = \sum_{x=-\infty}^\infty e^{itx}p(x) $$
            - 積率 moment
                $$ \mathbb E[X^n] = i^n \phi^{(n)}_X (0) $$
            - 逆転公式 inversion formula
                differential
            - FFT Fast Fourier Transform
                $$ \phi_X(t) = \int_{-\infty}^\infty\exp(itx)f_X(x)dx $$
                特性関数は確率密度関数のフーリエ変換に一致する
        - Laplace–Stieltjes transform
            $$ F_X^*(s) = \int_0^\infty e^{-sx}f_X(x)dx $$
    - 多変量確率変数 multivariate random variable
        - 確率方向量 probability vector
            - n個の連続型確率変数
                $$ X_1 : \Omega \to \mathbb R\\ \vdots \\ X_n : \Omega \to \mathbb R$$
            $$ (X_1, ..., X_n):\Omega \to \mathbb R $$
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
                    $$ f_X*f_Y = \int_{-\infty}^\infty f_X(w)f_Y(z-w)dw $$
                - CDF
                    $$ F_{X+Y}(z) = P(X+Y \leq z) \\ = \int_{-\infty}^\infty \int_{\infty}^{y=z-x}f_{X, Y}(x, y)dydx \\ = \int_{-\infty}^\infty F_Y(z-x)f_X(x)dx \\ = F_X *F_Y(z) $$
            - multi-variables
                $$ S_n = \sum_{i=1}^n X_i $$
                $$ P(S_1 \leq t) = P(X_1 \leq t) = F(t) \\ P(S_2 \leq t) = \int_0^t F(t-x)f(x)dx \\ = \int_0^t F(t-x)dF(x) \\ = F*F(t) = F^{(2)}(t) $$
            - dependent
                $$ Z = Y_1 + Y_2\\ F_Z(z) =\int_{-\infty}^\infty \int_{-\infty}^{z-x_1} f_{Y_1, Y_2} (y_1, y_2) dy_2 dy_1 $$
                - 変数変換
                    # $$ \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix}
                    \left( \begin{matrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2\\ \end{matrix} \right) \begin{pmatrix} X_1 - \mu_1 \\ X_2 - \mu_2 \end{pmatrix} $$
                    $$ Y_1 = \sigma_1^2(X_1 - \mu_1) + \rho \sigma_1 \sigma_2(X_2 - \mu_2) \\ Y_2 = \rho \sigma_1 \sigma_2(X_1 - \mu_1) + \sigma_2^2(X_2 - \mu_2) $$
                $$ = \int_{-\infty}^\infty \int_{-\infty}^{z-x_1} f_{X_1}(y_1) f_{X_2}(y_2) | \Sigma |dy_2 dy_1 $$
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
                    $$ \phi_X(t) = \sum_{x = 0}^\infty pq^x e^{itx} = \frac{p}{1-qe^{ix}} \\ |qe^{ix}| = q < 1 \\ t < \log \frac{1}{q} $$
                - 負の二項分布
                    $$ \phi_{S_n}(t) = \sum_{x = 0}^\infty \binom {-n}{x} p^nq^xe^{itx} \\ = p^n \sum_{x = 0}^\infty (-1)^x\binom {-n}{x} q^xe^{itx} \\ = p^n \sum_{x = 0}^\infty \binom {-n}{x} (-q)^xe^{itx}
                    $$
                    we apply $(1+u)^{-n} = \sum_{x=0}^\infty \binom{-n}{x} u^x$
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
                $$ \forall i, j \in \mathbb N, Cov(X_i, X_j) = 0 $$
            - 平均 average
                $$ \bar X_n = \frac{1}{n} \sum_{i = 1}^n X_i $$
            $$ \lim_{n \rightarrow \infty} \mathbb P(|\bar X_n - \mu| \geq \epsilon) = 0, \forall \epsilon > 0 $$
            $$ \lim_{n \rightarrow \infty} \mathbb P(|\bar X_n - \mu| < \epsilon) = 1, \forall \epsilon > 0 $$
            - 証明 proof
                $$ \bar X_n = \frac{1}{n}(\sum_{i = 1}^n X_i) \\ \mathbb E[\bar X_n] = \mu \\ \mathbb E[(\bar X_n-\mu)^2]= \frac{\sigma^2}{n} \\ \mathbb P((\bar X_n - \mu)^2 \geq \epsilon^2) = \frac{\sigma^2}{n \epsilon^2} \\ \lim_{n \rightarrow \infty} \mathbb P(|\bar X_n - \mu| \geq \epsilon) = 0, \forall \epsilon > 0 $$
            - 誤差が基準より大きくなる確率は0に収束させることができる定理（例外あり）
            - 裏を考えると有限のnでは基準を超える可能性がある
        - 大数の強法則 strong law of large number
            $$ \mathbb P(\lim_{n \rightarrow \infty} \bar X_n = \mu) = 1 $$
            - 証明 proof
                - assumption
                    - 独立同分布な確率変数列 $X_1, X_2, ...$
                    - 期待値有限
                        $$ \mathbb E[|X_i|] < \infty $$
                        - 裾の確率が0に収束
                            $$ \mathbb P(|X_i| > n) \xrightarrow{n\to\infty} 0 $$
                            - proof
                                [Markov’s inequality](https://www.notion.so/Markov-s-inequality-216ec42dd04b81588729e355952b6934?pvs=21)
                                $$ \mathbb P(|X_i|>n) \leq \frac{\mathbb E[|X_i|}{n} \\ \xrightarrow{n\to\infty} \\ \mathbb P(|X_i|>n) \to 0 $$
                        - 和の有限性
                            $$ \sum_{n=1}^\infty \mathbb P(|X_i| > n) = \mathbb E[|X_i|] < \infty $$
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
            $$ \lim_{n \to \infty }P\left(\frac{S_n- n\mu}{\sqrt n\sigma} \leq \alpha \right) \rightarrow \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\alpha e^{-\frac{x^2}{2}}dx $$
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
            $$ \mathbb E[|X|] < \infty $$
            - Truncation
                - 確率変数 X_i
                - 閾値 c_n
                $$ X_{i,n} = X_i \cdot 1_{|X_i| <c_n} $$
            - symmetrization
        - Kolmogorov’s maximum inequality
        - Kolmogorov’s two series theorem
        - Kolmogorov’s three series theorem
- 応用確率論
    - 単調収束定理
        - 単調増大
            - 測度空間
            - 単調増加
                $$ A_1 \subset A_2 \subset ... \subset \mathcal F $$
            $$ \mu (\bigcup^\infty_{n=1} A_n) = \lim_{n \to \infty} \mu(A_n) $$
        - 単調減少
            - 測度空間
            - 単調減少
                $$ A_1 \supset A_2 \supset ... \supset \mathcal F $$
            $$ \mu (\bigcap^\infty_{n=1} A_n) = \lim_{n \to \infty} \mu(A_n) $$