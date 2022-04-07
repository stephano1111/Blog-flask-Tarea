from flask import Flask, render_template #Servidor
from flask_sqlalchemy import SQLAlchemy #BD
from flask_marshmallow import Marshmallow #BD
from datetime import datetime

app = Flask(__name__)#Servidor

#BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
mm = Marshmallow(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(1000))
    created = db.Column(db.DateTime())

    def __init__(self, title, content, created):
        self.title = title
        self.content = content
        self.created = created
    
    def __repr__(self):
        return f'<Post {self.title}>'

db.create_all()#Crear la base de datos

class PostSchema(mm.Schema):
    class Meta:
        fields = ['id', 'title', 'content', 'created']

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

posts = Post.query.all()
print(posts)

"""Crear un post: 
my_post = Post(title='Corregir la fecha', content='Vamos a crear un nuevo post desde python para saber como se ve fecha y hora', created=datetime.now)
db.session.add(my_post)
db.session.commit()
"""

#Servidor
@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/enter')
def enter_blog():
    return render_template('enter.html')

@app.route('/register')
def register_blog():
    return render_template('register-sesion/register.html')

@app.route('/sesion')
def sesion_blog():
    return render_template('register-sesion/sesion.html')