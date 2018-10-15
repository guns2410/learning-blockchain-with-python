# Blockchain Block
import hashlib as hasher

# A Block object to hold the block information
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    # Generate the hash using the block's data
    def hash_block(self):
        hash_string = (str(self.index) +
                       str(self.timestamp) +
                       str(self.data) +
                       str(self.previous_hash))
        # Generate Hash using the entire block's data
        return hasher.sha256(hash_string.encode('utf-8')).hexdigest()
