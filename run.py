from application import app
from application import socketio
app.app_context().push()
if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0", port=5000, use_reloader=True, debug=True)
    # app.run(host='0.0.0.0', port=5050, debug=True)