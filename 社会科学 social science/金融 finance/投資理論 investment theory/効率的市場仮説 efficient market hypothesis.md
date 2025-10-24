情報は即座に市場全体に浸透する
投資家の反応が正規分布に従う
- weak-form efficiency
    過去の価格のhistorical dataを全て反映 
- semi-strong-form efficiency
    会計情報や株式分割情報の公開情報も反映
- strong-form efficiency
    insider情報や有料情報などの非公開情報も反映
- Proof That Properly Anticipated Prices Fluctuate Randomly (実証研究)
    市場が効率的であれば価格は酔歩運動に従う
    [investmenttheory.org](https://investmenttheory.org/uploads/3/4/8/2/34825752/paulsamuelson-proof.pdf)
- Grossman-Stiglitz paradox
    - original article
        [https://www.aeaweb.org/aer/top20/70.3.393-408.pdf](https://www.aeaweb.org/aer/top20/70.3.393-408.pdf)
    - the model
        R : the return of a safe asset
        u : the return of a risky asset 
        $$
        u = \theta + \epsilon
        $$
        \theta : random variable observable at a cost c
        \epsilon : random variable unobservable
        x : the supply of the risky assets
        \lambda : the percentage of informed traders
         P : price
        $$
        P_\lambda (\theta, x)
        $$
    - conjectures
        1. the more individuals are informed, the more informative is the price system
        2. the more individuals are informed, the lower the ratio of expected utility of the informed to the uninformed
        3. the higher the cost of information, the smaller will be the equilibrium percentage of individuals who are informed 
        4. If the quality of the informed trader's information increases, the more their demands will vary with their information and thus the more prices will vary with \theta
        5. The greater the magnitude of noise, the less informative will the price system be
        6. In the limit, when there is no noise, prices convey all information, and there is no incentive to purchase information.
        7. markets will be thinner under those conditions in which the percentage of individuals who are informed (X) is either near zero or near unity.
    - the securities
        - risk-less asset $M_i$
        - risky asset $X_i$
        $$
        W_{0i} = M_i + PX_i \\
        W_{1i} = RM_i + uX_i
        $$
    - Individual’s utility Maximization
        - assumption
            all individuals have the same utility function
        $$
        V_i(W_{1i}) = V(W_{1i}) = -e^{-aW_{1i}}, a>0
        $$
        a : the coefficient of absolute risk aversion 
        - informed
            $$
            X_I = \frac{\theta - RP}{a \sigma^2_{\epsilon}}
            $$
            - proof
                - \theta, \epsilon : multivariate normal distribution
                    $$
                    \mathbb E[\epsilon] = 0 \\
                    \mathbb E[\theta \epsilon] = 0 \\
                    Var(u^*|\theta) = Var(\epsilon^*) =\sigma^2_\epsilon > 0
                    $$
                $$
                \mathbb E[V(W_{1i})| \theta] = -\exp \left((-a)\mathbb E[W_{1i}|\theta] + \frac{(-a)^2}{2}Var[W_{1i}|\theta]\right)
                $$
                - expectation & variance
                    $$
                    W_{1i} = R(W_{0i} - PX_i) + uX_i \\
                    $$
                    $$
                    \mathbb E[W_{1i}|\theta] = RW_{0i} +X_I(-RP + \mathbb E[u|\theta]) \\
                    = RW_{0i} +X_I(-RP + \theta) 
                    $$
                    $$
                    Var[W_{1i}|\theta] = X_I^2 \sigma_\epsilon^2
                    $$
                $$
                = - \exp \left(-a[RW_{0i} + (\theta - RP)X_I - \frac{a}{2} \sigma_\epsilon^2 X_I^2] \right)
                $$
                maximize it with respect to X
                $$
                \frac{d \mathbb E[V(W_{1i})| \theta]}{d X_I} = 0 \\
                (\theta - RP- a \sigma^2_{\epsilon}X_I) \mathbb E[V(W_{1i})| \theta] = 0 \\
                X_I = \frac{\theta - RP}{a \sigma^2_{\epsilon}}
                $$
        - uninformed
            $$
            X_U = \frac{\mathbb E[u^* | P^*(\theta,x) = P] - RP}{a Var E[u^* | P^*(\theta,x) = P]}
            $$
    - demand and supply equibalium
    - question
        - budget constraint vs wealth
    - my interpretation
        金融資産の価格に全ての市場参加者の私的情報が反映される
        - proof of preposition
            A 効率的市場仮説(全ての情報が市場に反映される)
            B 情報収集に利益が存在する
            C 情報収集する人が存在する
            - Aを仮定
                $$
                A \Rightarrow \lnot B \\
                \lnot B \Rightarrow \lnot C \\
                \lnot C  \Rightarrow \lnot A 
                $$
                $$
                A \Rightarrow \lnot A
                $$
                矛盾
            - ¬Aを仮定
                $$
                \lnot A \Rightarrow B \\
                B \Rightarrow C \\
                C \Rightarrow A
                $$
                $$
                \lnot A \Rightarrow A
                $$
                矛盾
- 結合仮説問題 joint hypothesis problem
    市場効率性の（証明や反証のような十分な）検証を絶対的に不可能とする説