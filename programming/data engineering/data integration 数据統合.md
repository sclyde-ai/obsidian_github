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