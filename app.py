from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import jwt
import datetime

app = Flask(__name__)
CORS(app)

SECRET_KEY = "secret123"

# DB INIT
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS leads
                    (id INTEGER PRIMARY KEY, name TEXT, email TEXT, message TEXT)''')
    conn.close()

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data['username'] == "admin" and data['password'] == "admin":
        token = jwt.encode({
            'user': data['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({'token': token})
    return jsonify({'error': 'Invalid login'})

# CONTACT
@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO leads (name,email,message) VALUES (?,?,?)",
                 (data['name'], data['email'], data['message']))
    conn.commit()
    conn.close()
    return jsonify({"status": "saved"})

# GET LEADS (Protected)
@app.route('/leads', methods=['GET'])
def leads():
    token = request.headers.get('Authorization')

    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except:
        return jsonify({'error': 'Unauthorized'})

    conn = sqlite3.connect('database.db')
    data = conn.execute("SELECT * FROM leads").fetchall()
    conn.close()

    return jsonify(data)

# AI CHAT (Basic)
@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json['message']

    if "marketing" in msg.lower():
        reply = "Use SEO + Paid Ads for growth."
    else:
        reply = "AI suggests improving user engagement."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
