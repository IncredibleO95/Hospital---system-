from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Karibu kwenye mfumo wa hospitali!"

if __name__ == '__main__':
    app.run(debug=True)
def init_user_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    ''')
    conn.commit()
    conn.close()
init_user_db()
from flask import session

app.secret_key = 'hospital_secret_key'  # Muhimu kwa session

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = user[1]
            session['role'] = user[3]
            return f"Karibu {user[3]} {user[1]}!"
        else:
            return "Jina la mtumiaji au nenosiri si sahihi"
    return render_template('login.html')
