release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn api_basic.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
