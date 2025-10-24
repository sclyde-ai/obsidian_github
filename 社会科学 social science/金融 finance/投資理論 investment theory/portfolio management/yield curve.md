- yield(zero coupon bond)
    $$
    y_n^N = -\frac{1}{N-n}\log(B_n^N)
    $$
- yield(coupon bond)
    $$
    P_N = \sum_{m=1}^M B_0^{m} r_c F + B_0^N F
    $$
- spot rate
    yield at the present time
    $$
    B_0^N = \exp(-y_0^N N)
    $$
    $$
    y_0^N = -\frac{1}{N}\log(B_0^N)
    $$
- bootstrapping
    B(0, 1) → B(0, 2) → …
    と順番に求める方法
    - prameters
        $F$ : face value
        $r_c$ : coupon rate
        - time series to take coupons
            $$
            \{n_m\}_{m \in \{1, 2, ..., M\}}
            $$
- forward rate
    $$
    F_k^{n, N}(\omega) = \frac{\log B_k^{N}(\omega) - \log B_n^N(\omega)}{N-n}
    $$
- momentary forward rate
    $$
    f_k^N(\omega) = F_{k}^{n, n+1}(\omega)
    $$
- short rate
    $$
    r_n(\omega) = f_n^n (\omega)
    $$
- how to make yield curve
    - parametric model
        - nelson-Siegel
            $$
            f(T) = \beta_0 + \beta_1 e^{-\frac{T}{\tau}} + \beta_2 \frac{T}{\tau}e^{-\frac{T}{\tau}}
            $$
        - Svensson
            $$
            f(T) = \beta_0 + \beta_1 e^{-\frac{T}{\tau_1}} + \beta_2 \frac{T}{\tau_1}e^{-\frac{T}{\tau_1}} + \beta_2 \frac{T}{\tau_2}e^{-\frac{T}{\tau_2}}
            $$
    - bootstrapping + interpolation
        - pillar
            カーブを描く為の基準となる期間（時点）
        - bootstrapping
            $$
            PV_n - [\sum CF_n(T_i) \times DF_n(T_i)]
            $$
            $$
            \begin{pmatrix}
            PV_1 & -CF_1(T_1) & 0 & 0 & \dots & 0 \\
            PV_2 & -CF_2(T_1) & -CF_2(T_2) & 0 & \dots & 0 \\
            PV_3 & -CF_3(T_1) & -CF_3(T_2) &  -CF_3(T_3) & \dots & 0 \\
            \vdots & \vdots & \vdots & \ddots &\vdots \\
            PV_n & -CF_n(T_1) & -CF_n(T_2) &  -CF_3(T_3) & \dots & -CF_n(T_m)\\
            \end{pmatrix}
            \begin{pmatrix}
            1 \\ DF(T_1) \\ DF(T_2) \\ \vdots \\ DF(T_n)
            \end{pmatrix}
            = 
            \begin{pmatrix}
             0 \\ 0 \\ 0 \\ \vdots \\ 0
            \end{pmatrix}
            $$
        - interpolation 補間
            主にdiscount factorとzero coupon rate
            - 線形補間
            - 対数線形補間
            - spline補間
            - tension spline