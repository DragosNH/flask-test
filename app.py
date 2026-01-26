from flask import Flask, render_template
import os

app = Flask(__name__)

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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)