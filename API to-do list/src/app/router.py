from flask import Blueprint, request, jsonify
from app.models import Tasks
from app import db

routers = Blueprint('routers', __name__)

@routers.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Tasks.query.all()
    return jsonify([task.title for task in tasks])

@routers.route('/tasks', methods=['POST'])
def set_tasks():
    data = request.get_json()
    
    title = data.get('title')
    status = data.get('status')
    
    if not title or not status:
        return jsonify({'message': 'title and status are required'}), 400
    
    tasks = Tasks(title=title, state=status)
    db.session.add(tasks)
    db.session.commit()
    
    return jsonify({'message': 'Tasks created sucessfully'}), 201

@routers.route('/tasks/<ID>', methods=['PUT'])
def get_tasks_id(ID):
    tasks = Tasks.query.get(ID)
    return tasks.to_dict()
