# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello, World! Jenkins")
    return "Hello, World! Jenkins"

if __name__ == '__main__':
    app.run(debug=True)
