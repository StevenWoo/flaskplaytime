from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<h1 style='color:blue'>Welcome to swoo.club!</h1>"

@app.route("/test")
def moretest():
    return "<h2>test more</h2>"

@app.route("/cssgrid1")
def cssgrid1test():
    return render_template('cssgrid1.html')

@app.route("/cssgrid2")
def cssgrid2test():
    return render_template('cssgrid2.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/hello/')
@app.route('/hello/<input_name>')
def hello(input_name=None):
    return render_template('hello.html', name=input_name)

@app.route('/resume/')
def resume():
    return render_template('resume.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
            
