from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def home():
    return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>')
def myuser(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def four_oh_four(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def uh_oh(e):
    return render_template('500.html'), 500