from django.urls import path

from . import views

urlpatterns = [
    path("orders", views.OrdersListView.as_view(), name="orders-page"),
]
