from flask import Flask, jsonify, request
import os
import socket

app = Flask(__name__)


@app.route("/greeting")
def greeting():
  return jsonify({
    "server": socket.gethostname(),
    "greeting": os.environ.get("GREETING_FORMAT", "Hello %s.") % request.args.get("name")
  })

@app.route("/healthz")
def healthz():
  return "OK"