from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import json
from flask import jsonify
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def root_page():
    return render_template('index.html')

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

@app.route('/cycling')
def cycling():
    return render_template('cycling.html')

@app.route('/api/v1/test1')
def api_v1_test1():
    h = {}
    h['key1'] = 'value1'
    h['key2'] = 'value2'
    response = app.response_class(
        response=json.dumps(h),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/test2')
def api_v1_test2():
    h = {}
    h['key3'] = 'value3'
    h['key4'] = 'value4'
    return jsonify(h)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
            
