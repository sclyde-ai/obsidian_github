- 平均二乗誤差 MAE
    $$
    \frac{1}{2} |y - t|
    $$
- 平均絶対誤差 MSE
    $$
    \frac{1}{2} (y - t)^2
    $$
- hinge loss
    maximum margin
    $$
    \max(1 - t \cdot y, 0)
    $$
- cross entropy
    $$
    -t \cdot \log y
    $$
- huber loss
    $$
    \left\{
    \begin{matrix}
    \frac{1}{2} (y-t)^2 & |y-t| \leq \delta \\
    \delta (|y -t| -\frac{1}{2}\delta) & |y-t| > \delta
    \end{matrix}
    \right.
    $$
    - \delta
        the parameter that determines the threshold for switching between quadratic and linear loss.
- log cosh loss
    $$
    \log (\cosh (y - t))
    $$
- poisson loss
- logistic loss
    $$
    \log (1+ \exp (-y\cdot t))
    $$
- 0-1 loss
- TD time difference error
- website
    [論文読みサポート: 深層学習における損失関数 - Qiita](https://qiita.com/hiyoko1729/items/4351d7e5c6cfbef3ec1a)