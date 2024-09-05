from application import app, socketio
from flask import render_template, request, url_for, redirect,flash,get_flashed_messages, jsonify, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
import json

app.app_context().push()

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")  

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")  