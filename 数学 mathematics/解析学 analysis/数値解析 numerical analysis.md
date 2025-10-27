---
alias:
    ['数値解析', 'numerical analysis']
---
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