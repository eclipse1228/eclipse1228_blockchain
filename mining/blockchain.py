# genesis block (first maded)
import time 
from mining import db
from mining.models import Block
from utils.blockchain_utils import sorted_dict_by_key
class BlockChain: 
    def __init__(self) -> None:
        pass 

    def create_genesis_block(self,) -> bool:  # -> bool is return info
        block_exist = Block.query.all() # select * from 
        if block_exist: 
            print({
                'status':'Fail to create genesis Block',
                'errer':'Block(s) aleady exist'
            })
            return False
        
        genesis_block = Block(
            prev_hash = sorted_dict_by_key({}),
            nonce = 0,
            timestamp = time.time()
        )

        db.session.add(genesis_block) 
        db.session.commit()

        return True
    
    def create_block(self,nonce: int, prev_hash: str = None):
        # create new block chain
        try: 
            db.session.add(
                Block(
                prev_hash = prev_hash,
                nonce = nonce,
                timestamp = time.time()            
                )
            )
            db.session.commit()
        except Exception as e:
            print('Fail to block on db')
            print(f'Error: {e}')
            return False 
         
        
