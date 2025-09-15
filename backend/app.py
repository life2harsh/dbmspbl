from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='../frontend', static_url_path='/')
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    Migrate(app, db)
    from routes.comments import comments_bp
    from routes.likes import likes_bp
    app.register_blueprint(posts_bp, url_prefix='/api')
    app.register_blueprint(comments_bp, url_prefix='/api')
    app.register_blueprint(likes_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app

if __name__ == "__main__":
    app = create_app()yyy