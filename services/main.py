from flask import Flask, render_template, request, flash, redirect, url_for

# import fucntion from app
import app as service

app = Flask(__name__)
app.secret_key = b'dsadasw2w'
app.debug = True # auto reload when change the file

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(username, password)
    res , err = service.login(username, password)
    if err != None:
        flash(f"{err}")
        return redirect(url_for('index'))
    elif len(res) > 0:
        flash("login berhasil")
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    # Logika untuk dashboard
    return render_template('dashboard.html')   
# redirect page
#def dashboard():
    #return render_template('dashboard.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form["name"]
    username = request.form["reg_username"]
    password = request.form["reg_password"]
    confirm_password = request.form["password-repeat"]

    if password != confirm_password:
        flash("Registration Failed: Passwords do not match")
        return redirect(url_for('register_page'))

    success, error = service.register(name, username, password)
    if error:
        flash(f"Registration Failed: {error}")
    else:
        flash("Registration successful")
    return redirect(url_for('register_page'))

@app.route("/register_page")
def register_page():
    return render_template("register.html")

@app.route("/profile")
def profile_page():
    return render_template("profile.html")