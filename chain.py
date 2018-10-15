from block import Block
import datetime as date

def generate_genesis_block():
    return Block(0, date.datetime.now(), {
        'proof-of-work': 1,
        'transactions': list()
    }, 0)


blockchain = [generate_genesis_block()]
previous_block = blockchain[0]


def add_block(data):
    last_block = blockchain[len(blockchain) - 1]
    index = last_block.index + 1
    timestamp = date.datetime.now()
    prev_hash = last_block.hash
    block_to_add = Block(index, timestamp, data, prev_hash)
    blockchain.append(block_to_add)
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

