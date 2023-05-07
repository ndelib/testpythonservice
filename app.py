from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Howdy, this is a test Python service!'