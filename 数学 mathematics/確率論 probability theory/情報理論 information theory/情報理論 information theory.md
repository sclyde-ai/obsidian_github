- 平均情報量 entropy
    - 相互情報量と平均情報量の関係
        $$ I(X; Y) = H(X) - H(X|Y) \\ I(X; Y) = H(Y) - H(Y|X) \\ I(X; Y) = H(X) + H(Y) - H(X, Y) \\ I(X; Y) = I(Y; X) \\ I(X; X) = H(X) $$
    - 自己情報量 self-information
    - 自己相互情報量 pointwise mutual information
        $$ p(x, y) \log\ \frac{p(x, y)}{p(x)p(y)} $$
    - 条件付き相互情報量
    - 条件付き相対情報量
    - 連鎖律 chain law
        - 自己情報量
            $$ H(X_1, ..., X_n) = \sum_{i = 1}^{n} H(X_i|X_{i-1},..., X_1) $$
        - 相互情報量
        - 相対情報量
    - Jensenの不等式
    - 情報不等式
    - 対数和不等式
    - マルコフ連鎖
    - データ処理不等式
    - 十分統計量
    - Fanoの不等式
- 伝達情報量
- 符号化 encoding
    - 情報源符号化
        通信を高速にしたい
        - 情報源符号化定理
    - 情報路符号化
        通信を信頼できるものにしたい
        - 情報路符号化定理
- SCM statistical complexity measure
    $$ C = H_x\cdot D_{JS}(P, \pi) $$
    P : 系の確率分布
    \pi : 一様分布
    |entropy|SCM|characteristic|
    |---|---|---|
    |low|low|order|
    |middle|high|structure|
    |high|low|random|