import os

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/FileUpload', methods=['POST'])
def gen_ttl():
    with open("rp.ttl", 'r') as fin:
        return fin.read()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=7001, debug=True)