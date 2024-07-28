# Command list for the Project

___

## The command to run the site docker build on the server
```commandline
sudo docker compose -f "./docker-compose.yml" up
```


## The command to start the rebuild of the docker site on the server
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```

## Running the project locally
```commandline
poetry run python manage.py runserver
```

## Launching Django shell
```commandline
python manage.py shell
```

## Migrations in the Django project
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```

## Create superuser for the project
```commandline
python manage.py createsuperuser
```

## Create app for the project & start the project
```commandline
django-admin startproject advertisements
```
```commandline
python manage.py startapp app_advertisements
```

## Docker clean cache and stop the containers all
```commandline
sudo docker builder prune
```
```commandline
sudo docker image prune -a -f
```
```commandline
sudo docker container prune
```
```commandline
sudo docker rm $(docker ps -a -q)
```

* [Docker clean casssh](https://dev.to/ajeetraina/how-to-clear-docker-cache-2nnp)

## Project dependencies
```commandline
venv\Scripts\activate
```
```commandline
source venv/bin/activate
```
```commandline
pip install -r requirements.txt
```
___

[README.md](..%2FREADME.md)