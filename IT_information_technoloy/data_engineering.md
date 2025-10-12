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
            - RD relational database
                a type of database that organizes data into tables, with rows and columns, where data points are related to each other
                ![image.png](学問%20academics/notion/IT/ExportBlock-2d668fb2-00bc-4ec6-9092-d6ebd07875b4-Part-1/image%203.png)
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
        - data integration
            - 3要素
                - 抽出 extract
                    extract or copy raw data from multiple sources and store it in a staging area.
                - 変換 transform
                    transform and consolidate the raw data in the staging area to prepare it for the target data warehouse.
                    - 削除と整形 cleansing
                        removes errors and maps source data to the target data format.
                    - 重複削除 deduplication
                        identifies and removes duplicate records.
                    - 形式化 format revision
                        converts data, such as character sets, measurement units, and date/time values, into a consistent format.
                    - 導出 derivation
                        applies business rules to your data to calculate new values from existing values.
                    - joining
                        links the same data from different data sources.
                        - example
                            you can find the total purchase cost of one item by adding the purchase value from different vendors and storing only the final total in the target system.
                    - 分割 splitting
                        divide a column or data attribute into multiple columns in the target system. 
                        - example
                            if the data source saves the customer name as “Jane John Doe,” you can split it into a first, middle, and last name.
                    - 要約 summarization
                        improves data quality by reducing a large number of data values into a smaller dataset.
                    - 暗号化 encryption
                - 保存 load
            - ETL extract, transform, load
            - ELT extract, load transaction
            - 一時保存領域 staging area
            - EAI enterprise application integration
        - data warehouse
        - data lake