from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['SECRET_KEY'] = "namdhayplayground"

socketio = SocketIO(app)
app.app_context().push()

from application import route