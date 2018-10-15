import hashlib as hasher
import datetime as date
from src.block import Block 
from src.chain import blockchain, add_block, previous_block 

# How many blocks do we need for this chain
# after the genesis block

num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = add_block(previous_block)
    previous_block = block_to_add

    # Print to console the newly created block
    print ("Block #{} has been added to blockchain!".format(block_to_add.index))
    print ("Hash: {}\n".format(block_to_add.hash))
