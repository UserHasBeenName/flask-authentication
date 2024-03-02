from flask import Flask
from secrets import token_urlsafe

from blueprints.routes import main_blueprint, auth_blueprint

app = Flask(__name__)
app.secret_key = token_urlsafe(20)
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
