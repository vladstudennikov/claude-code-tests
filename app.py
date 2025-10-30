from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def get_next_id(tasks):
    """Get the next available task ID."""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks."""
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Task text is required'}), 400

    tasks = load_tasks()

    new_task = {
        'id': get_next_id(tasks),
        'text': data['text'],
        'created_at': datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True)
