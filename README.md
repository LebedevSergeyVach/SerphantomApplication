# Serphantom Space Application
<a name="up"></a>

The project is written on the [Django](https://www.djangoproject.com) framework.
The backend is written in [python](https://www.python.org).
Frontend is written using [bootstrap](https://getbootstrap.com).

This site hosts programs and applications for Windows and Android. Any user of the site can use the necessary programs or applications.
This site is written on pure enthusiasm.

___

### [Lebedev Sergey Vyacheslav](https://github.com/LebedevSergeyVach) – Product Lead & Fullstack Python-Developer.
### [Website Serphantom](https://serphantom.space) - a link to a website located on its server with a white (external) ip address connected. A fresh and constantly updated version of the site.

___

# Project deployment on the server [Debian](https://www.debian.org).

#### Download a project.
```commandline
git clone git@github.com:LebedevSergeyVach/SerphantomApplication.git
```
#### The command for configuring and migrating the project database on the Django framework on the server.
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
#### Creating and configuring a website administrator.
```commandline
python manage.py createsuperuser
```
#### The command to start the rebuild of the docker site on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```
#### The command to run the site docker build on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" up
```
#### Clearing dockers data and file cache.
```commandline
sudo docker container prune
```
```commandline
sudo docker builder prune
```

___

#### [README](README.md) [UP](#up)

___

# Приложения и продукция Serphantom Space
<a name="вверх"></a>

На данном сайте размещаются программы и приложения для Windows и Android. Любой пользователь сайта может необходимые ему программы или приложения.
Данный сайт написан на чистом энтузиазме.

___

# Ссылки и версии веб-сайта    
### [Лебедев Сергей Вячеславович](https://github.com/LebedevSergeyVach) – Руководитель продукта и Fullstack Python-разработчик.
### [Веб-сайт Serphantom](https://serphantom.space) - ссылка на веб-сайт, размещенный на собственном сервере с белым (внешним) IP-адресом. Свежая и постоянно обновляемая версия сайта.

___

## Развертывание проекта на сервере [Debian](https://www.debian.org).

#### Загрузка проекта.
```commandline
git clone git@github.com:LebedevSergeyVach/WebsiteProductPlacement.git
```
#### Команда для настройки и миграции базы данных проекта на фреймворке Django на сервере.
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
#### Создание и настройка администратора веб-сайта.
```commandline
python manage.py createsuperuser
```
#### Команда для запуска сборки сайта в docker на сервере.
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```
#### Команда для запуска docker-сборки сайта на сервере.
```commandline
sudo docker compose -f "./docker-compose.yml" up
```
#### Очистка данных docker и файлового кэша.
```commandline
sudo docker container prune
```
```commandline
sudo docker builder prune
```

---

#### [README](README.md) [ВВЕРХ](#вверх)

___

## Полезные расширения для Visual Studio Code

### Основные расширения

1. **Python**
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - Описание: Основное расширение для работы с Python в VSCode.

2. **Django**
   - [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
   - Описание: Поддержка синтаксиса и фрагментов кода для Django.

3. **Pylance**
   - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
   - Описание: Расширенная поддержка языка Python, включая IntelliSense и анализ кода.

### Инструменты форматирования и анализа кода

1. **ESLint**
   - [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
   - Описание: Инструмент анализа и форматирования JavaScript и TypeScript кода.

2. **Prettier**
   - [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
   - Описание: Инструмент форматирования кода для JavaScript, CSS и HTML.

### Визуальные улучшения

1. **Bracket Pair Colorizer**
   - [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
   - Описание: Визуальное выделение пар скобок.

2. **Material Icon Theme**
   - [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
   - Описание: Красивые иконки для файлов и папок.

### Инструменты разработки

1. **GitLens**
   - [GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
   - Описание: Расширенная поддержка Git в VSCode.

2. **Live Server**
   - [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
   - Описание: Локальный запуск и просмотр изменений в реальном времени.

3. **SQLite**
    - [SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
    - Описание: Работа с базами данных SQLite.
