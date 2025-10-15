- vector $\bm y_t$
- coefficient matrix $A_k$
- error/shock/innovation $\epsilon_t$
$$
\bm y_t = c + \sum_{k=1}^p A_k \bm y_{t-k} + \bm \epsilon_t
$$
- 定常性条件 stationary
    $$
    \det(I_k -\sum^p_{i=1} A_i z^i) = 0
    $$
- 予測誤差分散分解 FEVD Forecast Error Variance Decomposition
    - 移動平均表現 MA version
        $$
        y_t = \mu + \sum_{h=0}^\infin \psi_h  \epsilon_{t-h}
        $$
        - impulse response coefficient matrix
            $$
            \psi_h = \frac{\partial y_{t+h}}{\partial\epsilon_{t}}
            $$
            - how to calculate
                $$
                \psi_0 = I \\
                \psi_h = \sum_{j=1}^{\min(h, p)} A_j \psi_{h-j}
                $$
    - 分散共分散行列 variance covariance matrix
        $$
        \Sigma = \frac{1}{T-k} \sum_{t =1}^T \epsilon_t \times \epsilon_t
        \\ = (\sigma_{ij})_{i \in \{1, ... ,p\}, j \in \{1, ..., T\}}
        $$
        - outer product $\times$
    - Cholesky decomposition
        $$
        \Sigma = LL^\top
        $$
        - modified Cholesky decomposition
            $$
            \Sigma = LDL^\top
            $$
    - 直行化誤差 orthogonalized shock
        $$
        u_t = L^{-1} \epsilon_t
        $$
    - IRF impulse response function
        $$
        IRF_{i, j, h } = (\psi_h L)_{i, j}
        $$
        - normalized IRF
            $$
            IRF_{i, j, h}^{normalized} = (\psi_h L)_{i, j} \sqrt{\sigma_{j j}}
            $$
    - 予測誤差分散 forecasting error variance
        $$
        Var(y_{i, t+h}) = \sum_{s=0}^{h-1} (\psi_s  L\Sigma L^\top \psi_s^\top)_{i, i}
        $$
    - 寄与度 contribution ratio
        $$
        CR_{i, j, h} 
        = \frac{\sum_{s = 0}^{h-1} (IRF_{i, j, s}^{normalized})^2}{Var(y_{i, t+h}) } \\
        = \frac{\sum_{s = 0}^{h-1}(\psi_s L)^2_{i, j} \sigma^2_{j j}}{\sum_{s=0}^{h-1} (\psi_s  L\Sigma L^\top \psi_s^\top)_{i, i}}
        $$
        the contribution ratio of j for i
- SVAR structure VAR
- granger causality