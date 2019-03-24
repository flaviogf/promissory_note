pipenv run python manage.py migrate
pipenv run gunicorn -b 0.0.0.0 api.wsgi
