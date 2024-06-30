# Get All blockchain List
import collections
from mining.blockchain import BlockChain
from mining.models import Block, Transaction

def sorted_dict_by_key(unsorted_dic: dict):
    return collections.OrderedDict(
        sorted(unsorted_dic.items()), key=lambda keys: keys[0] # before hash, need to sorting 
    ) 

#  orderd by key uilts

# get blockChain info from database 
def get_blockchain(): 
    blockchain_exist = Block.query.all()
    if not blockchain_exist: 
        blockchain = BlockChain()
        blockchain.create_genesis_block()
    
    return build_blockchain_json()

def build_blockchain_json() -> dict:
    blocks= Block.query.filter(
        Block.timestamp
    ).order_by(Block.timestamp) # block timestamp 역순으로 호출 

    # 리턴할 dict 정의 
    result_dic = {
        'chain' : [], #
        'transaction_pool' : [],
    }

    for block in blocks: 
        result_dic['chain'].append(
            {
                'nonce':block.nonce,
                'prev_hash':block.prev.hash,
                'timestamp': block.timestamp,
                'transaction' : get_transcation_list(block)
            }
        )

# Get Block's transaction list 
def get_transcation_list(block:Block) -> list: 
    transaction_exist = Transaction.query.all()
    