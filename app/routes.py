from app import app
from flask import render_template, request, redirect, url_for
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/upload_rex')
def upload_rex():
    return render_template('upload_rex.html')
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
