$$ \lim_{x \to a} f(x) = \alpha $$
$$ \forall \epsilon>0, \existss \delta >0, \forall x \in \R, \\ 0 < |x-a|< \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
- 左極限
    $$ \lim_{x \to a-} f(x) = \alpha $$
    $$ \forall \delta>0, \existss \epsilon >0, \forall x \in \R, \\ 0 < a-x < \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
- 右極限
    $$ \lim_{x \to a+} f(x) = \alpha $$
    $$ \forall \delta>0, \existss \epsilon >0, \forall x \in \R, \\ 0 < x-a < \delta \Rightarrow |f(x)-\alpha| < \epsilon $$
- theorem
    - 一意性
        $$ a_n = b_n \Rightarrow \alpha = \beta, \forall n \in \mathbb N $$
    - 和
        $$ \alpha + \beta = \lim_{n \to \infty}(a_n + b_n) $$
    - 積
        $$ \alpha \beta = \lim_{n \to \infty} a_n b_n $$
    - 商
        $$ \alpha \ne 0 \Rightarrow \frac{\beta}{\alpha} = \lim_{n \to \infty} \frac{b_n}{a_n} $$
    - 大小関係
        $$ a_n \leq b_n \Rightarrow \alpha \leq \beta $$