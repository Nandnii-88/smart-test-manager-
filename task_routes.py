from flask import Blueprint, request, jsonify
from models.task import Task
from app import db, socketio

tasks = Blueprint('tasks', __name__)

@tasks.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = Task.query.all()

    output = []

    for t in task_list:
        output.append({
            'id': t.id,
            'title': t.title,
            'description': t.description,
            'priority': t.priority,
            'status': t.status
        })

    return jsonify(output)

@tasks.route('/tasks', methods=['POST'])
def add_task():
    data = request.json

    task = Task(
        title=data['title'],
        description=data['description'],
        priority=data['priority'],
        status=data['status']
    )

    db.session.add(task)
    db.session.commit()

    socketio.emit('task_update', {'message': 'New Task Added'})

    return jsonify({'message': 'Task Added'})

@tasks.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    data = request.json

    task.title = data['title']
    task.description = data['description']
    task.priority = data['priority']
    task.status = data['status']

    db.session.commit()

    return jsonify({'message': 'Task Updated'})

@tasks.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task Deleted'})
