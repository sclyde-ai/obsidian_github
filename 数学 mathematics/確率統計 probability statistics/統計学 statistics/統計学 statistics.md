- 基礎単語 basic vocabulary
    - 標本 sample
    - 母集団 population
    - 質的変数と量的変数
        - 質的変数 qualitative
            - 名義尺度
            - 順序尺度
        - 量的変数 quantitive
            - 間隔尺度
                値の差が重要
            - 比例尺度
                値の比が重要
                0の意味が特殊
    - 推定と予測
        - 推定
        - 予測
    - 相関と因果
        - 擬似相関/見かけの相関
            - 潜在変数
        - 因果律
            X → Y
            - 時間的先行性
                 XはYよりも前に起こる
            - 共変関係
                Xが起こればYが必ず起こる
                Xが起こらなければYは起こらない
            - 他変数の影響がない
    - 大文字
        確率変数
    - 小文字
        観測値
    - 標本数と標本サイズ
        | 標本数 | 標本の大きさ/標本サイズ |
        | --- | --- |
        | the number of sample  | sample size |
        | 標本抽出の回数 | 一回の標本抽出で抽出した個体数 |
- 頻度主義 frequentist
    試行を繰り返し行った際の事象の出現頻度の極限値を確率と定義する
- 記述統計 summary/descriptive statistics
    全数調査により母集団の要約や特徴を把握する
    - 要約統計量/記述統計量 summery/descriptive statistics
        標本の特徴を表現するための統計量
        - 積率統計量 moment
            積率母関数から取得できる統計量
            - 平均 average/mean
                - median
                    $$
                    \argmin_{x \in \R} \sum_{i=1}^n|x-x_i|
                    $$
                - mode
                    $$
                    \argmin_{x \in \R} \sum_{i=1}^n
                    \left \{
                    \begin{matrix}
                    1 & if & x = x_i \\
                    0 & if & x \ne x_i
                    \end{matrix}
                    \right.
                    $$
                - arithmetic mean
                    $$
                    \frac{\sum^n_{i=1}x_i}{n} \\
                    =\argmin_{x \in \R} \sum_{i=1}^n (x-x_i)^2
                    $$
                - geometric mean
                    $$
                    \left(\prod_{i=1}^n x_i\right)^{\frac{1}{n}}
                    \\ =
                    \argmin_{x \in \R_{\ne 0}} \sum_{i=1}^n \left(\ln(x) - \ln(x_i)\right)^2
                    $$
                - harmonic mean
                    $$
                    \frac{n}{\sum_{i=1}^n \frac{1}{xi}} \\
                    = \argmin_{x \in \R_{\ne 0}} \sum_{i=1}^n \left(\frac{1}{x} - \frac{1}{x_i}\right)^2
                    $$
                - weighted mean
                    $$
                    \frac{\sum_{i=1}^n w_ix_i}{\sum_{i=1}^n w_i} \\
                    = \argmin_{x \in \R} \sum_{i=1}^n w_i(x-x_i)^2
                    $$
                - generalized mean
                    $$
                    \left(\frac{\sum^n_{i=1}x_i^p}{n}\right)^{\frac{1}{p}}
                    $$
                - quasi-generalized mean
                    $$
                    f^{-1}\left(\frac{\sum^n_{i=1}f(x_i)}{n}\right)
                    $$
            - 分散 variance
                $$
                s^2 = \frac{1}{n} \sum_{i=1}^n (x_i -\bar x)^2
                $$
                - theorem
                    $$
                    s^2 = \bar {(x^2)}-(\bar x)^2
                    $$
                    $$
                    \bar x = \argmin_a \frac{1}{n}\sum_{i=1}^n (x_i -a)^2
                    $$
            - 標準偏差 standard deviation
                $$
                s = \sqrt {\frac{1}{n}\sum_{i=1}^n (x_i -\bar x)^2}
                $$
            - 平均偏差 mean absolute deviation
                $$
                s = \frac{1}{n}\sum_{i=1}^n |x_i -\bar x|
                $$
                - theorem
                    $$
                    median = \argmin_a \frac{1}{n}\sum_{i=1}^n (x_i -a)^2
                    $$
            - 変動係数 CV coefficient of variation
                $$
                \frac{標準偏差}{平均値}
                $$
            - 歪度 skewness
            - 尖度 kurtosis
        - 順序統計量 ordinal
            順序データから取得できる統計量
            $$
            x = \{x_1, ..., x_n\} \\
            x_1 \leq x_2 \leq ... \leq x_n
            $$
            - 中央値 median
                $$
                median(x) = 
                \left\{ 
                \begin{alignedat}{}   
                & x_k && n = 2k-1 \\
                & \frac{x_k + x_{k+1}}{2} && n=2k
                \end{alignedat} 
                \right.
                $$
            - 最頻値 mode
            - 最大値 max
                $$
                \max(x) = x_n
                $$
            - 最小値 min
                $$
                \min(x) = x_1
                $$
            - 範囲 range
                $$
                range(x) = x_n - x_1
                $$
            - 四分位数 quantile
                - 奇数
                    ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image.png)
                - 偶数
                    ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%201.png)
            - 四分位範囲 quantile range
        - 関係統計量 relation
            複数の変数から取得できる統計量
            - 共分散 covariance
                $$
                Cov(x, y) = \frac{S_{xy}}{n}= \sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)
                $$
            - 相関係数 correlation
                $$
                R = r_{xy} = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} = \frac{\sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)}
                {\sqrt{\sum_{i=1}^n (x_i-\bar x)^2 
                \sum_{i=1}^n (y_i-\bar y)^2}}
                $$
                - 相関係数行列
                    $$
                    R_{xx} = 
                    \begin{pmatrix} 
                      r_{x_1x_1} & \dots  & r_{x_1x_p} \\
                      \vdots & \ddots & \vdots \\
                      r_{x_px_1} & \dots  & r_{x_px_p}
                    \end{pmatrix} 
                    $$
    - 可視化
        - graph
            - 円
                割合の比較
            - 横棒
            - 縦棒
            - 線
                時系列の推移
            - 点
                相関関係
        - 度数分布表 histogram
            系列の分布を可視化
        - 箱ひげ図 box plot
            系列の分布を可視化。特に複数系列間の比較に適している
        - 散布図 scatter
            2系列間の相関関係の可視化
        - heatmap
            系列の全ての組み合わせの相関係数を可視化
- 推測統計 inferential statistics
    標本調査をして母集団の特徴を確率的に推測する
    - 推定 estimation
        母数(parameter)の推測
        - 推定量 estimator
            - 最尤推定量
            - 一致推定量
            - 不偏推定量
            - 有効推定量
        - 十分統計量 sufficient
    - 検定 test
        仮説の検証
        - 手順
            1. 仮説
            2. 有意水準
            3. 検定統計量
            4. 結論
        - p-value
        - 分布
            - 標準正規分布/z分布
                - 各種検定
                    - 母比率
                        - 検定
                            1. 仮説
                                $$
                                H_0: p = p \\
                                H_1: p \ne p
                                $$
                            2. 検定統計量
                                $$
                                z = \frac{\frac{x}{n}-p}{\sqrt{\frac{p(1-p)}{n}}}
                                $$
                            3. 棄却域
                                $$
                                |z| > z_{\frac{\alpha}{2}}
                                $$
                            4. 結論
                        - 推定
                        - 標準偏差
                            $$
                            \frac{\frac{X_A}{n_A} - \frac{X_B}{n_B}}{\sqrt{p(1-p)}\sqrt{\frac{1}{n_A} + \frac{1}{n_B}}}
                            $$
                    - 母比率の差
                        - 検定
                            1. 仮説
                                $$
                                H_0: p_A = p_B \\
                                H_1: p_A \ne p_B
                                $$
                            2. 検定統計量
                                $$
                                z = \frac{\frac{x_A}{n_A}-\frac{x_B}{n_B}}{\sqrt{\hat{p}(1-\hat{p})}\sqrt{\frac{1}{n_A}+\frac{1}{n_B}}}
                                $$
                            3. 棄却域
                                $$
                                |z| > z_{\frac{\alpha}{2}}(n-1)
                                $$
                            4. 結論
                        - 推定
            - t分布
                - 検定量
                    - 標本
                        $$
                        X_1, ...,X_n \sim N(\mu, \sigma)
                        $$
                    - 平均 $\bar X$
                        $$
                        \bar X = \frac{1}{n}\sum_{i = 1}^n X_i
                        $$
                    - 不偏分散 $S^2$
                        $$
                        S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar X)^2
                        $$
                    $$
                    t = \frac{\bar{X} -\mu}{S/\sqrt n}
                    $$
                - 区間推定
                    - 自由度 $\phi$
                    $$
                    \bar{x} \pm t_{\frac{\alpha}{2}}(\phi)\sqrt{\frac{\sigma^2}{{n}}}
                    $$
                - 各種検定
                    - 母平均
                        - 検定
                            1. 仮説
                                $$
                                H_0: u = u \\
                                H_1: u \ne u
                                $$
                            2. 検定統計量
                                $$
                                t = \frac{\bar{X} -u}{\sqrt{\frac{s^2}{{n}}}}
                                $$
                            3. 棄却域
                                $$
                                |t| > t_{\frac{\alpha}{2}}(n-1)
                                $$
                            4. 結論
                        - 推定
                            $$
                            \bar{X}-t_{\frac{\alpha}{2}}(n-1)\sqrt{\frac{s^2}{n}}
                            \leq u \leq 
                            \bar{X}+t_{\frac{\alpha}{2}}(n-1)\sqrt{\frac{s^2}{n}}
                            $$
                        - 標準偏差
                            $$
                            \sqrt{\frac{s^2}{{n}}}
                            $$
                        - 自由度
                            $$
                            n-1
                            $$
                    - 母平均の差（分散が等しい）
                        - 検定
                            1. 仮説
                                $$
                                H_0: u_A - u_B = 0 \\
                                H_1: u_A - u_B \ne 0
                                $$
                            2. 検定統計量
                                $$
                                t = \frac{u_A - u_B}{\sqrt{\frac{(n_A-1)s_A^2 + (n_B-1)s_B^2}{n_A+n_B-2}}}
                                $$
                            3. 棄却域
                                $$
                                |t| > t_{\frac{\alpha}{2}}(n_A+n_B-2)
                                $$
                            4. 結論
                        - 推定
                            $$
                            \bar{x}-t_{\frac{\alpha}{2}}(n-1)\sqrt{\frac{(n_A-1)s_A^2 + (n_B-1)s_B^2}{n_A+n_B-2}}\sqrt{\frac{1}{n_A}+\frac{1}{n_B}}
                            \\ \leq u \leq \\
                            \bar{x}+t_{\frac{\alpha}{2}}(n-1)\sqrt{\frac{(n_A-1)s_A^2 + (n_B-1)s_B^2}{n_A+n_B-2}}\sqrt{\frac{1}{n_A}+\frac{1}{n_B}}
                            $$
                        - 標準偏差
                            $$
                            \sqrt{\frac{(n_A-1)s_A^2 + (n_B-1)s_B^2}{n_A+n_B-2}}\sqrt{\frac{1}{n_A}+\frac{1}{n_B}}
                            $$
                        - 自由度
                            $$
                             n_A+n_B -2
                            $$
                    - 母平均の差（分散が異なる）
            - カイ二乗分布
                $$
                \chi^2 = \frac{S}{\sigma^2}
                $$
                - 各種検定
                    - 母分散
                        - 検定
                            1. 仮説
                                $$
                                H_0: \sigma^2 = \sigma^2 \\
                                H_1: \sigma^2 \ne \sigma^2
                                $$
                            2. 検定統計量
                                $$
                                \chi^2 = \frac{S}{\sigma^2}
                                $$
                            3. 棄却域
                                $$
                                \chi^2 < \chi^2_{1-\alpha/2}(n-1),\ \chi^2_{\alpha/2}(n-1) < \chi^2
                                $$
                            4. 結論
                        - 推定
                            $$
                            \frac{S}{\chi^2_{\alpha/2}(n-1)}, \frac{S}{\chi^2_{1-\alpha/2}(n-1)}
                            $$
                    - 母分散の比
                        - 検定
                            1. 仮説
                                $$
                                H_0: \sigma^2 = \sigma^2 \\
                                H_1: \sigma^2 \ne \sigma^2
                                $$
                            2. 検定統計量
                                $$
                                \chi^2 = \frac{S}{\sigma^2}
                                $$
                            3. 棄却域
                                $$
                                \chi^2 < \chi^2_{1-\alpha/2}(n-1),\ \chi^2_{\alpha/2}(n-1) < \chi^2
                                $$
                            4. 結論
                        - 推定
                            $$
                            \frac{S}{\chi^2_{\alpha/2}(n-1)}, \frac{S}{\chi^2_{1-\alpha/2}(n-1)}
                            $$
            - F分布
        - 検定
            - 適合度
                - 検定
                    1. 仮説
                    2. 検定統計量
                    3. 棄却域
                    4. 結論
                - 推定
            - 独立性
                - 検定
                    1. 仮説
                    2. 検定統計量
                    3. 棄却域
                    4. 結論
                - 推定
            - 尤度比 likelihood ratio test
            - 分散分析 ANOVA
            - fisherの正確性
            - wilcoxon順位和検定
            - K-S検定
- 統計模型選択基準 IC information criterion
    - AIC Akaike
        $$
        2k -2 \ln \hat L
        $$
        k : the number of parameter
        L : maximum likelihood
        - how to derive
            maximize the relative entropy
            - observation
                $$
                \{x_1, x_2, ..., x_n\}
                $$
    - BIC Bayesian
        $$
        -2\ln (\hat L)+k \ln(n)
        $$
    - AICc Akaike corrected
        $$
        AIC + \frac{2k(k+1)}{n-k-1}
        $$
    - DIC deviance
    - ABIC
    - HQIC Hannan-Quinn
        $$
        -2\ln (\hat L)+ 2k \ln (\ln(n))
        $$
    - MDL
    - cross validation
    - mallow Cp
        $$
        \frac{SSE}{MSE}+2p-n
        $$
        SSE 残差平方和
        MSE 平均二乗誤差
    - log likelihood
- 因果推論
    - modularity
- probabilistic machine learning
- 確率的機械学習