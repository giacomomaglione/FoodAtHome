from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/aboutus")
def about():
    return render_template('aboutus.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signin")
def signin():
    return render_template('signin.html')


@app.route("/signinlocal")
def signinlocal():
    return render_template('signinlocal.html')


@app.route("/signinrider")
def signinrider():
    return render_template('signinrider.html')




if __name__ == "__main__":
    app.run()
