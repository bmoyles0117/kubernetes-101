from flask import Flask, flash, redirect, render_template, request
from flask.ext.session import Session
import redis
import requests

redis_client = redis.Redis(host="redis")

app = Flask(__name__)
SESSION_TYPE = "redis"
SESSION_REDIS = redis_client
app.config.from_object(__name__)
Session(app)


@app.route("/")
def index():
  messages_response = requests.get("http://message-api/messages").json()

  return render_template("index.html", messages_response=messages_response)

@app.route("/send-message", methods=["POST"])
def send_message():
  requests.post("http://message-api/messages", data={
    "name": request.form.get("name"),
    "message": request.form.get("message")
  })

  greeting_response = requests.get("http://greeting-api/greeting", params={
    "name": request.form.get("name")
  }).json()

  flash("%s Your message has been created! Sincerely, %s" % (
    greeting_response["greeting"], 
    greeting_response["server"],
  ))

  return redirect("/")

@app.route("/healthz")
def healthz():
  # Will throw an exception when unavailable.
  redis_client.ping()

  return "OK"
