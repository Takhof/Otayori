from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# データベースモデル定義
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)

# 初期化
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    msg_text = request.form['message']
    if msg_text.strip():
        msg = Message(content=msg_text)
        db.session.add(msg)
        db.session.commit()
    return redirect('/')