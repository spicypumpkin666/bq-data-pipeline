TEST_ADDRESS = "0x00000000006c3852cbef3e08e8df289169ede581"

def BIGQUERY(address=None):
    return f"""SELECT
                  transactions.from_address,
                  count(transactions.from_address) as count
              FROM
              bigquery-public-data.crypto_ethereum.contracts as contracts
              JOIN bigquery-public-data.crypto_ethereum.transactions as transactions
              ON contracts.address = transactions.to_address
              WHERE contracts.address = {"'" + address + "'"}
              AND transactions.block_timestamp > TIMESTAMP('2023-01-01 00:00:01 UTC')
              GROUP BY contracts.address, transactions.from_address
              ORDER BY count desc
              LIMIT 10;"""



CREATE = """ CREATE TABLE IF NOT EXISTS opensea_users (
                id INTEGER PRIMARY KEY, 
                address TEXT NOT NULL, 
                interactions TEXT NOT NULL, 
                ethBalance REAL NOT NULL, 
                lastUpdatedAt DATETIME NOT NULL   
                );"""

INSERT = "INSERT INTO opensea_users " \
               "(id,address,interactions,ethBalance,lastUpdatedAt) " \
               "VALUES(?,?,?,?,?)"