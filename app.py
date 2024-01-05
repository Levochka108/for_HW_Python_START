"""
Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан 
cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, 
где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл 
с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените 'your_secret_key' на случайную строку

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        user_name = request.form['user_name']

        # Создаем cookie с данными пользователя
        response = make_response(render_template('welcome.html', user_name=user_name))
        response.set_cookie('user_name', user_name)

        return response

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Удаляем cookie с данными пользователя
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user_name')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
