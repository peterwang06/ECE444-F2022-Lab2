from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def myuser(name):
    return render_template('user2.html',name=name)