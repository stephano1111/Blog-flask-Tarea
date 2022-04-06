from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enter')
def enter_blog():
    return render_template('enter.html')

@app.route('/register')
def register_blog():
    return render_template('register.html')

@app.route('/sesion')
def sesion_blog():
    return render_template('sesion.html')