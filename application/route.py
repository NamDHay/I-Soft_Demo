from application import app, socketio
from flask_socketio import SocketIO, emit, disconnect
from flask import render_template, request, url_for, redirect,flash,get_flashed_messages, jsonify, copy_current_request_context
from application.FileData import FileData
from pathlib import Path
import json
import time

app.app_context().push()
file_data = FileData()
current_user = "admin"

@socketio.on('connect')
def handle_connect():
    global current_user
    directory_path = f"application/Json/{current_user}/data"
    files = file_data.list_files_in_directory(directory_path)
    for file_name in files:
        file_path = f"application/Json/{current_user}/data/{file_name}"
        data = file_data.read(file_path)
        string_data = {'filename': file_name, 'data': data}
        emit('File', string_data)

@socketio.on('writeFile')
def handle_write(String):
    global current_user
    filename = String.get('filename')
    file = f"application/Json/{current_user}/data/{filename}"
    data = String.get('data')
    file_data.write(file, data)

@socketio.on('loadFile')
def handle_load(String):
    global current_user
    filename = String.get('filename')
    file = f"application/Json/{current_user}/data/{filename}"
    data = file_data.read(file)
    String = {'filename': filename, 'data': data}
    print(String)
    emit('File', String)

@socketio.on('login')
def handle_login(String):
    global current_user
    current_user = String.get('usr')
    pwd = String.get('pwd')
    
    directory_path = f"application/Json/{current_user}"
    path = Path(directory_path)
    # sourcery skip: remove-redundant-path-exists
    if path.exists() and path.is_dir():
        pwd_dir = f"application/Json/{current_user}/setting/pwd"
        password = file_data.read(pwd_dir)
        if pwd == password:
            return dashboard()
        else:
            print("Wrong Password")
    else:
        print(f"{current_user}' does not exist")

@app.route("/")
def index():
    return redirect(url_for('dashboard'))

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")  

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():   
    return render_template("dashboard.html")