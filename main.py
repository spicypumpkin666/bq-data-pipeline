import sys
import logging as log

from db import Database
from get_node_data import W3NodeService
from get_transaction_data import getBigQueryData
from queries import CREATE, BIGQUERY, TEST_ADDRESS


log.basicConfig(level="INFO")


def main():
    log.info("begin")

    # option to change contract address, if not, defaults to test
    try:
        address = sys.argv[1]
    except IndexError:
        address = TEST_ADDRESS

    # initialize database, create new table in db if not exists
    db = Database("testdb.db")
    db.execute(CREATE)

    # write address into query
    query = BIGQUERY(address)
    # get contract's top interaction addresses from bigquery, returns {data} and [arr of addresses]
    queryData = getBigQueryData(query)
    interactedAddresses = queryData[1]
    log.info(f"Array of top 10 addresses {address} interacted with: {interactedAddresses}")

    # connect to node
    nodeDataService = W3NodeService("https://ethereum.publicnode.com")
    #data looks like {0: {'address': 0x123 'interactions': 123, 'ethBalance': 123, 'lastUpdatedAt': Time:Stamp}}
    dataset = nodeDataService.BuildDataset(queryData[0])

    # clear stale data from table
    db.dropOldData()
    log.info("old table cleared")
    # insert new data into table
    db.insertData(dataset)
    log.info("data successfully loaded")


if __name__ == "__main__":
    main()
