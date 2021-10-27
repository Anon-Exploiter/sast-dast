import pickle
import base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello, World!'


@app.route("/cmd", methods=["POST"])
def unsafe_pickle():
    data = base64.urlsafe_b64decode(request.form['cmd'])
    pickle.loads(data)
    return '', 204