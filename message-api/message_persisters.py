import MySQLdb
import os

class InMemoryMessagePersister(object):
  def __init__(self):
    self.messages = []

  def create_message(self, message):
    self.messages.append(message)
    return message

  def get_messages(self):
    return self.messages[::-1]

  def is_available(self):
    return True

class MysqlMessagePersister(object):
  def __init__(self):
    self.db = MySQLdb.connect(
      host="mysql",
      user=os.environ.get("MYSQL_USERNAME", "root"),
      passwd=os.environ.get("MYSQL_PASSWORD", ""),
      db="messages"
    )

  def create_message(self, message):
    with self.db as cursor:
      cursor.execute("INSERT INTO messages(`uuid`, `name`, `message`) VALUES(%s, %s, %s)", (
        message["uuid"],
        message["name"],
        message["message"]
      ))

    return message

  def get_messages(self):
    messages = []
    with self.db as cursor:
      cursor.execute("SELECT `uuid`, `name`, `message` FROM messages ORDER BY id DESC")
      for uuid, name, message in cursor.fetchall():
        messages.append({
          "uuid": uuid,
          "name": name,
          "message": message,
        })

    return messages

  def is_available(self):
    try:
      self.db.ping()
      return True
    except MySQLdb.OperationalError:
      return False