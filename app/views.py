from app import app, db, socketio
from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from flask_socketio import emit, join_room, leave_room, disconnect
from .tasks import test

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    pass

@socketio.on('connected')
def connected(data):
    emit('message', {'message': 'Connected %s to websocket' % (request.sid)})