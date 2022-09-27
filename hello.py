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

@app.errorhandler(404)
def four_oh_four(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def uh_oh(e):
    return render_template('500.html'), 500