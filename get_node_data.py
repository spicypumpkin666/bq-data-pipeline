from web3 import Web3
import logging as log
import datetime

log.basicConfig(level="INFO")


# class to handle all node interactions
class W3NodeService:

    def __init__(self, RPCNode):
        self.RPCNode = RPCNode
        self.W3 = self.setW3Node(self.RPCNode)

    # set node
    def setW3Node(self, RPCNode):
        w3 = Web3(Web3.HTTPProvider(RPCNode))
        log.info(f"web3 connected: {w3.isConnected()}")
        return w3

    # get data from node using address
    def getNodeData(self, address):
        addy = self.W3.toChecksumAddress(address)
        balance = self.W3.eth.getBalance(addy)
        eth = self.W3.fromWei(balance, "ether")
        log.info(f"{address} current balance: {eth}")
        return eth

    # add node data into dataset and add in timestamp
    def BuildDataset(self, queryData):
        log.info("starting build dataset")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for index in queryData:
            values = queryData[index]
            values.update({'ethBalance': float(self.getNodeData(values['address'])), "lastUpdatedAt": now})
        log.info(f"query data updated: {queryData}")

        return queryData
