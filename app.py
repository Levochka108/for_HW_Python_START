"""
Задание

Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.


"""



from flask import Flask, request, jsonify
from models import TaskCreate, TaskUpdate, TaskResponse, ErrorResponse
from database import tasks_db, task_id_counter

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Task API!'

# GET /tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([TaskResponse(**task.dict()) for task in tasks_db])

# GET /tasks/{id}
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks_db if t.id == task_id), None)
    if task:
        return jsonify(TaskResponse(**task.dict()))
    return jsonify(ErrorResponse(detail=f"Task with id {task_id} not found")), 404

# POST /tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_create = TaskCreate(**data)
    task_id = task_id_counter
    task = TaskInDB(id=task_id, status=False, **task_create.dict())
    tasks_db.append(task)
    task_id_counter += 1
    return jsonify(TaskResponse(**task.dict())), 201

# PUT /tasks/{id}
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks_db if t.id == task_id), None)
    if task:
        data = request.json
        task_update = TaskUpdate(**data)
        task.title = task_update.title
        task.description = task_update.description
        task.status = task_update.status
        return jsonify(TaskResponse(**task.dict()))
    return jsonify(ErrorResponse(detail=f"Task with id {task_id} not found")), 404

# DELETE /tasks/{id}
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return jsonify({"message": f"Task with id {task_id} deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
