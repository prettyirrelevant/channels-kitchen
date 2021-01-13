release: python manage.py migrate
web: uvicorn kitchen_project.asgi:application --port $PORT --host 0.0.0.0
worker: python manage.py runworker channel_layer