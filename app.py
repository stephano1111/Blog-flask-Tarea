from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enter')
def enter_blog():
    return render_template('enter.html')