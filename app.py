from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_message():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (text TEXT)")
    cursor.execute("INSERT INTO messages VALUES ('Deployed ~ via Jenkins CI/CD 🚀')")
    conn.commit()
    cursor.execute("SELECT text FROM messages")
    msg = cursor.fetchone()[0]
    conn.close()
    return msg

@app.route("/")
def home():
    message = get_message()
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
