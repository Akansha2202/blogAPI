release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn MyProject.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
