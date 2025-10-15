 
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