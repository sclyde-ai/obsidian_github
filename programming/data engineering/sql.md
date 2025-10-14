# operation
- SELECT
	dataを取得する
	- SELECT * FROM table; tableの中身を一覧で取得する
- UPDATE
- INSERT
	tableに新しい行を追加する
	- INSERT INTO table (column1, ...) VALUES (value1, ...); 
		tableのcolumnにvalueを追加する
- UPSERT
- CREATE
```sql
-- database
CREATE DATABASE database_name;
-- table
CREATE TABLE table_name (
	column1 datatype,
	column2 datatype,
	column3 datatype,
	...
);
```
- DROP
```sql
-- database
DROP DATABASE table_name;
-- table
DROP TABLE table_name;
```
- ALTER
# transaction operation
- BEGIN
    transactionを開始する
- COMMIT
    transactionを確定する
- ROLLBACK
# backslash
\d : 
\dt : tableを一覧で表示する
\l : 
- link
  https://zenn.dev/umi_mori/books/331c0c9ef9e5f0