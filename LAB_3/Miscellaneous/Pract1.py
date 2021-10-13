# Basic Program of TensorFlow.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import flask


app = flask.Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


if __name__ == '__main__':
    app.run()
