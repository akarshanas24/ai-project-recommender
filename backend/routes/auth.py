from flask import Blueprint, request, redirect, render_template, session, url_for
import sqlite3
from flask_bcrypt import Bcrypt
from flask import current_app as app

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth_bp.before_app_request
def init_bcrypt():
    bcrypt.init_app(app)

@auth_bp.route('/')
def home():
    return render_template('index.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
    except sqlite3.IntegrityError:
        return 'Username already exists'
    conn.close()
    return redirect(url_for('login_page'))

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()

    if user and bcrypt.check_password_hash(user[2], password):
        session['user_id'] = user[0]
        return redirect(url_for('chat.chat'))
    return 'Invalid username or password'

print("✅ auth.py loaded successfully!")
