import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello Medium!!'

@app.route('/new-route')
def new_route():
    return 'This is a new route'

if __name__ == '__main__':
    app.run()