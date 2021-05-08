from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world welcome to python flask app'
app.run(host='localhost', port=5000)
