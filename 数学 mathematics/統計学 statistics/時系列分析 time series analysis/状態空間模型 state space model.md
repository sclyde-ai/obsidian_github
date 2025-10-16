観測できない「状態」が「観測値」に影響を与える
- 画像 image
    ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image.jpeg)
- data
    - 観測値 observation
        $$
        y = (y_1, y_2,...)
        $$
    - 状態 state
        $$
        a = (a_1,a_2,...)
        $$
- 方程式
    - 観測方程式
        観測値と状態の関係式
        $$
        y_t = f(a_t) + \epsilon_t
        $$
    - 状態方程式
        状態の時間経過による関係式
        $$
        a_t = g(a_{t-1}) + \eta_t
        $$
- 推定
    - filtering
        過去と現在の観測値からnoiseを除去して状態を推定する
        - 画像 image
            ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%201.jpeg)
    - 平滑化 smoothing
        過去、現在、未来の観測値から状態を推定する
        - 画像 image
            ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%202.jpeg)
    - 将来予測 forecasting
        現在の状態から未来の状態を推定する
        - 画像 image
            ![image.jpeg](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%203.jpeg)
- 例 example
    - Kalman filter 線形
        - 観測方程式
            $$
            y_t = Z_t a_t + \epsilon_t
            $$
        - 状態方程式
            $$
            a_t = T_t a_{t-1} + \eta_t
            $$
- website
    [Pythonによるビジネス予測に活かす「状態空間モデル」の基礎と実装例](https://www.salesanalytics.co.jp/datascience/datascience250/)