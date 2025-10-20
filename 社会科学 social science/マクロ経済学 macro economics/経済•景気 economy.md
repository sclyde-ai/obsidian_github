- 定義 def
    - 経済/経世済民
        人々が生活に必要なモノやサービスの生産、分配、消費を行う活動とその仕組み全体
    - 景気
        売買・取引などの経済活動の状況
    - economy
        - the system of trade and industry by which the wealth of a country or region is made and used = 経済
        - the state of a country or region in terms of the production and consumption of goods and services and the supply of money = 景気
- 貸借の効果
    - 貸借なし
        消費=生産
        個人の消費量と生産量の合計は等しい
    - 貸借あり
        - 貸手
            先に消費するために債務を負う。支払金利が発生する。
            金利の分だけ生産を増やさなければならない
            全体として消費<生産となる。
        - 借手
            先に消費するために債権を得る。受取金利が発生する。
            金利の分だけ消費を増やせる
            全体として消費>生産となる。
- 金利に対する反応
    | 金利 | 上昇 | 下落 |
    | --- | --- | --- |
    | 株式 | 下落 | 上昇 |
    | 既発債 | 下落 | 上昇 |
    | 新発債 | 上昇 | 下落 |
    | 為替 | 高 | 安 |
    - 株式市場
        - 金利増加
            - 借入費用の増加して企業の収益が減少するので株価は下落する
            - 割引率が上昇してcashflowの価値が上昇するので株価は下落する
            - 債券の価値が上昇するので相対的に株価は下落する
    - 債券市場
        - 金利増加
            - 新発債の価値が上昇する
            - 新発債の価値が上昇するので相対的に既発債の価値が下落する
    - 為替市場
        - 金利増加
            - その通貨の金利による収益が増加するので価格は上昇する
    - 生産と消費、借入と貸出は互いに打ち消し合う
    - 金利は蓄積する
- 好景気/好況 boom
    経済活動が活発
    - 物価上昇 inflation
        物価が継続的に上昇すること
        a sustained increase in the general price level of goods and service
    - 経済活動
        - 消費/需要増加
        - 生産/供給増加
    - 企業
        - 雇用/賃金増加
        - 株価上昇
    - 貸借
        - 借入/貸出増加
            消費を増やすため
            生産を増やすため
    - 物価上昇が進むと…
        物価の上昇を抑えるため金利を上げる 
- 不景気/不況 recession
    経済活動が停滞
    - 物価下落 deflation
        物価が継続的に下降すること
        a sustained decrease in the general price level of goods and service
    - 経済活動
        - 消費/需要減少
        - 生産/供給減少
    - 企業
        - 雇用/賃金減少
        - 株価下落
    - 貸借
        - 借入/貸出減少
            金利の負担を減らすため
    - 物価下落が進むと…
        物価の下落を抑えるため金利を下げる
- stagflation
    不況によって需要が落ち込む通常とは異なり、原油価格の高騰などコスト要因によって不況下でも物価が上昇し、生活が苦しくなる厳しい経済状況
    the combination of high inflation, stagnant economic growth, and elevated unemployment
- depression
    a severe, long-term decline in economic activity characterized by significantly reduced output and productivity, high unemployment, and a substantial drop in GDP, lasting for several years or more
- mermaid 図表
    ```mermaid
    sequenceDiagram
        participant 消費
        participant 需要
        participant 供給
        participant 生産
        participant 借入
        participant 貸出
        participant 金利
        Note over 消費,借入: 借手
        Note over 貸出,金利: 貸手
        Note over 消費,需要: 消費者
        Note over 供給,生産: 生産者
    ```
    ```mermaid
    graph
    subgraph 消費者
        消費
        需要
    end
    subgraph 生産者
        供給
        生産
    end
    subgraph 貸手
        貸出
        金利
    end
    subgraph 借手
        direction LR
        消費者
        生産者
        借入
    end
    消費 <--> 需要
    需要 <--> 供給
    供給 <--> 生産
    消費 <--> 借入
    生産 <--> 借入
    借入 <--> 貸出
    貸出 --> 金利
    金利 --> 借入
    ```
    1. 需要増加
    2. 消費増加
    3. 供給増加
    4. 生産増加
    5. 借入増加
    6. 貸出増加
- boom and bust 栄枯盛衰