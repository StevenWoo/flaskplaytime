from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import json
from flask import jsonify
from flask import make_response
from flask import send_from_directory, request
from flask import Markup
import logging
import datetime
import time
import os
from weather_scrape import get_web_forecast
from weather_scrape import test_file
from weather_scrape import get_web_forecast_v2
app = Flask(__name__, static_folder='static')
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def root_page():
    return render_template('index.html')

@app.route("/personal")
def personal_page():
    return render_template('personal.html')

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder,'favicon.ico' )

@app.route('/reading_list')
def reading_list():
    return render_template('reading_list.html')

@app.route('/server_setup')
def server_setup():
    return render_template('server_setup.html')

@app.route("/cssgrid1")
def cssgrid1test():
    return render_template('cssgrid1.html')

@app.route("/cssgrid2")
def cssgrid2test():
    return render_template('cssgrid2.html')

@app.route("/js1test")
def js1test():
    return render_template('js1test.html')

@app.route('/hello/')
@app.route('/hello/<input_name>')
def hello(input_name=None):
    return render_template('hello.html', name=input_name)

def read_resume():
    with open('resume.txt', 'r') as file_object:
        text = file_object.read()
        return text

@app.route('/resume/')
def resume():
    file_text = read_resume()
    file_text = Markup(file_text.replace("\n", "<br />"))
    r = make_response(render_template('resume.html', text=file_text ))
    r.headers.set('Content-Security-Policy', "default-src 'self'; connect-src 'self'; report-uri 'https://swoo.club/api/v1/csp_report'")
    return r

url = 'forecast.weather.gov/MapClick.php?lat=37.3775&lon=-122.1144&lg=english&&FcstType=text'

@app.route('/bayareacycling')
def cycling():
    # todo parameterize latitude longitude
    # retrieve latitude longitude from browser
    text = get_web_forecast_v2(url)
    try:
        mtime = os.path.getmtime('templates/bayareacycling.html')        
    except OSError:
        mtime = 0
    last_modified_date = time.ctime(mtime)
    return render_template('bayareacycling.html', weather = text, forecast_url = 'https://' + url, updated = last_modified_date)

@app.route('/testscrape')
def test_scrape():
    text = test_file()
    return render_template('test_scrape.html', weather = text, forecast_url = url)


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
            
