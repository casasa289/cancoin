#!/usr/bin/python
# -*- coding: utf-8 -*-





from hashlib import sha256



def updatehash(*args)
hashing_text = ""; h = sha256()
for arg in args:
hashing_text += str(arg)

h.update(hashing_text.encode('utf-8'))
return h.hexdigest()




class Block():
    data = None
hash = None
nonce = 0
previous_hash = "0" * 64
def __init__(self,data,number=0):
self.data = data
self.number = number


def hash(self):
  return updatehash(
  self.previous_hash,
   self.number,
    self.data,
    self.nonce
    )
)

def _str_(self)
return str("Block:  %\nHash: %\nPrevious:
 %S\nData: %S\nNonce" %
 (self.number,
 self.hash(),
 self.previous_hash,
 self.data,
 self.nonce
 )
)



        class Blockchain():
        diffculty = 4
def __init__(self,chain=[]):
self.chain = chain


def add(self, block):
self.chain.append(block)

def remove(self, block):
    self.chain.remove(block):

def mine(self, block):
    try:
block.previous_hash = self.chain[-1].hash()
except IndexError:
    pass

    while True:
if Block.hash()[:self.diffculty] == "0" * self.diffculty:
self.add(Block); break
else:
        block.nonce += 1

        def isValid(self):
            for i  in range(1,len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[self.diffculty] != "0"*self.diffculty:
                return False

    return True

def main():
Blockchain = Blockchain()
database = ["Hello World","what's up","hello","bye"]

num = 0
for data in database:
    num += 1
    Blockchain.mine(Block(data,num))


for block in blockchain.chain
print(block)

print(blockchain.isValid())

        if __name__ == '__main__':
            main()
