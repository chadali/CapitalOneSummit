from app import app, db, socketio
from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from flask_socketio import emit, join_room, leave_room, disconnect
from .tasks import test, plotGraph, findAveragePrice, findHighestRating

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    pass

@socketio.on('connected')
def connected(data):
    emit('message', {'message': 'Connected %s to websocket' % (request.sid)})

@socketio.on('processGraph')
def processGraph(data):
    emit('message', {'message': 'Sending task to celery for graph %s' % data['graphNumber']})
    # Send task to celery with column, graph#, and unique user id as arguments
    plotGraph.apply_async(args=[data['column'], data['graphNumber'], request.sid])

@socketio.on('averagePrice')
def averagePrice(data):
    emit('message', {'message': 'Sending task to celery for average price'})
    findAveragePrice.apply_async(args=[request.sid])

@socketio.on('highestRating')
def highestRating(data):
    emit('message', {'message': 'Sending task to celery for highest rating'})
    findHighestRating.apply_async(args=[request.sid])

