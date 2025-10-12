- 制御性能
    - システムの安定性
        放置しても暴走しない
        - 漸近安定性
        - リアプノプ安定性
        - インパルス安定性
        - ステップ安定性
        - 有界入出力安定性/BIBO安定性
        - 内部安定性
    - 追従精度
    - 応答速度
    - overshoot/undershootの有無
    - 外乱への感度
    - 特性変動への感度
- model based control
    - 種類 type
        - 線形制御 linear control
        - 非線形制御 non-linear control
        - digital control
        - process control
        - servant control
    - 古典制御
        - PID制御
            比例要素と積分要素と微分要素
            $$
            u(t) = K_P e(t) + K_I  \int_0^t e(\tau) d\tau + K_D \dot e(t)
            $$
            - 比例要素 proportional
                $$
                K_P e(t)
                $$
            - 積分要素 integral
                $$
                K_I \int_0^t e(\tau) d\tau
                $$
            - 微分要素 derivative
                $$
                $$
        - loop 整形法
    - 現代制御
- model free control
[こんとろラボ](https://controlabo.com/)