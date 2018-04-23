from flask import Flask,render_template
#from flask_script import Manager #脚本和系统分离，插入外部脚本
#from flask_moment import Moment #时间日期扩展
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#manager = Manager(app)
#moment = Moment(app)
#db = SQLAlchemy(app)

'''class User():
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.Integer)
'''
@app.route('/')
def index():
    return render_template('base.html')



if __name__ == '__main__':
    app.run(debug=True)
