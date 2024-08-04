#!/bin/bash
# Bash script run locoally server an Django application

# Проверяем, передан ли флаг -r или --runserver
if [[ "$1" == "-r" || "$1" == "--runserver" ]]; then
    # Переходим в директорию первого проекта
    # cd ~/PycharmProjects/SerphantomApplication/ || exit
    # Запускаем сервер с помощью poetry
    echo "Start locoally runserver Django..."
    poetry run python advertisements/manage.py runserver

# Проверяем, передан ли флаг -mig или --migrate
elif [[ "$1" == "-mig" || "$1" == "--migrate" ]]; then
    # Переходим в директорию второго проекта
    # cd ~/PycharmProjects/SerphantomApplication/ || exit
    # Запускаем сервер с помощью poetry
    echo "Migrating from models database..."
    poetry run python advertisements/manage.py migrate

# Проверяем, передан ли флаг -mak или --makemigrations
elif [[ "$1" == "-mak" || "$1" == "--makemigrations" ]]; then
    # Переходим в директорию второго проекта
    # cd ~/PycharmProjects/SerphantomApplication/ || exit
    # Запускаем сервер с помощью poetry
    echo "Makemigrations from models database..."
    poetry run python advertisements/manage.py makemigrations

# Проверяем, передан ли флаг -c или --collectstatic
elif [[ "$1" == "-c" || "$1" == "--collectstatic" ]]; then
    # Переходим в директорию второго проекта
    # cd ~/PycharmProjects/SerphantomApplication/ || exit
    # Запускаем сервер с помощью poetry
    echo "Collectstatic from staticfiles..."
    poetry run python advertisements/manage.py collectstatic

# Проверяем, передан ли флаг -a или --admin
elif [[ "$1" == "-a" || "$1" == "--admin" ]]; then
    # Переходим в директорию второго проекта
    # cd ~/PycharmProjects/SerphantomApplication/ || exit
    # Запускаем сервер с помощью poetry
    echo "Creating super user server on fraimework Django..."
    poetry run python advertisements/manage.py createsuperuser

# Если флаг не передан, выводим сообщение об ошибке
else
    # Если флаг не передан или не распознан, выводим сообщение об ошибке
    # shellcheck disable=SC2028
    # $0 -> ./run.sh
    echo "    Команды для работы с фреймворком Django и Poetry.
    Использование: $0
    [ -r | --runserver ]         ->  запуск локального сервера
    [ -mig | --migrate ]         ->  запуск миграции базы данных и проекта
    [ -mak | --makemigrations ]  ->  подготовка к запуску миграций базы данных и проекта
    [ -c | --collectstatic ]     ->  сбор статических файлов в дирекорию staticfiles
    [ -a | --admin ]             ->  создание суперпользователя в базе данных фреймворка

    Пример команды запуска bash скрипта: ./run.sh -r или ./run.sh -runserver"
    exit 1
fi

# chmod +x run.sh

#./run.sh -r
# или
#./run.sh --runserver
