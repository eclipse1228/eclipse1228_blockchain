# flask's setting 
import base64
import os
import requests

from mining.secret import csrf_token_secret
# config's path 
BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DB ORM
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format( os.path.join(BASE_DIR, 'blockchain.db'))

# /// 면 내 컴퓨터 밑에, // 네트워크 # 참조를 위한 blockchain.db 의 위치를 알려준다. 

# ORM 객체의 변경사항을 지속적으로 추적하고 변동 이벤트에 대한 메시지 출력
# 불필요한 경우 False로 꺼 놓는 것을 추천
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Seret key for CSRF token
SECRET_KEY = csrf_token_secret

# 채굴 성공 -> 채굴 보상금 
BLOCKCHAIN_NETWORK = 'BLOCK CHAIN NETWORK'

# NOUNCE DIFFicult
MINING_DIFFICULTY = 5

# Mining Reword
MINING_REWORD = 15.0

