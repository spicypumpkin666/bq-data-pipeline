import logging as log

from google.cloud import bigquery

log.basicConfig(level="INFO")


def getBigQueryData(query):
    # use service account json to access bigquery
    client = bigquery.Client()
    log.info("connected to bigquery")

    # run sql query
    queryJob = client.query(query)
    log.info(f"query ran: {queryJob}")

    queryData = {}
    returnAddresses = []

    # load data from query into dict, create addresses array
    for index, row in enumerate(queryJob):
        queryData.update({index: {"address": row[0], "interactions": row[1]}})
        returnAddresses.append(row[0])

    return queryData, returnAddresses
