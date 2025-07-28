from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    msg = request.form['message']
    messages.append(msg)
    return redirect('/')