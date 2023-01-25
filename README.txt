
ETL to extract data from BigQuery's public ethereum dataset, combine it with data from on chain and deposit it into a
SQLite database.

Pipeline runs with `python3 main.py`, with option to add a contract address like 'python3 main.py 0xcontractaddress'

Doesn't yet run with docker. 