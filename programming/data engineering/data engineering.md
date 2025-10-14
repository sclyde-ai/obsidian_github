- data engineering
        - data
            - 種類 type
                - queue
                - stack
            - 構造 structure
                - 指標データ index data
                - checkpoint data
                    a snapshot of the data at a specific point in time, ensuring data consistency and allowing the system to resume processing from that point after a crash
                - 辞書データ dictionary data
                    metadata like object, user info, access auth, security and so on
                - log data
        - database
            - table
            - transaction
                the unit of process updating data
                - ACID
                    - atomicity 原始性
                        - 全ての操作が完全に実行される
                        - 一切実行されない
                        上記の2つの状況しか発生しないこと
                    - consistency 一貫性
                        transaction完了後にdatabaseの規則が変化しないこと
                        - idempotent
                    - isolation 独立性/分離性
                        transactionの途中経過が他のtransactionに影響を与えないこと
                    - durability 耐久性/永続性
                        transactionがcommitされると、その変更が永続的にdatabaseに保存されること
                - 操作 operation
                    - BEGIN
                        transactionを開始を宣言する
                    - COMMIT
                        transactionの全ての操作を確定する
                    - ROLLBACK
                        transactionの操作を取消する
                        - ROLLBACK TO
                            savepointまでrollbackする
                            ```sql
                            ROLLBACK TO save_point
                            ```
                    - SAVEPOINT
                        中間点設定して部分的なrollbackを可能にする
                        - RELEASE SAVEPOINT
                            savepointを解消する
                        - code example
                            ```sql
                            BEGIN;
                            UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A';
                            SAVEPOINT savepoint1;
                            UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B';
                            -- エラーが発生した場合
                            ROLLBACK TO savepoint1; -- savepoint1以降の操作をキャンセル
                            COMMIT;
                            ```
                    - SET TRANSACTION
                    - LOCK
                        他のtransactionによるaccessを制御する
                        - SHARE
                        - EXCLUSIVE
                - roll forward
                - lock
                    held on SQL Server resources, such as rows read or modified during a transaction, to prevent concurrent use of resources by different transactions
                - deadlock
                    occurs when two or more processes are unable to proceed because each is waiting for the other to release resources
                - commit
                - aport
            - backup
                - 完全 full
                    | Sunday  | Monday | Tuesday  | Wednesday |
                    | --- | --- | --- | --- |
                    | 1 2 | 1 2 3 | 1 2 3 4 | 1 2 3 4 5 |
                    | full | full | full | full |
                - 差分 differential
                    | Sunday  | Monday | Tuesday  | Wednesday |
                    | --- | --- | --- | --- |
                    | 1 2 | 3 | 3 4 | 3 4 5 |
                    | full | diff | diff | diff |
                - 増分 incremental
                    | Sunday  | Monday | Tuesday  | Wednesday |
                    | --- | --- | --- | --- |
                    | 1 2 | 3 | 4 | 5 |
                    | full | inc | inc | inc |
                |  | backup time | restoration time |
                | --- | --- | --- |
                | full | long | short |
                | differential | middle | middle |
                | incremental | short | long |
        - data warehouse
        - data lake