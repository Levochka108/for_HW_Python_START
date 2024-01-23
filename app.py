"""
Задание

Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
"""
from flask import Flask, render_template, request, redirect, url_for
import os
import requests
from io import BytesIO
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def download_image(url, output_folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_name = os.path.join(output_folder, os.path.basename(url))
            with open(image_name, 'wb') as file:
                file.write(response.content)
                return image_name
    except Exception as e:
        return f"Error downloading {url}: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    urls = request.form.getlist('url')
    if not urls:
        return redirect(url_for('index'))

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    downloaded_images = []
    for url in urls:
        image_path = download_image(url, app.config['UPLOAD_FOLDER'])
        if image_path:
            downloaded_images.append(image_path)

    return render_template('result.html', images=downloaded_images)

if __name__ == '__main__':
    app.run(debug=True)
