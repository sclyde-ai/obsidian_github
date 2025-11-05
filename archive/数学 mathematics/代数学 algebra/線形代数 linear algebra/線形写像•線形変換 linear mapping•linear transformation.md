---
alias:
    ['線形写像', '線形変換', 'linear mapping linear transformation']
---
- 定義 def
    写像 $f: \mathbb R \rightarrow \R^m$
    - 加法性 additivity
        $$ f(x+ y) = f(x) + f(y) \\ \forall x, y \in \mathbb R $$
    - 斉次性 homogeneity
        $$ f(kx) = k f(x) \\ \forall x \in \mathbb R, \forall k \in \mathbb R$$
- 拡大縮小変換 scale
    横にx倍、縦にy倍
    $$ \begin{pmatrix} x & 0 \\ 0 & y \end{pmatrix} $$
- 回転変換 rotate
    $\theta$回転
    $$ \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} $$
- 鏡映変換 reflection
    - x軸対称
        $$ \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} $$
    - y軸対称
        $$ \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} $$
    - 原点対称
        $$ \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} $$
    - 直線x = y対称
        $$ \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} $$
- squeeze
    $$ (x, y) \to (ax, \frac{y}{a}) $$
- affine変換 affine transformation
    同次座標
    - 平行移動 translation
        横にx、縦にy移動
        $$ \begin{pmatrix} 1 & 0 & x \\ 0 & 1 & y \\ 0 & 0 & 1 \end{pmatrix} $$