from app import app, socketio

# "Python3 run.py to run local server"
if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
