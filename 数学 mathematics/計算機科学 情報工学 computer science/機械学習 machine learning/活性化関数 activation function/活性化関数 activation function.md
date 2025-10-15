
        - ridge function
            $$
            f : \R^d \to \R
            $$
        - step
            $$
            f(x) = 
            \left\{
            \begin{matrix}
            0 & if & x < 0 \\
            1 & if & x \geq0 
            \end{matrix}
            \right.
            $$
        - sigmoid
            $$
            f(x) = \frac{1}{1+\exp(-x)}
            $$
        - identity function 恒等関数
        - step function
        - sigmoid function
            $$
            \sigma(x)= \frac{1}{1+e^{-x}} = \frac{e^x}{1+e^x}
            $$
            ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%203.png)
        - softmax
            $$
            \sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}
            $$
        - tanh
            $$
            \sigma(x)= \frac{e^x-e^{-x}}{e^x+e^{-x}} = \frac{1-e^{-2x}}{1+e^{-2x}}
            $$
            ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%204.png)
        - ReLU Rectified Linear Unit
            $$
            f(x) = 
            \left\{
            \begin{matrix}
            0 & if & x < 0 \\
            x & if & x \geq0 
            \end{matrix}
            \right.
            $$
            $$
            f(x) = \max(0, x) = \frac{x+|x|}{2}
            $$
        - PReLU
        - leakyReLU
        - ELU
        - GELU Gaussian Error Linear Unit
            $$
            f(x) = x \Phi(x)
            $$
            - \Phi 正規分布の累積分布関数
        - Swish
        - Mish