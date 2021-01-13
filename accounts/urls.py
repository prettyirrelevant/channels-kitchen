from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "accounts/signup/manager",
        views.ManagerCreateView.as_view(),
        name="manager-signup",
    ),
    path(
        "accounts/signup/kitchen",
        views.KitchenCreateView.as_view(),
        name="kitchen-signup",
    ),
    path(
        "accounts/signup/counter",
        views.CounterCreateView.as_view(),
        name="counter-signup",
    ),
    path("manager", views.manager, name="manager-page"),
    path("kitchen", views.KitchenListView.as_view(), name="kitchen-page"),
    path("counter", views.CounterListView.as_view(), name="counter-page"),
    path(
        "accounts/login",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("accounts/logout", LogoutView.as_view(), name="logout"),
]
