release: python manage.py migrate
web: uvicorn kitchen_project.asgi:application -p $PORT -b 0.0.0.0
worker: python manage.py runworker channel_layer