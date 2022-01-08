import settings
from flask import Flask, render_template
from flask_socketio import SocketIO


SERVICE_URL = settings.SERVICE_URL if settings.SERVICE_URL else '/'

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY
socket_io = SocketIO(app)


@app.route(f'{SERVICE_URL}/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socket_io.run(app, host="0.0.0.0", port=settings.PORT)
