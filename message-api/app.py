from flask import Flask, jsonify, request
from message_persisters import InMemoryMessagePersister, MysqlMessagePersister
import os
import socket
import uuid

app = Flask(__name__)

if os.environ.get("PERSISTENCE") == "mysql":
  message_persister = MysqlMessagePersister()
else:
  message_persister = InMemoryMessagePersister()

def get_messages():
  return messages

@app.route("/messages", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    return jsonify(message_persister.create_message({
      "uuid": str(uuid.uuid4()),
      "name": request.form.get("name"),
      "message": request.form.get("message")
    }))

  return jsonify({
    "server": socket.gethostname(),
    "persister": message_persister.__class__.__name__,
    "messages": message_persister.get_messages()
  })

@app.route("/healthz")
def healthz():
  if message_persister.is_available():
    return "OK"

  return "Message persister unavailable.", 500
