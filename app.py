from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, threaded=True)
# my ip addr 124.53.242.101

@app.route("/mainurl", methods=['POST'])
def mainurl():

    today = datetime.today()

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": today."
                    }
                }
            ]
        }
    }

    return jsonify(res)