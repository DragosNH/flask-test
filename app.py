from flask import Flask, render_template, redirect, url_for, request
import os
from flask_login import LoginManager, login_required
from http import HTTPStatus

app = Flask(__name__)
login_manager = LoginManager()


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/my-page")
def my_page():
    return render_template('mypage.html')

@app.route("/my-fans")
def my_fans():
    return render_template('myfans.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

# ------ Login area ------

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/settings")
@login_required
def settings():
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)