from flask import Flask, request
from src.chain import blockchain, add_block, generate_proof_of_work
import json


# Calculates the next proof-of-work number
# The next proof should be divisible by both 9 and the last proof value
def proff_of_work(last_proof):
    # find the next proof of work
    incrementor = last_proof + 1

    # keep incrementing until it is divisible by 9
    # and the proof of work previously generated
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    # return the generated proof of work
    return incrementor


# Initiate Flask
node = Flask(__name__)

# Hold the transactions for computation
node_transactions = []

# Creates a new transaction of transferring tokens from
# one user to the another


@node.route('/txion', methods=['POST'])
def transaction():
    if request.method == 'POST':
        # Extract Transaction data from post
        new_txion = request.get_json()
        # Add node to list
        node_transactions.append(new_txion)
        # Once the transaction is successful
        # log to console
        print('New Transaction!')
        print('From : {}'.format(new_txion['from']))
        print('To: {}'.format(new_txion['to']))
        print('Amount: {}', format(new_txion['amount']))

        return 'Transaction submitted successfully!\n'


# A sample miner's wallet address
miner_address = 'abcd'

# A get request URL to mine tokens


@node.route('/mine', methods=['GET'])
def mine():
    # Get the latest block in the chain and get it's proof-of-work value
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']

    # Calculate the current proof of work
    proof = generate_proof_of_work(last_proof)

    # add to the transaction history
    node_transactions.append({
        'from': 'network',
        'to': miner_address,
        'amount': 1
    })

    # Create the block data to create a block in the chain
    new_block_data = {
        'proof-of-work': proof,
        'transactions': list(node_transactions)
    }

    # Empty the transaction list once the transaction is mined
    node_transactions[:] = []

    # Add the block to the chain
    new_block = add_block(new_block_data)

    # Return the newly created block
    return json.dumps({
        'index': new_block.index,
        'timestamp': str(new_block.timestamp),
        'data': new_block.data,
        'hash': new_block.hash
    })


# View all the blocks that exist in the chain
@node.route('/blocks', methods=['GET'])
def blocks():
    # An initial variable to hold the chain data converted to dictionary
    chain_to_send = []

    # Convert blocks to dictionaries so that we can send them as json objects
    for block in blockchain:
        chain_to_send.append({
            'index': str(block.index),
            'timestamp': str(block.timestamp),
            'data': str(block.data),
            'previous_hash': block.previous_hash,
            'hash': str(block.hash)
        })

    # convert the dictionay to json object and return the output
    return json.dumps(chain_to_send)


# Run the server, defaults to port 5000
node.run()
