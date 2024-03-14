from flask import render_template, Blueprint, request, make_response, flash
from blueprints.forms import SignupForm, LoginForm
from database.database import open_db
from werkzeug.security import generate_password_hash, check_password_hash

# TODO: Session Cookies! In Server!

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
@auth_blueprint.route("/login/submit", methods=["GET", "POST"])
def login_submit():
    form = LoginForm(request.form)

    db = open_db()
    cu = db.cursor()
    
        
    cu.execute("SELECT * FROM users WHERE username = $1", (form.username.data.lower(),)) 

    try:
        user = cu.fetchone()
        if user and check_password_hash(user[1], form.password.data):
            flash(f"Successfully logged in as {user[0]}")
            return render_template("index.html")
        else:
            flash("Your username or password is incorrect.")
            return render_template("login.html", form = LoginForm())
    except IndexError:
        flash("Your username or password is incorrect.")
        return render_template("login.html", form = LoginForm())

@auth_blueprint.route("/signup/submit", methods=["GET", "POST"])
def signup_submit():
    form = SignupForm(request.form)
    
    if form.validate_on_submit():
        db = open_db()
        cu = db.cursor()
        cu.execute("SELECT * FROM users WHERE username = $1", (form.username.data.lower(),))
        if not cu.fetchone():
            resp = make_response

            cu.execute("INSERT INTO users(username, password) VALUES($1, $2)", (form.username.data.lower(), generate_password_hash(form.password.data)))
            db.commit()
            flash("Successfully signed in!")
        else:
            flash("Somebody with this name already exists.")
            return render_template("signup.html", form=SignupForm())


    return render_template("index.html")