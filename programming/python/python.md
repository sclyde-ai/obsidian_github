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
- import anything from parent dir
	```
	import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)
	```

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