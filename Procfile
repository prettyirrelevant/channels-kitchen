release: python manage.py migrate
web: uvicorn kitchen_project.asgi:application -p $PORT
worker: python manage.py runworker channel_layer