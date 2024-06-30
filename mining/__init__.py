from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from mining import config
migrate = Migrate()
db = SQLAlchemy()

# 실행시 이것부터 
def create_app(): 
    app = Flask(__name__)     # __name__ 은 mining임 (mining 을 초기화하기 때문에)

    app.config.from_object(config) # 설정 파일을 적용한다. 
    
    db.init_app(app) # db는 app에 있는걸 적용

    migrate.init_app(app, db, render_as_batch=True) # render_as_batch : SQLite는 필요없는 필드, (필수값) 있으면 드롭을 못 하는데, 필요한것만 복사해서 가져오기
    
    from . import models            
    from mining.views import main_views

    app.register_blueprint(main_views.bp)  
    return app 
