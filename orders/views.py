from django.views.generic import ListView

from .models import Order


class OrdersListView(ListView):
    template_name = "orders/orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.order_by("-created_on")
