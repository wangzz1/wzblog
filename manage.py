from flask import Flask,render_template
from flask_bootstrap import Bootstrap #提供bootstrap base模板
from flask_script import Manager #脚本和系统分离，插入外部脚本
from flask_moment import Moment #时间日期扩展
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
