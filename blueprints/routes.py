from flask import render_template, Blueprint, request, make_response
from blueprints.forms import SignupForm, LoginForm
from database.database import open_db
from werkzeug.security import generate_password_hash, check_password_hash


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

# Add submit for POST request
# @auth_blueprint.route("/login/submit", methods=["GET", "POST"])
# def login_submit():
#     form = LoginForm(request.form)
#     return render_template("index.html", form=form)

@auth_blueprint.route("/signup/submit", methods=["GET", "POST"])
def signup_submit():
    # print(request.form.get("username"))
    # print(request.form.get("password"))
    form = SignupForm(request.form)
    
    if form.validate_on_submit():
        db = open_db()
        cu = db.cursor()
        cu.execute("")
        cu.execute("SELECT * FROM users WHERE username = $1", (form.username.data.lower(),))
        if not cu.fetchone():
            resp = make_response

            cu.execute("INSERT INTO users(username, password) VALUES($1, $2)", (form.username.data.lower(), generate_password_hash(form.password.data)))
            db.commit()


    return render_template("index.html")