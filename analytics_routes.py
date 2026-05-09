from flask import Blueprint, jsonify
from models.task import Task
from utils.analytics import task_analytics

analytics = Blueprint('analytics', __name__)

@analytics.route('/analytics')
def analytics_data():

    tasks = Task.query.all()

    task_data = []

    for t in tasks:
        task_data.append({
            'status': t.status
        })

    result = task_analytics(task_data)

    return jsonify(result)
