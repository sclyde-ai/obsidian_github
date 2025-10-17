- 仕組み system
    - block
        - transaction data
        - timestamp
        - previous block’s hash
        - nonce/number used once
    - chain
    - consensus mechanism
        - math
            user : n 
            remaining block : m
        - PoW proof of work
        - PoS proof of stake
        - PoA proof of authority
- 長所 merit
    - 改竄耐性 tamper-proofing
    - 追跡可能性 traceability
    - 分散型 decentralization
- 短所 demerit
    - scalability問題
        参加者や取引数が増加すると処理に時間がかかってしまう問題
    - 51%攻撃
        過半数の計算資源を誰か一人が独占すると改竄が容易になるという問題
- 処理方式
    - on-chain
        全ての取引をblockchainに記録する。
    - off-chain
        最終結果のみをblockchainに記録する。取引や処理は外部で行う。
    |  | on-chain | off-chain |
    | --- | --- | --- |
    | 分散性 | 高い | 低い |
    | 透明性 | 高い | 低い |
    | 処理速度 | 遅い | 早い |
- 参加形式
    - 参加自由型 permissionless
        参加者に制限がなく許可が必要ない
        - public
            誰でも参加できる
    - 許可型 permissioned
        特定の人のみが参加できる
        - consortium
            複数の管理者が存在する
        - private
            単独の管理者によって参加者が制限される
    |  | public  | private |
    | --- | --- | --- |
    | 分散性 | 高い | 低い |
    | 透明性 | 高い | 低い |
    | 処理速度 | 遅い | 早い |

- 社会実装例
    - 貨幣
    - supply chain
    - 物流
    - 医療情報
    - 秘匿データ
    - 電子投票