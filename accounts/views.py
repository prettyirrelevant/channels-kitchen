from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from orders.models import Order
from .decorators import manager_required, kitchen_required, counter_required
from .forms import ManagerCreationForm, KitchenCreationForm, CounterCreationForm
from .models import User


def home(request):
    if request.user.is_authenticated:
        if request.user.is_manager:
            return redirect("manager-page")
        elif request.user.is_kitchen:
            return redirect("kitchen-page")
        else:
            return redirect("counter-page")
    return render(request, "accounts/index.html")


@login_required
@manager_required
def manager(request):
    return render(request, "accounts/manager.html")


class ManagerCreateView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = ManagerCreationForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        kwargs["type_of_user"] = "Manager"
        return super().get_context_data(**kwargs)


@method_decorator([login_required, kitchen_required], name="dispatch")
class KitchenListView(ListView):
    template_name = "accounts/kitchen.html"
    context_object_name = "orders"
    queryset = Order.objects.filter(status=1).order_by("-created_on")


@method_decorator([login_required, manager_required], name="dispatch")
class KitchenCreateView(CreateView):
    model = User
    template_name = "accounts/staff_create.html"
    form_class = KitchenCreationForm
    success_url = reverse_lazy("manager-page")

    def get_context_data(self, **kwargs):
        kwargs["type_of_user"] = "Kitchen"
        return super().get_context_data(**kwargs)


@method_decorator([login_required, counter_required], name="dispatch")
class CounterListView(ListView):
    template_name = "accounts/counter.html"
    context_object_name = "orders"
    queryset = Order.objects.filter(status=0).order_by("-created_on")


@method_decorator([login_required, manager_required], name="dispatch")
class CounterCreateView(CreateView):
    model = User
    template_name = "accounts/staff_create.html"
    form_class = CounterCreationForm
    success_url = reverse_lazy("manager-page")

    def get_context_data(self, **kwargs):
        kwargs["type_of_user"] = "Counter"
        return super().get_context_data(**kwargs)
