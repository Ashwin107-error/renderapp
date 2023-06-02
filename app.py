from flask import Flask,jsonify

app = Flask(__name__)

def hello_world():
    return jsonify({
        "message": "Hello World."
    })

# Starting the Server
if __name__ == '__main__':
    app.run()