from flask import Flask, g
from secrets import token_urlsafe

from blueprints.routes import main_blueprint, auth_blueprint

app = Flask(__name__)

# Tell the application to close the database after context is popped
@app.teardown_appcontext
def close_db(*kwargs):
    # Find DB
    db = getattr(g, "_database", None)
    if db is not None:
        # Close DB if it is found
        db.close()

# Generate a random key for the cryptograph
app.secret_key = token_urlsafe(20)

# Establish paths created in /blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
