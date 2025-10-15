



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