from flask import Flask


## WSGI application
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask application!'

if __name__ == '__main__':
    app.run()