rm db.sqlite3
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
