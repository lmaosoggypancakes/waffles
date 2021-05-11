import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from . import models
from django.db.models.signals import post_save
class ChatConsumer(WebsocketConsumer):
    connected_users = []
    def connect(self):
        print(self.scope["user"])
        self.__class__.connected_users.append(self)
        self.accept()
    def receive(self, text_data):
        data = json.loads(text_data)
        message = models.Message(content=data["body"], user_from=self.scope["user"], user_to=models.User.objects.get(username=data['to']))
        message.save() # no need to worry about sending message because the signal helper function will take care of it
    def send_message(self, ctx):
        self.send(json.dumps(ctx))
    @classmethod
    def message_handler(cls, sender, **data):
        for user in cls.connected_users:
            print("Hello!")
            if user.scope["user"] == data["instance"].user_to:
                user.send_message(data["instance"].serialize())

post_save.connect(ChatConsumer.message_handler, sender=models.Message)