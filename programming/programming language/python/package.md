---
alias:
    ['package']
---
## special files
- __init__.py
- setup.py
- pyproject.toml
## layout
-  src layout
    project/
    ├── src/
    │   └── package/
    │       ├── __init__.py
    │       └── module1.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_module1.py
    ├── pyproject.toml
    ├── README.md
    └── .gitignore
-  flat layout
    project/
    ├── package/  
    │   ├── __init__.py
    │   └── module1.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_module1.py
    ├── pyproject.toml
    └── README.md