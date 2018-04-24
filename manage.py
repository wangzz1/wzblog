from flask import Flask,render_template
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    manager.run()
