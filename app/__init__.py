from flask import Flask
from flask_mail import Mail
import os
from dotenv import load_dotenv

# Add print statement to debug
print("Loading environment variables...")
load_dotenv()
print(f"Secret key loaded: {os.getenv('SECRET_KEY')}")

mail = Mail()

def create_app():
    app = Flask(__name__, 
                template_folder=os.path.abspath('templates'),
                static_folder=os.path.abspath('app/static'))
    
    app.secret_key = os.getenv('SECRET_KEY')
    
    # Mail settings
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
    
    mail.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app 