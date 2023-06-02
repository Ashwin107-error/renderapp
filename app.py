from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "message": "Hello World."
    })

# Starting the Server
if __name__ == '__main__':
    app.run(host="localhost",port=5009)