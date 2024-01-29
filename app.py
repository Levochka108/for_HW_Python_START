"""
Задание

Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
"""
import os
import time
import requests
import threading
import multiprocessing
import asyncio

def download_image(url, output_folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_name = os.path.basename(url)
            image_path = os.path.join(output_folder, image_name)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {image_name}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def download_images_multithreaded(urls, output_folder):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url, output_folder))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Multithreaded download finished in {end_time - start_time} seconds")

def download_images_multiprocess(urls, output_folder):
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url, output_folder))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Multiprocess download finished in {end_time - start_time} seconds")

async def download_image_async(url, output_folder):
    try:
        response = await asyncio.to_thread(requests.get, url)
        if response.status_code == 200:
            image_name = os.path.basename(url)
            image_path = os.path.join(output_folder, image_name)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {image_name}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

async def download_images_async(urls, output_folder):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = download_image_async(url, output_folder)
        tasks.append(task)

    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Asynchronous download finished in {end_time - start_time} seconds")

if __name__ == "__main__":
    output_folder = "uploads"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("Starting downloads...")

    while True:
        url = input("Enter a URL to download (or 'exit' to quit): ")
        if url.lower() == 'exit':
            break
        download_image(url, output_folder)

    print("All downloads completed!")
