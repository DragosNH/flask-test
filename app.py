from flask import Flask, render_template, request, redirect, session
import os

FAKE_USERS = {
    "admin": "1234",
    "dragos": "password"
}

app = Flask(__name__)
app.secret_key = "dev-secret-key"

@app.route("/")
def index():
    user = session.get("user")
    return render_template('index.html', user=user)

@app.route("/my-page")
def my_page():
    return render_template('mypage.html')

@app.route("/my-fans")
def my_fans():
    return render_template('myfans.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print("DEBUG:", username, password)

        if username in FAKE_USERS and FAKE_USERS[username] == password:
            session["user"] = username
            return redirect("/")
        else:
            error = "Invalid username or password"

    return render_template('login.html')
    



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)