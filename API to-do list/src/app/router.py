from flask import Blueprint, request, jsonify
from app.models import Tasks
from app import db

routers = Blueprint('routers', __name__)

@routers.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Tasks.query.all()
    return jsonify([task.to_dict() for task in tasks])

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

@routers.route('/tasks/<ID>', methods=['GET'])
def get_tasks_id(ID):
    tasks = Tasks.query.get(ID)
    return tasks.to_dict()

@routers.route('/tasks/title', methods=['PUT'])
def update_title_task():
    data = request.get_json()
    
    tasks = Tasks.query.get(data.get('id'))
    if tasks:
        tasks.title = data.get('title')
        db.session.commit()
        return jsonify({'message': 'OK'})
    return jsonify({'message': 'Error'})

@routers.route('/tasks/state', methods=['PUT'])
def update_state_task():
    data = request.get_json()
    
    task = Tasks.query.get(data.get('id'))
    
    if task:
        task.state = data.get('state')
        db.session.commit()
        return jsonify({'message': 'OK'})
    return jsonify('message', 'Error')

@routers.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Tasks.query.get(id)
    
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'OK'})
    return jsonify({'message': 'Error'})
