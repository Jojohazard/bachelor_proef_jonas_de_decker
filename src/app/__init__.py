from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import web_bp
    app.register_blueprint(web_bp)

    return app