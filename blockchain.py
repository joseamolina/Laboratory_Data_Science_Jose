import json
import hashlib



class Block:
    __slots__ = ('data', 'hash', 'previous_hash', 'timestamp', 'pow')

    def __init__(self, data, hash_r, previous_hash, timestamp, pow_r, difficulty):
        self.data = data
        self.hash = ''
        self.previous_hash = previous_hash
        self.previous_block = None
        self.timestamp = timestamp
        self.pow = 0
        self._mine(difficulty)

    def _mine(self, difficulty):
        xhash = self.hash
        zeros_before = '0' * difficulty
        while not xhash.startswith(zeros_before):
            self.pow += 1
            xhash = self.get_json_str()

    def get_json_str(self):
        return "{ 'data': '{0}', " \
               "'previous_hash': '{1}', " \
               "'timestamp': {2}, " \
               "'pow': '{3}'}".format(self.data,
                                      self.previous_hash,
                                      self.timestamp,
                                      self.pow)


class Blockchain:

    def __init__(self, difficulty):
        self.chain = None
        self.difficulty = difficulty



    def calculate_hash(self, block):
        return hashlib.sha256(block.get_json_str())
