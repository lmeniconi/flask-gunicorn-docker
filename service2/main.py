from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Service 2!</p>"

if __name__ == "__main__":
    from os import getenv
    app.run(debug=getenv('DEBUG', False), host='0.0.0.0', port=3000)