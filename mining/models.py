from mining import db # 

class Block(db.Model): # db.model 을 상속 받는다. 
    id = db.Column(db.Integer, primary_key=True)
    prev_hash = db.Column(db.String(300), nullable=True)
    nonce = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.Float, nullable=True)

class Transaction(db.Model):
    '''거래정보: 하나의 블록에 담겨져 있는 거래 정보'''
    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.Integer, db.ForeignKey('block.id'))
    send_addr = db.Column(db.String(300))
    recv_addr = db.Column(db.String(300))
    amount = db.Column(db.Float())
    blockchain = db.relationship(
    'Block',
    backref=db.backref('transactions')
    )
    # db.relationship은.. block의 transaction 다 가져오기
    # backref 는 여기에 속하는거 다 준다! 라는 의미이다. 