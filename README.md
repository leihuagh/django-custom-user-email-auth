# django-custom-user-email-auth

Base Template for project from [django-custom-user](https://github.com/mokgadirasekgala/django-custom-user). Factory boy use for model Factories. Clone the repo and use as the base for your project

## Properties
python version : 3.6.8

django version : 2.0.9

user model : extends Abstract user model extra field "life_motto" username removed and authentication done using email 
db : Django default = SQLite

## Getting started
Clone repo and cd into directory

### Running app

You will migrate and import the admin user to be able to access admin
```bash
docker-compose build
docker-compose run --rm web-app python manage.py migrate
docker-compose run --rm web-app python manage.py import
docker-compose up
```
Access the app at [http://localhost:8000](http://localhost:8000/)
Access the admin at [http://localhost:8000/admin](http://localhost:8000/admin)

Login using 
  email : admin@email.com
  password : adminadmin

### Running migrations 
```bash
docker-compose run --rm web-app python manage.py migrate
```

###Running tests
```bash
docker-compose run --rm web-app python manage.py test
```

### Creating super user
```bash
docker-compose run --rm web-app python manage.py createsuperuser
```

### Running shell 
```bash
docker-compose up -d
docker-compose run --rm web-app python manage.py shell
```

### changing Author
You will see that Author comes up as Mokgadi Rasekgala when you run the app. Change it the docker-compose.yml file to your name  or by running
```shell
docker-compose run -e AUTHOR={your name} web-app
```

## Making Modifications
Feel free to delete the life_motto field was added so you see how to add a non required field to the admin. If you add a required field you must add it to the Create form add_fieldset in the admin.py and in the CustomUser factory
