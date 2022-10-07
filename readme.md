# Command to install requirement
pip install -r requirements.txt

# Command to create database on local
create database rpn_db;
create user amir with encrypted password 'pwd';
alter database user_registration_db owner to amir;


# Command to start application on local
python manage.py start

# Url to Swagger
http://127.0.0.1:5000/ui/


# Command to get all routes
python manage.py routes

# Command to migrate Database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade



