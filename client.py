import requests

# Получение списка всех задач
response = requests.get('http://127.0.0.1:5000/tasks')
print(response.json())

# Получение задачи с определенным идентификатором (замените {id} на фактический идентификатор)
response = requests.get('http://127.0.0.1:5000/tasks/{id}')
print(response.json())

# Добавление новой задачи
data = {"title": "New Task", "description": "Task description"}
response = requests.post('http://127.0.0.1:5000/tasks', json=data)
print(response.json())

# Обновление задачи с определенным идентификатором (замените {id} на фактический идентификатор)
data = {"title": "Updated Task", "description": "Updated description", "status": True}
response = requests.put('http://127.0.0.1:5000/tasks/{id}', json=data)
print(response.json())

# Удаление задачи с определенным идентификатором (замените {id} на фактический идентификатор)
response = requests.delete('http://127.0.0.1:5000/tasks/{id}')
print(response.text)
