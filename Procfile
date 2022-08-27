release: python backend/manage.py migrate
web: gunicorn --pythonpath backend cfehome.wsgi  --log-file -