# Real-Estate Agency website  
Used Django for the backend side  
Jinja for making dynamic changes on frontend templates  
PostgreSQL for the accounts and properties database (local)  

# How to run  
Install Django using
```
pip install django
```
Configure your database in settings.py or create a new PostgreSQL database in your system using the settings.py credentials  
Then run the following commands :
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open localhost:8000 on your browser to view the app
