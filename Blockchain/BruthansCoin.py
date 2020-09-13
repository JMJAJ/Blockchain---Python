import hashlib
import json
import time
from datetime import datetime

j = 75
a = 0
i = 0
k = 1

seconds = time.time()
local_time = time.ctime(seconds)

admin = "Jxint"
print("User: " + admin)
print("\n")

class Transaction():
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount

class Block():
    def __init__(self, tstamp,  transactionsList, prevhash=''): #nonce
        self.nonce = 0
        self.tstamp = tstamp # local_time
        self.transactionsList = transactionsList
        self.prevhash = prevhash
        self.hash = self.calcHash()
    def calcHash(self):
        block_string = json.dumps({"nonce":self.nonce, "tstamp":str(self.tstamp), "transaction":self.transactionsList[0].amount, "prevhash":self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def mineBlock(self, diffic):
        while(self.hash[:diffic] != str('').zfill(diffic)):
            self.nonce += 1
            self.hash = self.calcHash()
        print("Block mined:", self.hash)
    def __str__(self):
        string = "nonce: " + str(self.nonce) + "\n"
        string += "tstamp: " + str(local_time) + "\n"
        string += "transaction: " + str(self.transactionsList) + "\n"
        string += "prevhash: " + str(self.prevhash) + "\n"
        string += "hash: " + str(self.hash) + "\n"

        return string

class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(), ]
        self.pendingTransactions = []
        self.mining_reward = 100
        self.difficulty = 4
    def generateGenesisBlock(self):
        return Block('19/08/2003', [Transaction(None, None, 0),])
    def getLastBlock(self):
        return self.chain[-1]
#    def addBlock(self, newBlock):
#        newBlock.prevhash = self.getLastBlock().hash
#        newBlock.mineBlock(self.difficulty)
#        self.chain.append(newBlock)
    def minePendingTransatin(self, mining_reward_address):
        block = Block(datetime.now(), self.pendingTransactions)
        block.mineBlock(self.difficulty)
        print("Block mined, reward:", self.mining_reward)
        self.chain.append(block)
        self.pendingTransactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def createTransaction(self, T):
        self.pendingTransactions.append(T)
    def getBalance(self, address):
        balance = 0
        for b in self.chain:
            for t in b.transactionsList:
                if t.to_address == address:
                    balance += t.amount
                if t.from_address == address:
                    balance += t.amount
        return balance

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            prevb = self.chain[i-1]
            currb = self.chain[i]
            if(currb.hash != currb.calcHash()):
                print("Invalid block")
                return False
            if(currb.prevhash != prevb.hash):
                print("Invalid chain")
                return False
        return True


brutCoin = BlockChain()
brutCoin.createTransaction(Transaction('address1', 'address2', 100))
brutCoin.createTransaction(Transaction('address2', 'address1', 50))
print("Starting mining...")
brutCoin.minePendingTransatin("brutaddress")
print("BrutCoin miner balance is ", brutCoin.getBalance("brutaddress"))

print("\n")

for a in range(5):   
    k+=1
    i+=1
    j+=25
    print("Adding the " + str(k) + ". block: \n")
    #brutCoin.addBlock(Block(i, local_time, j))
    brutCoin.createTransaction(Transaction('address1', 'address2', 200))
    brutCoin.createTransaction(Transaction('address2', 'address1', 150))
    print("Starting mining again...")
    brutCoin.minePendingTransatin("brutaddress")
    print("BrutCoin miner balance is:", brutCoin.getBalance("brutaddress"))
    print("\n")


# print("Adding the first block: ")
# brutCoin.addBlock(Block(1, local_time, 100))
# print("Adding the second block: ")
# brutCoin.addBlock(Block(2, local_time, 50))

# brutCoin.chain[1].transaction = 333                           Invalid block - I want to make a mistake
# brutCoin.chain[1].hash = brutCoin.chain[1].calcHash()         Invalid chain - I want to make a mistake

# for b in brutCoin.chain: 
#     print(b)
# print(brutCoin.isChainValid())

# bblock = Block(1, '11/09/2020', 100)
# bblock.printHashes()

