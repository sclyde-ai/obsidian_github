# special files
- __init__.py
- setup.py
- pyproject.toml
# src layout
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
# flat layout
    project/
    ├── package/  
    │   ├── __init__.py
    │   └── module1.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_module1.py
    ├── pyproject.toml
    └── README.md
# application layout
    app/
    ├── app/
    │   ├── __main__.py
    │   ├── models/
    │   ├── views/
    │   └── controllers/
    ├── libs/
    │   └── common_utils/
    ├── configs/
    │   ├── development.toml
    │   └── production.toml
    ├── scripts/
    │   └── migrate_db.py
    ├── tests/
    ├── docs/
    ├── pyproject.toml
    └── README.md