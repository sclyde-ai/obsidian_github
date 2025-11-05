---
alias:
    ['ベイズ統計', 'Bayesian statistics']
---
    主観に基づく確率を新情報を追加しながら改善する
- 客観確率 objective probability
    客観的な観測結果と理論的考察により導く確率
- 主観確率 subjective probability
    ある主体が評価した確率
- 事前確率 prior probability
    情報がないときの確率
- 事後確率 posterior probability
    情報があるときの確率
- ベイズの定理 Bayesian theorem
    $$
    \mathbb P(\theta|x) 
    = \frac{\mathbb P(x|\theta)\mathbb P(\theta)}{\mathbb P(x)} 
    $$
- ベイズ推定
- 尤度 likelihood
    dataが得られたときそのdataの得られやすさを表す
    - 設定 setting
        - 母数\theta
        - 標本 X = X_1, …, X_n
        - 母集団 D
        - 確率分布関数 f_D
        - 観測値 x = x_1, …, x_n
    - 尤度関数 likelihood function
        $$
        L(\theta) = f_D(x|\theta) = \mathbb P(x|\theta)
        $$
        - 問題設定
            「母数\thetaが不明な確率分布f_Dに従う母集団から標本を得た時データを説明する\thetaは?」
            観測値が得られる確率は
            $$
            f_D(x_1,...,x_n|\theta) = \mathbb P(x_1, ...,x_n|\theta)
            $$
            この確率を最大にする\thetaを求めたい
    - 最尤推定 MLE maximum likelihood estimation
        $$
        \hat \theta = \argmax_\theta L(\theta)
        $$
        - 尤度方程式
            $$
            \frac{\partial}{\partial \theta} \ln L(\theta) = 0
            $$
    - 最大事後確率推定 MAP maximum a posteriori estimation
        $$
        \hat \theta 
        = \argmax_\theta \mathbb P(\theta|x) 
        = \argmax_\theta \frac{\mathbb P(x|\theta)\mathbb P(\theta)}{\mathbb P(x)} 
        = \argmax_\theta \mathbb P(x|\theta)\mathbb P(\theta)
        $$
    - website
        [院生卒業してからやっと最尤推定を理解した話｜HAO WANG](https://note.com/hao_wang/n/n540922596e93)
        [最尤推定とベイズ推定 - Qiita](https://qiita.com/k8o/items/23e70d7ea8d797b6ff86)