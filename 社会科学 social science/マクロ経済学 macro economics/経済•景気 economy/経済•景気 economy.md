---
alias:
    ['経済', '景気', 'economy']
---
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