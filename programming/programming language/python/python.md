### data型
- bool
### prefix
- f
    formated string literal
- b
    bytes literal
- r
    raw string literal
- u
    unicode string literal
### 書式code
- strfftime 
### useful template
### with & context manager
- context manegerあり
    ```
    with ContextManeger() as file:
        ...
    ```
- context mangerなし
    ```
    file = ContextManager()
    try:
        ...
    finally:
        file.close()
    ```