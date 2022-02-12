"""
    Пока не получилось за Traefik reverse proxy настроить общение по websocket, поэтому работает с long-polling.
"""

import settings
import os
import random
import datetime as dt
from math import pi, sin
from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet


# eventlet.monkey_patch()       # this for multiple nodes? see flask_socketio docs -> deployment
SERVICE_URL = settings.SERVICE_URL if settings.SERVICE_URL else '/'
app = Flask(__name__, static_url_path=SERVICE_URL + '/static')
app.config['SECRET_KEY'] = settings.SECRET_KEY
socket = SocketIO(app, path=f'{SERVICE_URL}/socket.io')
# socket = SocketIO(app, path=f'{SERVICE_URL}/socket.io', transports=['websocket', 'polling'])

# socket = SocketIO(app, message_queue='redis://')      # это на будущее для нескольких socketIO на одном хосте


@app.route(f'{SERVICE_URL}')
def index():
    files = [f for f in os.listdir('static/resources/')]
    filename = 'resources/' + random.choice(files)
    return render_template('index.html', filename=filename, srvURL=SERVICE_URL)


@socket.on(f'calculate')
def calculate(data: dict):
    latitude = data.get('latitude', 0)      # in degrees!
    birthday = data.get('birthday', None)
    if not latitude or not birthday:
        return 0
    # calculation of travel time in seconds
    travel_time = dt.datetime.now() - dt.datetime.fromisoformat(birthday)

    # calculation of linear velocity at latitude
    latitude = pi / 2 - abs(latitude) / 180 * pi
    radius = settings.EARTH_RADIUS * sin(latitude)
    velocity = 2 * pi * radius / 86400     # km/sec

    mileage = travel_time.total_seconds() * (velocity + settings.EARTH_VELOCITY)
    return mileage


if __name__ == '__main__':
    socket.run(app, host="0.0.0.0", port=settings.PORT)
    # socket.run(app, host="0.0.0.0", port=settings.PORT, keyfile='key.pem', certfile='cert.pem')
