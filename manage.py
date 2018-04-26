import os
from flask import Flask,render_template,request,redirect,session,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import InputRequired,DataRequired,Email

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wangzhe'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manage = Manager(app)

#登录表单
class MyForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(),Email()])
    password = PasswordField('password',validators=[InputRequired()])
    submit = SubmitField('Log in')

#数据库类
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



#路由
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    form = MyForm()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        if email in User.query.all():
            if User.password(password):
                return redirect("https://www.baidu.com")

    return render_template('login.html', form=form)




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    manage.run()
