# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello, World! Jenkins, Test")
    return "Hello, World! Jenkins"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
