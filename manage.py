import os
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True,index=True)
    password = db.Column(db.VARCHAR(200))
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    article = db.Column(db.Text)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(debug=True)
