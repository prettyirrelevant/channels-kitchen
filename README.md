# channels-kitchen
A simple order management system with real-time updates using Django Channels

## Routes
- `/orders`: List all orders. Accessible by every user(either logged in or not).
- `/manager`: Manager's dashboard. 
- `/kitchen`: Kitchen staff's dashboard. Accessible by kitchen staff(s) and manager(s).
- `/counter`: Counter staff's dashboard. Accessible by counter staff(s) and manager(s).
- `/accounts/signup/manager`:  Manager's account creation.
- `/accounts/signup/kitchen`: Kitchen staff's account creation. Only manager(s) can create an account.
- `/accounts/signup/counter`: Counter staff's account creation. Only manager(s) can create an account.
- `/accounts/login`: Login
- `/accounts/logout`: Logout

## Live Demo
This project is live on [Heroku](https://channels-kitchen.herokuapp.com)

## Local Development
1. Clone this repository.
2. Create a virtual environment.
3. Activate the virtual environment.
4. Install all project dependencies.
5. Make sure Redis-5.0 and above is installed on your system. If not, make the following changes to `kitchen_project/settings/development.py`
```diff
- CHANNEL_LAYERS = {
-    'default': {
-        'BACKEND': 'channels_redis.core.RedisChannelLayer',
-        'CONFIG': {
-            "hosts": [('127.0.0.1', 6379)],
-        },
-    },
- }
+ CHANNEL_LAYERS = {
+    "default": {
+        "BACKEND": "channels.layers.InMemoryChannelLayer"
+    }
+ }
```
6. Run migrations.
7. Start development server.

## Note
Although `/kitchen` and `/counter` routes are accessible to managers, actions on those routes are restricted to kitchen staff(s) and counter staff(s) respectively.
