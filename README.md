# Todo List Web App

A simple single-page Todo List application built with Flask, HTML, CSS, JavaScript, and Bootstrap.

## Features

- Create new tasks with a text input and Create button
- View all tasks in a list
- Tasks stored persistently in a JSON file
- Each task includes:
  - Unique ID
  - Task text
  - Created timestamp
- Bootstrap styling for a clean, responsive interface

## Requirements

- Python 3.7+
- Flask

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter a task description in the input field
2. Click the "Create" button or press Enter
3. Your task will appear in the list below with a timestamp
4. Tasks are automatically saved to `tasks.json`

## File Structure

- `app.py` - Flask backend with API endpoints
- `templates/index.html` - Frontend HTML with Bootstrap and JavaScript
- `tasks.json` - JSON file storing all tasks (created automatically)
- `requirements.txt` - Python dependencies
