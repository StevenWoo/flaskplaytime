from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Welcome to swoo.club!</h1>"

@app.route("/test")
def moretest():
    return "<h2>test more</h2>"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

if __name__ == "__main__":
  app.run(host='0.0.0.0')
            
