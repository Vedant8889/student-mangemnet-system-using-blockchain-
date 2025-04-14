import hashlib
import json
import os
from time import time

class Blockchain:
    def __init__(self, filename='blockchain.json'):
        self.filename = filename
        self.chain = self.load_chain()
        if not self.chain:
            self.chain = []
            self.create_block(student_data="Genesis Block")

    def create_block(self, student_data):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'student_data': student_data,
            'previous_hash': self.chain[-1]['hash'] if self.chain else '0',
        }
        block['hash'] = self.hash(block)
        self.chain.append(block)
        self.save_chain()
        return block

    def hash(self, block):
        block_copy = block.copy()
        block_copy.pop('hash', None)  # Exclude hash from hashing
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def save_chain(self):
        with open(self.filename, 'w') as file:
            json.dump(self.chain, file, indent=4)

    def load_chain(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return None

    def get_chain(self):
        return self.chain


# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Add sample student data
    blockchain.create_block(student_data={"name": "Alice", "roll_no": "001", "grade": "A"})
    blockchain.create_block(student_data={"name": "Bob", "roll_no": "002", "grade": "B"})
    
    # Print blockchain
    print(json.dumps(blockchain.get_chain(), indent=4))
