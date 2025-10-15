[微分積分 calculus](https://www.notion.so/calculus-216ec42dd04b81f8bc86fb3a81ca77ff?pvs=21)

- フーリエ解析 Fourier transform
    関数を三角関数に分解
    - 三角関数系 trigonometric system
        $$
        \{\cos nx, \sin nx| n \in \N\} \\
        \{1, \cos x, \sin x, \cos 2x, \sin 2x, ...| n \in \N\}
        $$
    - フーリエ級数 Fourier series
        $$
        f(x) = \frac{a_0}{2}+ \sum_{n=1}^\infin (a_n \cos nx + b_n \sin nx)
        $$
    - フーリエ級数 Fourier transform
        $$
        \hat f(\xi) = \int_{-\infin}^\infin f(x) e^{-2\pi ix\xi}dx
        $$
    - 逆フーリエ変換 inverse Fourier transform
        $$
        f(x) = \int_{-\infin}^\infin \hat f(\xi) e^{2\pi ix\xi}d\xi
        $$
    - 内積
    - 離散フーリエ変換
        - ナイキスト周波数
            取得したデータの時間間隔により復元できる周期関数の周波数の上限が存在する
        - 標本化定理 sampling theorem
            元の信号をその最大周波数の2倍を超えた周波数で標本化すればよい
    - youtube
        https://youtube.com/watch?v=fGos3wrKeHY&si=u_3Gw6Chsxyge6AS
- 微分方程式 differential equation
    - 変数分離形/一階微分方程式
        $$
        \frac{dy}{dx} = f(x)g(y)
        $$
        - 解法
            $$
            \frac{1}{g(y)}\frac{dy}{dx} = f(x) \\
            \int \frac{1}{g(x)}\frac{dy}{dx}dx = \int f(x)dx
            $$
        - 置換積分
            $$
            \int f(x) dx = \int f(g(t))\frac{dx}{dt}dt
            $$
    - 同次形
        $$
        \frac{dy}{dx} = f(\frac{y}{x})
        $$
    - 一階線形微分方程式
        $$
        \frac{dy}{dx} + p(x)y = g(x)
        $$
    - ベルヌーイの微分方程式
        $$
        \frac{dy}{dx} + p(x)y = g(x)y^\alpha
        $$
    - 完全微分方程式
        $$
        \frac{\partial F(x,y)}{\partial x}dx + \frac{\partial F(x, y)}{\partial y}dy = 0
        $$
    - クレローの微分方程式
        $$
        y = x \frac{dy}{dx} + f(\frac{dy}{dx})
        $$
    - 二階線形同次微分方程式
        $$
        \frac{d^2y}{dx^2} + p(x) \frac{dy}{dx} + g(x)y = 0
        $$
    - 二階線形非同次微分方程式
        $$
        \frac{d^2y}{dx^2} + p(x) \frac{dy}{dx} + g(x)y = f(x)
        $$
    - ルンゲクッタ法
    - 境界値問題 boundary value problem
    - 固有値問題
    - neural OED
- 複素解析 complex number
    $$
    a + bi\\
    i = \sqrt{-1}
    $$
    - exp & tri
        $$
        \exp iz = \cos z + i\sin z
        $$
        - exp
            $$
            \exp z= \sum_{n=0}^\infin \frac{z^n}{n!}
            $$
        - sin
            $$
            \sin z = \sum_{n=0}^\infin \frac{z^{2n+1}}{(2n+1)!}
            $$
        - cos
            $$
            \sin z = \sum_{n=0}^\infin \frac{z^{2n}}{(2n)!}
            $$
        - Eular formula
            $$
            \exp \theta = \cos \theta + i\sin i\theta
            $$
        - Eular equation
            $$
            e^{\pi i} = -1
            $$
    - log
        $$
        w = \ln z
        $$
        $$
        w = u+iv \\
        z = e^w \\
        re^{i\theta} = e^u\cdot e^{iv} \\
        r = e^u \Rightarrow u = \ln r\\
        e^{i\theta} = e^{iv} \Rightarrow v = \theta + 2n\pi
        $$
        $$
        w = \ln z = \ln r +i(\theta + 2n\pi) \\
        w = \ln |z| + i \arg z + 2n\pi i
        $$
    - differential
        $$
        \frac{df(z)}{dz} = \lim_{\Delta z \to 0} \frac{f(z+\Delta z)-f(z)}{\Delta z}
        $$
        - Cauchy Lieman
            - setting
                $$
                z = x+iy \\
                f(z) = u(x,y) +iv(x,y)
                $$
            - CR equation
                $$
                \frac{\partial u}{\partial x}(x, y) = \frac{\partial v}{\partial y}(x, y) \\
                \frac{\partial u}{\partial y}(x, y) = -\frac{\partial v}{\partial x}(x, y)
                $$
            - f(z) が微分可能
            - u(x, y)とv(x, y)が全微分可能かつCRの公式が成立
            上記二つが同値関係
            - 必要条件(上→下)
                $$
                \frac{f(z+\Delta z)-f(z)}{\Delta z} \\ = \frac{(u(x+\Delta x, y + \Delta y) + i v(x+\Delta x, y + \Delta y)) - (u(x, y) + i v(x, y))}{\Delta x + i \Delta y}
                \\ = \frac{(u(x+\Delta x, y + \Delta y) - u(x, y)) + i (v(x+\Delta x, y + \Delta y)+ v(x, y))}{\Delta x + i \Delta y}
                $$
                - 実軸平行
                    $$
                    \frac{df(z)}{dz} = \frac{\partial u}{\partial x}(x,y) + i \frac{\partial v}{\partial x}(x,y)
                    $$
                - 虚軸平行
                    $$
                    \frac{df(z)}{dz} = -i \frac{\partial u}{\partial y}(x,y) + \frac{\partial v}{\partial y}(x,y)
                    $$
            - 十分条件(下→上)
    - calculus
    - pdf
        [kansuron.pdf](kansuron.pdf)
- 超準解析 nonstandard analysis
    - フィルター filter
        定義3.2. F を自然数N の部分集合の集まりとする．F がフィルターであるとは次の条件を
        満たす事である．
        1. F は空集合でない．
        2. A, B ∈ F ならばA ∩ B ∈ F である．
        3. A ∈ F かつA ⊂ B ⊂ N ならばB ∈ F である．
        4. F は空集合を含まない．
        - フレッシェ・フィルター
            自然数の有限部分集合とは，有限個の自然数の集まりの事である．自然数の有限部
            分集合の補集合の集まりをF とすると，これはフィルターである．式で書くと
            F= {Xc | X ⊂ N は有限集合}
        - 超フィルター
            定義3.7. F を自然数N の部分集合の集まりとし，フィルターの条件を満たしているとす
            る．このF が超フィルターであるとは次の条件を満たす事である．
            • もし他のフィルターF ′ がF ⊂ F ′ を満たすならば，F= F ′ である．つまりF より大
            きいフィルターは存在しない
        - 
        命題3.9. フィルターF に対して，次の4 つの条件は同値である．
        1. F は超フィルターである．
        2. どんな部分集合A ⊂ N に対しても，A ∈ F かAc ∈ F のどちらか一つが必ず成立す
        る．（この時両方が成立する事はない．）
        3. 部分集合A, B ⊂ N がA ∪ B ∈ F ならば，A ∈ F かB ∈ F のどちらかが成立する．
        （この時は両方成立してもよい．）
        4. 部分集合A1, . . . , An ⊂ N がA1 ∪ · · · ∪ An ∈ F ならば，あるi に対してAi ∈ F である．
- 局所凸位相ベクトル空間 locally convex topological vector space
- Fréchet derivative
    https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
- holder continuous
- 数値計算
    - 二分法
    - ニュートン法
        - 目的 purpose
            関数 f(x) について f(a) = bとなるaを求めたい
        $$
        x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
        $$
        ![image.png](学問%20academics/notion/math/ExportBlock-cb2c20a1-8e45-4a53-98cb-57377ce1c41e-Part-1/image%204.png)
        - 導出
            $$
            x_n-x_{n+1}:f(x_n) = 1:f'(x_n) \\
            f'(x_n)(x_n-x_{n+1}) = f(x_n) \\
            x_n-x_{n+1}= \frac{f(x_n)}{f'(x_n)} \\
            x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)} 
            $$
    - brent法
- website
    [多変数関数の極値判定 - 数学についていろいろ解説するブログ](https://shakayami-math.hatenablog.com/entry/2020/08/08/175457)