# Project setup:
`init.sh` - bash script to setup venv

# Test csv generator
`generate_csv_base.sh` - crate csv with fake data


# Test save csv to database 
`save_csv_to_database_base.sh` - save csv with fake data to the database

# Run tests
`test.sh`

# Run pylint
`pylint.sh`

# Run mypy
`mypy.sh`


# Test coverage: module `csv_handler`
|  Name | Stmts  | Miss  | Cover  |
|---|---|---|---|
|csv_handler/__init__.py  |                        0   |   0  | 100%|
|csv_handler/csv_generator/__init__.py     |       0   |   0  | 100%|
|csv_handler/csv_generator/csv_generator.py  |    36   |   0  | 100%|
|csv_handler/csv_generator/utils.py   |           15   |   0  | 100%|
|csv_handler/csv_parser/__init__.py   |            0  |    0  | 100%|
|csv_handler/csv_parser/csv_parser.py  |           8  |    0  | 100%|
|csv_handler/db_handler/__init__.py    |           0  |    0  | 100%|
|csv_handler/db_handler/handler.py    |           20  |   20  |   0%|
|csv_handler/settings.py             |           17   |   0   |100%|
|csv_handler/utils/__init__.py       |             0  |    0  | 100%|
|csv_handler/utils/log.py         |               24   |   0   |100%|
|---|---|---|---|
| TOTAL   |  120 | 20  |  83%  |