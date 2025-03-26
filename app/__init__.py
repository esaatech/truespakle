from flask import Flask
import os

def create_app():
    app = Flask(__name__, 
                template_folder=os.path.abspath('templates'),
                static_folder=os.path.abspath('app/static'))
    
    app.secret_key = 'your-secret-key-here'
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app 