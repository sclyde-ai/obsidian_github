- 体 field
    - 定義 def
        集合R
        - 加法 addiction
            - 結合律 associativity
                $$ (x+y)+z = x+(y+z) \\ \forall x,y,z \in \mathbb R$$
            - 交換律 commutativity
                $$ x+y = y+x \\ \forall x,y \in \mathbb R$$
            - 単位元 identity
                $$ \existss 0 \in \R, x+0=0+x=x, \forall x \in \mathbb R$$
            - 逆元 inverse
                $$ \existss -x \in \R, x+(-x)= (-x)+x = 0, \forall x \in \mathbb R$$
        - 乗法 multiplication
            - 結合律 associativity
                $$ (x\cdot y)\cdot z = x \cdot (y\cdot z) \\ \forall x,y,z \in \mathbb R$$
            - 交換律 commutativity
                $$ x \cdot y = y \cdot x \\ \forall x,y \in \mathbb R$$
            - 単位元 identity
                $$ \existss 1 \in \R, x \cdot 1= 1\cdot x = x, \forall x \in \mathbb R$$
            - 逆元 inverse
                $$ \existss y \in \R, x \cdot x^{-1}= x^{-1} \cdot x = 1, \forall x\in \mathbb R$$
        - 分配律 distributivity
            $$ x \cdot (y+z) = x \cdot y + x\cdot z, \forall x,y,z \in \mathbb R$$
    - 性質 prop
        - 単位元の一意性
            単位元0_1, 0_2が存在すると仮定
            $$ x + 0_1 = x = x + 0_2 $$
        - 逆元の一意性
            $$ x + (-x) = 0 = x + (-x) $$
        - 単位元の逆元
            $$ 0 + 0 = 0 $$
        - 加法単位元の積
            $$ x \cdot 0 = x\cdot (0+0)\\ = x\cdot 0 + x \cdot 0 \\ x\cdot 0 + (-x \cdot 0) = x \cdot 0 + x\cdot 0 + (-x \cdot 0) \\ 0 = x \cdot 0
            $$
        - 加法単位元の乗法逆元
            $$ x \cdot 0 = 0, \forall x \in \mathbb R$$
        - 積の逆元
            $$ (x^{-1} \cdot y^{-1}) \cdot (x\cdot y) = (x^{-1} \cdot y^{-1}) \cdot (y \cdot x) = x^{-1} (\cdot y^{-1} \cdot y) \cdot x = x^{-1} \cdot x = 1 $$
        - 加法逆元と乗法
            $$ 0 = 0\cdot x = (1+(-1))\cdot x = 1 \cdot x + (-1)\cdot x = x +(-1)\cdot x = 0 $$
- 全順序 total order
    - 大小関係
        - 反射律
            $$ x \geq x, \forall x \in \mathbb R$$
        - 反対称律
            $$ x \leq y \land y \leq x \Rightarrow x = y \\ \forall x, y \in \mathbb R$$
        - 推移律
            $$ x \leq y \land y \leq z\Rightarrow x \leq z \\ \forall x,y,z \in \mathbb R$$
        - 完備律
            $$ x \leq y \lor y \leq x \\ \forall x, y \in \mathbb R$$
    - 同値関係
        - 反射律
        - 対称律
        - 推移律
    - 狭義大小関係
        - 非反射律
        - 非対称律
        - 推移律
        - 三分律
    - 最大値/最小値
        - 最大値
            $$ \max A: \existss a \in A, \forall x\in A, x \leq a $$
        - 最小値
            $$ \min A: \existss a \in A, \forall x\in A, a \leq x $$
        - 最大値/最小値が存在しない集合
            $$ A = \{x \in \mathbb R| a < x < b\} $$
        - 有限集合は最大値/最小値を持つ
        - 最大値/最小値の一意性
    - 上界/下界
        - 上界
            $$ \existss a \in \R, \forall x \in A, x \leq a $$
        - 下界
            $$ \existss a \in \R, \forall x \in A, a \leq x $$
        - 上界集合
            $$ U(A) = \{a \in \R| \forall x \in A, x \leq a\} $$
        - 下界集合
            $$ L(A) = \{a \in \R| \forall x \in A, a \leq x\} $$
        - 上に有界
            $$ U(A) \ne \phi $$
        - 下に有界
            $$ L(A) \ne \phi $$
        - 有界
            $$ U(A) \ne \phi \land L(A) \ne \phi $$
        - 上に有界と最大値
            $$ \existss \max A \in A \Rightarrow \max A \in U(A) $$
        - 下に有界と最小値
            $$ \existss \min A \in A \Rightarrow \min A \in L(A) $$
    - 上限/下限
        - 上限
            - 半順序集合
                $$ \sup A = \min U(A) $$
            - 実数
                $$ \forall x \in A, x \leq \alpha \\ \forall \epsilon \in \R_{++}, \existss x \in A, \alpha - \epsilon \leq x \leq \alpha $$
        - 下限
            - 半順序集合
                $$ \inf A = \max L(A) $$
            - 実数
                $$ \forall x \in A, \alpha \leq x \\ \forall \epsilon \in \R_{++}, \existss x \in A, \alpha \leq x \leq \alpha + \epsilon $$
        - 上限と最大値
            $$ \existss \max A \in A \Rightarrow \max A = \sup A $$
            $$ \existss \sup A\in A \Rightarrow \max A = \sup A $$
        - 下限と最小値
            $$ \existss \min A \in A \Rightarrow \min A = \inf A $$
            $$ \existss \inf A \in A \Rightarrow \min A = \inf A $$
        - 有限集合
            $$ \sup A = \max A \\ \inf A = \min A $$
        - 近似性質
            $$ \forall \epsilon \in \R_{++}, \existss x \in A, \sup A - \epsilon < x < \sup A $$
            $$ \forall \epsilon \in \R_{++}, \existss x \in A, \inf A < x < \inf A + \epsilon $$
        - 包含関係
            $$ A \subset B \Rightarrow \sup A \leq \sup B $$
            $$ A \subset B \Rightarrow \inf B \leq \inf A $$
        - 上限と下限
            $$ \sup A = \inf (-A) \\ \inf A = \sup (-A) $$
        - 定数倍
        - 和
    - 上極限/下極限
        - 上極限
            $$ \varlimsup_{n\to \infty}a_n =\limsup_{n \to \infty} a_n = \lim_{n \to \infty} \left(\sup_{k \geq n}a_k \right) $$
            - 解説
                $$ S_n = \sup \{x_n, x_{n+1}, ...\} $$
                $$
                \{x_n, x_{n+1}, ...\} \supset \{x_{n+1}, x_{n+2}...\} \supset ... \\ \sup\{x_n, x_{n+1}, ...\} \geq \sup\{x_{n+1}, x_{n+2}...\} \geq ... \\ S_n \geq S_{n+1} \geq ... $$
                $$ \lim_{n \to \infty} S_n $$
        - 下極限
            $$ \varliminf_{n \to \infty}a_n = \liminf_{n \to \infty} a_n = \lim_{n \to \infty} \left(\inf_{k \geq n}a_k \right) $$
        ![limsup-lininf-1024x693.png](attachment:5125dce4-3615-4c83-bc8d-03d728d858d5:limsup-lininf-1024x693.png)
- 区間
    - 開区間 open interval
        $$ (a, b) $$
    - 閉区間 closed interval
        $$ [a, b] $$
    - 半開区間 half-open interval
        $$ (a, b], [a, b) $$
    - 片側無限開区間 open unbounded interval
        $$ (-\infty, a), (a, \infty) $$
    - 片側無限閉区間 closed unbounded interval
        $$ (-\infty, a],[b, \infty) $$
    - 両側無限区間 entire real line
        $$ (-\infty, \infty) $$
    - 空集合 empty interval
        $$ \phi $$
    - 一点集合 singleton interval
        $$ [a, a] $$
- 連続性 continuity
    - アルキメデスの原理
        $$ \forall a, b \in \R, \existss n \in \mathbb N, an > b $$
        - 自然数の極限
            $$ \lim_{n \rightarrow \infty} n = +\infty $$
            - 証明 proof
                $$ \forall a, b \in \R, \existss n \in \mathbb N, n > \frac{b}{a} $$
    - 連続の公理
        - デデキントの公理 Dedekind’s axiom
            - デデキント切断 dedekind cut
                $$ A \cup B = \mathbb Q \\ A \cap B = \phi \\ A \ne \phi \land B \ne \phi \\ \forall a, b \in \R, a \in A \land b \in B \Rightarrow a < b $$
                となるA|Bをデデキント切断という
            デデキント切断を実数とする
        - W 上に有界な集合は上限を持つ
            $$ U(A) \ne \phi ,\existss \sup A \in \mathbb R$$
        - M 上に有界な単調増加数列は数列の上限に収束する
            $$ A = \{a_n|\forall n, m \in \mathbb N, n < m \Rightarrow a_n < a_m\} \\ \lim_{n \rightarrow \infty} a_n = \sup A $$
            - W → M
                上に有界なので上限が存在し
                $$ \alpha = \sup A $$
                書き換えると
                $$ \forall \epsilon \in \R_{++}, \existss N \in \mathbb N \\ \alpha -\epsilon < a_N \\ \alpha - a_N < \epsilon $$
                単調増加なので
                $$ \forall n \geq N, \\ 0 \leq \alpha - a_n < \epsilon $$
                全部書き下すと
                $$ \forall \epsilon \in \R_{++}, \existss N \in \mathbb N, \forall n \geq N, \\ 0 \leq \alpha - a_n < \epsilon \\ \lim_{n \rightarrow \infty} a_n = \alpha
                $$
        - A&K アルキメデスの原理と区間収縮法
            [アルキメデスの原理](https://www.notion.so/216ec42dd04b812087c3d37d46b94f80?pvs=21)
            - 区間収縮法
                $$ I_n = [a_n, b_n] \\ \forall n \in \mathbb N, I_n \subset I_{n+1} \\ \bigcap_{n=1}^\infty I_n \ne \phi $$
                $$ \lim_{n \rightarrow \infty} (b_n - a_n) = 0 \\ \existss c \in \R, \bigcap_{n=1}^\infty I_n = \{c\} $$
            - M → A&K
                $$ \lim_{n \rightarrow \infty} a_n = \alpha, \lim_{n \rightarrow \infty} b_n = \beta \\ a_n < b_n, \alpha \leq \beta $$
        - B-W 有界数列は収束部分列を持つ
            - 有界数列
                $$
                $$
        - A&C アルキメデスの原理と任意のコーシー列の収束
            [アルキメデスの原理](https://www.notion.so/216ec42dd04b812087c3d37d46b94f80?pvs=21)
            - コーシー列
                $$ \forall \epsilon \in \R_{++}, \existss N \in \mathbb N, |a_n - a_m| < \epsilon $$
                $$ \lim_{n \rightarrow \infty} a_n \in \mathbb R$$
- 拡大実数系
    $$ \mathbb R\cup \{-\infty, \infty\} $$
    - def
        $$ \forall a \in \R, a \leq \infty \\ \forall a \in \R, \infty \leq a $$
    - 絶対値
        $$ |-\infty| = |\infty| = \infty $$
    - 加法
        $$ a + \infty = \infty\\ a - \infty = -\infty $$
    - 可換モノイド
        - 結合法則
            $$ \forall a,b,c \in (-\infty, \infty], (a+b)+c = a+(b+c) $$
        - 単位元
            $$ \forall a \in (-\infty, \infty], a+0 = 0+a = a $$
        - 交換法則
            $$ \forall a, b \in (-\infty, \infty], a+b=b+a $$
    - 乗法
        $$ a\cdot (\pm\infty) = \left\{ \begin{matrix} \pm \infty & if & a>0 \\ 0 & if & a=0 \\ \pm \infty & if & a<0 \\ \end{matrix} \right. $$
    - theorem
        - [0, \infty]は加法に関して単位元0の可換モノイド
        - [0, \infty]は乗法に関して単位元1の可換モノイド
        - 分配法則
            $$ a, b, c \in [0, \infty], (a+b)\cdot c = a\cdot c+ b \cdot c $$