FROM python:3.12

WORKDIR /app

# Install the application dependencies
COPY . .

RUN pip install -r requirements.txt

# CMD ["python", "app.py"]
CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "--timeout", "600", "--workers", "3","app:app"]

# CMD gunicorn --bind 0.0.0.0:8000 wsgi:app

# bind = '0.0.0.0:9000'
# workers = 8
# worker_class = 'gevent'
# max_requests = 5000
# max_requests_jitter = 50
# keepalive = 45