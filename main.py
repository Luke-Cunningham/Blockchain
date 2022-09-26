"""
Blockchain
    Luke Cunningham
    5/16/2022

    Program acts as a basic blockchain.
"""


class Block:

    def __init__(self, data, prev_hash=0):
        self._data = data
        self._next = None
        self._hash = hash(data) + prev_hash

    def add_block(self, data):
        current = self
        while current._next is not None:
            current = current._next

        print("Transaction added. New hash is " + str(current._hash))
        current._next = Block(data, current._hash)

    def replay(self, prev_hash=0):
        print("Replaying Blockchain")
        current = self
        while current is not None:
            if current._hash == hash(current._data) + prev_hash:
                print(current._data)
                prev_hash = current._hash
                current = current._next
            else:
                print("Blockchain is Corrupted!!")
                exit()

        print("Blockchain Verified. End of Transactions.")
        print("Final hash is " + str(prev_hash))


if __name__ == '__main__':
    new_chain = Block("Starting Balance Eric = $1000")
    new_chain.add_block("Eric Pays Kimia $10 for providing a great idea")
    new_chain.add_block("Eric Pays the cat $50 for ending the noise")
    new_chain.add_block("The cat pays Pet Food Express $20 for catnip")
    print()
    new_chain.replay()
    print()

    # Cat tried to hack the chain
    fraud = "Eric Pays the cat $500 for ending the noise"
    new_chain._next._next._data = fraud
    new_chain.replay()
