class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_votes = []

    def new_block(self):
        #creates a new block and adds it to the chain
    
    def new_vote(self, voter, vote):
        #creates a new vote and adds it to the current_votes
        self.current_votes.append(
            'voter' : voter,
            'vote' : vote
        )
    @staticmethod
    def hash():
        #hashes a block
    
    @property
    def last_block(self):
        #returns last block in the chain
        return self.chain[len(self.chain) -1]