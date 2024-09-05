from application import app, socketio
from flask_socketio import SocketIO, emit, disconnect
from flask import render_template, request, url_for, redirect,flash,get_flashed_messages, jsonify, copy_current_request_context
import json

app.app_context().push()

class FileData:
    def read(self, file):
        with open(file, 'r') as openfile:
            json_object = json.load(openfile)
            json_object = json.dumps(json_object)
        return json_object
    
    def write(self, file, data):
        with open(file, "w") as outfile:
            json.dump(data, outfile, indent=4)  # Added indent for better readability
        print("Data written to file successfully.")

@socketio.on('connect')
def handle_connect():
    file_data = FileData()
    data = file_data.read("application/Json/data.json")
    print(data)
    emit('Data', data)

@app.route("/")
def index():
    return redirect(url_for('dashboard'))

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")  

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    file_data = FileData()
    data = file_data.read("application/Json/data.json")
    print(data)
    socketio.emit('Data', data)
    return render_template("dashboard.html")  