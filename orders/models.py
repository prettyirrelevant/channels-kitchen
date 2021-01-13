from django.db import models

from accounts.models import User

FOOD_CHOICES = [
    (1, "Rice and Beans"),
    (2, "Fried Rice and Chicken"),
    (3, "Bread and Beans"),
    (4, "Pap and Akara"),
]

ORDER_STATUS = [(0, "Created"), (1, "Pending"), (2, "Fulfilled")]


class Order(models.Model):
    order_number = models.CharField(blank=False, null=True, max_length=30, unique=True)
    food_choice = models.IntegerField(choices=FOOD_CHOICES, blank=False, null=False)
    quantity = models.IntegerField(null=False)
    status = models.IntegerField(choices=ORDER_STATUS, null=False, blank=False)
    taken_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="taken_orders", null=True
    )
    fulfilled_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="fulfilled_orders", null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def food_choice_display(self):
        return self.get_food_choice_display()

    @property
    def status_display(self):
        return self.get_status_display()

    @property
    def isoformat(self):
        return self.created_on.isoformat()
