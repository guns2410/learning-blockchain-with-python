from src.block import Block
import datetime as date


# Generates the first genesis block
def generate_genesis_block():
    return Block(0, date.datetime.now(), {
        'proof-of-work': 1,
        'transactions': list() # Empty transaction list as the genesis block
    }, 0)

# Initiate the blockchain and assign the previous_block to the genesis block
blockchain = [generate_genesis_block()]
previous_block = blockchain[0]


# Adds a new block with specific data to the blockchain
def add_block(data):
    # Get the last block in the chain
    last_block = blockchain[len(blockchain) - 1]
    index = last_block.index + 1
    timestamp = date.datetime.now()
    prev_hash = last_block.hash

    # Create a new block and append to the existing blockchain
    block_to_add = Block(index, timestamp, data, prev_hash)
    blockchain.append(block_to_add)

    # Return the newly created block
    return block_to_add


def generate_proof_of_work(last_proof):
    # Initial proof of work which is greater than the last proof of work
    incrementor = last_proof + 1

    # Keep incrementing the proof of work until it is divisible by
    # 9 and the last_proof of the block
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    # Return the newly created proof of work
    return incrementor 

