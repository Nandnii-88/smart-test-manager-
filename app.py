from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()
socketio = SocketIO()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
socketio.init_app(app)

from routes.auth_routes import auth
from routes.task_routes import tasks
from routes.analytics_routes import analytics

app.register_blueprint(auth)
app.register_blueprint(tasks)
app.register_blueprint(analytics)

@app.route('/')
def home():
    return render_template('dashboard.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
