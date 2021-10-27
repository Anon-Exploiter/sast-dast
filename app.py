import os
import base64, pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello, World!'


# RCE
@app.route("/cmd", methods=["GET"])
def rce():
    if request.args.get('c'):
        return os.popen(request.args.get('c')).read(), 200

    return ':P', 400


# Unsafe pickle deserialization
@app.route("/cmd", methods=["POST"])
def unsafe_pickle():
    data = base64.urlsafe_b64decode(request.form['cmd'])
    pickle.loads(data)
    return '', 204
