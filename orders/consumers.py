import json
import secrets

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from orders.models import Order


class OrderConsumer(WebsocketConsumer):
    def connect(self):
        self.room = "orders"
        async_to_sync(self.channel_layer.group_add)(self.room, self.channel_name)

        # Debugging
        # print(
        #     f"User:{self.scope['user']} with ID:{self.channel_name} added to {self.room}"
        # )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.room, self.channel_name)
        # Debugging
        # print(
        #     f"User:{self.scope['user']} with ID:{self.channel_name} removed from {self.room}"
        # )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        action = text_data_json["action"]
        order = None

        # take order from counter staff
        if action == "take-order":
            order = Order.objects.get(order_number=text_data_json["order_id"])
            order.taken_by = self.scope["user"]
            order.status = 1
            order.save()

        # fulfill order from kitchen staff
        elif action == "fulfill-order":
            order = Order.objects.get(order_number=text_data_json["order_id"])
            order.fulfilled_by = self.scope["user"]
            order.status = 2
            order.save()

        # create order
        elif action == "create-order":
            order = Order.objects.create(
                order_number=secrets.token_hex(8),
                food_choice=secrets.choice([1, 2, 3, 4]),
                status=0,
                quantity=secrets.choice(list(range(1, 30))),
            )

        async_to_sync(self.channel_layer.group_send)(
            self.room,
            {
                "type": "order_update",
                "data": {
                    "action": action,
                    "order_id": order.order_number,
                    "food_name": order.food_choice_display,
                    "quantity": order.quantity,
                    "status": order.status_display,
                    "created_on": order.created_on.isoformat(),
                },
            },
        )

    def order_update(self, event):
        data = event["data"]
        self.send(text_data=json.dumps(data))
