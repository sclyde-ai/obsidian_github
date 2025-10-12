- DDL data definition language
    - CREATE
        - database
            ```sql
            CREATE DATABASE database_name;
            ```
        - table
            ```sql
            CREATE TABLE table_name (
                column1 datatype,
                column2 datatype,
                column3 datatype,
                ...
            );
            ```
    - DROP
        - database
            ```sql
            DROP DATABASE table_name;
            ```
        - table
            ```sql
            DROP TABLE table_name;
            ```
    - ALTER
- DML data manipulation language
    - INSERT INTO VALUES
        ```sql
        INSERT INTO table_name (column1, column2, column3, ...)
        VALUES (value1, value2, value3, ...);
        ```
    - UPDATAE SET
        ```sql
        UPDATE table_name
        SET column1 = value1, column2 = value2, ...
        WHERE condition;
        ```
    - DELETE FROM
        ```sql
        DELETE FROM table_name
        WHERE condition;
        ```
    - SELECT FROM
        ```sql
        SELECT column1, column2, ...
        FROM table_name
        WHERE condition;
        ```
        - all
            ```sql
            SELECT * FROM table_name;
            ```
        - order
            ```sql
            SELECT column1, column2, ...
            FROM table_name
            ORDER BY column1 ASC|DESC;
            ```
        - function
            ```sql
            SELECT COUNT(column_name) FROM table_name;
            SELECT SUM(column_name) FROM table_name;
            SELECT AVG(column_name) FROM table_name;
            SELECT MIN(column_name) FROM table_name;
            SELECT MAX(column_name) FROM table_name;
            ```
        - group
            ```sql
            SELECT column1, COUNT(column2)
            FROM table_name
            GROUP BY column1;
            ```
- DCL data control language
    - BEGIN
    - COMMIT
    - ROLLBACK
    - SAVEPOINT
- DBMS database management system
- RDBMS relational database management system
- example
    - MySQL
    - mariaDB
    - PostgreSQL