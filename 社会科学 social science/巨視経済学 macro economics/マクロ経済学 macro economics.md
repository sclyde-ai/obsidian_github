- 数学理論 math theory
    - 45度分析
    - IS-LM analysis
        - IS Investment-Savings 財サービス市場
                $$
                Y = C + I + G + NX
                $$
                - C consumption 消費
                    $$
                    C = c_0 + c_1*(Y-T) \\
                    \frac{\partial C}{\partial (Y-T)} = c_1 > 0
                    $$
                - 可処分所得
                        $$
                        Y - T
                        $$
                    - 限界消費性向 MPC marginal propensity to consume
                        $$
                        c_1 
                        $$
                    - 限界貯蓄性向 MPS marginal propensity to save
                        $$
                        1 - c_1
                        $$
                - I investment 投資
                    $$
                    I = i_0 + i_1*r \\
                    \frac{\partial I}{\partial r} = i_1 < 0    
                    $$
                    - $i_1$ 利子弾力性 interest elasticity of investment
                    - r 金利 rate
                - G government expenditure 政府支出
                - NX net export 純輸出 (trade balance 貿易収支)
                    $$
                    NX(e) = EX(e) - IM(e) \\
                    \frac{\partial NX}{\partial e} < 0
                    $$
                    - EX 輸出 export
                    - IM 輸入 import
                    - e 為替レート
                - S saving 貯蓄
                    $$
                    S = I = Y - C - G \\
                    = (Y - T - C) + (T - G) \\ 
                    = PS + GS
                    $$
                    - PS private saving 民間貯蓄
                        $$
                        PS = Y-T-C
                        $$
                    - GS government saving 公的貯蓄
                        $$
                        GS = T-G
                        $$
                - T tax 税
            - LM Liquidity-Money 貨幣市場
                $$
                \frac{M}{P} = F(Y, r) \\
                \frac{\partial F}{\partial Y} > 0, \frac{\partial F}{\partial r} < 0
                $$
                - M 貨幣供給量 money supply
                    - M1 = 要求払い預金 demand deposit
                    - M2 = M1 + 準通貨 quasi money
                    - M3 = M2 + 譲渡性預金 CD
                - P 物価 price
                - Y 生産量 yield
                - r 金利 rate
                - 変数を動かすと…
                    金利上昇→物価上昇
                    金利下落→物価下落
                    通貨量増加→物価上昇
                    通貨量減少→物価下落
            - 金融政策
                Mの変更 → LM曲線の移動
                rの変更
            - 財政政策
                G or Tの変更 → IS曲線の移動
            - 開放経済
                $$
                NX \ne 0
                $$
                - 変動為替相場制度
                    - 外生変数
                        - G
                        - T
                        - r*
                        - P
                    - 内生変数
                        - Y
                        - r
                        - e
                        - NX
                - 固定為替相場制度
                    - 外生変数
                        - G
                        - T
                        - e
                        - r*
                        - P
                    - 内生変数
                        - Y
                        - r
                        - M
                        - NX
            - 閉鎖経済
                $$
                NX = 0
                $$
                - 外生変数
                    - G
                    - T
                    - M
                    - P
                - 内生変数
                    - Y
                    - r
            - 小国
            - 大国
        - AD-AS model
            - AD aggregate demand
            - AS aggregate supply
- 古典派経済学 classical
        神の見えざる手
        労働価値説
        - 基本概念
            - 労働価値説
                商品の価値は商品生産に必要な労働量によって客観的に決まる。
                - 使用価値 use-value
                - 交換価値 exchange-value
                - 価値≠貨幣
                - 投下労働説
                - 支配労働説
            - 富
                国家の富とは消費財のこと
            - 神の見えざる手
        - 価格調整/セイの法則
            需要と供給が価格の変動により均衡する
        - 成長模型 growth model
            - Solow-Swan model(neoclassical growth model)
                1. **生産関数**
                    $$
                    Y=F(K,L,A)
                    $$
                    $Y$ : 総生産量
                    $K$ : 資本ストック
                    $L$ : 労働投入
                    $A$ : 技術水準（全要素生産性）
                    - **限界生産性逓減の法則**
                        $$
                        \frac{\partial^2 F(K)}{\partial K^2}  < 0
                        $$
                2. **資本蓄積式**
                    $$
                    \frac{\partial K}{\partial t} =sF(K)−\delta K
                    $$
                    $s$ : 貯蓄率
                    $\delta$ : 資本減耗率
                3. **定常状態 Steady State**
                    変数が一定の率で成長し続ける状態
                    $$
                    \frac{\partial K}{\partial t} = 0 
                    $$
                4. **黄金律 Golden Rule**
                    定常状態で消費を最大にする資本
                    $$
                    F(K^*)−δK^*=0
                    $$
                    $K^*$ : 定常状態の資本 
            - neoclassical stochastic growth model
                1. 目的関数
                    $$
                    \max_{k_{t+1}, c_t, \ell_t} \mathbb{E}_0 [\sum_{t=0}^\infty \beta^t u(c_t, \ell_t)]
                    $$
                    - $c_t$ : 消費
                    - $l_t$ : 労働
                    - $k_{t+1}$ : 次期の資本
                    - $\beta \in (0, 1)$: 割引率
                    - $u$ : 効用関数
                2. 制約条件
                    $$
                    c_t + k_{t+1} = (1 - \delta) k_t + \theta_t f(k_t, \ell_t)
                    $$
                    - $\delta \in (0, 1)$ : 資本減耗率
                    - $f$ : 生産関数
                3. 生産性の確率過程
                    $$
                    \ln \theta_{t+1} = \rho \ln \theta_t + \sigma \varepsilon_{t+1} \quad \varepsilon_{t+1} \sim N(0, 1)
                    $$
                    - $\theta_t$ : 生産性レベル。
                    - $\rho$ : 自己相関係数 $(-1 < \rho < 1)$
                    - $\sigma$ : ショックの標準偏差
            - endogenous growth theory
        - 貨幣数量説
            - fisher方程式
                $$
                MV = PY
                $$
                M 貨幣供給量
                V 貨幣の所得流通速度
                P 価格水準
                Y 生産量
        - 完全分配の法則
            $$
            pY = wL + rK
            $$
            p 物価 price 
            Y 生産量 yield
            w 賃金 wage
            L 労働量 labor
            r 株価 stock price
            K 資本 capital
        - 人物
            - Adam Smith
            - David Ricardo
- 新古典派経済学 neoclassical
        効用理論
        - Lucas critique
            期待または経済法則が再帰性を持つ
            政策を変更したことで、人の行動と期待が変化し、政策の効果を変える可能性がある。
            解決策として期待形成の過程を考慮する必要がある
        - 合理的期待仮説 rational expectations hypothesis
            個々の経済主体は、利用可能な全ての情報をもとに将来の経済変数の予測を行う。
        - real business cycle
        - 人物
            - Alfred Marshall
- マルクス経済学 Malxian
        - 剰余価値説
            不払労働が剰余価値となる
        - 人物
            - Karl Marx
- ケインズ経済学 Keynesian
        - 数量調整/有効需要の原理
            需要と供給が生産量の変動により均衡する
        - 三面等価
            総生産と総所得と総支出は常に等しい
        - 人物
            - John Maynard Keynes
- 現代貨幣理論 MMT modern monetary theory
        自国通貨を発行できる政府は財政赤字で破綻しない、財政赤字を気にせず公共事業を拡充できる、という経済理論
        governments with fiat currencies (like the US, UK, Japan, and Canada) can create money to finance their expenditures without being limited by revenues or borrowing