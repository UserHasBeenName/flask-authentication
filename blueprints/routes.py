from flask import render_template, Blueprint
from blueprints.forms import SignupForm, LoginForm

# Initialise the routes blueprint
main_blueprint = Blueprint("main_blueprint", __name__)
auth_blueprint = Blueprint("auth_blueprint", __name__)

# Main page
@main_blueprint.route("/")
def index():
    return render_template("index.html")

@main_blueprint.route("/profile")
def profile():
    return "Profile"

# Signup page
@auth_blueprint.route("/signup")
def signup():
    return render_template("signup.html", form=SignupForm())

# Login page
@auth_blueprint.route("/login")
def login():
    return render_template("login.html", form=LoginForm())

