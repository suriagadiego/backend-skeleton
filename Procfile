release: python backend/manage.py migrate
web: gunicorn --pythonpath cfehome cfehome.wsgi  --log-file -