from flask import Flask, g, send_from_directory
from secrets import token_urlsafe

from blueprints.routes import main_blueprint, auth_blueprint
from database.database import open_db

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")

# Build the schema if it does not already exist
def build_schema():
    with open("database/schema.sql", "r") as file, app.app_context():
        open_db().cursor().executescript(file.read())

build_schema()

# Tell the application to close the database after context is popped
@app.teardown_appcontext
def close_db(*kwargs) -> None:
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
